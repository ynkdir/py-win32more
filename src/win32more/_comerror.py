from __future__ import annotations

from ctypes import wstring_at

from win32more._win32api import (
    BSTR,
    HRESULT,
    S_OK,
    FormatError,
    GetErrorInfo,
    IErrorInfo,
    IRestrictedErrorInfo,
    SysFreeString,
    SysStringLen,
)


class ComError(OSError):
    def __init__(self, hr):
        self._hr = hr
        self._error_info = IErrorInfo(own=True)
        if GetErrorInfo(0, self._error_info) != S_OK:
            self._error_info = None
        super().__init__(hr, self._message())

    def _message(self) -> str:
        return (
            self._winrt_restricted_description()
            or self._winrt_description()
            or self._com_description()
            or self._win32_message()
            or ""
        )

    def _win32_message(self) -> str | None:
        return FormatError(self._hr)

    def _com_description(self) -> str | None:
        if self._error_info is None:
            return None

        description = BSTR()
        r = self._error_info.GetDescription(description)
        if r != S_OK:
            return None

        try:
            return self._copy_message(description)
        finally:
            SysFreeString(description)

    def _winrt_description(self) -> str | None:
        details = self._winrt_error_details()
        if details is None:
            return None
        return details["description"]

    def _winrt_restricted_description(self) -> str | None:
        details = self._winrt_error_details()
        if details is None:
            return None
        return details["restricted_description"]

    def _winrt_error_details(self) -> str | None:
        if self._error_info is None:
            return None

        try:
            restricted_error_info = self._error_info.as_(IRestrictedErrorInfo)
        except OSError:
            return None

        description = BSTR()
        error = HRESULT()
        restricted_description = BSTR()
        capability_sid = BSTR()
        r = restricted_error_info.GetErrorDetails(description, error, restricted_description, capability_sid)
        if r != S_OK:
            return None

        try:
            return {
                "restricted_description": self._copy_message(restricted_description),
                "error": error.value,
                "description": self._copy_message(description),
                "capability_sid": self._copy_message(capability_sid),
            }
        finally:
            SysFreeString(description)
            SysFreeString(restricted_description)
            SysFreeString(capability_sid)

    def _copy_message(self, p: BSTR) -> str | None:
        if not p:
            return None
        return wstring_at(p, SysStringLen(p)).strip()
