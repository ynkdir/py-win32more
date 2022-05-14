from win32more import *
import win32more.System.Com.Marshal
import win32more.Foundation
import win32more.Graphics.Gdi
import win32more.System.Com
import win32more.UI.WindowsAndMessaging

def __getattr__(name):
    if name == "__path__":
        raise AttributeError()
    setattr(win32more.System.Com.Marshal, name, eval(f"_define_{name}()"))
    return getattr(win32more.System.Com.Marshal, name)
def _define_IMarshal_head():
    class IMarshal(win32more.System.Com.IUnknown_head):
        Guid = Guid('00000003-0000-0000-c000-000000000046')
    return IMarshal
def _define_IMarshal():
    IMarshal = win32more.System.Com.Marshal.IMarshal_head
    IMarshal.GetUnmarshalClass = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),c_void_p,UInt32,c_void_p,UInt32,POINTER(Guid), use_last_error=False)(3, 'GetUnmarshalClass', ((1, 'riid'),(1, 'pv'),(1, 'dwDestContext'),(1, 'pvDestContext'),(1, 'mshlflags'),(1, 'pCid'),)))
    IMarshal.GetMarshalSizeMax = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),c_void_p,UInt32,c_void_p,UInt32,POINTER(UInt32), use_last_error=False)(4, 'GetMarshalSizeMax', ((1, 'riid'),(1, 'pv'),(1, 'dwDestContext'),(1, 'pvDestContext'),(1, 'mshlflags'),(1, 'pSize'),)))
    IMarshal.MarshalInterface = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IStream_head,POINTER(Guid),c_void_p,UInt32,c_void_p,UInt32, use_last_error=False)(5, 'MarshalInterface', ((1, 'pStm'),(1, 'riid'),(1, 'pv'),(1, 'dwDestContext'),(1, 'pvDestContext'),(1, 'mshlflags'),)))
    IMarshal.UnmarshalInterface = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IStream_head,POINTER(Guid),POINTER(c_void_p), use_last_error=False)(6, 'UnmarshalInterface', ((1, 'pStm'),(1, 'riid'),(1, 'ppv'),)))
    IMarshal.ReleaseMarshalData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IStream_head, use_last_error=False)(7, 'ReleaseMarshalData', ((1, 'pStm'),)))
    IMarshal.DisconnectObject = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(8, 'DisconnectObject', ((1, 'dwReserved'),)))
    return IMarshal
def _define_IMarshal2_head():
    class IMarshal2(win32more.System.Com.Marshal.IMarshal_head):
        Guid = Guid('000001cf-0000-0000-c000-000000000046')
    return IMarshal2
def _define_IMarshal2():
    IMarshal2 = win32more.System.Com.Marshal.IMarshal2_head
    return IMarshal2
def _define_IMarshalingStream_head():
    class IMarshalingStream(win32more.System.Com.IStream_head):
        Guid = Guid('d8f2f5e6-6102-4863-9f26-389a4676efde')
    return IMarshalingStream
def _define_IMarshalingStream():
    IMarshalingStream = win32more.System.Com.Marshal.IMarshalingStream_head
    IMarshalingStream.GetMarshalingContextAttribute = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.CO_MARSHALING_CONTEXT_ATTRIBUTES,POINTER(UIntPtr), use_last_error=False)(14, 'GetMarshalingContextAttribute', ((1, 'attribute'),(1, 'pAttributeValue'),)))
    return IMarshalingStream
