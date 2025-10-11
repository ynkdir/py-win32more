from __future__ import annotations

from ._bstr import bstr
from ._win32 import FAILED, WinError
from ._win32api import (
    HRESULT,
    S_OK,
    CreateErrorInfo,
    FormatError,
    GetErrorInfo,
    ICreateErrorInfo,
    IErrorInfo,
    IRestrictedErrorInfo,
    SetErrorInfo,
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

        description = bstr(own=True)
        r = self._error_info.GetDescription(description)
        if r != S_OK:
            return None

        return str(description).strip()

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

        description = bstr(own=True)
        error = HRESULT()
        restricted_description = bstr(own=True)
        capability_sid = bstr(own=True)
        r = restricted_error_info.GetErrorDetails(description, error, restricted_description, capability_sid)
        if r != S_OK:
            return None

        return {
            "restricted_description": str(restricted_description).strip(),
            "error": error.value,
            "description": str(description).strip(),
            "capability_sid": str(capability_sid).strip(),
        }


def set_error_info(description: str) -> None:
    info = ICreateErrorInfo(own=True)
    hr = CreateErrorInfo(info)
    if FAILED(hr):
        raise WinError(hr)
    hr = info.SetDescription(bstr(description, own=True))
    if FAILED(hr):
        raise WinError(hr)
    hr = SetErrorInfo(0, info.as_(IErrorInfo))
    if FAILED(hr):
        raise WinError(hr)
