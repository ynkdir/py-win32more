from win32more import *
import win32more.Foundation
import win32more.Media.MediaFoundation
import win32more.System.WinRT

def __getattr__(name):
    module = globals()
    try:
        f = module[f"_define_{name}"]
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    module[name] = f()
    return module[name]
def __dir__():
    return __all__
CLSID_AudioFrameNativeFactory = '16a0a3b9-9f65-4102-9367-2cda3a4f372a'
CLSID_VideoFrameNativeFactory = 'd194386a-04e3-4814-8100-b2b0ae6d78c7'
def _define_IAudioFrameNative_head():
    class IAudioFrameNative(win32more.System.WinRT.IInspectable_head):
        Guid = Guid('20be1e2e-930f-4746-9335-3c332f255093')
    return IAudioFrameNative
def _define_IAudioFrameNative():
    IAudioFrameNative = win32more.System.WinRT.Media.IAudioFrameNative_head
    IAudioFrameNative.GetData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(c_void_p), use_last_error=False)(6, 'GetData', ((1, 'riid'),(1, 'ppv'),)))
    return IAudioFrameNative
def _define_IVideoFrameNative_head():
    class IVideoFrameNative(win32more.System.WinRT.IInspectable_head):
        Guid = Guid('26ba702b-314a-4620-aaf6-7a51aa58fa18')
    return IVideoFrameNative
def _define_IVideoFrameNative():
    IVideoFrameNative = win32more.System.WinRT.Media.IVideoFrameNative_head
    IVideoFrameNative.GetData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(c_void_p), use_last_error=False)(6, 'GetData', ((1, 'riid'),(1, 'ppv'),)))
    IVideoFrameNative.GetDevice = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(c_void_p), use_last_error=False)(7, 'GetDevice', ((1, 'riid'),(1, 'ppv'),)))
    return IVideoFrameNative
def _define_IAudioFrameNativeFactory_head():
    class IAudioFrameNativeFactory(win32more.System.WinRT.IInspectable_head):
        Guid = Guid('7bd67cf8-bf7d-43e6-af8d-b170ee0c0110')
    return IAudioFrameNativeFactory
def _define_IAudioFrameNativeFactory():
    IAudioFrameNativeFactory = win32more.System.WinRT.Media.IAudioFrameNativeFactory_head
    IAudioFrameNativeFactory.CreateFromMFSample = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.MediaFoundation.IMFSample_head,win32more.Foundation.BOOL,POINTER(Guid),POINTER(c_void_p), use_last_error=False)(6, 'CreateFromMFSample', ((1, 'data'),(1, 'forceReadOnly'),(1, 'riid'),(1, 'ppv'),)))
    return IAudioFrameNativeFactory
def _define_IVideoFrameNativeFactory_head():
    class IVideoFrameNativeFactory(win32more.System.WinRT.IInspectable_head):
        Guid = Guid('69e3693e-8e1e-4e63-ac4c-7fdc21d9731d')
    return IVideoFrameNativeFactory
def _define_IVideoFrameNativeFactory():
    IVideoFrameNativeFactory = win32more.System.WinRT.Media.IVideoFrameNativeFactory_head
    IVideoFrameNativeFactory.CreateFromMFSample = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.MediaFoundation.IMFSample_head,POINTER(Guid),UInt32,UInt32,win32more.Foundation.BOOL,POINTER(win32more.Media.MediaFoundation.MFVideoArea_head),win32more.Media.MediaFoundation.IMFDXGIDeviceManager_head,POINTER(Guid),POINTER(c_void_p), use_last_error=False)(6, 'CreateFromMFSample', ((1, 'data'),(1, 'subtype'),(1, 'width'),(1, 'height'),(1, 'forceReadOnly'),(1, 'minDisplayAperture'),(1, 'device'),(1, 'riid'),(1, 'ppv'),)))
    return IVideoFrameNativeFactory
__all__ = [
    "CLSID_AudioFrameNativeFactory",
    "CLSID_VideoFrameNativeFactory",
    "IAudioFrameNative",
    "IVideoFrameNative",
    "IAudioFrameNativeFactory",
    "IVideoFrameNativeFactory",
]