STDMSHLFLAGS = Int32
SMEXF_SERVER = 1
SMEXF_HANDLER = 2
def _define_BSTR_UserSize():
    try:
        return WINFUNCTYPE(UInt32,POINTER(UInt32),UInt32,POINTER(win32more.Foundation.BSTR), use_last_error=False)(("BSTR_UserSize", windll["OLEAUT32"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_BSTR_UserMarshal():
    try:
        return WINFUNCTYPE(c_char_p_no,POINTER(UInt32),c_char_p_no,POINTER(win32more.Foundation.BSTR), use_last_error=False)(("BSTR_UserMarshal", windll["OLEAUT32"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_BSTR_UserUnmarshal():
    try:
        return WINFUNCTYPE(c_char_p_no,POINTER(UInt32),POINTER(Byte),POINTER(win32more.Foundation.BSTR), use_last_error=False)(("BSTR_UserUnmarshal", windll["OLEAUT32"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_BSTR_UserFree():
    try:
        return WINFUNCTYPE(Void,POINTER(UInt32),POINTER(win32more.Foundation.BSTR), use_last_error=False)(("BSTR_UserFree", windll["OLEAUT32"]), ((1, 'param0'),(1, 'param1'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HWND_UserSize():
    try:
        return WINFUNCTYPE(UInt32,POINTER(UInt32),UInt32,POINTER(win32more.Foundation.HWND), use_last_error=False)(("HWND_UserSize", windll["OLE32"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HWND_UserMarshal():
    try:
        return WINFUNCTYPE(c_char_p_no,POINTER(UInt32),c_char_p_no,POINTER(win32more.Foundation.HWND), use_last_error=False)(("HWND_UserMarshal", windll["OLE32"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HWND_UserUnmarshal():
    try:
        return WINFUNCTYPE(c_char_p_no,POINTER(UInt32),POINTER(Byte),POINTER(win32more.Foundation.HWND), use_last_error=False)(("HWND_UserUnmarshal", windll["OLE32"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HWND_UserFree():
    try:
        return WINFUNCTYPE(Void,POINTER(UInt32),POINTER(win32more.Foundation.HWND), use_last_error=False)(("HWND_UserFree", windll["OLE32"]), ((1, 'param0'),(1, 'param1'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VARIANT_UserSize():
    try:
        return WINFUNCTYPE(UInt32,POINTER(UInt32),UInt32,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(("VARIANT_UserSize", windll["OLEAUT32"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VARIANT_UserMarshal():
    try:
        return WINFUNCTYPE(c_char_p_no,POINTER(UInt32),c_char_p_no,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(("VARIANT_UserMarshal", windll["OLEAUT32"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VARIANT_UserUnmarshal():
    try:
        return WINFUNCTYPE(c_char_p_no,POINTER(UInt32),POINTER(Byte),POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(("VARIANT_UserUnmarshal", windll["OLEAUT32"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VARIANT_UserFree():
    try:
        return WINFUNCTYPE(Void,POINTER(UInt32),POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(("VARIANT_UserFree", windll["OLEAUT32"]), ((1, 'param0'),(1, 'param1'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_BSTR_UserSize64():
    try:
        return WINFUNCTYPE(UInt32,POINTER(UInt32),UInt32,POINTER(win32more.Foundation.BSTR), use_last_error=False)(("BSTR_UserSize64", windll["OLEAUT32"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_BSTR_UserMarshal64():
    try:
        return WINFUNCTYPE(c_char_p_no,POINTER(UInt32),c_char_p_no,POINTER(win32more.Foundation.BSTR), use_last_error=False)(("BSTR_UserMarshal64", windll["OLEAUT32"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_BSTR_UserUnmarshal64():
    try:
        return WINFUNCTYPE(c_char_p_no,POINTER(UInt32),POINTER(Byte),POINTER(win32more.Foundation.BSTR), use_last_error=False)(("BSTR_UserUnmarshal64", windll["OLEAUT32"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_BSTR_UserFree64():
    try:
        return WINFUNCTYPE(Void,POINTER(UInt32),POINTER(win32more.Foundation.BSTR), use_last_error=False)(("BSTR_UserFree64", windll["OLEAUT32"]), ((1, 'param0'),(1, 'param1'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HWND_UserSize64():
    try:
        return WINFUNCTYPE(UInt32,POINTER(UInt32),UInt32,POINTER(win32more.Foundation.HWND), use_last_error=False)(("HWND_UserSize64", windll["OLE32"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HWND_UserMarshal64():
    try:
        return WINFUNCTYPE(c_char_p_no,POINTER(UInt32),c_char_p_no,POINTER(win32more.Foundation.HWND), use_last_error=False)(("HWND_UserMarshal64", windll["OLE32"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HWND_UserUnmarshal64():
    try:
        return WINFUNCTYPE(c_char_p_no,POINTER(UInt32),POINTER(Byte),POINTER(win32more.Foundation.HWND), use_last_error=False)(("HWND_UserUnmarshal64", windll["OLE32"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HWND_UserFree64():
    try:
        return WINFUNCTYPE(Void,POINTER(UInt32),POINTER(win32more.Foundation.HWND), use_last_error=False)(("HWND_UserFree64", windll["OLE32"]), ((1, 'param0'),(1, 'param1'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VARIANT_UserSize64():
    try:
        return WINFUNCTYPE(UInt32,POINTER(UInt32),UInt32,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(("VARIANT_UserSize64", windll["OLEAUT32"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VARIANT_UserMarshal64():
    try:
        return WINFUNCTYPE(c_char_p_no,POINTER(UInt32),c_char_p_no,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(("VARIANT_UserMarshal64", windll["OLEAUT32"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VARIANT_UserUnmarshal64():
    try:
        return WINFUNCTYPE(c_char_p_no,POINTER(UInt32),POINTER(Byte),POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(("VARIANT_UserUnmarshal64", windll["OLEAUT32"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VARIANT_UserFree64():
    try:
        return WINFUNCTYPE(Void,POINTER(UInt32),POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(("VARIANT_UserFree64", windll["OLEAUT32"]), ((1, 'param0'),(1, 'param1'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CLIPFORMAT_UserSize():
    try:
        return WINFUNCTYPE(UInt32,POINTER(UInt32),UInt32,POINTER(UInt16), use_last_error=False)(("CLIPFORMAT_UserSize", windll["OLE32"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CLIPFORMAT_UserMarshal():
    try:
        return WINFUNCTYPE(c_char_p_no,POINTER(UInt32),c_char_p_no,POINTER(UInt16), use_last_error=False)(("CLIPFORMAT_UserMarshal", windll["OLE32"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CLIPFORMAT_UserUnmarshal():
    try:
        return WINFUNCTYPE(c_char_p_no,POINTER(UInt32),POINTER(Byte),POINTER(UInt16), use_last_error=False)(("CLIPFORMAT_UserUnmarshal", windll["OLE32"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CLIPFORMAT_UserFree():
    try:
        return WINFUNCTYPE(Void,POINTER(UInt32),POINTER(UInt16), use_last_error=False)(("CLIPFORMAT_UserFree", windll["OLE32"]), ((1, 'param0'),(1, 'param1'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HBITMAP_UserSize():
    try:
        return WINFUNCTYPE(UInt32,POINTER(UInt32),UInt32,POINTER(win32more.Graphics.Gdi.HBITMAP), use_last_error=False)(("HBITMAP_UserSize", windll["OLE32"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HBITMAP_UserMarshal():
    try:
        return WINFUNCTYPE(c_char_p_no,POINTER(UInt32),c_char_p_no,POINTER(win32more.Graphics.Gdi.HBITMAP), use_last_error=False)(("HBITMAP_UserMarshal", windll["OLE32"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HBITMAP_UserUnmarshal():
    try:
        return WINFUNCTYPE(c_char_p_no,POINTER(UInt32),POINTER(Byte),POINTER(win32more.Graphics.Gdi.HBITMAP), use_last_error=False)(("HBITMAP_UserUnmarshal", windll["OLE32"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HBITMAP_UserFree():
    try:
        return WINFUNCTYPE(Void,POINTER(UInt32),POINTER(win32more.Graphics.Gdi.HBITMAP), use_last_error=False)(("HBITMAP_UserFree", windll["OLE32"]), ((1, 'param0'),(1, 'param1'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HDC_UserSize():
    try:
        return WINFUNCTYPE(UInt32,POINTER(UInt32),UInt32,POINTER(win32more.Graphics.Gdi.HDC), use_last_error=False)(("HDC_UserSize", windll["OLE32"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HDC_UserMarshal():
    try:
        return WINFUNCTYPE(c_char_p_no,POINTER(UInt32),c_char_p_no,POINTER(win32more.Graphics.Gdi.HDC), use_last_error=False)(("HDC_UserMarshal", windll["OLE32"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HDC_UserUnmarshal():
    try:
        return WINFUNCTYPE(c_char_p_no,POINTER(UInt32),POINTER(Byte),POINTER(win32more.Graphics.Gdi.HDC), use_last_error=False)(("HDC_UserUnmarshal", windll["OLE32"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HDC_UserFree():
    try:
        return WINFUNCTYPE(Void,POINTER(UInt32),POINTER(win32more.Graphics.Gdi.HDC), use_last_error=False)(("HDC_UserFree", windll["OLE32"]), ((1, 'param0'),(1, 'param1'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HICON_UserSize():
    try:
        return WINFUNCTYPE(UInt32,POINTER(UInt32),UInt32,POINTER(win32more.UI.WindowsAndMessaging.HICON), use_last_error=False)(("HICON_UserSize", windll["OLE32"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HICON_UserMarshal():
    try:
        return WINFUNCTYPE(c_char_p_no,POINTER(UInt32),c_char_p_no,POINTER(win32more.UI.WindowsAndMessaging.HICON), use_last_error=False)(("HICON_UserMarshal", windll["OLE32"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HICON_UserUnmarshal():
    try:
        return WINFUNCTYPE(c_char_p_no,POINTER(UInt32),POINTER(Byte),POINTER(win32more.UI.WindowsAndMessaging.HICON), use_last_error=False)(("HICON_UserUnmarshal", windll["OLE32"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HICON_UserFree():
    try:
        return WINFUNCTYPE(Void,POINTER(UInt32),POINTER(win32more.UI.WindowsAndMessaging.HICON), use_last_error=False)(("HICON_UserFree", windll["OLE32"]), ((1, 'param0'),(1, 'param1'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SNB_UserSize():
    try:
        return WINFUNCTYPE(UInt32,POINTER(UInt32),UInt32,POINTER(POINTER(POINTER(UInt16))), use_last_error=False)(("SNB_UserSize", windll["ole32"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SNB_UserMarshal():
    try:
        return WINFUNCTYPE(c_char_p_no,POINTER(UInt32),c_char_p_no,POINTER(POINTER(POINTER(UInt16))), use_last_error=False)(("SNB_UserMarshal", windll["ole32"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SNB_UserUnmarshal():
    try:
        return WINFUNCTYPE(c_char_p_no,POINTER(UInt32),POINTER(Byte),POINTER(POINTER(POINTER(UInt16))), use_last_error=False)(("SNB_UserUnmarshal", windll["ole32"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SNB_UserFree():
    try:
        return WINFUNCTYPE(Void,POINTER(UInt32),POINTER(POINTER(POINTER(UInt16))), use_last_error=False)(("SNB_UserFree", windll["ole32"]), ((1, 'param0'),(1, 'param1'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_STGMEDIUM_UserSize():
    try:
        return WINFUNCTYPE(UInt32,POINTER(UInt32),UInt32,POINTER(win32more.System.Com.STGMEDIUM_head), use_last_error=False)(("STGMEDIUM_UserSize", windll["OLE32"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_STGMEDIUM_UserMarshal():
    try:
        return WINFUNCTYPE(c_char_p_no,POINTER(UInt32),c_char_p_no,POINTER(win32more.System.Com.STGMEDIUM_head), use_last_error=False)(("STGMEDIUM_UserMarshal", windll["OLE32"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_STGMEDIUM_UserUnmarshal():
    try:
        return WINFUNCTYPE(c_char_p_no,POINTER(UInt32),POINTER(Byte),POINTER(win32more.System.Com.STGMEDIUM_head), use_last_error=False)(("STGMEDIUM_UserUnmarshal", windll["OLE32"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_STGMEDIUM_UserFree():
    try:
        return WINFUNCTYPE(Void,POINTER(UInt32),POINTER(win32more.System.Com.STGMEDIUM_head), use_last_error=False)(("STGMEDIUM_UserFree", windll["OLE32"]), ((1, 'param0'),(1, 'param1'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CLIPFORMAT_UserSize64():
    try:
        return WINFUNCTYPE(UInt32,POINTER(UInt32),UInt32,POINTER(UInt16), use_last_error=False)(("CLIPFORMAT_UserSize64", windll["OLE32"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CLIPFORMAT_UserMarshal64():
    try:
        return WINFUNCTYPE(c_char_p_no,POINTER(UInt32),c_char_p_no,POINTER(UInt16), use_last_error=False)(("CLIPFORMAT_UserMarshal64", windll["OLE32"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CLIPFORMAT_UserUnmarshal64():
    try:
        return WINFUNCTYPE(c_char_p_no,POINTER(UInt32),POINTER(Byte),POINTER(UInt16), use_last_error=False)(("CLIPFORMAT_UserUnmarshal64", windll["OLE32"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CLIPFORMAT_UserFree64():
    try:
        return WINFUNCTYPE(Void,POINTER(UInt32),POINTER(UInt16), use_last_error=False)(("CLIPFORMAT_UserFree64", windll["OLE32"]), ((1, 'param0'),(1, 'param1'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HBITMAP_UserSize64():
    try:
        return WINFUNCTYPE(UInt32,POINTER(UInt32),UInt32,POINTER(win32more.Graphics.Gdi.HBITMAP), use_last_error=False)(("HBITMAP_UserSize64", windll["OLE32"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HBITMAP_UserMarshal64():
    try:
        return WINFUNCTYPE(c_char_p_no,POINTER(UInt32),c_char_p_no,POINTER(win32more.Graphics.Gdi.HBITMAP), use_last_error=False)(("HBITMAP_UserMarshal64", windll["OLE32"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HBITMAP_UserUnmarshal64():
    try:
        return WINFUNCTYPE(c_char_p_no,POINTER(UInt32),POINTER(Byte),POINTER(win32more.Graphics.Gdi.HBITMAP), use_last_error=False)(("HBITMAP_UserUnmarshal64", windll["OLE32"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HBITMAP_UserFree64():
    try:
        return WINFUNCTYPE(Void,POINTER(UInt32),POINTER(win32more.Graphics.Gdi.HBITMAP), use_last_error=False)(("HBITMAP_UserFree64", windll["OLE32"]), ((1, 'param0'),(1, 'param1'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HDC_UserSize64():
    try:
        return WINFUNCTYPE(UInt32,POINTER(UInt32),UInt32,POINTER(win32more.Graphics.Gdi.HDC), use_last_error=False)(("HDC_UserSize64", windll["OLE32"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HDC_UserMarshal64():
    try:
        return WINFUNCTYPE(c_char_p_no,POINTER(UInt32),c_char_p_no,POINTER(win32more.Graphics.Gdi.HDC), use_last_error=False)(("HDC_UserMarshal64", windll["OLE32"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HDC_UserUnmarshal64():
    try:
        return WINFUNCTYPE(c_char_p_no,POINTER(UInt32),POINTER(Byte),POINTER(win32more.Graphics.Gdi.HDC), use_last_error=False)(("HDC_UserUnmarshal64", windll["OLE32"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HDC_UserFree64():
    try:
        return WINFUNCTYPE(Void,POINTER(UInt32),POINTER(win32more.Graphics.Gdi.HDC), use_last_error=False)(("HDC_UserFree64", windll["OLE32"]), ((1, 'param0'),(1, 'param1'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HICON_UserSize64():
    try:
        return WINFUNCTYPE(UInt32,POINTER(UInt32),UInt32,POINTER(win32more.UI.WindowsAndMessaging.HICON), use_last_error=False)(("HICON_UserSize64", windll["OLE32"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HICON_UserMarshal64():
    try:
        return WINFUNCTYPE(c_char_p_no,POINTER(UInt32),c_char_p_no,POINTER(win32more.UI.WindowsAndMessaging.HICON), use_last_error=False)(("HICON_UserMarshal64", windll["OLE32"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HICON_UserUnmarshal64():
    try:
        return WINFUNCTYPE(c_char_p_no,POINTER(UInt32),POINTER(Byte),POINTER(win32more.UI.WindowsAndMessaging.HICON), use_last_error=False)(("HICON_UserUnmarshal64", windll["OLE32"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HICON_UserFree64():
    try:
        return WINFUNCTYPE(Void,POINTER(UInt32),POINTER(win32more.UI.WindowsAndMessaging.HICON), use_last_error=False)(("HICON_UserFree64", windll["OLE32"]), ((1, 'param0'),(1, 'param1'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SNB_UserSize64():
    try:
        return WINFUNCTYPE(UInt32,POINTER(UInt32),UInt32,POINTER(POINTER(POINTER(UInt16))), use_last_error=False)(("SNB_UserSize64", windll["ole32"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SNB_UserMarshal64():
    try:
        return WINFUNCTYPE(c_char_p_no,POINTER(UInt32),c_char_p_no,POINTER(POINTER(POINTER(UInt16))), use_last_error=False)(("SNB_UserMarshal64", windll["ole32"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SNB_UserUnmarshal64():
    try:
        return WINFUNCTYPE(c_char_p_no,POINTER(UInt32),POINTER(Byte),POINTER(POINTER(POINTER(UInt16))), use_last_error=False)(("SNB_UserUnmarshal64", windll["ole32"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SNB_UserFree64():
    try:
        return WINFUNCTYPE(Void,POINTER(UInt32),POINTER(POINTER(POINTER(UInt16))), use_last_error=False)(("SNB_UserFree64", windll["ole32"]), ((1, 'param0'),(1, 'param1'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_STGMEDIUM_UserSize64():
    try:
        return WINFUNCTYPE(UInt32,POINTER(UInt32),UInt32,POINTER(win32more.System.Com.STGMEDIUM_head), use_last_error=False)(("STGMEDIUM_UserSize64", windll["OLE32"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_STGMEDIUM_UserMarshal64():
    try:
        return WINFUNCTYPE(c_char_p_no,POINTER(UInt32),c_char_p_no,POINTER(win32more.System.Com.STGMEDIUM_head), use_last_error=False)(("STGMEDIUM_UserMarshal64", windll["OLE32"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_STGMEDIUM_UserUnmarshal64():
    try:
        return WINFUNCTYPE(c_char_p_no,POINTER(UInt32),POINTER(Byte),POINTER(win32more.System.Com.STGMEDIUM_head), use_last_error=False)(("STGMEDIUM_UserUnmarshal64", windll["OLE32"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_STGMEDIUM_UserFree64():
    try:
        return WINFUNCTYPE(Void,POINTER(UInt32),POINTER(win32more.System.Com.STGMEDIUM_head), use_last_error=False)(("STGMEDIUM_UserFree64", windll["OLE32"]), ((1, 'param0'),(1, 'param1'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CoGetMarshalSizeMax():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32),POINTER(Guid),win32more.System.Com.IUnknown_head,UInt32,c_void_p,UInt32, use_last_error=False)(("CoGetMarshalSizeMax", windll["OLE32"]), ((1, 'pulSize'),(1, 'riid'),(1, 'pUnk'),(1, 'dwDestContext'),(1, 'pvDestContext'),(1, 'mshlflags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CoMarshalInterface():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IStream_head,POINTER(Guid),win32more.System.Com.IUnknown_head,UInt32,c_void_p,UInt32, use_last_error=False)(("CoMarshalInterface", windll["OLE32"]), ((1, 'pStm'),(1, 'riid'),(1, 'pUnk'),(1, 'dwDestContext'),(1, 'pvDestContext'),(1, 'mshlflags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CoUnmarshalInterface():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IStream_head,POINTER(Guid),POINTER(c_void_p), use_last_error=False)(("CoUnmarshalInterface", windll["OLE32"]), ((1, 'pStm'),(1, 'riid'),(1, 'ppv'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CoMarshalHresult():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IStream_head,win32more.Foundation.HRESULT, use_last_error=False)(("CoMarshalHresult", windll["OLE32"]), ((1, 'pstm'),(1, 'hresult'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CoUnmarshalHresult():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IStream_head,POINTER(win32more.Foundation.HRESULT), use_last_error=False)(("CoUnmarshalHresult", windll["OLE32"]), ((1, 'pstm'),(1, 'phresult'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CoReleaseMarshalData():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IStream_head, use_last_error=False)(("CoReleaseMarshalData", windll["OLE32"]), ((1, 'pStm'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CoGetStandardMarshal():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),win32more.System.Com.IUnknown_head,UInt32,c_void_p,UInt32,POINTER(win32more.System.Com.Marshal.IMarshal_head), use_last_error=False)(("CoGetStandardMarshal", windll["OLE32"]), ((1, 'riid'),(1, 'pUnk'),(1, 'dwDestContext'),(1, 'pvDestContext'),(1, 'mshlflags'),(1, 'ppMarshal'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CoGetStdMarshalEx():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head,UInt32,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(("CoGetStdMarshalEx", windll["OLE32"]), ((1, 'pUnkOuter'),(1, 'smexflags'),(1, 'ppUnkInner'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CoMarshalInterThreadInterfaceInStream():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),win32more.System.Com.IUnknown_head,POINTER(win32more.System.Com.IStream_head), use_last_error=False)(("CoMarshalInterThreadInterfaceInStream", windll["OLE32"]), ((1, 'riid'),(1, 'pUnk'),(1, 'ppStm'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_LPSAFEARRAY_UserSize():
    try:
        return WINFUNCTYPE(UInt32,POINTER(UInt32),UInt32,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)), use_last_error=False)(("LPSAFEARRAY_UserSize", windll["OLEAUT32"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_LPSAFEARRAY_UserMarshal():
    try:
        return WINFUNCTYPE(c_char_p_no,POINTER(UInt32),c_char_p_no,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)), use_last_error=False)(("LPSAFEARRAY_UserMarshal", windll["OLEAUT32"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_LPSAFEARRAY_UserUnmarshal():
    try:
        return WINFUNCTYPE(c_char_p_no,POINTER(UInt32),POINTER(Byte),POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)), use_last_error=False)(("LPSAFEARRAY_UserUnmarshal", windll["OLEAUT32"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_LPSAFEARRAY_UserFree():
    try:
        return WINFUNCTYPE(Void,POINTER(UInt32),POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)), use_last_error=False)(("LPSAFEARRAY_UserFree", windll["OLEAUT32"]), ((1, 'param0'),(1, 'param1'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_LPSAFEARRAY_UserSize64():
    try:
        return WINFUNCTYPE(UInt32,POINTER(UInt32),UInt32,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)), use_last_error=False)(("LPSAFEARRAY_UserSize64", windll["OLEAUT32"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_LPSAFEARRAY_UserMarshal64():
    try:
        return WINFUNCTYPE(c_char_p_no,POINTER(UInt32),c_char_p_no,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)), use_last_error=False)(("LPSAFEARRAY_UserMarshal64", windll["OLEAUT32"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_LPSAFEARRAY_UserUnmarshal64():
    try:
        return WINFUNCTYPE(c_char_p_no,POINTER(UInt32),POINTER(Byte),POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)), use_last_error=False)(("LPSAFEARRAY_UserUnmarshal64", windll["OLEAUT32"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_LPSAFEARRAY_UserFree64():
    try:
        return WINFUNCTYPE(Void,POINTER(UInt32),POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)), use_last_error=False)(("LPSAFEARRAY_UserFree64", windll["OLEAUT32"]), ((1, 'param0'),(1, 'param1'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HACCEL_UserSize():
    try:
        return WINFUNCTYPE(UInt32,POINTER(UInt32),UInt32,POINTER(win32more.UI.WindowsAndMessaging.HACCEL), use_last_error=False)(("HACCEL_UserSize", windll["OLE32"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HACCEL_UserMarshal():
    try:
        return WINFUNCTYPE(c_char_p_no,POINTER(UInt32),c_char_p_no,POINTER(win32more.UI.WindowsAndMessaging.HACCEL), use_last_error=False)(("HACCEL_UserMarshal", windll["OLE32"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HACCEL_UserUnmarshal():
    try:
        return WINFUNCTYPE(c_char_p_no,POINTER(UInt32),POINTER(Byte),POINTER(win32more.UI.WindowsAndMessaging.HACCEL), use_last_error=False)(("HACCEL_UserUnmarshal", windll["OLE32"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HACCEL_UserFree():
    try:
        return WINFUNCTYPE(Void,POINTER(UInt32),POINTER(win32more.UI.WindowsAndMessaging.HACCEL), use_last_error=False)(("HACCEL_UserFree", windll["OLE32"]), ((1, 'param0'),(1, 'param1'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HGLOBAL_UserSize():
    try:
        return WINFUNCTYPE(UInt32,POINTER(UInt32),UInt32,POINTER(IntPtr), use_last_error=False)(("HGLOBAL_UserSize", windll["OLE32"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HGLOBAL_UserMarshal():
    try:
        return WINFUNCTYPE(c_char_p_no,POINTER(UInt32),c_char_p_no,POINTER(IntPtr), use_last_error=False)(("HGLOBAL_UserMarshal", windll["OLE32"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HGLOBAL_UserUnmarshal():
    try:
        return WINFUNCTYPE(c_char_p_no,POINTER(UInt32),POINTER(Byte),POINTER(IntPtr), use_last_error=False)(("HGLOBAL_UserUnmarshal", windll["OLE32"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HGLOBAL_UserFree():
    try:
        return WINFUNCTYPE(Void,POINTER(UInt32),POINTER(IntPtr), use_last_error=False)(("HGLOBAL_UserFree", windll["OLE32"]), ((1, 'param0'),(1, 'param1'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HMENU_UserSize():
    try:
        return WINFUNCTYPE(UInt32,POINTER(UInt32),UInt32,POINTER(win32more.UI.WindowsAndMessaging.HMENU), use_last_error=False)(("HMENU_UserSize", windll["OLE32"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HMENU_UserMarshal():
    try:
        return WINFUNCTYPE(c_char_p_no,POINTER(UInt32),c_char_p_no,POINTER(win32more.UI.WindowsAndMessaging.HMENU), use_last_error=False)(("HMENU_UserMarshal", windll["OLE32"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HMENU_UserUnmarshal():
    try:
        return WINFUNCTYPE(c_char_p_no,POINTER(UInt32),POINTER(Byte),POINTER(win32more.UI.WindowsAndMessaging.HMENU), use_last_error=False)(("HMENU_UserUnmarshal", windll["OLE32"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HMENU_UserFree():
    try:
        return WINFUNCTYPE(Void,POINTER(UInt32),POINTER(win32more.UI.WindowsAndMessaging.HMENU), use_last_error=False)(("HMENU_UserFree", windll["OLE32"]), ((1, 'param0'),(1, 'param1'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HACCEL_UserSize64():
    try:
        return WINFUNCTYPE(UInt32,POINTER(UInt32),UInt32,POINTER(win32more.UI.WindowsAndMessaging.HACCEL), use_last_error=False)(("HACCEL_UserSize64", windll["OLE32"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HACCEL_UserMarshal64():
    try:
        return WINFUNCTYPE(c_char_p_no,POINTER(UInt32),c_char_p_no,POINTER(win32more.UI.WindowsAndMessaging.HACCEL), use_last_error=False)(("HACCEL_UserMarshal64", windll["OLE32"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HACCEL_UserUnmarshal64():
    try:
        return WINFUNCTYPE(c_char_p_no,POINTER(UInt32),POINTER(Byte),POINTER(win32more.UI.WindowsAndMessaging.HACCEL), use_last_error=False)(("HACCEL_UserUnmarshal64", windll["OLE32"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HACCEL_UserFree64():
    try:
        return WINFUNCTYPE(Void,POINTER(UInt32),POINTER(win32more.UI.WindowsAndMessaging.HACCEL), use_last_error=False)(("HACCEL_UserFree64", windll["OLE32"]), ((1, 'param0'),(1, 'param1'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HGLOBAL_UserSize64():
    try:
        return WINFUNCTYPE(UInt32,POINTER(UInt32),UInt32,POINTER(IntPtr), use_last_error=False)(("HGLOBAL_UserSize64", windll["OLE32"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HGLOBAL_UserMarshal64():
    try:
        return WINFUNCTYPE(c_char_p_no,POINTER(UInt32),c_char_p_no,POINTER(IntPtr), use_last_error=False)(("HGLOBAL_UserMarshal64", windll["OLE32"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HGLOBAL_UserUnmarshal64():
    try:
        return WINFUNCTYPE(c_char_p_no,POINTER(UInt32),POINTER(Byte),POINTER(IntPtr), use_last_error=False)(("HGLOBAL_UserUnmarshal64", windll["OLE32"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HGLOBAL_UserFree64():
    try:
        return WINFUNCTYPE(Void,POINTER(UInt32),POINTER(IntPtr), use_last_error=False)(("HGLOBAL_UserFree64", windll["OLE32"]), ((1, 'param0'),(1, 'param1'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HMENU_UserSize64():
    try:
        return WINFUNCTYPE(UInt32,POINTER(UInt32),UInt32,POINTER(win32more.UI.WindowsAndMessaging.HMENU), use_last_error=False)(("HMENU_UserSize64", windll["OLE32"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HMENU_UserMarshal64():
    try:
        return WINFUNCTYPE(c_char_p_no,POINTER(UInt32),c_char_p_no,POINTER(win32more.UI.WindowsAndMessaging.HMENU), use_last_error=False)(("HMENU_UserMarshal64", windll["OLE32"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HMENU_UserUnmarshal64():
    try:
        return WINFUNCTYPE(c_char_p_no,POINTER(UInt32),POINTER(Byte),POINTER(win32more.UI.WindowsAndMessaging.HMENU), use_last_error=False)(("HMENU_UserUnmarshal64", windll["OLE32"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HMENU_UserFree64():
    try:
        return WINFUNCTYPE(Void,POINTER(UInt32),POINTER(win32more.UI.WindowsAndMessaging.HMENU), use_last_error=False)(("HMENU_UserFree64", windll["OLE32"]), ((1, 'param0'),(1, 'param1'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HPALETTE_UserSize():
    try:
        return WINFUNCTYPE(UInt32,POINTER(UInt32),UInt32,POINTER(win32more.Graphics.Gdi.HPALETTE), use_last_error=False)(("HPALETTE_UserSize", windll["OLE32"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HPALETTE_UserMarshal():
    try:
        return WINFUNCTYPE(c_char_p_no,POINTER(UInt32),c_char_p_no,POINTER(win32more.Graphics.Gdi.HPALETTE), use_last_error=False)(("HPALETTE_UserMarshal", windll["OLE32"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HPALETTE_UserUnmarshal():
    try:
        return WINFUNCTYPE(c_char_p_no,POINTER(UInt32),POINTER(Byte),POINTER(win32more.Graphics.Gdi.HPALETTE), use_last_error=False)(("HPALETTE_UserUnmarshal", windll["OLE32"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HPALETTE_UserFree():
    try:
        return WINFUNCTYPE(Void,POINTER(UInt32),POINTER(win32more.Graphics.Gdi.HPALETTE), use_last_error=False)(("HPALETTE_UserFree", windll["OLE32"]), ((1, 'param0'),(1, 'param1'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HPALETTE_UserSize64():
    try:
        return WINFUNCTYPE(UInt32,POINTER(UInt32),UInt32,POINTER(win32more.Graphics.Gdi.HPALETTE), use_last_error=False)(("HPALETTE_UserSize64", windll["OLE32"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HPALETTE_UserMarshal64():
    try:
        return WINFUNCTYPE(c_char_p_no,POINTER(UInt32),c_char_p_no,POINTER(win32more.Graphics.Gdi.HPALETTE), use_last_error=False)(("HPALETTE_UserMarshal64", windll["OLE32"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HPALETTE_UserUnmarshal64():
    try:
        return WINFUNCTYPE(c_char_p_no,POINTER(UInt32),POINTER(Byte),POINTER(win32more.Graphics.Gdi.HPALETTE), use_last_error=False)(("HPALETTE_UserUnmarshal64", windll["OLE32"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HPALETTE_UserFree64():
    try:
        return WINFUNCTYPE(Void,POINTER(UInt32),POINTER(win32more.Graphics.Gdi.HPALETTE), use_last_error=False)(("HPALETTE_UserFree64", windll["OLE32"]), ((1, 'param0'),(1, 'param1'),))
    except (FileNotFoundError, AttributeError):
        return None
__all__ = [
    "IMarshal",
    "IMarshal2",
    "IMarshalingStream",
    "STDMSHLFLAGS",
    "SMEXF_SERVER",
    "SMEXF_HANDLER",
    "BSTR_UserSize",
    "BSTR_UserMarshal",
    "BSTR_UserUnmarshal",
    "BSTR_UserFree",
    "HWND_UserSize",
    "HWND_UserMarshal",
    "HWND_UserUnmarshal",
    "HWND_UserFree",
    "VARIANT_UserSize",
    "VARIANT_UserMarshal",
    "VARIANT_UserUnmarshal",
    "VARIANT_UserFree",
    "BSTR_UserSize64",
    "BSTR_UserMarshal64",
    "BSTR_UserUnmarshal64",
    "BSTR_UserFree64",
    "HWND_UserSize64",
    "HWND_UserMarshal64",
    "HWND_UserUnmarshal64",
    "HWND_UserFree64",
    "VARIANT_UserSize64",
    "VARIANT_UserMarshal64",
    "VARIANT_UserUnmarshal64",
    "VARIANT_UserFree64",
    "CLIPFORMAT_UserSize",
    "CLIPFORMAT_UserMarshal",
    "CLIPFORMAT_UserUnmarshal",
    "CLIPFORMAT_UserFree",
    "HBITMAP_UserSize",
    "HBITMAP_UserMarshal",
    "HBITMAP_UserUnmarshal",
    "HBITMAP_UserFree",
    "HDC_UserSize",
    "HDC_UserMarshal",
    "HDC_UserUnmarshal",
    "HDC_UserFree",
    "HICON_UserSize",
    "HICON_UserMarshal",
    "HICON_UserUnmarshal",
    "HICON_UserFree",
    "SNB_UserSize",
    "SNB_UserMarshal",
    "SNB_UserUnmarshal",
    "SNB_UserFree",
    "STGMEDIUM_UserSize",
    "STGMEDIUM_UserMarshal",
    "STGMEDIUM_UserUnmarshal",
    "STGMEDIUM_UserFree",
    "CLIPFORMAT_UserSize64",
    "CLIPFORMAT_UserMarshal64",
    "CLIPFORMAT_UserUnmarshal64",
    "CLIPFORMAT_UserFree64",
    "HBITMAP_UserSize64",
    "HBITMAP_UserMarshal64",
    "HBITMAP_UserUnmarshal64",
    "HBITMAP_UserFree64",
    "HDC_UserSize64",
    "HDC_UserMarshal64",
    "HDC_UserUnmarshal64",
    "HDC_UserFree64",
    "HICON_UserSize64",
    "HICON_UserMarshal64",
    "HICON_UserUnmarshal64",
    "HICON_UserFree64",
    "SNB_UserSize64",
    "SNB_UserMarshal64",
    "SNB_UserUnmarshal64",
    "SNB_UserFree64",
    "STGMEDIUM_UserSize64",
    "STGMEDIUM_UserMarshal64",
    "STGMEDIUM_UserUnmarshal64",
    "STGMEDIUM_UserFree64",
    "CoGetMarshalSizeMax",
    "CoMarshalInterface",
    "CoUnmarshalInterface",
    "CoMarshalHresult",
    "CoUnmarshalHresult",
    "CoReleaseMarshalData",
    "CoGetStandardMarshal",
    "CoGetStdMarshalEx",
    "CoMarshalInterThreadInterfaceInStream",
    "LPSAFEARRAY_UserSize",
    "LPSAFEARRAY_UserMarshal",
    "LPSAFEARRAY_UserUnmarshal",
    "LPSAFEARRAY_UserFree",
    "LPSAFEARRAY_UserSize64",
    "LPSAFEARRAY_UserMarshal64",
    "LPSAFEARRAY_UserUnmarshal64",
    "LPSAFEARRAY_UserFree64",
    "HACCEL_UserSize",
    "HACCEL_UserMarshal",
    "HACCEL_UserUnmarshal",
    "HACCEL_UserFree",
    "HGLOBAL_UserSize",
    "HGLOBAL_UserMarshal",
    "HGLOBAL_UserUnmarshal",
    "HGLOBAL_UserFree",
    "HMENU_UserSize",
    "HMENU_UserMarshal",
    "HMENU_UserUnmarshal",
    "HMENU_UserFree",
    "HACCEL_UserSize64",
    "HACCEL_UserMarshal64",
    "HACCEL_UserUnmarshal64",
    "HACCEL_UserFree64",
    "HGLOBAL_UserSize64",
    "HGLOBAL_UserMarshal64",
    "HGLOBAL_UserUnmarshal64",
    "HGLOBAL_UserFree64",
    "HMENU_UserSize64",
    "HMENU_UserMarshal64",
    "HMENU_UserUnmarshal64",
    "HMENU_UserFree64",
    "HPALETTE_UserSize",
    "HPALETTE_UserMarshal",
    "HPALETTE_UserUnmarshal",
    "HPALETTE_UserFree",
    "HPALETTE_UserSize64",
    "HPALETTE_UserMarshal64",
    "HPALETTE_UserUnmarshal64",
    "HPALETTE_UserFree64",
]
