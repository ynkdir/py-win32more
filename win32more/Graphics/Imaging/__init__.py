from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import win32more.Foundation
import win32more.Graphics.Direct2D.Common
import win32more.Graphics.Dxgi.Common
import win32more.Graphics.Gdi
import win32more.Graphics.Imaging
import win32more.System.Com
import win32more.System.Com.StructuredStorage
import win32more.UI.WindowsAndMessaging
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        if name in _arch_optional:
            return None
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
def __dir__():
    return __all__
WINCODEC_SDK_VERSION1: UInt32 = 566
WINCODEC_SDK_VERSION2: UInt32 = 567
CLSID_WICImagingFactory: Guid = Guid('cacaf262-9370-4615-a1-3b-9f-55-39-da-4c-0a')
CLSID_WICImagingFactory1: Guid = Guid('cacaf262-9370-4615-a1-3b-9f-55-39-da-4c-0a')
CLSID_WICImagingFactory2: Guid = Guid('317d06e8-5f24-433d-bd-f7-79-ce-68-d8-ab-c2')
WINCODEC_SDK_VERSION: UInt32 = 567
GUID_VendorMicrosoft: Guid = Guid('f0e749ca-edef-4589-a7-3a-ee-0e-62-6a-2a-2b')
GUID_VendorMicrosoftBuiltIn: Guid = Guid('257a30fd-06b6-462b-ae-a4-63-f7-0b-86-e5-33')
CLSID_WICPngDecoder: Guid = Guid('389ea17b-5078-4cde-b6-ef-25-c1-51-75-c7-51')
CLSID_WICPngDecoder1: Guid = Guid('389ea17b-5078-4cde-b6-ef-25-c1-51-75-c7-51')
CLSID_WICPngDecoder2: Guid = Guid('e018945b-aa86-4008-9b-d4-67-77-a1-e4-0c-11')
CLSID_WICBmpDecoder: Guid = Guid('6b462062-7cbf-400d-9f-db-81-3d-d1-0f-27-78')
CLSID_WICIcoDecoder: Guid = Guid('c61bfcdf-2e0f-4aad-a8-d7-e0-6b-af-eb-cd-fe')
CLSID_WICJpegDecoder: Guid = Guid('9456a480-e88b-43ea-9e-73-0b-2d-9b-71-b1-ca')
CLSID_WICGifDecoder: Guid = Guid('381dda3c-9ce9-4834-a2-3e-1f-98-f8-fc-52-be')
CLSID_WICTiffDecoder: Guid = Guid('b54e85d9-fe23-499f-8b-88-6a-ce-a7-13-75-2b')
CLSID_WICWmpDecoder: Guid = Guid('a26cec36-234c-4950-ae-16-e3-4a-ac-e7-1d-0d')
CLSID_WICDdsDecoder: Guid = Guid('9053699f-a341-429d-9e-90-ee-43-7c-f8-0c-73')
CLSID_WICBmpEncoder: Guid = Guid('69be8bb4-d66d-47c8-86-5a-ed-15-89-43-37-82')
CLSID_WICPngEncoder: Guid = Guid('27949969-876a-41d7-94-47-56-8f-6a-35-a4-dc')
CLSID_WICJpegEncoder: Guid = Guid('1a34f5c1-4a5a-46dc-b6-44-1f-45-67-e7-a6-76')
CLSID_WICGifEncoder: Guid = Guid('114f5598-0b22-40a0-86-a1-c8-3e-a4-95-ad-bd')
CLSID_WICTiffEncoder: Guid = Guid('0131be10-2001-4c5f-a9-b0-cc-88-fa-b6-4c-e8')
CLSID_WICWmpEncoder: Guid = Guid('ac4ce3cb-e1c1-44cd-82-15-5a-16-65-50-9e-c2')
CLSID_WICDdsEncoder: Guid = Guid('a61dde94-66ce-4ac1-88-1b-71-68-05-88-89-5e')
CLSID_WICAdngDecoder: Guid = Guid('981d9411-909e-42a7-8f-5d-a7-47-ff-05-2e-db')
CLSID_WICJpegQualcommPhoneEncoder: Guid = Guid('68ed5c62-f534-4979-b2-b3-68-6a-12-b2-b3-4c')
CLSID_WICHeifDecoder: Guid = Guid('e9a4a80a-44fe-4de4-89-71-71-50-b1-0a-51-99')
CLSID_WICHeifEncoder: Guid = Guid('0dbecec1-9eb3-4860-9c-6f-dd-be-86-63-45-75')
CLSID_WICWebpDecoder: Guid = Guid('7693e886-51c9-4070-84-19-9f-70-73-8e-c8-fa')
CLSID_WICRAWDecoder: Guid = Guid('41945702-8302-44a6-94-45-ac-98-e8-af-a0-86')
GUID_ContainerFormatBmp: Guid = Guid('0af1d87e-fcfe-4188-bd-eb-a7-90-64-71-cb-e3')
GUID_ContainerFormatPng: Guid = Guid('1b7cfaf4-713f-473c-bb-cd-61-37-42-5f-ae-af')
GUID_ContainerFormatIco: Guid = Guid('a3a860c4-338f-4c17-91-9a-fb-a4-b5-62-8f-21')
GUID_ContainerFormatJpeg: Guid = Guid('19e4a5aa-5662-4fc5-a0-c0-17-58-02-8e-10-57')
GUID_ContainerFormatTiff: Guid = Guid('163bcc30-e2e9-4f0b-96-1d-a3-e9-fd-b7-88-a3')
GUID_ContainerFormatGif: Guid = Guid('1f8a5601-7d4d-4cbd-9c-82-1b-c8-d4-ee-b9-a5')
GUID_ContainerFormatWmp: Guid = Guid('57a37caa-367a-4540-91-6b-f1-83-c5-09-3a-4b')
GUID_ContainerFormatDds: Guid = Guid('9967cb95-2e85-4ac8-8c-a2-83-d7-cc-d4-25-c9')
GUID_ContainerFormatAdng: Guid = Guid('f3ff6d0d-38c0-41c4-b1-fe-1f-38-24-f1-7b-84')
GUID_ContainerFormatHeif: Guid = Guid('e1e62521-6787-405b-a3-39-50-07-15-b5-76-3f')
GUID_ContainerFormatWebp: Guid = Guid('e094b0e2-67f2-45b3-b0-ea-11-53-37-ca-7c-f3')
GUID_ContainerFormatRaw: Guid = Guid('fe99ce60-f19c-433c-a3-ae-00-ac-ef-a9-ca-21')
CLSID_WICImagingCategories: Guid = Guid('fae3d380-fea4-4623-8c-75-c6-b6-11-10-b6-81')
CATID_WICBitmapDecoders: Guid = Guid('7ed96837-96f0-4812-b2-11-f1-3c-24-11-7e-d3')
CATID_WICBitmapEncoders: Guid = Guid('ac757296-3522-4e11-98-62-c1-7b-e5-a1-76-7e')
CATID_WICPixelFormats: Guid = Guid('2b46e70f-cda7-473e-89-f6-dc-96-30-a2-39-0b')
CATID_WICFormatConverters: Guid = Guid('7835eae8-bf14-49d1-93-ce-53-3a-40-7b-22-48')
CATID_WICMetadataReader: Guid = Guid('05af94d8-7174-4cd2-be-4a-41-24-b8-0e-e4-b8')
CATID_WICMetadataWriter: Guid = Guid('abe3b9a4-257d-4b97-bd-1a-29-4a-f4-96-22-2e')
CLSID_WICDefaultFormatConverter: Guid = Guid('1a3f11dc-b514-4b17-8c-5f-21-54-51-38-52-f1')
CLSID_WICFormatConverterHighColor: Guid = Guid('ac75d454-9f37-48f8-b9-72-4e-19-bc-85-60-11')
CLSID_WICFormatConverterNChannel: Guid = Guid('c17cabb2-d4a3-47d7-a5-57-33-9b-2e-fb-d4-f1')
CLSID_WICFormatConverterWMPhoto: Guid = Guid('9cb5172b-d600-46ba-ab-77-77-bb-7e-3a-00-d9')
CLSID_WICPlanarFormatConverter: Guid = Guid('184132b8-32f8-4784-91-31-dd-72-24-b2-34-38')
WIC_JPEG_MAX_COMPONENT_COUNT: UInt32 = 4
WIC_JPEG_MAX_TABLE_INDEX: UInt32 = 3
WIC_JPEG_SAMPLE_FACTORS_ONE: UInt32 = 17
WIC_JPEG_SAMPLE_FACTORS_THREE_420: UInt32 = 1118498
WIC_JPEG_SAMPLE_FACTORS_THREE_422: UInt32 = 1118497
WIC_JPEG_SAMPLE_FACTORS_THREE_440: UInt32 = 1118482
WIC_JPEG_SAMPLE_FACTORS_THREE_444: UInt32 = 1118481
WIC_JPEG_QUANTIZATION_BASELINE_ONE: UInt32 = 0
WIC_JPEG_QUANTIZATION_BASELINE_THREE: UInt32 = 65792
WIC_JPEG_HUFFMAN_BASELINE_ONE: UInt32 = 0
WIC_JPEG_HUFFMAN_BASELINE_THREE: UInt32 = 1118464
GUID_WICPixelFormatDontCare: Guid = Guid('6fddc324-4e03-4bfe-b1-85-3d-77-76-8d-c9-00')
GUID_WICPixelFormat1bppIndexed: Guid = Guid('6fddc324-4e03-4bfe-b1-85-3d-77-76-8d-c9-01')
GUID_WICPixelFormat2bppIndexed: Guid = Guid('6fddc324-4e03-4bfe-b1-85-3d-77-76-8d-c9-02')
GUID_WICPixelFormat4bppIndexed: Guid = Guid('6fddc324-4e03-4bfe-b1-85-3d-77-76-8d-c9-03')
GUID_WICPixelFormat8bppIndexed: Guid = Guid('6fddc324-4e03-4bfe-b1-85-3d-77-76-8d-c9-04')
GUID_WICPixelFormatBlackWhite: Guid = Guid('6fddc324-4e03-4bfe-b1-85-3d-77-76-8d-c9-05')
GUID_WICPixelFormat2bppGray: Guid = Guid('6fddc324-4e03-4bfe-b1-85-3d-77-76-8d-c9-06')
GUID_WICPixelFormat4bppGray: Guid = Guid('6fddc324-4e03-4bfe-b1-85-3d-77-76-8d-c9-07')
GUID_WICPixelFormat8bppGray: Guid = Guid('6fddc324-4e03-4bfe-b1-85-3d-77-76-8d-c9-08')
GUID_WICPixelFormat8bppAlpha: Guid = Guid('e6cd0116-eeba-4161-aa-85-27-dd-9f-b3-a8-95')
GUID_WICPixelFormat16bppBGR555: Guid = Guid('6fddc324-4e03-4bfe-b1-85-3d-77-76-8d-c9-09')
GUID_WICPixelFormat16bppBGR565: Guid = Guid('6fddc324-4e03-4bfe-b1-85-3d-77-76-8d-c9-0a')
GUID_WICPixelFormat16bppBGRA5551: Guid = Guid('05ec7c2b-f1e6-4961-ad-46-e1-cc-81-0a-87-d2')
GUID_WICPixelFormat16bppGray: Guid = Guid('6fddc324-4e03-4bfe-b1-85-3d-77-76-8d-c9-0b')
GUID_WICPixelFormat24bppBGR: Guid = Guid('6fddc324-4e03-4bfe-b1-85-3d-77-76-8d-c9-0c')
GUID_WICPixelFormat24bppRGB: Guid = Guid('6fddc324-4e03-4bfe-b1-85-3d-77-76-8d-c9-0d')
GUID_WICPixelFormat32bppBGR: Guid = Guid('6fddc324-4e03-4bfe-b1-85-3d-77-76-8d-c9-0e')
GUID_WICPixelFormat32bppBGRA: Guid = Guid('6fddc324-4e03-4bfe-b1-85-3d-77-76-8d-c9-0f')
GUID_WICPixelFormat32bppPBGRA: Guid = Guid('6fddc324-4e03-4bfe-b1-85-3d-77-76-8d-c9-10')
GUID_WICPixelFormat32bppGrayFloat: Guid = Guid('6fddc324-4e03-4bfe-b1-85-3d-77-76-8d-c9-11')
GUID_WICPixelFormat32bppRGB: Guid = Guid('d98c6b95-3efe-47d6-bb-25-eb-17-48-ab-0c-f1')
GUID_WICPixelFormat32bppRGBA: Guid = Guid('f5c7ad2d-6a8d-43dd-a7-a8-a2-99-35-26-1a-e9')
GUID_WICPixelFormat32bppPRGBA: Guid = Guid('3cc4a650-a527-4d37-a9-16-31-42-c7-eb-ed-ba')
GUID_WICPixelFormat48bppRGB: Guid = Guid('6fddc324-4e03-4bfe-b1-85-3d-77-76-8d-c9-15')
GUID_WICPixelFormat48bppBGR: Guid = Guid('e605a384-b468-46ce-bb-2e-36-f1-80-e6-43-13')
GUID_WICPixelFormat64bppRGB: Guid = Guid('a1182111-186d-4d42-bc-6a-9c-83-03-a8-df-f9')
GUID_WICPixelFormat64bppRGBA: Guid = Guid('6fddc324-4e03-4bfe-b1-85-3d-77-76-8d-c9-16')
GUID_WICPixelFormat64bppBGRA: Guid = Guid('1562ff7c-d352-46f9-97-9e-42-97-6b-79-22-46')
GUID_WICPixelFormat64bppPRGBA: Guid = Guid('6fddc324-4e03-4bfe-b1-85-3d-77-76-8d-c9-17')
GUID_WICPixelFormat64bppPBGRA: Guid = Guid('8c518e8e-a4ec-468b-ae-70-c9-a3-5a-9c-55-30')
GUID_WICPixelFormat16bppGrayFixedPoint: Guid = Guid('6fddc324-4e03-4bfe-b1-85-3d-77-76-8d-c9-13')
GUID_WICPixelFormat32bppBGR101010: Guid = Guid('6fddc324-4e03-4bfe-b1-85-3d-77-76-8d-c9-14')
GUID_WICPixelFormat48bppRGBFixedPoint: Guid = Guid('6fddc324-4e03-4bfe-b1-85-3d-77-76-8d-c9-12')
GUID_WICPixelFormat48bppBGRFixedPoint: Guid = Guid('49ca140e-cab6-493b-9d-df-60-18-7c-37-53-2a')
GUID_WICPixelFormat96bppRGBFixedPoint: Guid = Guid('6fddc324-4e03-4bfe-b1-85-3d-77-76-8d-c9-18')
GUID_WICPixelFormat96bppRGBFloat: Guid = Guid('e3fed78f-e8db-4acf-84-c1-e9-7f-61-36-b3-27')
GUID_WICPixelFormat128bppRGBAFloat: Guid = Guid('6fddc324-4e03-4bfe-b1-85-3d-77-76-8d-c9-19')
GUID_WICPixelFormat128bppPRGBAFloat: Guid = Guid('6fddc324-4e03-4bfe-b1-85-3d-77-76-8d-c9-1a')
GUID_WICPixelFormat128bppRGBFloat: Guid = Guid('6fddc324-4e03-4bfe-b1-85-3d-77-76-8d-c9-1b')
GUID_WICPixelFormat32bppCMYK: Guid = Guid('6fddc324-4e03-4bfe-b1-85-3d-77-76-8d-c9-1c')
GUID_WICPixelFormat64bppRGBAFixedPoint: Guid = Guid('6fddc324-4e03-4bfe-b1-85-3d-77-76-8d-c9-1d')
GUID_WICPixelFormat64bppBGRAFixedPoint: Guid = Guid('356de33c-54d2-4a23-bb-04-9b-7b-f9-b1-d4-2d')
GUID_WICPixelFormat64bppRGBFixedPoint: Guid = Guid('6fddc324-4e03-4bfe-b1-85-3d-77-76-8d-c9-40')
GUID_WICPixelFormat128bppRGBAFixedPoint: Guid = Guid('6fddc324-4e03-4bfe-b1-85-3d-77-76-8d-c9-1e')
GUID_WICPixelFormat128bppRGBFixedPoint: Guid = Guid('6fddc324-4e03-4bfe-b1-85-3d-77-76-8d-c9-41')
GUID_WICPixelFormat64bppRGBAHalf: Guid = Guid('6fddc324-4e03-4bfe-b1-85-3d-77-76-8d-c9-3a')
GUID_WICPixelFormat64bppPRGBAHalf: Guid = Guid('58ad26c2-c623-4d9d-b3-20-38-7e-49-f8-c4-42')
GUID_WICPixelFormat64bppRGBHalf: Guid = Guid('6fddc324-4e03-4bfe-b1-85-3d-77-76-8d-c9-42')
GUID_WICPixelFormat48bppRGBHalf: Guid = Guid('6fddc324-4e03-4bfe-b1-85-3d-77-76-8d-c9-3b')
GUID_WICPixelFormat32bppRGBE: Guid = Guid('6fddc324-4e03-4bfe-b1-85-3d-77-76-8d-c9-3d')
GUID_WICPixelFormat16bppGrayHalf: Guid = Guid('6fddc324-4e03-4bfe-b1-85-3d-77-76-8d-c9-3e')
GUID_WICPixelFormat32bppGrayFixedPoint: Guid = Guid('6fddc324-4e03-4bfe-b1-85-3d-77-76-8d-c9-3f')
GUID_WICPixelFormat32bppRGBA1010102: Guid = Guid('25238d72-fcf9-4522-b5-14-55-78-e5-ad-55-e0')
GUID_WICPixelFormat32bppRGBA1010102XR: Guid = Guid('00de6b9a-c101-434b-b5-02-d0-16-5e-e1-12-2c')
GUID_WICPixelFormat32bppR10G10B10A2: Guid = Guid('604e1bb5-8a3c-4b65-b1-1c-bc-0b-8d-d7-5b-7f')
GUID_WICPixelFormat32bppR10G10B10A2HDR10: Guid = Guid('9c215c5d-1acc-4f0e-a4-bc-70-fb-3a-e8-fd-28')
GUID_WICPixelFormat64bppCMYK: Guid = Guid('6fddc324-4e03-4bfe-b1-85-3d-77-76-8d-c9-1f')
GUID_WICPixelFormat24bpp3Channels: Guid = Guid('6fddc324-4e03-4bfe-b1-85-3d-77-76-8d-c9-20')
GUID_WICPixelFormat32bpp4Channels: Guid = Guid('6fddc324-4e03-4bfe-b1-85-3d-77-76-8d-c9-21')
GUID_WICPixelFormat40bpp5Channels: Guid = Guid('6fddc324-4e03-4bfe-b1-85-3d-77-76-8d-c9-22')
GUID_WICPixelFormat48bpp6Channels: Guid = Guid('6fddc324-4e03-4bfe-b1-85-3d-77-76-8d-c9-23')
GUID_WICPixelFormat56bpp7Channels: Guid = Guid('6fddc324-4e03-4bfe-b1-85-3d-77-76-8d-c9-24')
GUID_WICPixelFormat64bpp8Channels: Guid = Guid('6fddc324-4e03-4bfe-b1-85-3d-77-76-8d-c9-25')
GUID_WICPixelFormat48bpp3Channels: Guid = Guid('6fddc324-4e03-4bfe-b1-85-3d-77-76-8d-c9-26')
GUID_WICPixelFormat64bpp4Channels: Guid = Guid('6fddc324-4e03-4bfe-b1-85-3d-77-76-8d-c9-27')
GUID_WICPixelFormat80bpp5Channels: Guid = Guid('6fddc324-4e03-4bfe-b1-85-3d-77-76-8d-c9-28')
GUID_WICPixelFormat96bpp6Channels: Guid = Guid('6fddc324-4e03-4bfe-b1-85-3d-77-76-8d-c9-29')
GUID_WICPixelFormat112bpp7Channels: Guid = Guid('6fddc324-4e03-4bfe-b1-85-3d-77-76-8d-c9-2a')
GUID_WICPixelFormat128bpp8Channels: Guid = Guid('6fddc324-4e03-4bfe-b1-85-3d-77-76-8d-c9-2b')
GUID_WICPixelFormat40bppCMYKAlpha: Guid = Guid('6fddc324-4e03-4bfe-b1-85-3d-77-76-8d-c9-2c')
GUID_WICPixelFormat80bppCMYKAlpha: Guid = Guid('6fddc324-4e03-4bfe-b1-85-3d-77-76-8d-c9-2d')
GUID_WICPixelFormat32bpp3ChannelsAlpha: Guid = Guid('6fddc324-4e03-4bfe-b1-85-3d-77-76-8d-c9-2e')
GUID_WICPixelFormat40bpp4ChannelsAlpha: Guid = Guid('6fddc324-4e03-4bfe-b1-85-3d-77-76-8d-c9-2f')
GUID_WICPixelFormat48bpp5ChannelsAlpha: Guid = Guid('6fddc324-4e03-4bfe-b1-85-3d-77-76-8d-c9-30')
GUID_WICPixelFormat56bpp6ChannelsAlpha: Guid = Guid('6fddc324-4e03-4bfe-b1-85-3d-77-76-8d-c9-31')
GUID_WICPixelFormat64bpp7ChannelsAlpha: Guid = Guid('6fddc324-4e03-4bfe-b1-85-3d-77-76-8d-c9-32')
GUID_WICPixelFormat72bpp8ChannelsAlpha: Guid = Guid('6fddc324-4e03-4bfe-b1-85-3d-77-76-8d-c9-33')
GUID_WICPixelFormat64bpp3ChannelsAlpha: Guid = Guid('6fddc324-4e03-4bfe-b1-85-3d-77-76-8d-c9-34')
GUID_WICPixelFormat80bpp4ChannelsAlpha: Guid = Guid('6fddc324-4e03-4bfe-b1-85-3d-77-76-8d-c9-35')
GUID_WICPixelFormat96bpp5ChannelsAlpha: Guid = Guid('6fddc324-4e03-4bfe-b1-85-3d-77-76-8d-c9-36')
GUID_WICPixelFormat112bpp6ChannelsAlpha: Guid = Guid('6fddc324-4e03-4bfe-b1-85-3d-77-76-8d-c9-37')
GUID_WICPixelFormat128bpp7ChannelsAlpha: Guid = Guid('6fddc324-4e03-4bfe-b1-85-3d-77-76-8d-c9-38')
GUID_WICPixelFormat144bpp8ChannelsAlpha: Guid = Guid('6fddc324-4e03-4bfe-b1-85-3d-77-76-8d-c9-39')
GUID_WICPixelFormat8bppY: Guid = Guid('91b4db54-2df9-42f0-b4-49-29-09-bb-3d-f8-8e')
GUID_WICPixelFormat8bppCb: Guid = Guid('1339f224-6bfe-4c3e-93-02-e4-f3-a6-d0-ca-2a')
GUID_WICPixelFormat8bppCr: Guid = Guid('b8145053-2116-49f0-88-35-ed-84-4b-20-5c-51')
GUID_WICPixelFormat16bppCbCr: Guid = Guid('ff95ba6e-11e0-4263-bb-45-01-72-1f-34-60-a4')
GUID_WICPixelFormat16bppYQuantizedDctCoefficients: Guid = Guid('a355f433-48e8-4a42-84-d8-e2-aa-26-ca-80-a4')
GUID_WICPixelFormat16bppCbQuantizedDctCoefficients: Guid = Guid('d2c4ff61-56a5-49c2-8b-5c-4c-19-25-96-48-37')
GUID_WICPixelFormat16bppCrQuantizedDctCoefficients: Guid = Guid('2fe354f0-1680-42d8-92-31-e7-3c-05-65-bf-c1')
FACILITY_WINCODEC_ERR: UInt32 = 2200
WINCODEC_ERR_BASE: UInt32 = 8192
WINCODEC_ERR_GENERIC_ERROR: Int32 = -2147467259
WINCODEC_ERR_INVALIDPARAMETER: Int32 = -2147024809
WINCODEC_ERR_OUTOFMEMORY: Int32 = -2147024882
WINCODEC_ERR_NOTIMPLEMENTED: Int32 = -2147467263
WINCODEC_ERR_ABORTED: Int32 = -2147467260
WINCODEC_ERR_ACCESSDENIED: Int32 = -2147024891
WICRawChangeNotification_ExposureCompensation: UInt32 = 1
WICRawChangeNotification_NamedWhitePoint: UInt32 = 2
WICRawChangeNotification_KelvinWhitePoint: UInt32 = 4
WICRawChangeNotification_RGBWhitePoint: UInt32 = 8
WICRawChangeNotification_Contrast: UInt32 = 16
WICRawChangeNotification_Gamma: UInt32 = 32
WICRawChangeNotification_Sharpness: UInt32 = 64
WICRawChangeNotification_Saturation: UInt32 = 128
WICRawChangeNotification_Tint: UInt32 = 256
WICRawChangeNotification_NoiseReduction: UInt32 = 512
WICRawChangeNotification_DestinationColorContext: UInt32 = 1024
WICRawChangeNotification_ToneCurve: UInt32 = 2048
WICRawChangeNotification_Rotation: UInt32 = 4096
WICRawChangeNotification_RenderMode: UInt32 = 8192
GUID_MetadataFormatUnknown: Guid = Guid('a45e592f-9078-4a7c-ad-b5-4e-dc-4f-d6-1b-1f')
GUID_MetadataFormatIfd: Guid = Guid('537396c6-2d8a-4bb6-9b-f8-2f-0a-8e-2a-3a-df')
GUID_MetadataFormatSubIfd: Guid = Guid('58a2e128-2db9-4e57-bb-14-51-77-89-1e-d3-31')
GUID_MetadataFormatExif: Guid = Guid('1c3c4f9d-b84a-467d-94-93-36-cf-bd-59-ea-57')
GUID_MetadataFormatGps: Guid = Guid('7134ab8a-9351-44ad-af-62-44-8d-b6-b5-02-ec')
GUID_MetadataFormatInterop: Guid = Guid('ed686f8e-681f-4c8b-bd-41-a8-ad-db-f6-b3-fc')
GUID_MetadataFormatApp0: Guid = Guid('79007028-268d-45d6-a3-c2-35-4e-6a-50-4b-c9')
GUID_MetadataFormatApp1: Guid = Guid('8fd3dfc3-f951-492b-81-7f-69-c2-e6-d9-a5-b0')
GUID_MetadataFormatApp13: Guid = Guid('326556a2-f502-4354-9c-c0-8e-3f-48-ea-f6-b5')
GUID_MetadataFormatIPTC: Guid = Guid('4fab0914-e129-4087-a1-d1-bc-81-2d-45-a7-b5')
GUID_MetadataFormatIRB: Guid = Guid('16100d66-8570-4bb9-b9-2d-fd-a4-b2-3e-ce-67')
GUID_MetadataFormat8BIMIPTC: Guid = Guid('0010568c-0852-4e6a-b1-91-5c-33-ac-5b-04-30')
GUID_MetadataFormat8BIMResolutionInfo: Guid = Guid('739f305d-81db-43cb-ac-5e-55-01-3e-f9-f0-03')
GUID_MetadataFormat8BIMIPTCDigest: Guid = Guid('1ca32285-9ccd-4786-8b-d8-79-53-9d-b6-a0-06')
GUID_MetadataFormatXMP: Guid = Guid('bb5acc38-f216-4cec-a6-c5-5f-6e-73-97-63-a9')
GUID_MetadataFormatThumbnail: Guid = Guid('243dcee9-8703-40ee-8e-f0-22-a6-00-b8-05-8c')
GUID_MetadataFormatChunktEXt: Guid = Guid('568d8936-c0a9-4923-90-5d-df-2b-38-23-8f-bc')
GUID_MetadataFormatXMPStruct: Guid = Guid('22383cf1-ed17-4e2e-af-17-d8-5b-8f-6b-30-d0')
GUID_MetadataFormatXMPBag: Guid = Guid('833cca5f-dcb7-4516-80-6f-65-96-ab-26-dc-e4')
GUID_MetadataFormatXMPSeq: Guid = Guid('63e8df02-eb6c-456c-a2-24-b2-5e-79-4f-d6-48')
GUID_MetadataFormatXMPAlt: Guid = Guid('7b08a675-91aa-481b-a7-98-4d-a9-49-08-61-3b')
GUID_MetadataFormatLSD: Guid = Guid('e256031e-6299-4929-b9-8d-5a-c8-84-af-ba-92')
GUID_MetadataFormatIMD: Guid = Guid('bd2bb086-4d52-48dd-96-77-db-48-3e-85-ae-8f')
GUID_MetadataFormatGCE: Guid = Guid('2a25cad8-deeb-4c69-a7-88-0e-c2-26-6d-ca-fd')
GUID_MetadataFormatAPE: Guid = Guid('2e043dc2-c967-4e05-87-5e-61-8b-f6-7e-85-c3')
GUID_MetadataFormatJpegChrominance: Guid = Guid('f73d0dcf-cec6-4f85-9b-0e-1c-39-56-b1-be-f7')
GUID_MetadataFormatJpegLuminance: Guid = Guid('86908007-edfc-4860-8d-4b-4e-e6-e8-3e-60-58')
GUID_MetadataFormatJpegComment: Guid = Guid('220e5f33-afd3-474e-9d-31-7d-4f-e7-30-f5-57')
GUID_MetadataFormatGifComment: Guid = Guid('c4b6e0e0-cfb4-4ad3-ab-33-9a-ad-23-55-a3-4a')
GUID_MetadataFormatChunkgAMA: Guid = Guid('f00935a5-1d5d-4cd1-81-b2-93-24-d7-ec-a7-81')
GUID_MetadataFormatChunkbKGD: Guid = Guid('e14d3571-6b47-4dea-b6-0a-87-ce-0a-78-df-b7')
GUID_MetadataFormatChunkiTXt: Guid = Guid('c2bec729-0b68-4b77-aa-0e-62-95-a6-ac-18-14')
GUID_MetadataFormatChunkcHRM: Guid = Guid('9db3655b-2842-44b3-80-67-12-e9-b3-75-55-6a')
GUID_MetadataFormatChunkhIST: Guid = Guid('c59a82da-db74-48a4-bd-6a-b6-9c-49-31-ef-95')
GUID_MetadataFormatChunkiCCP: Guid = Guid('eb4349ab-b685-450f-91-b5-e8-02-e8-92-53-6c')
GUID_MetadataFormatChunksRGB: Guid = Guid('c115fd36-cc6f-4e3f-83-63-52-4b-87-c6-b0-d9')
GUID_MetadataFormatChunktIME: Guid = Guid('6b00ae2d-e24b-460a-98-b6-87-8b-d0-30-72-fd')
GUID_MetadataFormatDds: Guid = Guid('4a064603-8c33-4e60-9c-29-13-62-31-70-2d-08')
GUID_MetadataFormatHeif: Guid = Guid('817ef3e1-1288-45f4-a8-52-26-0d-9e-7c-ce-83')
GUID_MetadataFormatHeifHDR: Guid = Guid('568b8d8a-1e65-438c-89-68-d6-0e-10-12-be-b9')
GUID_MetadataFormatWebpANIM: Guid = Guid('6dc4fda6-78e6-4102-ae-35-bc-fa-1e-dc-c7-8b')
GUID_MetadataFormatWebpANMF: Guid = Guid('43c105ee-b93b-4abb-b0-03-a0-8c-0d-87-04-71')
CLSID_WICUnknownMetadataReader: Guid = Guid('699745c2-5066-4b82-a8-e3-d4-04-78-db-ec-8c')
CLSID_WICUnknownMetadataWriter: Guid = Guid('a09cca86-27ba-4f39-90-53-12-1f-a4-dc-08-fc')
CLSID_WICApp0MetadataWriter: Guid = Guid('f3c633a2-46c8-498e-8f-bb-cc-6f-72-1b-bc-de')
CLSID_WICApp0MetadataReader: Guid = Guid('43324b33-a78f-480f-91-11-96-38-aa-cc-c8-32')
CLSID_WICApp1MetadataWriter: Guid = Guid('ee366069-1832-420f-b3-81-04-79-ad-06-6f-19')
CLSID_WICApp1MetadataReader: Guid = Guid('dde33513-774e-4bcd-ae-79-02-f4-ad-fe-62-fc')
CLSID_WICApp13MetadataWriter: Guid = Guid('7b19a919-a9d6-49e5-bd-45-02-c3-4e-4e-4c-d5')
CLSID_WICApp13MetadataReader: Guid = Guid('aa7e3c50-864c-4604-bc-04-8b-0b-76-e6-37-f6')
CLSID_WICIfdMetadataReader: Guid = Guid('8f914656-9d0a-4eb2-90-19-0b-f9-6d-8a-9e-e6')
CLSID_WICIfdMetadataWriter: Guid = Guid('b1ebfc28-c9bd-47a2-8d-33-b9-48-76-97-77-a7')
CLSID_WICSubIfdMetadataReader: Guid = Guid('50d42f09-ecd1-4b41-b6-5d-da-1f-da-a7-56-63')
CLSID_WICSubIfdMetadataWriter: Guid = Guid('8ade5386-8e9b-4f4c-ac-f2-f0-00-87-06-b2-38')
CLSID_WICExifMetadataReader: Guid = Guid('d9403860-297f-4a49-bf-9b-77-89-81-50-a4-42')
CLSID_WICExifMetadataWriter: Guid = Guid('c9a14cda-c339-460b-90-78-d4-de-bc-fa-be-91')
CLSID_WICGpsMetadataReader: Guid = Guid('3697790b-223b-484e-99-25-c4-86-92-18-f1-7a')
CLSID_WICGpsMetadataWriter: Guid = Guid('cb8c13e4-62b5-4c96-a4-8b-6b-a6-ac-e3-9c-76')
CLSID_WICInteropMetadataReader: Guid = Guid('b5c8b898-0074-459f-b7-00-86-0d-46-51-ea-14')
CLSID_WICInteropMetadataWriter: Guid = Guid('122ec645-cd7e-44d8-b1-86-2c-8c-20-c3-b5-0f')
CLSID_WICThumbnailMetadataReader: Guid = Guid('fb012959-f4f6-44d7-9d-09-da-a0-87-a9-db-57')
CLSID_WICThumbnailMetadataWriter: Guid = Guid('d049b20c-5dd0-44fe-b0-b3-8f-92-c8-e6-d0-80')
CLSID_WICIPTCMetadataReader: Guid = Guid('03012959-f4f6-44d7-9d-09-da-a0-87-a9-db-57')
CLSID_WICIPTCMetadataWriter: Guid = Guid('1249b20c-5dd0-44fe-b0-b3-8f-92-c8-e6-d0-80')
CLSID_WICIRBMetadataReader: Guid = Guid('d4dcd3d7-b4c2-47d9-a6-bf-b8-9b-a3-96-a4-a3')
CLSID_WICIRBMetadataWriter: Guid = Guid('5c5c1935-0235-4434-80-bc-25-1b-c1-ec-39-c6')
CLSID_WIC8BIMIPTCMetadataReader: Guid = Guid('0010668c-0801-4da6-a4-a4-82-65-22-b6-d2-8f')
CLSID_WIC8BIMIPTCMetadataWriter: Guid = Guid('00108226-ee41-44a2-9e-9c-4b-e4-d5-b1-d2-cd')
CLSID_WIC8BIMResolutionInfoMetadataReader: Guid = Guid('5805137a-e348-4f7c-b3-cc-6d-b9-96-5a-05-99')
CLSID_WIC8BIMResolutionInfoMetadataWriter: Guid = Guid('4ff2fe0e-e74a-4b71-98-c4-ab-7d-c1-67-07-ba')
CLSID_WIC8BIMIPTCDigestMetadataReader: Guid = Guid('02805f1e-d5aa-415b-82-c5-61-c0-33-a9-88-a6')
CLSID_WIC8BIMIPTCDigestMetadataWriter: Guid = Guid('2db5e62b-0d67-495f-8f-9d-c2-f0-18-86-47-ac')
CLSID_WICPngTextMetadataReader: Guid = Guid('4b59afcc-b8c3-408a-b6-70-89-e5-fa-b6-fd-a7')
CLSID_WICPngTextMetadataWriter: Guid = Guid('b5ebafb9-253e-4a72-a7-44-07-62-d2-68-56-83')
CLSID_WICXMPMetadataReader: Guid = Guid('72b624df-ae11-4948-a6-5c-35-1e-b0-82-94-19')
CLSID_WICXMPMetadataWriter: Guid = Guid('1765e14e-1bd4-462e-b6-b1-59-0b-f1-26-2a-c6')
CLSID_WICXMPStructMetadataReader: Guid = Guid('01b90d9a-8209-47f7-9c-52-e1-24-4b-f5-0c-ed')
CLSID_WICXMPStructMetadataWriter: Guid = Guid('22c21f93-7ddb-411c-9b-17-c5-b7-bd-06-4a-bc')
CLSID_WICXMPBagMetadataReader: Guid = Guid('e7e79a30-4f2c-4fab-8d-00-39-4f-2d-6b-be-be')
CLSID_WICXMPBagMetadataWriter: Guid = Guid('ed822c8c-d6be-4301-a6-31-0e-14-16-ba-d2-8f')
CLSID_WICXMPSeqMetadataReader: Guid = Guid('7f12e753-fc71-43d7-a5-1d-92-f3-59-77-ab-b5')
CLSID_WICXMPSeqMetadataWriter: Guid = Guid('6d68d1de-d432-4b0f-92-3a-09-11-83-a9-bd-a7')
CLSID_WICXMPAltMetadataReader: Guid = Guid('aa94dcc2-b8b0-4898-b8-35-00-0a-ab-d7-43-93')
CLSID_WICXMPAltMetadataWriter: Guid = Guid('076c2a6c-f78f-4c46-a7-23-35-83-e7-08-76-ea')
CLSID_WICLSDMetadataReader: Guid = Guid('41070793-59e4-479a-a1-f7-95-4a-dc-2e-f5-fc')
CLSID_WICLSDMetadataWriter: Guid = Guid('73c037e7-e5d9-4954-87-6a-6d-a8-1d-6e-57-68')
CLSID_WICGCEMetadataReader: Guid = Guid('b92e345d-f52d-41f3-b5-62-08-1b-c7-72-e3-b9')
CLSID_WICGCEMetadataWriter: Guid = Guid('af95dc76-16b2-47f4-b3-ea-3c-31-79-66-93-e7')
CLSID_WICIMDMetadataReader: Guid = Guid('7447a267-0015-42c8-a8-f1-fb-3b-94-c6-83-61')
CLSID_WICIMDMetadataWriter: Guid = Guid('8c89071f-452e-4e95-96-82-9d-10-24-62-71-72')
CLSID_WICAPEMetadataReader: Guid = Guid('1767b93a-b021-44ea-92-0f-86-3c-11-f4-f7-68')
CLSID_WICAPEMetadataWriter: Guid = Guid('bd6edfca-2890-482f-b2-33-8d-73-39-a1-cf-8d')
CLSID_WICJpegChrominanceMetadataReader: Guid = Guid('50b1904b-f28f-4574-93-f4-0b-ad-e8-2c-69-e9')
CLSID_WICJpegChrominanceMetadataWriter: Guid = Guid('3ff566f0-6e6b-49d4-96-e6-b7-88-86-69-2c-62')
CLSID_WICJpegLuminanceMetadataReader: Guid = Guid('356f2f88-05a6-4728-b9-a4-1b-fb-ce-04-d8-38')
CLSID_WICJpegLuminanceMetadataWriter: Guid = Guid('1d583abc-8a0e-4657-99-82-a3-80-ca-58-fb-4b')
CLSID_WICJpegCommentMetadataReader: Guid = Guid('9f66347c-60c4-4c4d-ab-58-d2-35-86-85-f6-07')
CLSID_WICJpegCommentMetadataWriter: Guid = Guid('e573236f-55b1-4eda-81-ea-9f-65-db-02-90-d3')
CLSID_WICGifCommentMetadataReader: Guid = Guid('32557d3b-69dc-4f95-83-6e-f5-97-2b-2f-61-59')
CLSID_WICGifCommentMetadataWriter: Guid = Guid('a02797fc-c4ae-418c-af-95-e6-37-c7-ea-d2-a1')
CLSID_WICPngGamaMetadataReader: Guid = Guid('3692ca39-e082-4350-9e-1f-37-04-cb-08-3c-d5')
CLSID_WICPngGamaMetadataWriter: Guid = Guid('ff036d13-5d4b-46dd-b1-0f-10-66-93-d9-fe-4f')
CLSID_WICPngBkgdMetadataReader: Guid = Guid('0ce7a4a6-03e8-4a60-9d-15-28-2e-f3-2e-e7-da')
CLSID_WICPngBkgdMetadataWriter: Guid = Guid('68e3f2fd-31ae-4441-bb-6a-fd-70-47-52-5f-90')
CLSID_WICPngItxtMetadataReader: Guid = Guid('aabfb2fa-3e1e-4a8f-89-77-55-56-fb-94-ea-23')
CLSID_WICPngItxtMetadataWriter: Guid = Guid('31879719-e751-4df8-98-1d-68-df-f6-77-04-ed')
CLSID_WICPngChrmMetadataReader: Guid = Guid('f90b5f36-367b-402a-9d-d1-bc-0f-d5-9d-8f-62')
CLSID_WICPngChrmMetadataWriter: Guid = Guid('e23ce3eb-5608-4e83-bc-ef-27-b1-98-7e-51-d7')
CLSID_WICPngHistMetadataReader: Guid = Guid('877a0bb7-a313-4491-87-b5-2e-6d-05-94-f5-20')
CLSID_WICPngHistMetadataWriter: Guid = Guid('8a03e749-672e-446e-bf-1f-2c-11-d2-33-b6-ff')
CLSID_WICPngIccpMetadataReader: Guid = Guid('f5d3e63b-cb0f-4628-a4-78-6d-82-44-be-36-b1')
CLSID_WICPngIccpMetadataWriter: Guid = Guid('16671e5f-0ce6-4cc4-97-68-e8-9f-e5-01-8a-de')
CLSID_WICPngSrgbMetadataReader: Guid = Guid('fb40360c-547e-4956-a3-b9-d4-41-88-59-ba-66')
CLSID_WICPngSrgbMetadataWriter: Guid = Guid('a6ee35c6-87ec-47df-9f-22-1d-5a-ad-84-0c-82')
CLSID_WICPngTimeMetadataReader: Guid = Guid('d94edf02-efe5-4f0d-85-c8-f5-a6-8b-30-00-b1')
CLSID_WICPngTimeMetadataWriter: Guid = Guid('1ab78400-b5a3-4d91-8a-ce-33-fc-d1-49-9b-e6')
CLSID_WICDdsMetadataReader: Guid = Guid('276c88ca-7533-4a86-b6-76-66-b3-60-80-d4-84')
CLSID_WICDdsMetadataWriter: Guid = Guid('fd688bbd-31ed-4db7-a7-23-93-49-27-d3-83-67')
CLSID_WICHeifMetadataReader: Guid = Guid('acddfc3f-85ec-41bc-bd-ef-1b-c2-62-e4-db-05')
CLSID_WICHeifMetadataWriter: Guid = Guid('3ae45e79-40bc-4401-ac-e5-dd-3c-b1-6e-6a-fe')
CLSID_WICHeifHDRMetadataReader: Guid = Guid('2438de3d-94d9-4be8-84-a8-4d-e9-5a-57-5e-75')
CLSID_WICWebpAnimMetadataReader: Guid = Guid('076f9911-a348-465c-a8-07-a2-52-f3-f2-d3-de')
CLSID_WICWebpAnmfMetadataReader: Guid = Guid('85a10b03-c9f6-439f-be-5e-c0-fb-ef-67-80-7c')
@winfunctype('WindowsCodecs.dll')
def WICConvertBitmapSource(dstFormat: POINTER(Guid), pISrc: win32more.Graphics.Imaging.IWICBitmapSource_head, ppIDst: POINTER(win32more.Graphics.Imaging.IWICBitmapSource_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('WindowsCodecs.dll')
def WICCreateBitmapFromSection(width: UInt32, height: UInt32, pixelFormat: POINTER(Guid), hSection: win32more.Foundation.HANDLE, stride: UInt32, offset: UInt32, ppIBitmap: POINTER(win32more.Graphics.Imaging.IWICBitmap_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('WindowsCodecs.dll')
def WICCreateBitmapFromSectionEx(width: UInt32, height: UInt32, pixelFormat: POINTER(Guid), hSection: win32more.Foundation.HANDLE, stride: UInt32, offset: UInt32, desiredAccessLevel: win32more.Graphics.Imaging.WICSectionAccessLevel, ppIBitmap: POINTER(win32more.Graphics.Imaging.IWICBitmap_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('WindowsCodecs.dll')
def WICMapGuidToShortName(guid: POINTER(Guid), cchName: UInt32, wzName: win32more.Foundation.PWSTR, pcchActual: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
@winfunctype('WindowsCodecs.dll')
def WICMapShortNameToGuid(wzName: win32more.Foundation.PWSTR, pguid: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
@winfunctype('WindowsCodecs.dll')
def WICMapSchemaToName(guidMetadataFormat: POINTER(Guid), pwzSchema: win32more.Foundation.PWSTR, cchName: UInt32, wzName: win32more.Foundation.PWSTR, pcchActual: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
@winfunctype('WindowsCodecs.dll')
def WICMatchMetadataContent(guidContainerFormat: POINTER(Guid), pguidVendor: POINTER(Guid), pIStream: win32more.System.Com.IStream_head, pguidMetadataFormat: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
@winfunctype('WindowsCodecs.dll')
def WICSerializeMetadataContent(guidContainerFormat: POINTER(Guid), pIWriter: win32more.Graphics.Imaging.IWICMetadataWriter_head, dwPersistOptions: UInt32, pIStream: win32more.System.Com.IStream_head) -> win32more.Foundation.HRESULT: ...
@winfunctype('WindowsCodecs.dll')
def WICGetMetadataContentSize(guidContainerFormat: POINTER(Guid), pIWriter: win32more.Graphics.Imaging.IWICMetadataWriter_head, pcbSize: POINTER(win32more.Foundation.ULARGE_INTEGER_head)) -> win32more.Foundation.HRESULT: ...
class IWICBitmap(c_void_p):
    extends: win32more.Graphics.Imaging.IWICBitmapSource
    Guid = Guid('00000121-a8f2-4877-ba-0a-fd-2b-66-45-fb-94')
    @commethod(8)
    def Lock(prcLock: POINTER(win32more.Graphics.Imaging.WICRect_head), flags: UInt32, ppILock: POINTER(win32more.Graphics.Imaging.IWICBitmapLock_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def SetPalette(pIPalette: win32more.Graphics.Imaging.IWICPalette_head) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def SetResolution(dpiX: Double, dpiY: Double) -> win32more.Foundation.HRESULT: ...
class IWICBitmapClipper(c_void_p):
    extends: win32more.Graphics.Imaging.IWICBitmapSource
    Guid = Guid('e4fbcf03-223d-4e81-93-33-d6-35-55-6d-d1-b5')
    @commethod(8)
    def Initialize(pISource: win32more.Graphics.Imaging.IWICBitmapSource_head, prc: POINTER(win32more.Graphics.Imaging.WICRect_head)) -> win32more.Foundation.HRESULT: ...
class IWICBitmapCodecInfo(c_void_p):
    extends: win32more.Graphics.Imaging.IWICComponentInfo
    Guid = Guid('e87a44c4-b76e-4c47-8b-09-29-8e-b1-2a-27-14')
    @commethod(11)
    def GetContainerFormat(pguidContainerFormat: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def GetPixelFormats(cFormats: UInt32, pguidPixelFormats: POINTER(Guid), pcActual: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def GetColorManagementVersion(cchColorManagementVersion: UInt32, wzColorManagementVersion: win32more.Foundation.PWSTR, pcchActual: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def GetDeviceManufacturer(cchDeviceManufacturer: UInt32, wzDeviceManufacturer: win32more.Foundation.PWSTR, pcchActual: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def GetDeviceModels(cchDeviceModels: UInt32, wzDeviceModels: win32more.Foundation.PWSTR, pcchActual: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def GetMimeTypes(cchMimeTypes: UInt32, wzMimeTypes: win32more.Foundation.PWSTR, pcchActual: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def GetFileExtensions(cchFileExtensions: UInt32, wzFileExtensions: win32more.Foundation.PWSTR, pcchActual: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def DoesSupportAnimation(pfSupportAnimation: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def DoesSupportChromakey(pfSupportChromakey: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(20)
    def DoesSupportLossless(pfSupportLossless: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(21)
    def DoesSupportMultiframe(pfSupportMultiframe: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(22)
    def MatchesMimeType(wzMimeType: win32more.Foundation.PWSTR, pfMatches: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
class IWICBitmapCodecProgressNotification(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('64c1024e-c3cf-4462-80-78-88-c2-b1-1c-46-d9')
    @commethod(3)
    def RegisterProgressNotification(pfnProgressNotification: win32more.Graphics.Imaging.PFNProgressNotification, pvData: c_void_p, dwProgressFlags: UInt32) -> win32more.Foundation.HRESULT: ...
class IWICBitmapDecoder(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('9edde9e7-8dee-47ea-99-df-e6-fa-f2-ed-44-bf')
    @commethod(3)
    def QueryCapability(pIStream: win32more.System.Com.IStream_head, pdwCapability: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Initialize(pIStream: win32more.System.Com.IStream_head, cacheOptions: win32more.Graphics.Imaging.WICDecodeOptions) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetContainerFormat(pguidContainerFormat: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetDecoderInfo(ppIDecoderInfo: POINTER(win32more.Graphics.Imaging.IWICBitmapDecoderInfo_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def CopyPalette(pIPalette: win32more.Graphics.Imaging.IWICPalette_head) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetMetadataQueryReader(ppIMetadataQueryReader: POINTER(win32more.Graphics.Imaging.IWICMetadataQueryReader_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def GetPreview(ppIBitmapSource: POINTER(win32more.Graphics.Imaging.IWICBitmapSource_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def GetColorContexts(cCount: UInt32, ppIColorContexts: POINTER(win32more.Graphics.Imaging.IWICColorContext_head), pcActualCount: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def GetThumbnail(ppIThumbnail: POINTER(win32more.Graphics.Imaging.IWICBitmapSource_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def GetFrameCount(pCount: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def GetFrame(index: UInt32, ppIBitmapFrame: POINTER(win32more.Graphics.Imaging.IWICBitmapFrameDecode_head)) -> win32more.Foundation.HRESULT: ...
class IWICBitmapDecoderInfo(c_void_p):
    extends: win32more.Graphics.Imaging.IWICBitmapCodecInfo
    Guid = Guid('d8cd007f-d08f-4191-9b-fc-23-6e-a7-f0-e4-b5')
    @commethod(23)
    def GetPatterns(cbSizePatterns: UInt32, pPatterns: POINTER(win32more.Graphics.Imaging.WICBitmapPattern_head), pcPatterns: POINTER(UInt32), pcbPatternsActual: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(24)
    def MatchesPattern(pIStream: win32more.System.Com.IStream_head, pfMatches: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(25)
    def CreateInstance(ppIBitmapDecoder: POINTER(win32more.Graphics.Imaging.IWICBitmapDecoder_head)) -> win32more.Foundation.HRESULT: ...
class IWICBitmapEncoder(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('00000103-a8f2-4877-ba-0a-fd-2b-66-45-fb-94')
    @commethod(3)
    def Initialize(pIStream: win32more.System.Com.IStream_head, cacheOption: win32more.Graphics.Imaging.WICBitmapEncoderCacheOption) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetContainerFormat(pguidContainerFormat: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetEncoderInfo(ppIEncoderInfo: POINTER(win32more.Graphics.Imaging.IWICBitmapEncoderInfo_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def SetColorContexts(cCount: UInt32, ppIColorContext: POINTER(win32more.Graphics.Imaging.IWICColorContext_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def SetPalette(pIPalette: win32more.Graphics.Imaging.IWICPalette_head) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def SetThumbnail(pIThumbnail: win32more.Graphics.Imaging.IWICBitmapSource_head) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def SetPreview(pIPreview: win32more.Graphics.Imaging.IWICBitmapSource_head) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def CreateNewFrame(ppIFrameEncode: POINTER(win32more.Graphics.Imaging.IWICBitmapFrameEncode_head), ppIEncoderOptions: POINTER(win32more.System.Com.StructuredStorage.IPropertyBag2_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def Commit() -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def GetMetadataQueryWriter(ppIMetadataQueryWriter: POINTER(win32more.Graphics.Imaging.IWICMetadataQueryWriter_head)) -> win32more.Foundation.HRESULT: ...
class IWICBitmapEncoderInfo(c_void_p):
    extends: win32more.Graphics.Imaging.IWICBitmapCodecInfo
    Guid = Guid('94c9b4ee-a09f-4f92-8a-1e-4a-9b-ce-7e-76-fb')
    @commethod(23)
    def CreateInstance(ppIBitmapEncoder: POINTER(win32more.Graphics.Imaging.IWICBitmapEncoder_head)) -> win32more.Foundation.HRESULT: ...
class IWICBitmapFlipRotator(c_void_p):
    extends: win32more.Graphics.Imaging.IWICBitmapSource
    Guid = Guid('5009834f-2d6a-41ce-9e-1b-17-c5-af-f7-a7-82')
    @commethod(8)
    def Initialize(pISource: win32more.Graphics.Imaging.IWICBitmapSource_head, options: win32more.Graphics.Imaging.WICBitmapTransformOptions) -> win32more.Foundation.HRESULT: ...
class IWICBitmapFrameDecode(c_void_p):
    extends: win32more.Graphics.Imaging.IWICBitmapSource
    Guid = Guid('3b16811b-6a43-4ec9-a8-13-3d-93-0c-13-b9-40')
    @commethod(8)
    def GetMetadataQueryReader(ppIMetadataQueryReader: POINTER(win32more.Graphics.Imaging.IWICMetadataQueryReader_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def GetColorContexts(cCount: UInt32, ppIColorContexts: POINTER(win32more.Graphics.Imaging.IWICColorContext_head), pcActualCount: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def GetThumbnail(ppIThumbnail: POINTER(win32more.Graphics.Imaging.IWICBitmapSource_head)) -> win32more.Foundation.HRESULT: ...
class IWICBitmapFrameEncode(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('00000105-a8f2-4877-ba-0a-fd-2b-66-45-fb-94')
    @commethod(3)
    def Initialize(pIEncoderOptions: win32more.System.Com.StructuredStorage.IPropertyBag2_head) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def SetSize(uiWidth: UInt32, uiHeight: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def SetResolution(dpiX: Double, dpiY: Double) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def SetPixelFormat(pPixelFormat: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def SetColorContexts(cCount: UInt32, ppIColorContext: POINTER(win32more.Graphics.Imaging.IWICColorContext_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def SetPalette(pIPalette: win32more.Graphics.Imaging.IWICPalette_head) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def SetThumbnail(pIThumbnail: win32more.Graphics.Imaging.IWICBitmapSource_head) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def WritePixels(lineCount: UInt32, cbStride: UInt32, cbBufferSize: UInt32, pbPixels: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def WriteSource(pIBitmapSource: win32more.Graphics.Imaging.IWICBitmapSource_head, prc: POINTER(win32more.Graphics.Imaging.WICRect_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def Commit() -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def GetMetadataQueryWriter(ppIMetadataQueryWriter: POINTER(win32more.Graphics.Imaging.IWICMetadataQueryWriter_head)) -> win32more.Foundation.HRESULT: ...
class IWICBitmapLock(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('00000123-a8f2-4877-ba-0a-fd-2b-66-45-fb-94')
    @commethod(3)
    def GetSize(puiWidth: POINTER(UInt32), puiHeight: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetStride(pcbStride: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetDataPointer(pcbBufferSize: POINTER(UInt32), ppbData: POINTER(c_char_p_no)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetPixelFormat(pPixelFormat: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
class IWICBitmapScaler(c_void_p):
    extends: win32more.Graphics.Imaging.IWICBitmapSource
    Guid = Guid('00000302-a8f2-4877-ba-0a-fd-2b-66-45-fb-94')
    @commethod(8)
    def Initialize(pISource: win32more.Graphics.Imaging.IWICBitmapSource_head, uiWidth: UInt32, uiHeight: UInt32, mode: win32more.Graphics.Imaging.WICBitmapInterpolationMode) -> win32more.Foundation.HRESULT: ...
class IWICBitmapSource(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('00000120-a8f2-4877-ba-0a-fd-2b-66-45-fb-94')
    @commethod(3)
    def GetSize(puiWidth: POINTER(UInt32), puiHeight: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetPixelFormat(pPixelFormat: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetResolution(pDpiX: POINTER(Double), pDpiY: POINTER(Double)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def CopyPalette(pIPalette: win32more.Graphics.Imaging.IWICPalette_head) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def CopyPixels(prc: POINTER(win32more.Graphics.Imaging.WICRect_head), cbStride: UInt32, cbBufferSize: UInt32, pbBuffer: c_char_p_no) -> win32more.Foundation.HRESULT: ...
class IWICBitmapSourceTransform(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('3b16811b-6a43-4ec9-b7-13-3d-5a-0c-13-b9-40')
    @commethod(3)
    def CopyPixels(prc: POINTER(win32more.Graphics.Imaging.WICRect_head), uiWidth: UInt32, uiHeight: UInt32, pguidDstFormat: POINTER(Guid), dstTransform: win32more.Graphics.Imaging.WICBitmapTransformOptions, nStride: UInt32, cbBufferSize: UInt32, pbBuffer: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetClosestSize(puiWidth: POINTER(UInt32), puiHeight: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetClosestPixelFormat(pguidDstFormat: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def DoesSupportTransform(dstTransform: win32more.Graphics.Imaging.WICBitmapTransformOptions, pfIsSupported: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
class IWICColorContext(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('3c613a02-34b2-44ea-9a-7c-45-ae-a9-c6-fd-6d')
    @commethod(3)
    def InitializeFromFilename(wzFilename: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def InitializeFromMemory(pbBuffer: c_char_p_no, cbBufferSize: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def InitializeFromExifColorSpace(value: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetType(pType: POINTER(win32more.Graphics.Imaging.WICColorContextType)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetProfileBytes(cbBuffer: UInt32, pbBuffer: c_char_p_no, pcbActual: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetExifColorSpace(pValue: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
class IWICColorTransform(c_void_p):
    extends: win32more.Graphics.Imaging.IWICBitmapSource
    Guid = Guid('b66f034f-d0e2-40ab-b4-36-6d-e3-9e-32-1a-94')
    @commethod(8)
    def Initialize(pIBitmapSource: win32more.Graphics.Imaging.IWICBitmapSource_head, pIContextSource: win32more.Graphics.Imaging.IWICColorContext_head, pIContextDest: win32more.Graphics.Imaging.IWICColorContext_head, pixelFmtDest: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
class IWICComponentFactory(c_void_p):
    extends: win32more.Graphics.Imaging.IWICImagingFactory
    Guid = Guid('412d0c3a-9650-44fa-af-5b-dd-2a-06-c8-e8-fb')
    @commethod(28)
    def CreateMetadataReader(guidMetadataFormat: POINTER(Guid), pguidVendor: POINTER(Guid), dwOptions: UInt32, pIStream: win32more.System.Com.IStream_head, ppIReader: POINTER(win32more.Graphics.Imaging.IWICMetadataReader_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(29)
    def CreateMetadataReaderFromContainer(guidContainerFormat: POINTER(Guid), pguidVendor: POINTER(Guid), dwOptions: UInt32, pIStream: win32more.System.Com.IStream_head, ppIReader: POINTER(win32more.Graphics.Imaging.IWICMetadataReader_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(30)
    def CreateMetadataWriter(guidMetadataFormat: POINTER(Guid), pguidVendor: POINTER(Guid), dwMetadataOptions: UInt32, ppIWriter: POINTER(win32more.Graphics.Imaging.IWICMetadataWriter_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(31)
    def CreateMetadataWriterFromReader(pIReader: win32more.Graphics.Imaging.IWICMetadataReader_head, pguidVendor: POINTER(Guid), ppIWriter: POINTER(win32more.Graphics.Imaging.IWICMetadataWriter_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(32)
    def CreateQueryReaderFromBlockReader(pIBlockReader: win32more.Graphics.Imaging.IWICMetadataBlockReader_head, ppIQueryReader: POINTER(win32more.Graphics.Imaging.IWICMetadataQueryReader_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(33)
    def CreateQueryWriterFromBlockWriter(pIBlockWriter: win32more.Graphics.Imaging.IWICMetadataBlockWriter_head, ppIQueryWriter: POINTER(win32more.Graphics.Imaging.IWICMetadataQueryWriter_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(34)
    def CreateEncoderPropertyBag(ppropOptions: POINTER(win32more.System.Com.StructuredStorage.PROPBAG2_head), cCount: UInt32, ppIPropertyBag: POINTER(win32more.System.Com.StructuredStorage.IPropertyBag2_head)) -> win32more.Foundation.HRESULT: ...
class IWICComponentInfo(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('23bc3f0a-698b-4357-88-6b-f2-4d-50-67-13-34')
    @commethod(3)
    def GetComponentType(pType: POINTER(win32more.Graphics.Imaging.WICComponentType)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetCLSID(pclsid: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetSigningStatus(pStatus: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetAuthor(cchAuthor: UInt32, wzAuthor: win32more.Foundation.PWSTR, pcchActual: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetVendorGUID(pguidVendor: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetVersion(cchVersion: UInt32, wzVersion: win32more.Foundation.PWSTR, pcchActual: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def GetSpecVersion(cchSpecVersion: UInt32, wzSpecVersion: win32more.Foundation.PWSTR, pcchActual: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def GetFriendlyName(cchFriendlyName: UInt32, wzFriendlyName: win32more.Foundation.PWSTR, pcchActual: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
class IWICDdsDecoder(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('409cd537-8532-40cb-97-74-e2-fe-b2-df-4e-9c')
    @commethod(3)
    def GetParameters(pParameters: POINTER(win32more.Graphics.Imaging.WICDdsParameters_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetFrame(arrayIndex: UInt32, mipLevel: UInt32, sliceIndex: UInt32, ppIBitmapFrame: POINTER(win32more.Graphics.Imaging.IWICBitmapFrameDecode_head)) -> win32more.Foundation.HRESULT: ...
class IWICDdsEncoder(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('5cacdb4c-407e-41b3-b9-36-d0-f0-10-cd-67-32')
    @commethod(3)
    def SetParameters(pParameters: POINTER(win32more.Graphics.Imaging.WICDdsParameters_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetParameters(pParameters: POINTER(win32more.Graphics.Imaging.WICDdsParameters_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def CreateNewFrame(ppIFrameEncode: POINTER(win32more.Graphics.Imaging.IWICBitmapFrameEncode_head), pArrayIndex: POINTER(UInt32), pMipLevel: POINTER(UInt32), pSliceIndex: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
class IWICDdsFrameDecode(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('3d4c0c61-18a4-41e4-bd-80-48-1a-4f-c9-f4-64')
    @commethod(3)
    def GetSizeInBlocks(pWidthInBlocks: POINTER(UInt32), pHeightInBlocks: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetFormatInfo(pFormatInfo: POINTER(win32more.Graphics.Imaging.WICDdsFormatInfo_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def CopyBlocks(prcBoundsInBlocks: POINTER(win32more.Graphics.Imaging.WICRect_head), cbStride: UInt32, cbBufferSize: UInt32, pbBuffer: c_char_p_no) -> win32more.Foundation.HRESULT: ...
class IWICDevelopRaw(c_void_p):
    extends: win32more.Graphics.Imaging.IWICBitmapFrameDecode
    Guid = Guid('fbec5e44-f7be-4b65-b7-f8-c0-c8-1f-ef-02-6d')
    @commethod(11)
    def QueryRawCapabilitiesInfo(pInfo: POINTER(win32more.Graphics.Imaging.WICRawCapabilitiesInfo_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def LoadParameterSet(ParameterSet: win32more.Graphics.Imaging.WICRawParameterSet) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def GetCurrentParameterSet(ppCurrentParameterSet: POINTER(win32more.System.Com.StructuredStorage.IPropertyBag2_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def SetExposureCompensation(ev: Double) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def GetExposureCompensation(pEV: POINTER(Double)) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def SetWhitePointRGB(Red: UInt32, Green: UInt32, Blue: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def GetWhitePointRGB(pRed: POINTER(UInt32), pGreen: POINTER(UInt32), pBlue: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def SetNamedWhitePoint(WhitePoint: win32more.Graphics.Imaging.WICNamedWhitePoint) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def GetNamedWhitePoint(pWhitePoint: POINTER(win32more.Graphics.Imaging.WICNamedWhitePoint)) -> win32more.Foundation.HRESULT: ...
    @commethod(20)
    def SetWhitePointKelvin(WhitePointKelvin: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(21)
    def GetWhitePointKelvin(pWhitePointKelvin: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(22)
    def GetKelvinRangeInfo(pMinKelvinTemp: POINTER(UInt32), pMaxKelvinTemp: POINTER(UInt32), pKelvinTempStepValue: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(23)
    def SetContrast(Contrast: Double) -> win32more.Foundation.HRESULT: ...
    @commethod(24)
    def GetContrast(pContrast: POINTER(Double)) -> win32more.Foundation.HRESULT: ...
    @commethod(25)
    def SetGamma(Gamma: Double) -> win32more.Foundation.HRESULT: ...
    @commethod(26)
    def GetGamma(pGamma: POINTER(Double)) -> win32more.Foundation.HRESULT: ...
    @commethod(27)
    def SetSharpness(Sharpness: Double) -> win32more.Foundation.HRESULT: ...
    @commethod(28)
    def GetSharpness(pSharpness: POINTER(Double)) -> win32more.Foundation.HRESULT: ...
    @commethod(29)
    def SetSaturation(Saturation: Double) -> win32more.Foundation.HRESULT: ...
    @commethod(30)
    def GetSaturation(pSaturation: POINTER(Double)) -> win32more.Foundation.HRESULT: ...
    @commethod(31)
    def SetTint(Tint: Double) -> win32more.Foundation.HRESULT: ...
    @commethod(32)
    def GetTint(pTint: POINTER(Double)) -> win32more.Foundation.HRESULT: ...
    @commethod(33)
    def SetNoiseReduction(NoiseReduction: Double) -> win32more.Foundation.HRESULT: ...
    @commethod(34)
    def GetNoiseReduction(pNoiseReduction: POINTER(Double)) -> win32more.Foundation.HRESULT: ...
    @commethod(35)
    def SetDestinationColorContext(pColorContext: win32more.Graphics.Imaging.IWICColorContext_head) -> win32more.Foundation.HRESULT: ...
    @commethod(36)
    def SetToneCurve(cbToneCurveSize: UInt32, pToneCurve: POINTER(win32more.Graphics.Imaging.WICRawToneCurve_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(37)
    def GetToneCurve(cbToneCurveBufferSize: UInt32, pToneCurve: POINTER(win32more.Graphics.Imaging.WICRawToneCurve_head), pcbActualToneCurveBufferSize: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(38)
    def SetRotation(Rotation: Double) -> win32more.Foundation.HRESULT: ...
    @commethod(39)
    def GetRotation(pRotation: POINTER(Double)) -> win32more.Foundation.HRESULT: ...
    @commethod(40)
    def SetRenderMode(RenderMode: win32more.Graphics.Imaging.WICRawRenderMode) -> win32more.Foundation.HRESULT: ...
    @commethod(41)
    def GetRenderMode(pRenderMode: POINTER(win32more.Graphics.Imaging.WICRawRenderMode)) -> win32more.Foundation.HRESULT: ...
    @commethod(42)
    def SetNotificationCallback(pCallback: win32more.Graphics.Imaging.IWICDevelopRawNotificationCallback_head) -> win32more.Foundation.HRESULT: ...
class IWICDevelopRawNotificationCallback(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('95c75a6e-3e8c-4ec2-85-a8-ae-bc-c5-51-e5-9b')
    @commethod(3)
    def Notify(NotificationMask: UInt32) -> win32more.Foundation.HRESULT: ...
class IWICEnumMetadataItem(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('dc2bb46d-3f07-481e-86-25-22-0c-4a-ed-bb-33')
    @commethod(3)
    def Next(celt: UInt32, rgeltSchema: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), rgeltId: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), rgeltValue: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), pceltFetched: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(celt: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def Reset() -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(ppIEnumMetadataItem: POINTER(win32more.Graphics.Imaging.IWICEnumMetadataItem_head)) -> win32more.Foundation.HRESULT: ...
class IWICFastMetadataEncoder(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('b84e2c09-78c9-4ac4-8b-d3-52-4a-e1-66-3a-2f')
    @commethod(3)
    def Commit() -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetMetadataQueryWriter(ppIMetadataQueryWriter: POINTER(win32more.Graphics.Imaging.IWICMetadataQueryWriter_head)) -> win32more.Foundation.HRESULT: ...
class IWICFormatConverter(c_void_p):
    extends: win32more.Graphics.Imaging.IWICBitmapSource
    Guid = Guid('00000301-a8f2-4877-ba-0a-fd-2b-66-45-fb-94')
    @commethod(8)
    def Initialize(pISource: win32more.Graphics.Imaging.IWICBitmapSource_head, dstFormat: POINTER(Guid), dither: win32more.Graphics.Imaging.WICBitmapDitherType, pIPalette: win32more.Graphics.Imaging.IWICPalette_head, alphaThresholdPercent: Double, paletteTranslate: win32more.Graphics.Imaging.WICBitmapPaletteType) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def CanConvert(srcPixelFormat: POINTER(Guid), dstPixelFormat: POINTER(Guid), pfCanConvert: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
class IWICFormatConverterInfo(c_void_p):
    extends: win32more.Graphics.Imaging.IWICComponentInfo
    Guid = Guid('9f34fb65-13f4-4f15-bc-57-37-26-b5-e5-3d-9f')
    @commethod(11)
    def GetPixelFormats(cFormats: UInt32, pPixelFormatGUIDs: POINTER(Guid), pcActual: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def CreateInstance(ppIConverter: POINTER(win32more.Graphics.Imaging.IWICFormatConverter_head)) -> win32more.Foundation.HRESULT: ...
class IWICImagingFactory(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('ec5ec8a9-c395-4314-9c-77-54-d7-a9-35-ff-70')
    @commethod(3)
    def CreateDecoderFromFilename(wzFilename: win32more.Foundation.PWSTR, pguidVendor: POINTER(Guid), dwDesiredAccess: UInt32, metadataOptions: win32more.Graphics.Imaging.WICDecodeOptions, ppIDecoder: POINTER(win32more.Graphics.Imaging.IWICBitmapDecoder_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def CreateDecoderFromStream(pIStream: win32more.System.Com.IStream_head, pguidVendor: POINTER(Guid), metadataOptions: win32more.Graphics.Imaging.WICDecodeOptions, ppIDecoder: POINTER(win32more.Graphics.Imaging.IWICBitmapDecoder_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def CreateDecoderFromFileHandle(hFile: UIntPtr, pguidVendor: POINTER(Guid), metadataOptions: win32more.Graphics.Imaging.WICDecodeOptions, ppIDecoder: POINTER(win32more.Graphics.Imaging.IWICBitmapDecoder_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def CreateComponentInfo(clsidComponent: POINTER(Guid), ppIInfo: POINTER(win32more.Graphics.Imaging.IWICComponentInfo_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def CreateDecoder(guidContainerFormat: POINTER(Guid), pguidVendor: POINTER(Guid), ppIDecoder: POINTER(win32more.Graphics.Imaging.IWICBitmapDecoder_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def CreateEncoder(guidContainerFormat: POINTER(Guid), pguidVendor: POINTER(Guid), ppIEncoder: POINTER(win32more.Graphics.Imaging.IWICBitmapEncoder_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def CreatePalette(ppIPalette: POINTER(win32more.Graphics.Imaging.IWICPalette_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def CreateFormatConverter(ppIFormatConverter: POINTER(win32more.Graphics.Imaging.IWICFormatConverter_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def CreateBitmapScaler(ppIBitmapScaler: POINTER(win32more.Graphics.Imaging.IWICBitmapScaler_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def CreateBitmapClipper(ppIBitmapClipper: POINTER(win32more.Graphics.Imaging.IWICBitmapClipper_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def CreateBitmapFlipRotator(ppIBitmapFlipRotator: POINTER(win32more.Graphics.Imaging.IWICBitmapFlipRotator_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def CreateStream(ppIWICStream: POINTER(win32more.Graphics.Imaging.IWICStream_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def CreateColorContext(ppIWICColorContext: POINTER(win32more.Graphics.Imaging.IWICColorContext_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def CreateColorTransformer(ppIWICColorTransform: POINTER(win32more.Graphics.Imaging.IWICColorTransform_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def CreateBitmap(uiWidth: UInt32, uiHeight: UInt32, pixelFormat: POINTER(Guid), option: win32more.Graphics.Imaging.WICBitmapCreateCacheOption, ppIBitmap: POINTER(win32more.Graphics.Imaging.IWICBitmap_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def CreateBitmapFromSource(pIBitmapSource: win32more.Graphics.Imaging.IWICBitmapSource_head, option: win32more.Graphics.Imaging.WICBitmapCreateCacheOption, ppIBitmap: POINTER(win32more.Graphics.Imaging.IWICBitmap_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def CreateBitmapFromSourceRect(pIBitmapSource: win32more.Graphics.Imaging.IWICBitmapSource_head, x: UInt32, y: UInt32, width: UInt32, height: UInt32, ppIBitmap: POINTER(win32more.Graphics.Imaging.IWICBitmap_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(20)
    def CreateBitmapFromMemory(uiWidth: UInt32, uiHeight: UInt32, pixelFormat: POINTER(Guid), cbStride: UInt32, cbBufferSize: UInt32, pbBuffer: c_char_p_no, ppIBitmap: POINTER(win32more.Graphics.Imaging.IWICBitmap_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(21)
    def CreateBitmapFromHBITMAP(hBitmap: win32more.Graphics.Gdi.HBITMAP, hPalette: win32more.Graphics.Gdi.HPALETTE, options: win32more.Graphics.Imaging.WICBitmapAlphaChannelOption, ppIBitmap: POINTER(win32more.Graphics.Imaging.IWICBitmap_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(22)
    def CreateBitmapFromHICON(hIcon: win32more.UI.WindowsAndMessaging.HICON, ppIBitmap: POINTER(win32more.Graphics.Imaging.IWICBitmap_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(23)
    def CreateComponentEnumerator(componentTypes: UInt32, options: UInt32, ppIEnumUnknown: POINTER(win32more.System.Com.IEnumUnknown_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(24)
    def CreateFastMetadataEncoderFromDecoder(pIDecoder: win32more.Graphics.Imaging.IWICBitmapDecoder_head, ppIFastEncoder: POINTER(win32more.Graphics.Imaging.IWICFastMetadataEncoder_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(25)
    def CreateFastMetadataEncoderFromFrameDecode(pIFrameDecoder: win32more.Graphics.Imaging.IWICBitmapFrameDecode_head, ppIFastEncoder: POINTER(win32more.Graphics.Imaging.IWICFastMetadataEncoder_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(26)
    def CreateQueryWriter(guidMetadataFormat: POINTER(Guid), pguidVendor: POINTER(Guid), ppIQueryWriter: POINTER(win32more.Graphics.Imaging.IWICMetadataQueryWriter_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(27)
    def CreateQueryWriterFromReader(pIQueryReader: win32more.Graphics.Imaging.IWICMetadataQueryReader_head, pguidVendor: POINTER(Guid), ppIQueryWriter: POINTER(win32more.Graphics.Imaging.IWICMetadataQueryWriter_head)) -> win32more.Foundation.HRESULT: ...
class IWICJpegFrameDecode(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('8939f66e-c46a-4c21-a9-d1-98-b3-27-ce-16-79')
    @commethod(3)
    def DoesSupportIndexing(pfIndexingSupported: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def SetIndexing(options: win32more.Graphics.Imaging.WICJpegIndexingOptions, horizontalIntervalSize: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def ClearIndexing() -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetAcHuffmanTable(scanIndex: UInt32, tableIndex: UInt32, pAcHuffmanTable: POINTER(win32more.Graphics.Dxgi.Common.DXGI_JPEG_AC_HUFFMAN_TABLE_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetDcHuffmanTable(scanIndex: UInt32, tableIndex: UInt32, pDcHuffmanTable: POINTER(win32more.Graphics.Dxgi.Common.DXGI_JPEG_DC_HUFFMAN_TABLE_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetQuantizationTable(scanIndex: UInt32, tableIndex: UInt32, pQuantizationTable: POINTER(win32more.Graphics.Dxgi.Common.DXGI_JPEG_QUANTIZATION_TABLE_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def GetFrameHeader(pFrameHeader: POINTER(win32more.Graphics.Imaging.WICJpegFrameHeader_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def GetScanHeader(scanIndex: UInt32, pScanHeader: POINTER(win32more.Graphics.Imaging.WICJpegScanHeader_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def CopyScan(scanIndex: UInt32, scanOffset: UInt32, cbScanData: UInt32, pbScanData: c_char_p_no, pcbScanDataActual: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def CopyMinimalStream(streamOffset: UInt32, cbStreamData: UInt32, pbStreamData: c_char_p_no, pcbStreamDataActual: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
class IWICJpegFrameEncode(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('2f0c601f-d2c6-468c-ab-fa-49-49-5d-98-3e-d1')
    @commethod(3)
    def GetAcHuffmanTable(scanIndex: UInt32, tableIndex: UInt32, pAcHuffmanTable: POINTER(win32more.Graphics.Dxgi.Common.DXGI_JPEG_AC_HUFFMAN_TABLE_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetDcHuffmanTable(scanIndex: UInt32, tableIndex: UInt32, pDcHuffmanTable: POINTER(win32more.Graphics.Dxgi.Common.DXGI_JPEG_DC_HUFFMAN_TABLE_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetQuantizationTable(scanIndex: UInt32, tableIndex: UInt32, pQuantizationTable: POINTER(win32more.Graphics.Dxgi.Common.DXGI_JPEG_QUANTIZATION_TABLE_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def WriteScan(cbScanData: UInt32, pbScanData: c_char_p_no) -> win32more.Foundation.HRESULT: ...
class IWICMetadataBlockReader(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('feaa2a8d-b3f3-43e4-b2-5c-d1-de-99-0a-1a-e1')
    @commethod(3)
    def GetContainerFormat(pguidContainerFormat: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetCount(pcCount: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetReaderByIndex(nIndex: UInt32, ppIMetadataReader: POINTER(win32more.Graphics.Imaging.IWICMetadataReader_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetEnumerator(ppIEnumMetadata: POINTER(win32more.System.Com.IEnumUnknown_head)) -> win32more.Foundation.HRESULT: ...
class IWICMetadataBlockWriter(c_void_p):
    extends: win32more.Graphics.Imaging.IWICMetadataBlockReader
    Guid = Guid('08fb9676-b444-41e8-8d-be-6a-53-a5-42-bf-f1')
    @commethod(7)
    def InitializeFromBlockReader(pIMDBlockReader: win32more.Graphics.Imaging.IWICMetadataBlockReader_head) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetWriterByIndex(nIndex: UInt32, ppIMetadataWriter: POINTER(win32more.Graphics.Imaging.IWICMetadataWriter_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def AddWriter(pIMetadataWriter: win32more.Graphics.Imaging.IWICMetadataWriter_head) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def SetWriterByIndex(nIndex: UInt32, pIMetadataWriter: win32more.Graphics.Imaging.IWICMetadataWriter_head) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def RemoveWriterByIndex(nIndex: UInt32) -> win32more.Foundation.HRESULT: ...
class IWICMetadataHandlerInfo(c_void_p):
    extends: win32more.Graphics.Imaging.IWICComponentInfo
    Guid = Guid('aba958bf-c672-44d1-8d-61-ce-6d-f2-e6-82-c2')
    @commethod(11)
    def GetMetadataFormat(pguidMetadataFormat: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def GetContainerFormats(cContainerFormats: UInt32, pguidContainerFormats: POINTER(Guid), pcchActual: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def GetDeviceManufacturer(cchDeviceManufacturer: UInt32, wzDeviceManufacturer: win32more.Foundation.PWSTR, pcchActual: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def GetDeviceModels(cchDeviceModels: UInt32, wzDeviceModels: win32more.Foundation.PWSTR, pcchActual: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def DoesRequireFullStream(pfRequiresFullStream: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def DoesSupportPadding(pfSupportsPadding: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def DoesRequireFixedSize(pfFixedSize: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
class IWICMetadataQueryReader(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('30989668-e1c9-4597-b3-95-45-8e-ed-b8-08-df')
    @commethod(3)
    def GetContainerFormat(pguidContainerFormat: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetLocation(cchMaxLength: UInt32, wzNamespace: win32more.Foundation.PWSTR, pcchActualLength: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetMetadataByName(wzName: win32more.Foundation.PWSTR, pvarValue: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetEnumerator(ppIEnumString: POINTER(win32more.System.Com.IEnumString_head)) -> win32more.Foundation.HRESULT: ...
class IWICMetadataQueryWriter(c_void_p):
    extends: win32more.Graphics.Imaging.IWICMetadataQueryReader
    Guid = Guid('a721791a-0def-4d06-bd-91-21-18-bf-1d-b1-0b')
    @commethod(7)
    def SetMetadataByName(wzName: win32more.Foundation.PWSTR, pvarValue: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def RemoveMetadataByName(wzName: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
class IWICMetadataReader(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('9204fe99-d8fc-4fd5-a0-01-95-36-b0-67-a8-99')
    @commethod(3)
    def GetMetadataFormat(pguidMetadataFormat: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetMetadataHandlerInfo(ppIHandler: POINTER(win32more.Graphics.Imaging.IWICMetadataHandlerInfo_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetCount(pcCount: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetValueByIndex(nIndex: UInt32, pvarSchema: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), pvarId: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), pvarValue: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetValue(pvarSchema: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), pvarId: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), pvarValue: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetEnumerator(ppIEnumMetadata: POINTER(win32more.Graphics.Imaging.IWICEnumMetadataItem_head)) -> win32more.Foundation.HRESULT: ...
class IWICMetadataReaderInfo(c_void_p):
    extends: win32more.Graphics.Imaging.IWICMetadataHandlerInfo
    Guid = Guid('eebf1f5b-07c1-4447-a3-ab-22-ac-af-78-a8-04')
    @commethod(18)
    def GetPatterns(guidContainerFormat: POINTER(Guid), cbSize: UInt32, pPattern: POINTER(win32more.Graphics.Imaging.WICMetadataPattern_head), pcCount: POINTER(UInt32), pcbActual: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def MatchesPattern(guidContainerFormat: POINTER(Guid), pIStream: win32more.System.Com.IStream_head, pfMatches: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(20)
    def CreateInstance(ppIReader: POINTER(win32more.Graphics.Imaging.IWICMetadataReader_head)) -> win32more.Foundation.HRESULT: ...
class IWICMetadataWriter(c_void_p):
    extends: win32more.Graphics.Imaging.IWICMetadataReader
    Guid = Guid('f7836e16-3be0-470b-86-bb-16-0d-0a-ec-d7-de')
    @commethod(9)
    def SetValue(pvarSchema: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), pvarId: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), pvarValue: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def SetValueByIndex(nIndex: UInt32, pvarSchema: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), pvarId: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), pvarValue: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def RemoveValue(pvarSchema: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), pvarId: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def RemoveValueByIndex(nIndex: UInt32) -> win32more.Foundation.HRESULT: ...
class IWICMetadataWriterInfo(c_void_p):
    extends: win32more.Graphics.Imaging.IWICMetadataHandlerInfo
    Guid = Guid('b22e3fba-3925-4323-b5-c1-9e-bf-c4-30-f2-36')
    @commethod(18)
    def GetHeader(guidContainerFormat: POINTER(Guid), cbSize: UInt32, pHeader: POINTER(win32more.Graphics.Imaging.WICMetadataHeader_head), pcbActual: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def CreateInstance(ppIWriter: POINTER(win32more.Graphics.Imaging.IWICMetadataWriter_head)) -> win32more.Foundation.HRESULT: ...
class IWICPalette(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('00000040-a8f2-4877-ba-0a-fd-2b-66-45-fb-94')
    @commethod(3)
    def InitializePredefined(ePaletteType: win32more.Graphics.Imaging.WICBitmapPaletteType, fAddTransparentColor: win32more.Foundation.BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def InitializeCustom(pColors: POINTER(UInt32), cCount: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def InitializeFromBitmap(pISurface: win32more.Graphics.Imaging.IWICBitmapSource_head, cCount: UInt32, fAddTransparentColor: win32more.Foundation.BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def InitializeFromPalette(pIPalette: win32more.Graphics.Imaging.IWICPalette_head) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetType(pePaletteType: POINTER(win32more.Graphics.Imaging.WICBitmapPaletteType)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetColorCount(pcCount: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def GetColors(cCount: UInt32, pColors: POINTER(UInt32), pcActualColors: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def IsBlackWhite(pfIsBlackWhite: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def IsGrayscale(pfIsGrayscale: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def HasAlpha(pfHasAlpha: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
class IWICPersistStream(c_void_p):
    extends: win32more.System.Com.IPersistStream
    Guid = Guid('00675040-6908-45f8-86-a3-49-c7-df-d6-d9-ad')
    @commethod(8)
    def LoadEx(pIStream: win32more.System.Com.IStream_head, pguidPreferredVendor: POINTER(Guid), dwPersistOptions: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def SaveEx(pIStream: win32more.System.Com.IStream_head, dwPersistOptions: UInt32, fClearDirty: win32more.Foundation.BOOL) -> win32more.Foundation.HRESULT: ...
class IWICPixelFormatInfo(c_void_p):
    extends: win32more.Graphics.Imaging.IWICComponentInfo
    Guid = Guid('e8eda601-3d48-431a-ab-44-69-05-9b-e8-8b-be')
    @commethod(11)
    def GetFormatGUID(pFormat: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def GetColorContext(ppIColorContext: POINTER(win32more.Graphics.Imaging.IWICColorContext_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def GetBitsPerPixel(puiBitsPerPixel: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def GetChannelCount(puiChannelCount: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def GetChannelMask(uiChannelIndex: UInt32, cbMaskBuffer: UInt32, pbMaskBuffer: c_char_p_no, pcbActual: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
class IWICPixelFormatInfo2(c_void_p):
    extends: win32more.Graphics.Imaging.IWICPixelFormatInfo
    Guid = Guid('a9db33a2-af5f-43c7-b6-79-74-f5-98-4b-5a-a4')
    @commethod(16)
    def SupportsTransparency(pfSupportsTransparency: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def GetNumericRepresentation(pNumericRepresentation: POINTER(win32more.Graphics.Imaging.WICPixelFormatNumericRepresentation)) -> win32more.Foundation.HRESULT: ...
class IWICPlanarBitmapFrameEncode(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('f928b7b8-2221-40c1-b7-2e-7e-82-f1-97-4d-1a')
    @commethod(3)
    def WritePixels(lineCount: UInt32, pPlanes: POINTER(win32more.Graphics.Imaging.WICBitmapPlane_head), cPlanes: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def WriteSource(ppPlanes: POINTER(win32more.Graphics.Imaging.IWICBitmapSource_head), cPlanes: UInt32, prcSource: POINTER(win32more.Graphics.Imaging.WICRect_head)) -> win32more.Foundation.HRESULT: ...
class IWICPlanarBitmapSourceTransform(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('3aff9cce-be95-4303-b9-27-e7-d1-6f-f4-a6-13')
    @commethod(3)
    def DoesSupportTransform(puiWidth: POINTER(UInt32), puiHeight: POINTER(UInt32), dstTransform: win32more.Graphics.Imaging.WICBitmapTransformOptions, dstPlanarOptions: win32more.Graphics.Imaging.WICPlanarOptions, pguidDstFormats: POINTER(Guid), pPlaneDescriptions: POINTER(win32more.Graphics.Imaging.WICBitmapPlaneDescription_head), cPlanes: UInt32, pfIsSupported: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def CopyPixels(prcSource: POINTER(win32more.Graphics.Imaging.WICRect_head), uiWidth: UInt32, uiHeight: UInt32, dstTransform: win32more.Graphics.Imaging.WICBitmapTransformOptions, dstPlanarOptions: win32more.Graphics.Imaging.WICPlanarOptions, pDstPlanes: POINTER(win32more.Graphics.Imaging.WICBitmapPlane_head), cPlanes: UInt32) -> win32more.Foundation.HRESULT: ...
class IWICPlanarFormatConverter(c_void_p):
    extends: win32more.Graphics.Imaging.IWICBitmapSource
    Guid = Guid('bebee9cb-83b0-4dcc-81-32-b0-aa-a5-5e-ac-96')
    @commethod(8)
    def Initialize(ppPlanes: POINTER(win32more.Graphics.Imaging.IWICBitmapSource_head), cPlanes: UInt32, dstFormat: POINTER(Guid), dither: win32more.Graphics.Imaging.WICBitmapDitherType, pIPalette: win32more.Graphics.Imaging.IWICPalette_head, alphaThresholdPercent: Double, paletteTranslate: win32more.Graphics.Imaging.WICBitmapPaletteType) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def CanConvert(pSrcPixelFormats: POINTER(Guid), cSrcPlanes: UInt32, dstPixelFormat: POINTER(Guid), pfCanConvert: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
class IWICProgressCallback(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('4776f9cd-9517-45fa-bf-24-e8-9c-5e-c5-c6-0c')
    @commethod(3)
    def Notify(uFrameNum: UInt32, operation: win32more.Graphics.Imaging.WICProgressOperation, dblProgress: Double) -> win32more.Foundation.HRESULT: ...
class IWICProgressiveLevelControl(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('daac296f-7aa5-4dbf-8d-15-22-5c-59-76-f8-91')
    @commethod(3)
    def GetLevelCount(pcLevels: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetCurrentLevel(pnLevel: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def SetCurrentLevel(nLevel: UInt32) -> win32more.Foundation.HRESULT: ...
class IWICStream(c_void_p):
    extends: win32more.System.Com.IStream
    Guid = Guid('135ff860-22b7-4ddf-b0-f6-21-8f-4f-29-9a-43')
    @commethod(14)
    def InitializeFromIStream(pIStream: win32more.System.Com.IStream_head) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def InitializeFromFilename(wzFileName: win32more.Foundation.PWSTR, dwDesiredAccess: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def InitializeFromMemory(pbBuffer: c_char_p_no, cbBufferSize: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def InitializeFromIStreamRegion(pIStream: win32more.System.Com.IStream_head, ulOffset: win32more.Foundation.ULARGE_INTEGER, ulMaxSize: win32more.Foundation.ULARGE_INTEGER) -> win32more.Foundation.HRESULT: ...
class IWICStreamProvider(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('449494bc-b468-4927-96-d7-ba-90-d3-1a-b5-05')
    @commethod(3)
    def GetStream(ppIStream: POINTER(win32more.System.Com.IStream_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetPersistOptions(pdwPersistOptions: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetPreferredVendorGUID(pguidPreferredVendor: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def RefreshStream() -> win32more.Foundation.HRESULT: ...
@winfunctype_pointer
def PFNProgressNotification(pvData: c_void_p, uFrameNum: UInt32, operation: win32more.Graphics.Imaging.WICProgressOperation, dblProgress: Double) -> win32more.Foundation.HRESULT: ...
WIC8BIMIptcDigestProperties = UInt32
WIC8BIMIptcDigestProperties_WIC8BIMIptcDigestPString: WIC8BIMIptcDigestProperties = 1
WIC8BIMIptcDigestProperties_WIC8BIMIptcDigestIptcDigest: WIC8BIMIptcDigestProperties = 2
WIC8BIMIptcDigestProperties_WIC8BIMIptcDigestProperties_FORCE_DWORD: WIC8BIMIptcDigestProperties = 2147483647
WIC8BIMIptcProperties = UInt32
WIC8BIMIptcProperties_WIC8BIMIptcPString: WIC8BIMIptcProperties = 0
WIC8BIMIptcProperties_WIC8BIMIptcEmbeddedIPTC: WIC8BIMIptcProperties = 1
WIC8BIMIptcProperties_WIC8BIMIptcProperties_FORCE_DWORD: WIC8BIMIptcProperties = 2147483647
WIC8BIMResolutionInfoProperties = UInt32
WIC8BIMResolutionInfoProperties_WIC8BIMResolutionInfoPString: WIC8BIMResolutionInfoProperties = 1
WIC8BIMResolutionInfoProperties_WIC8BIMResolutionInfoHResolution: WIC8BIMResolutionInfoProperties = 2
WIC8BIMResolutionInfoProperties_WIC8BIMResolutionInfoHResolutionUnit: WIC8BIMResolutionInfoProperties = 3
WIC8BIMResolutionInfoProperties_WIC8BIMResolutionInfoWidthUnit: WIC8BIMResolutionInfoProperties = 4
WIC8BIMResolutionInfoProperties_WIC8BIMResolutionInfoVResolution: WIC8BIMResolutionInfoProperties = 5
WIC8BIMResolutionInfoProperties_WIC8BIMResolutionInfoVResolutionUnit: WIC8BIMResolutionInfoProperties = 6
WIC8BIMResolutionInfoProperties_WIC8BIMResolutionInfoHeightUnit: WIC8BIMResolutionInfoProperties = 7
WIC8BIMResolutionInfoProperties_WIC8BIMResolutionInfoProperties_FORCE_DWORD: WIC8BIMResolutionInfoProperties = 2147483647
WICBitmapAlphaChannelOption = Int32
WICBitmapAlphaChannelOption_WICBitmapUseAlpha: WICBitmapAlphaChannelOption = 0
WICBitmapAlphaChannelOption_WICBitmapUsePremultipliedAlpha: WICBitmapAlphaChannelOption = 1
WICBitmapAlphaChannelOption_WICBitmapIgnoreAlpha: WICBitmapAlphaChannelOption = 2
WICBitmapAlphaChannelOption_WICBITMAPALPHACHANNELOPTIONS_FORCE_DWORD: WICBitmapAlphaChannelOption = 2147483647
WICBitmapCreateCacheOption = Int32
WICBitmapCreateCacheOption_WICBitmapNoCache: WICBitmapCreateCacheOption = 0
WICBitmapCreateCacheOption_WICBitmapCacheOnDemand: WICBitmapCreateCacheOption = 1
WICBitmapCreateCacheOption_WICBitmapCacheOnLoad: WICBitmapCreateCacheOption = 2
WICBitmapCreateCacheOption_WICBITMAPCREATECACHEOPTION_FORCE_DWORD: WICBitmapCreateCacheOption = 2147483647
WICBitmapDecoderCapabilities = Int32
WICBitmapDecoderCapabilities_WICBitmapDecoderCapabilitySameEncoder: WICBitmapDecoderCapabilities = 1
WICBitmapDecoderCapabilities_WICBitmapDecoderCapabilityCanDecodeAllImages: WICBitmapDecoderCapabilities = 2
WICBitmapDecoderCapabilities_WICBitmapDecoderCapabilityCanDecodeSomeImages: WICBitmapDecoderCapabilities = 4
WICBitmapDecoderCapabilities_WICBitmapDecoderCapabilityCanEnumerateMetadata: WICBitmapDecoderCapabilities = 8
WICBitmapDecoderCapabilities_WICBitmapDecoderCapabilityCanDecodeThumbnail: WICBitmapDecoderCapabilities = 16
WICBitmapDecoderCapabilities_WICBITMAPDECODERCAPABILITIES_FORCE_DWORD: WICBitmapDecoderCapabilities = 2147483647
WICBitmapDitherType = Int32
WICBitmapDitherType_WICBitmapDitherTypeNone: WICBitmapDitherType = 0
WICBitmapDitherType_WICBitmapDitherTypeSolid: WICBitmapDitherType = 0
WICBitmapDitherType_WICBitmapDitherTypeOrdered4x4: WICBitmapDitherType = 1
WICBitmapDitherType_WICBitmapDitherTypeOrdered8x8: WICBitmapDitherType = 2
WICBitmapDitherType_WICBitmapDitherTypeOrdered16x16: WICBitmapDitherType = 3
WICBitmapDitherType_WICBitmapDitherTypeSpiral4x4: WICBitmapDitherType = 4
WICBitmapDitherType_WICBitmapDitherTypeSpiral8x8: WICBitmapDitherType = 5
WICBitmapDitherType_WICBitmapDitherTypeDualSpiral4x4: WICBitmapDitherType = 6
WICBitmapDitherType_WICBitmapDitherTypeDualSpiral8x8: WICBitmapDitherType = 7
WICBitmapDitherType_WICBitmapDitherTypeErrorDiffusion: WICBitmapDitherType = 8
WICBitmapDitherType_WICBITMAPDITHERTYPE_FORCE_DWORD: WICBitmapDitherType = 2147483647
WICBitmapEncoderCacheOption = Int32
WICBitmapEncoderCacheOption_WICBitmapEncoderCacheInMemory: WICBitmapEncoderCacheOption = 0
WICBitmapEncoderCacheOption_WICBitmapEncoderCacheTempFile: WICBitmapEncoderCacheOption = 1
WICBitmapEncoderCacheOption_WICBitmapEncoderNoCache: WICBitmapEncoderCacheOption = 2
WICBitmapEncoderCacheOption_WICBITMAPENCODERCACHEOPTION_FORCE_DWORD: WICBitmapEncoderCacheOption = 2147483647
WICBitmapInterpolationMode = Int32
WICBitmapInterpolationMode_WICBitmapInterpolationModeNearestNeighbor: WICBitmapInterpolationMode = 0
WICBitmapInterpolationMode_WICBitmapInterpolationModeLinear: WICBitmapInterpolationMode = 1
WICBitmapInterpolationMode_WICBitmapInterpolationModeCubic: WICBitmapInterpolationMode = 2
WICBitmapInterpolationMode_WICBitmapInterpolationModeFant: WICBitmapInterpolationMode = 3
WICBitmapInterpolationMode_WICBitmapInterpolationModeHighQualityCubic: WICBitmapInterpolationMode = 4
WICBitmapInterpolationMode_WICBITMAPINTERPOLATIONMODE_FORCE_DWORD: WICBitmapInterpolationMode = 2147483647
WICBitmapLockFlags = Int32
WICBitmapLockFlags_WICBitmapLockRead: WICBitmapLockFlags = 1
WICBitmapLockFlags_WICBitmapLockWrite: WICBitmapLockFlags = 2
WICBitmapLockFlags_WICBITMAPLOCKFLAGS_FORCE_DWORD: WICBitmapLockFlags = 2147483647
WICBitmapPaletteType = Int32
WICBitmapPaletteType_WICBitmapPaletteTypeCustom: WICBitmapPaletteType = 0
WICBitmapPaletteType_WICBitmapPaletteTypeMedianCut: WICBitmapPaletteType = 1
WICBitmapPaletteType_WICBitmapPaletteTypeFixedBW: WICBitmapPaletteType = 2
WICBitmapPaletteType_WICBitmapPaletteTypeFixedHalftone8: WICBitmapPaletteType = 3
WICBitmapPaletteType_WICBitmapPaletteTypeFixedHalftone27: WICBitmapPaletteType = 4
WICBitmapPaletteType_WICBitmapPaletteTypeFixedHalftone64: WICBitmapPaletteType = 5
WICBitmapPaletteType_WICBitmapPaletteTypeFixedHalftone125: WICBitmapPaletteType = 6
WICBitmapPaletteType_WICBitmapPaletteTypeFixedHalftone216: WICBitmapPaletteType = 7
WICBitmapPaletteType_WICBitmapPaletteTypeFixedWebPalette: WICBitmapPaletteType = 7
WICBitmapPaletteType_WICBitmapPaletteTypeFixedHalftone252: WICBitmapPaletteType = 8
WICBitmapPaletteType_WICBitmapPaletteTypeFixedHalftone256: WICBitmapPaletteType = 9
WICBitmapPaletteType_WICBitmapPaletteTypeFixedGray4: WICBitmapPaletteType = 10
WICBitmapPaletteType_WICBitmapPaletteTypeFixedGray16: WICBitmapPaletteType = 11
WICBitmapPaletteType_WICBitmapPaletteTypeFixedGray256: WICBitmapPaletteType = 12
WICBitmapPaletteType_WICBITMAPPALETTETYPE_FORCE_DWORD: WICBitmapPaletteType = 2147483647
class WICBitmapPattern(Structure):
    Position: win32more.Foundation.ULARGE_INTEGER
    Length: UInt32
    Pattern: c_char_p_no
    Mask: c_char_p_no
    EndOfStream: win32more.Foundation.BOOL
class WICBitmapPlane(Structure):
    Format: Guid
    pbBuffer: c_char_p_no
    cbStride: UInt32
    cbBufferSize: UInt32
class WICBitmapPlaneDescription(Structure):
    Format: Guid
    Width: UInt32
    Height: UInt32
WICBitmapTransformOptions = Int32
WICBitmapTransformOptions_WICBitmapTransformRotate0: WICBitmapTransformOptions = 0
WICBitmapTransformOptions_WICBitmapTransformRotate90: WICBitmapTransformOptions = 1
WICBitmapTransformOptions_WICBitmapTransformRotate180: WICBitmapTransformOptions = 2
WICBitmapTransformOptions_WICBitmapTransformRotate270: WICBitmapTransformOptions = 3
WICBitmapTransformOptions_WICBitmapTransformFlipHorizontal: WICBitmapTransformOptions = 8
WICBitmapTransformOptions_WICBitmapTransformFlipVertical: WICBitmapTransformOptions = 16
WICBitmapTransformOptions_WICBITMAPTRANSFORMOPTIONS_FORCE_DWORD: WICBitmapTransformOptions = 2147483647
WICColorContextType = Int32
WICColorContextType_WICColorContextUninitialized: WICColorContextType = 0
WICColorContextType_WICColorContextProfile: WICColorContextType = 1
WICColorContextType_WICColorContextExifColorSpace: WICColorContextType = 2
WICComponentEnumerateOptions = Int32
WICComponentEnumerateOptions_WICComponentEnumerateDefault: WICComponentEnumerateOptions = 0
WICComponentEnumerateOptions_WICComponentEnumerateRefresh: WICComponentEnumerateOptions = 1
WICComponentEnumerateOptions_WICComponentEnumerateDisabled: WICComponentEnumerateOptions = -2147483648
WICComponentEnumerateOptions_WICComponentEnumerateUnsigned: WICComponentEnumerateOptions = 1073741824
WICComponentEnumerateOptions_WICComponentEnumerateBuiltInOnly: WICComponentEnumerateOptions = 536870912
WICComponentEnumerateOptions_WICCOMPONENTENUMERATEOPTIONS_FORCE_DWORD: WICComponentEnumerateOptions = 2147483647
WICComponentSigning = Int32
WICComponentSigning_WICComponentSigned: WICComponentSigning = 1
WICComponentSigning_WICComponentUnsigned: WICComponentSigning = 2
WICComponentSigning_WICComponentSafe: WICComponentSigning = 4
WICComponentSigning_WICComponentDisabled: WICComponentSigning = -2147483648
WICComponentSigning_WICCOMPONENTSIGNING_FORCE_DWORD: WICComponentSigning = 2147483647
WICComponentType = Int32
WICComponentType_WICDecoder: WICComponentType = 1
WICComponentType_WICEncoder: WICComponentType = 2
WICComponentType_WICPixelFormatConverter: WICComponentType = 4
WICComponentType_WICMetadataReader: WICComponentType = 8
WICComponentType_WICMetadataWriter: WICComponentType = 16
WICComponentType_WICPixelFormat: WICComponentType = 32
WICComponentType_WICAllComponents: WICComponentType = 63
WICComponentType_WICCOMPONENTTYPE_FORCE_DWORD: WICComponentType = 2147483647
WICDdsAlphaMode = Int32
WICDdsAlphaMode_WICDdsAlphaModeUnknown: WICDdsAlphaMode = 0
WICDdsAlphaMode_WICDdsAlphaModeStraight: WICDdsAlphaMode = 1
WICDdsAlphaMode_WICDdsAlphaModePremultiplied: WICDdsAlphaMode = 2
WICDdsAlphaMode_WICDdsAlphaModeOpaque: WICDdsAlphaMode = 3
WICDdsAlphaMode_WICDdsAlphaModeCustom: WICDdsAlphaMode = 4
WICDdsAlphaMode_WICDDSALPHAMODE_FORCE_DWORD: WICDdsAlphaMode = 2147483647
WICDdsDimension = Int32
WICDdsDimension_WICDdsTexture1D: WICDdsDimension = 0
WICDdsDimension_WICDdsTexture2D: WICDdsDimension = 1
WICDdsDimension_WICDdsTexture3D: WICDdsDimension = 2
WICDdsDimension_WICDdsTextureCube: WICDdsDimension = 3
WICDdsDimension_WICDDSTEXTURE_FORCE_DWORD: WICDdsDimension = 2147483647
class WICDdsFormatInfo(Structure):
    DxgiFormat: win32more.Graphics.Dxgi.Common.DXGI_FORMAT
    BytesPerBlock: UInt32
    BlockWidth: UInt32
    BlockHeight: UInt32
class WICDdsParameters(Structure):
    Width: UInt32
    Height: UInt32
    Depth: UInt32
    MipLevels: UInt32
    ArraySize: UInt32
    DxgiFormat: win32more.Graphics.Dxgi.Common.DXGI_FORMAT
    Dimension: win32more.Graphics.Imaging.WICDdsDimension
    AlphaMode: win32more.Graphics.Imaging.WICDdsAlphaMode
WICDecodeOptions = Int32
WICDecodeOptions_WICDecodeMetadataCacheOnDemand: WICDecodeOptions = 0
WICDecodeOptions_WICDecodeMetadataCacheOnLoad: WICDecodeOptions = 1
WICDecodeOptions_WICMETADATACACHEOPTION_FORCE_DWORD: WICDecodeOptions = 2147483647
WICGifApplicationExtensionProperties = UInt32
WICGifApplicationExtensionProperties_WICGifApplicationExtensionApplication: WICGifApplicationExtensionProperties = 1
WICGifApplicationExtensionProperties_WICGifApplicationExtensionData: WICGifApplicationExtensionProperties = 2
WICGifApplicationExtensionProperties_WICGifApplicationExtensionProperties_FORCE_DWORD: WICGifApplicationExtensionProperties = 2147483647
WICGifCommentExtensionProperties = UInt32
WICGifCommentExtensionProperties_WICGifCommentExtensionText: WICGifCommentExtensionProperties = 1
WICGifCommentExtensionProperties_WICGifCommentExtensionProperties_FORCE_DWORD: WICGifCommentExtensionProperties = 2147483647
WICGifGraphicControlExtensionProperties = UInt32
WICGifGraphicControlExtensionProperties_WICGifGraphicControlExtensionDisposal: WICGifGraphicControlExtensionProperties = 1
WICGifGraphicControlExtensionProperties_WICGifGraphicControlExtensionUserInputFlag: WICGifGraphicControlExtensionProperties = 2
WICGifGraphicControlExtensionProperties_WICGifGraphicControlExtensionTransparencyFlag: WICGifGraphicControlExtensionProperties = 3
WICGifGraphicControlExtensionProperties_WICGifGraphicControlExtensionDelay: WICGifGraphicControlExtensionProperties = 4
WICGifGraphicControlExtensionProperties_WICGifGraphicControlExtensionTransparentColorIndex: WICGifGraphicControlExtensionProperties = 5
WICGifGraphicControlExtensionProperties_WICGifGraphicControlExtensionProperties_FORCE_DWORD: WICGifGraphicControlExtensionProperties = 2147483647
WICGifImageDescriptorProperties = UInt32
WICGifImageDescriptorProperties_WICGifImageDescriptorLeft: WICGifImageDescriptorProperties = 1
WICGifImageDescriptorProperties_WICGifImageDescriptorTop: WICGifImageDescriptorProperties = 2
WICGifImageDescriptorProperties_WICGifImageDescriptorWidth: WICGifImageDescriptorProperties = 3
WICGifImageDescriptorProperties_WICGifImageDescriptorHeight: WICGifImageDescriptorProperties = 4
WICGifImageDescriptorProperties_WICGifImageDescriptorLocalColorTableFlag: WICGifImageDescriptorProperties = 5
WICGifImageDescriptorProperties_WICGifImageDescriptorInterlaceFlag: WICGifImageDescriptorProperties = 6
WICGifImageDescriptorProperties_WICGifImageDescriptorSortFlag: WICGifImageDescriptorProperties = 7
WICGifImageDescriptorProperties_WICGifImageDescriptorLocalColorTableSize: WICGifImageDescriptorProperties = 8
WICGifImageDescriptorProperties_WICGifImageDescriptorProperties_FORCE_DWORD: WICGifImageDescriptorProperties = 2147483647
WICGifLogicalScreenDescriptorProperties = UInt32
WICGifLogicalScreenDescriptorProperties_WICGifLogicalScreenSignature: WICGifLogicalScreenDescriptorProperties = 1
WICGifLogicalScreenDescriptorProperties_WICGifLogicalScreenDescriptorWidth: WICGifLogicalScreenDescriptorProperties = 2
WICGifLogicalScreenDescriptorProperties_WICGifLogicalScreenDescriptorHeight: WICGifLogicalScreenDescriptorProperties = 3
WICGifLogicalScreenDescriptorProperties_WICGifLogicalScreenDescriptorGlobalColorTableFlag: WICGifLogicalScreenDescriptorProperties = 4
WICGifLogicalScreenDescriptorProperties_WICGifLogicalScreenDescriptorColorResolution: WICGifLogicalScreenDescriptorProperties = 5
WICGifLogicalScreenDescriptorProperties_WICGifLogicalScreenDescriptorSortFlag: WICGifLogicalScreenDescriptorProperties = 6
WICGifLogicalScreenDescriptorProperties_WICGifLogicalScreenDescriptorGlobalColorTableSize: WICGifLogicalScreenDescriptorProperties = 7
WICGifLogicalScreenDescriptorProperties_WICGifLogicalScreenDescriptorBackgroundColorIndex: WICGifLogicalScreenDescriptorProperties = 8
WICGifLogicalScreenDescriptorProperties_WICGifLogicalScreenDescriptorPixelAspectRatio: WICGifLogicalScreenDescriptorProperties = 9
WICGifLogicalScreenDescriptorProperties_WICGifLogicalScreenDescriptorProperties_FORCE_DWORD: WICGifLogicalScreenDescriptorProperties = 2147483647
WICHeifHdrProperties = UInt32
WICHeifHdrProperties_WICHeifHdrMaximumLuminanceLevel: WICHeifHdrProperties = 1
WICHeifHdrProperties_WICHeifHdrMaximumFrameAverageLuminanceLevel: WICHeifHdrProperties = 2
WICHeifHdrProperties_WICHeifHdrMinimumMasteringDisplayLuminanceLevel: WICHeifHdrProperties = 3
WICHeifHdrProperties_WICHeifHdrMaximumMasteringDisplayLuminanceLevel: WICHeifHdrProperties = 4
WICHeifHdrProperties_WICHeifHdrCustomVideoPrimaries: WICHeifHdrProperties = 5
WICHeifHdrProperties_WICHeifHdrProperties_FORCE_DWORD: WICHeifHdrProperties = 2147483647
WICHeifProperties = UInt32
WICHeifProperties_WICHeifOrientation: WICHeifProperties = 1
WICHeifProperties_WICHeifProperties_FORCE_DWORD: WICHeifProperties = 2147483647
class WICImageParameters(Structure):
    PixelFormat: win32more.Graphics.Direct2D.Common.D2D1_PIXEL_FORMAT
    DpiX: Single
    DpiY: Single
    Top: Single
    Left: Single
    PixelWidth: UInt32
    PixelHeight: UInt32
WICJpegChrominanceProperties = UInt32
WICJpegChrominanceProperties_WICJpegChrominanceTable: WICJpegChrominanceProperties = 1
WICJpegChrominanceProperties_WICJpegChrominanceProperties_FORCE_DWORD: WICJpegChrominanceProperties = 2147483647
WICJpegCommentProperties = UInt32
WICJpegCommentProperties_WICJpegCommentText: WICJpegCommentProperties = 1
WICJpegCommentProperties_WICJpegCommentProperties_FORCE_DWORD: WICJpegCommentProperties = 2147483647
class WICJpegFrameHeader(Structure):
    Width: UInt32
    Height: UInt32
    TransferMatrix: win32more.Graphics.Imaging.WICJpegTransferMatrix
    ScanType: win32more.Graphics.Imaging.WICJpegScanType
    cComponents: UInt32
    ComponentIdentifiers: UInt32
    SampleFactors: UInt32
    QuantizationTableIndices: UInt32
WICJpegIndexingOptions = UInt32
WICJpegIndexingOptions_WICJpegIndexingOptionsGenerateOnDemand: WICJpegIndexingOptions = 0
WICJpegIndexingOptions_WICJpegIndexingOptionsGenerateOnLoad: WICJpegIndexingOptions = 1
WICJpegIndexingOptions_WICJpegIndexingOptions_FORCE_DWORD: WICJpegIndexingOptions = 2147483647
WICJpegLuminanceProperties = UInt32
WICJpegLuminanceProperties_WICJpegLuminanceTable: WICJpegLuminanceProperties = 1
WICJpegLuminanceProperties_WICJpegLuminanceProperties_FORCE_DWORD: WICJpegLuminanceProperties = 2147483647
class WICJpegScanHeader(Structure):
    cComponents: UInt32
    RestartInterval: UInt32
    ComponentSelectors: UInt32
    HuffmanTableIndices: UInt32
    StartSpectralSelection: Byte
    EndSpectralSelection: Byte
    SuccessiveApproximationHigh: Byte
    SuccessiveApproximationLow: Byte
WICJpegScanType = UInt32
WICJpegScanType_WICJpegScanTypeInterleaved: WICJpegScanType = 0
WICJpegScanType_WICJpegScanTypePlanarComponents: WICJpegScanType = 1
WICJpegScanType_WICJpegScanTypeProgressive: WICJpegScanType = 2
WICJpegScanType_WICJpegScanType_FORCE_DWORD: WICJpegScanType = 2147483647
WICJpegTransferMatrix = UInt32
WICJpegTransferMatrix_WICJpegTransferMatrixIdentity: WICJpegTransferMatrix = 0
WICJpegTransferMatrix_WICJpegTransferMatrixBT601: WICJpegTransferMatrix = 1
WICJpegTransferMatrix_WICJpegTransferMatrix_FORCE_DWORD: WICJpegTransferMatrix = 2147483647
WICJpegYCrCbSubsamplingOption = Int32
WICJpegYCrCbSubsamplingOption_WICJpegYCrCbSubsamplingDefault: WICJpegYCrCbSubsamplingOption = 0
WICJpegYCrCbSubsamplingOption_WICJpegYCrCbSubsampling420: WICJpegYCrCbSubsamplingOption = 1
WICJpegYCrCbSubsamplingOption_WICJpegYCrCbSubsampling422: WICJpegYCrCbSubsamplingOption = 2
WICJpegYCrCbSubsamplingOption_WICJpegYCrCbSubsampling444: WICJpegYCrCbSubsamplingOption = 3
WICJpegYCrCbSubsamplingOption_WICJpegYCrCbSubsampling440: WICJpegYCrCbSubsamplingOption = 4
WICJpegYCrCbSubsamplingOption_WICJPEGYCRCBSUBSAMPLING_FORCE_DWORD: WICJpegYCrCbSubsamplingOption = 2147483647
WICMetadataCreationOptions = Int32
WICMetadataCreationOptions_WICMetadataCreationDefault: WICMetadataCreationOptions = 0
WICMetadataCreationOptions_WICMetadataCreationAllowUnknown: WICMetadataCreationOptions = 0
WICMetadataCreationOptions_WICMetadataCreationFailUnknown: WICMetadataCreationOptions = 65536
WICMetadataCreationOptions_WICMetadataCreationMask: WICMetadataCreationOptions = -65536
class WICMetadataHeader(Structure):
    Position: win32more.Foundation.ULARGE_INTEGER
    Length: UInt32
    Header: c_char_p_no
    DataOffset: win32more.Foundation.ULARGE_INTEGER
class WICMetadataPattern(Structure):
    Position: win32more.Foundation.ULARGE_INTEGER
    Length: UInt32
    Pattern: c_char_p_no
    Mask: c_char_p_no
    DataOffset: win32more.Foundation.ULARGE_INTEGER
WICNamedWhitePoint = Int32
WICNamedWhitePoint_WICWhitePointDefault: WICNamedWhitePoint = 1
WICNamedWhitePoint_WICWhitePointDaylight: WICNamedWhitePoint = 2
WICNamedWhitePoint_WICWhitePointCloudy: WICNamedWhitePoint = 4
WICNamedWhitePoint_WICWhitePointShade: WICNamedWhitePoint = 8
WICNamedWhitePoint_WICWhitePointTungsten: WICNamedWhitePoint = 16
WICNamedWhitePoint_WICWhitePointFluorescent: WICNamedWhitePoint = 32
WICNamedWhitePoint_WICWhitePointFlash: WICNamedWhitePoint = 64
WICNamedWhitePoint_WICWhitePointUnderwater: WICNamedWhitePoint = 128
WICNamedWhitePoint_WICWhitePointCustom: WICNamedWhitePoint = 256
WICNamedWhitePoint_WICWhitePointAutoWhiteBalance: WICNamedWhitePoint = 512
WICNamedWhitePoint_WICWhitePointAsShot: WICNamedWhitePoint = 1
WICNamedWhitePoint_WICNAMEDWHITEPOINT_FORCE_DWORD: WICNamedWhitePoint = 2147483647
WICPersistOptions = Int32
WICPersistOptions_WICPersistOptionDefault: WICPersistOptions = 0
WICPersistOptions_WICPersistOptionLittleEndian: WICPersistOptions = 0
WICPersistOptions_WICPersistOptionBigEndian: WICPersistOptions = 1
WICPersistOptions_WICPersistOptionStrictFormat: WICPersistOptions = 2
WICPersistOptions_WICPersistOptionNoCacheStream: WICPersistOptions = 4
WICPersistOptions_WICPersistOptionPreferUTF8: WICPersistOptions = 8
WICPersistOptions_WICPersistOptionMask: WICPersistOptions = 65535
WICPixelFormatNumericRepresentation = UInt32
WICPixelFormatNumericRepresentation_WICPixelFormatNumericRepresentationUnspecified: WICPixelFormatNumericRepresentation = 0
WICPixelFormatNumericRepresentation_WICPixelFormatNumericRepresentationIndexed: WICPixelFormatNumericRepresentation = 1
WICPixelFormatNumericRepresentation_WICPixelFormatNumericRepresentationUnsignedInteger: WICPixelFormatNumericRepresentation = 2
WICPixelFormatNumericRepresentation_WICPixelFormatNumericRepresentationSignedInteger: WICPixelFormatNumericRepresentation = 3
WICPixelFormatNumericRepresentation_WICPixelFormatNumericRepresentationFixed: WICPixelFormatNumericRepresentation = 4
WICPixelFormatNumericRepresentation_WICPixelFormatNumericRepresentationFloat: WICPixelFormatNumericRepresentation = 5
WICPixelFormatNumericRepresentation_WICPixelFormatNumericRepresentation_FORCE_DWORD: WICPixelFormatNumericRepresentation = 2147483647
WICPlanarOptions = Int32
WICPlanarOptions_WICPlanarOptionsDefault: WICPlanarOptions = 0
WICPlanarOptions_WICPlanarOptionsPreserveSubsampling: WICPlanarOptions = 1
WICPlanarOptions_WICPLANAROPTIONS_FORCE_DWORD: WICPlanarOptions = 2147483647
WICPngBkgdProperties = UInt32
WICPngBkgdProperties_WICPngBkgdBackgroundColor: WICPngBkgdProperties = 1
WICPngBkgdProperties_WICPngBkgdProperties_FORCE_DWORD: WICPngBkgdProperties = 2147483647
WICPngChrmProperties = UInt32
WICPngChrmProperties_WICPngChrmWhitePointX: WICPngChrmProperties = 1
WICPngChrmProperties_WICPngChrmWhitePointY: WICPngChrmProperties = 2
WICPngChrmProperties_WICPngChrmRedX: WICPngChrmProperties = 3
WICPngChrmProperties_WICPngChrmRedY: WICPngChrmProperties = 4
WICPngChrmProperties_WICPngChrmGreenX: WICPngChrmProperties = 5
WICPngChrmProperties_WICPngChrmGreenY: WICPngChrmProperties = 6
WICPngChrmProperties_WICPngChrmBlueX: WICPngChrmProperties = 7
WICPngChrmProperties_WICPngChrmBlueY: WICPngChrmProperties = 8
WICPngChrmProperties_WICPngChrmProperties_FORCE_DWORD: WICPngChrmProperties = 2147483647
WICPngFilterOption = Int32
WICPngFilterOption_WICPngFilterUnspecified: WICPngFilterOption = 0
WICPngFilterOption_WICPngFilterNone: WICPngFilterOption = 1
WICPngFilterOption_WICPngFilterSub: WICPngFilterOption = 2
WICPngFilterOption_WICPngFilterUp: WICPngFilterOption = 3
WICPngFilterOption_WICPngFilterAverage: WICPngFilterOption = 4
WICPngFilterOption_WICPngFilterPaeth: WICPngFilterOption = 5
WICPngFilterOption_WICPngFilterAdaptive: WICPngFilterOption = 6
WICPngFilterOption_WICPNGFILTEROPTION_FORCE_DWORD: WICPngFilterOption = 2147483647
WICPngGamaProperties = UInt32
WICPngGamaProperties_WICPngGamaGamma: WICPngGamaProperties = 1
WICPngGamaProperties_WICPngGamaProperties_FORCE_DWORD: WICPngGamaProperties = 2147483647
WICPngHistProperties = UInt32
WICPngHistProperties_WICPngHistFrequencies: WICPngHistProperties = 1
WICPngHistProperties_WICPngHistProperties_FORCE_DWORD: WICPngHistProperties = 2147483647
WICPngIccpProperties = UInt32
WICPngIccpProperties_WICPngIccpProfileName: WICPngIccpProperties = 1
WICPngIccpProperties_WICPngIccpProfileData: WICPngIccpProperties = 2
WICPngIccpProperties_WICPngIccpProperties_FORCE_DWORD: WICPngIccpProperties = 2147483647
WICPngItxtProperties = UInt32
WICPngItxtProperties_WICPngItxtKeyword: WICPngItxtProperties = 1
WICPngItxtProperties_WICPngItxtCompressionFlag: WICPngItxtProperties = 2
WICPngItxtProperties_WICPngItxtLanguageTag: WICPngItxtProperties = 3
WICPngItxtProperties_WICPngItxtTranslatedKeyword: WICPngItxtProperties = 4
WICPngItxtProperties_WICPngItxtText: WICPngItxtProperties = 5
WICPngItxtProperties_WICPngItxtProperties_FORCE_DWORD: WICPngItxtProperties = 2147483647
WICPngSrgbProperties = UInt32
WICPngSrgbProperties_WICPngSrgbRenderingIntent: WICPngSrgbProperties = 1
WICPngSrgbProperties_WICPngSrgbProperties_FORCE_DWORD: WICPngSrgbProperties = 2147483647
WICPngTimeProperties = UInt32
WICPngTimeProperties_WICPngTimeYear: WICPngTimeProperties = 1
WICPngTimeProperties_WICPngTimeMonth: WICPngTimeProperties = 2
WICPngTimeProperties_WICPngTimeDay: WICPngTimeProperties = 3
WICPngTimeProperties_WICPngTimeHour: WICPngTimeProperties = 4
WICPngTimeProperties_WICPngTimeMinute: WICPngTimeProperties = 5
WICPngTimeProperties_WICPngTimeSecond: WICPngTimeProperties = 6
WICPngTimeProperties_WICPngTimeProperties_FORCE_DWORD: WICPngTimeProperties = 2147483647
WICProgressNotification = Int32
WICProgressNotification_WICProgressNotificationBegin: WICProgressNotification = 65536
WICProgressNotification_WICProgressNotificationEnd: WICProgressNotification = 131072
WICProgressNotification_WICProgressNotificationFrequent: WICProgressNotification = 262144
WICProgressNotification_WICProgressNotificationAll: WICProgressNotification = -65536
WICProgressNotification_WICPROGRESSNOTIFICATION_FORCE_DWORD: WICProgressNotification = 2147483647
WICProgressOperation = Int32
WICProgressOperation_WICProgressOperationCopyPixels: WICProgressOperation = 1
WICProgressOperation_WICProgressOperationWritePixels: WICProgressOperation = 2
WICProgressOperation_WICProgressOperationAll: WICProgressOperation = 65535
WICProgressOperation_WICPROGRESSOPERATION_FORCE_DWORD: WICProgressOperation = 2147483647
WICRawCapabilities = Int32
WICRawCapabilities_WICRawCapabilityNotSupported: WICRawCapabilities = 0
WICRawCapabilities_WICRawCapabilityGetSupported: WICRawCapabilities = 1
WICRawCapabilities_WICRawCapabilityFullySupported: WICRawCapabilities = 2
WICRawCapabilities_WICRAWCAPABILITIES_FORCE_DWORD: WICRawCapabilities = 2147483647
class WICRawCapabilitiesInfo(Structure):
    cbSize: UInt32
    CodecMajorVersion: UInt32
    CodecMinorVersion: UInt32
    ExposureCompensationSupport: win32more.Graphics.Imaging.WICRawCapabilities
    ContrastSupport: win32more.Graphics.Imaging.WICRawCapabilities
    RGBWhitePointSupport: win32more.Graphics.Imaging.WICRawCapabilities
    NamedWhitePointSupport: win32more.Graphics.Imaging.WICRawCapabilities
    NamedWhitePointSupportMask: UInt32
    KelvinWhitePointSupport: win32more.Graphics.Imaging.WICRawCapabilities
    GammaSupport: win32more.Graphics.Imaging.WICRawCapabilities
    TintSupport: win32more.Graphics.Imaging.WICRawCapabilities
    SaturationSupport: win32more.Graphics.Imaging.WICRawCapabilities
    SharpnessSupport: win32more.Graphics.Imaging.WICRawCapabilities
    NoiseReductionSupport: win32more.Graphics.Imaging.WICRawCapabilities
    DestinationColorProfileSupport: win32more.Graphics.Imaging.WICRawCapabilities
    ToneCurveSupport: win32more.Graphics.Imaging.WICRawCapabilities
    RotationSupport: win32more.Graphics.Imaging.WICRawRotationCapabilities
    RenderModeSupport: win32more.Graphics.Imaging.WICRawCapabilities
WICRawParameterSet = Int32
WICRawParameterSet_WICAsShotParameterSet: WICRawParameterSet = 1
WICRawParameterSet_WICUserAdjustedParameterSet: WICRawParameterSet = 2
WICRawParameterSet_WICAutoAdjustedParameterSet: WICRawParameterSet = 3
WICRawParameterSet_WICRAWPARAMETERSET_FORCE_DWORD: WICRawParameterSet = 2147483647
WICRawRenderMode = Int32
WICRawRenderMode_WICRawRenderModeDraft: WICRawRenderMode = 1
WICRawRenderMode_WICRawRenderModeNormal: WICRawRenderMode = 2
WICRawRenderMode_WICRawRenderModeBestQuality: WICRawRenderMode = 3
WICRawRenderMode_WICRAWRENDERMODE_FORCE_DWORD: WICRawRenderMode = 2147483647
WICRawRotationCapabilities = Int32
WICRawRotationCapabilities_WICRawRotationCapabilityNotSupported: WICRawRotationCapabilities = 0
WICRawRotationCapabilities_WICRawRotationCapabilityGetSupported: WICRawRotationCapabilities = 1
WICRawRotationCapabilities_WICRawRotationCapabilityNinetyDegreesSupported: WICRawRotationCapabilities = 2
WICRawRotationCapabilities_WICRawRotationCapabilityFullySupported: WICRawRotationCapabilities = 3
WICRawRotationCapabilities_WICRAWROTATIONCAPABILITIES_FORCE_DWORD: WICRawRotationCapabilities = 2147483647
class WICRawToneCurve(Structure):
    cPoints: UInt32
    aPoints: win32more.Graphics.Imaging.WICRawToneCurvePoint * 1
class WICRawToneCurvePoint(Structure):
    Input: Double
    Output: Double
class WICRect(Structure):
    X: Int32
    Y: Int32
    Width: Int32
    Height: Int32
WICSectionAccessLevel = UInt32
WICSectionAccessLevel_WICSectionAccessLevelRead: WICSectionAccessLevel = 1
WICSectionAccessLevel_WICSectionAccessLevelReadWrite: WICSectionAccessLevel = 3
WICSectionAccessLevel_WICSectionAccessLevel_FORCE_DWORD: WICSectionAccessLevel = 2147483647
WICTiffCompressionOption = Int32
WICTiffCompressionOption_WICTiffCompressionDontCare: WICTiffCompressionOption = 0
WICTiffCompressionOption_WICTiffCompressionNone: WICTiffCompressionOption = 1
WICTiffCompressionOption_WICTiffCompressionCCITT3: WICTiffCompressionOption = 2
WICTiffCompressionOption_WICTiffCompressionCCITT4: WICTiffCompressionOption = 3
WICTiffCompressionOption_WICTiffCompressionLZW: WICTiffCompressionOption = 4
WICTiffCompressionOption_WICTiffCompressionRLE: WICTiffCompressionOption = 5
WICTiffCompressionOption_WICTiffCompressionZIP: WICTiffCompressionOption = 6
WICTiffCompressionOption_WICTiffCompressionLZWHDifferencing: WICTiffCompressionOption = 7
WICTiffCompressionOption_WICTIFFCOMPRESSIONOPTION_FORCE_DWORD: WICTiffCompressionOption = 2147483647
WICWebpAnimProperties = UInt32
WICWebpAnimProperties_WICWebpAnimLoopCount: WICWebpAnimProperties = 1
WICWebpAnimProperties_WICWebpAnimProperties_FORCE_DWORD: WICWebpAnimProperties = 2147483647
WICWebpAnmfProperties = UInt32
WICWebpAnmfProperties_WICWebpAnmfFrameDuration: WICWebpAnmfProperties = 1
WICWebpAnmfProperties_WICWebpAnmfProperties_FORCE_DWORD: WICWebpAnmfProperties = 2147483647
make_head(_module, 'IWICBitmap')
make_head(_module, 'IWICBitmapClipper')
make_head(_module, 'IWICBitmapCodecInfo')
make_head(_module, 'IWICBitmapCodecProgressNotification')
make_head(_module, 'IWICBitmapDecoder')
make_head(_module, 'IWICBitmapDecoderInfo')
make_head(_module, 'IWICBitmapEncoder')
make_head(_module, 'IWICBitmapEncoderInfo')
make_head(_module, 'IWICBitmapFlipRotator')
make_head(_module, 'IWICBitmapFrameDecode')
make_head(_module, 'IWICBitmapFrameEncode')
make_head(_module, 'IWICBitmapLock')
make_head(_module, 'IWICBitmapScaler')
make_head(_module, 'IWICBitmapSource')
make_head(_module, 'IWICBitmapSourceTransform')
make_head(_module, 'IWICColorContext')
make_head(_module, 'IWICColorTransform')
make_head(_module, 'IWICComponentFactory')
make_head(_module, 'IWICComponentInfo')
make_head(_module, 'IWICDdsDecoder')
make_head(_module, 'IWICDdsEncoder')
make_head(_module, 'IWICDdsFrameDecode')
make_head(_module, 'IWICDevelopRaw')
make_head(_module, 'IWICDevelopRawNotificationCallback')
make_head(_module, 'IWICEnumMetadataItem')
make_head(_module, 'IWICFastMetadataEncoder')
make_head(_module, 'IWICFormatConverter')
make_head(_module, 'IWICFormatConverterInfo')
make_head(_module, 'IWICImagingFactory')
make_head(_module, 'IWICJpegFrameDecode')
make_head(_module, 'IWICJpegFrameEncode')
make_head(_module, 'IWICMetadataBlockReader')
make_head(_module, 'IWICMetadataBlockWriter')
make_head(_module, 'IWICMetadataHandlerInfo')
make_head(_module, 'IWICMetadataQueryReader')
make_head(_module, 'IWICMetadataQueryWriter')
make_head(_module, 'IWICMetadataReader')
make_head(_module, 'IWICMetadataReaderInfo')
make_head(_module, 'IWICMetadataWriter')
make_head(_module, 'IWICMetadataWriterInfo')
make_head(_module, 'IWICPalette')
make_head(_module, 'IWICPersistStream')
make_head(_module, 'IWICPixelFormatInfo')
make_head(_module, 'IWICPixelFormatInfo2')
make_head(_module, 'IWICPlanarBitmapFrameEncode')
make_head(_module, 'IWICPlanarBitmapSourceTransform')
make_head(_module, 'IWICPlanarFormatConverter')
make_head(_module, 'IWICProgressCallback')
make_head(_module, 'IWICProgressiveLevelControl')
make_head(_module, 'IWICStream')
make_head(_module, 'IWICStreamProvider')
make_head(_module, 'PFNProgressNotification')
make_head(_module, 'WICBitmapPattern')
make_head(_module, 'WICBitmapPlane')
make_head(_module, 'WICBitmapPlaneDescription')
make_head(_module, 'WICDdsFormatInfo')
make_head(_module, 'WICDdsParameters')
make_head(_module, 'WICImageParameters')
make_head(_module, 'WICJpegFrameHeader')
make_head(_module, 'WICJpegScanHeader')
make_head(_module, 'WICMetadataHeader')
make_head(_module, 'WICMetadataPattern')
make_head(_module, 'WICRawCapabilitiesInfo')
make_head(_module, 'WICRawToneCurve')
make_head(_module, 'WICRawToneCurvePoint')
make_head(_module, 'WICRect')
__all__ = [
    "CATID_WICBitmapDecoders",
    "CATID_WICBitmapEncoders",
    "CATID_WICFormatConverters",
    "CATID_WICMetadataReader",
    "CATID_WICMetadataWriter",
    "CATID_WICPixelFormats",
    "CLSID_WIC8BIMIPTCDigestMetadataReader",
    "CLSID_WIC8BIMIPTCDigestMetadataWriter",
    "CLSID_WIC8BIMIPTCMetadataReader",
    "CLSID_WIC8BIMIPTCMetadataWriter",
    "CLSID_WIC8BIMResolutionInfoMetadataReader",
    "CLSID_WIC8BIMResolutionInfoMetadataWriter",
    "CLSID_WICAPEMetadataReader",
    "CLSID_WICAPEMetadataWriter",
    "CLSID_WICAdngDecoder",
    "CLSID_WICApp0MetadataReader",
    "CLSID_WICApp0MetadataWriter",
    "CLSID_WICApp13MetadataReader",
    "CLSID_WICApp13MetadataWriter",
    "CLSID_WICApp1MetadataReader",
    "CLSID_WICApp1MetadataWriter",
    "CLSID_WICBmpDecoder",
    "CLSID_WICBmpEncoder",
    "CLSID_WICDdsDecoder",
    "CLSID_WICDdsEncoder",
    "CLSID_WICDdsMetadataReader",
    "CLSID_WICDdsMetadataWriter",
    "CLSID_WICDefaultFormatConverter",
    "CLSID_WICExifMetadataReader",
    "CLSID_WICExifMetadataWriter",
    "CLSID_WICFormatConverterHighColor",
    "CLSID_WICFormatConverterNChannel",
    "CLSID_WICFormatConverterWMPhoto",
    "CLSID_WICGCEMetadataReader",
    "CLSID_WICGCEMetadataWriter",
    "CLSID_WICGifCommentMetadataReader",
    "CLSID_WICGifCommentMetadataWriter",
    "CLSID_WICGifDecoder",
    "CLSID_WICGifEncoder",
    "CLSID_WICGpsMetadataReader",
    "CLSID_WICGpsMetadataWriter",
    "CLSID_WICHeifDecoder",
    "CLSID_WICHeifEncoder",
    "CLSID_WICHeifHDRMetadataReader",
    "CLSID_WICHeifMetadataReader",
    "CLSID_WICHeifMetadataWriter",
    "CLSID_WICIMDMetadataReader",
    "CLSID_WICIMDMetadataWriter",
    "CLSID_WICIPTCMetadataReader",
    "CLSID_WICIPTCMetadataWriter",
    "CLSID_WICIRBMetadataReader",
    "CLSID_WICIRBMetadataWriter",
    "CLSID_WICIcoDecoder",
    "CLSID_WICIfdMetadataReader",
    "CLSID_WICIfdMetadataWriter",
    "CLSID_WICImagingCategories",
    "CLSID_WICImagingFactory",
    "CLSID_WICImagingFactory1",
    "CLSID_WICImagingFactory2",
    "CLSID_WICInteropMetadataReader",
    "CLSID_WICInteropMetadataWriter",
    "CLSID_WICJpegChrominanceMetadataReader",
    "CLSID_WICJpegChrominanceMetadataWriter",
    "CLSID_WICJpegCommentMetadataReader",
    "CLSID_WICJpegCommentMetadataWriter",
    "CLSID_WICJpegDecoder",
    "CLSID_WICJpegEncoder",
    "CLSID_WICJpegLuminanceMetadataReader",
    "CLSID_WICJpegLuminanceMetadataWriter",
    "CLSID_WICJpegQualcommPhoneEncoder",
    "CLSID_WICLSDMetadataReader",
    "CLSID_WICLSDMetadataWriter",
    "CLSID_WICPlanarFormatConverter",
    "CLSID_WICPngBkgdMetadataReader",
    "CLSID_WICPngBkgdMetadataWriter",
    "CLSID_WICPngChrmMetadataReader",
    "CLSID_WICPngChrmMetadataWriter",
    "CLSID_WICPngDecoder",
    "CLSID_WICPngDecoder1",
    "CLSID_WICPngDecoder2",
    "CLSID_WICPngEncoder",
    "CLSID_WICPngGamaMetadataReader",
    "CLSID_WICPngGamaMetadataWriter",
    "CLSID_WICPngHistMetadataReader",
    "CLSID_WICPngHistMetadataWriter",
    "CLSID_WICPngIccpMetadataReader",
    "CLSID_WICPngIccpMetadataWriter",
    "CLSID_WICPngItxtMetadataReader",
    "CLSID_WICPngItxtMetadataWriter",
    "CLSID_WICPngSrgbMetadataReader",
    "CLSID_WICPngSrgbMetadataWriter",
    "CLSID_WICPngTextMetadataReader",
    "CLSID_WICPngTextMetadataWriter",
    "CLSID_WICPngTimeMetadataReader",
    "CLSID_WICPngTimeMetadataWriter",
    "CLSID_WICRAWDecoder",
    "CLSID_WICSubIfdMetadataReader",
    "CLSID_WICSubIfdMetadataWriter",
    "CLSID_WICThumbnailMetadataReader",
    "CLSID_WICThumbnailMetadataWriter",
    "CLSID_WICTiffDecoder",
    "CLSID_WICTiffEncoder",
    "CLSID_WICUnknownMetadataReader",
    "CLSID_WICUnknownMetadataWriter",
    "CLSID_WICWebpAnimMetadataReader",
    "CLSID_WICWebpAnmfMetadataReader",
    "CLSID_WICWebpDecoder",
    "CLSID_WICWmpDecoder",
    "CLSID_WICWmpEncoder",
    "CLSID_WICXMPAltMetadataReader",
    "CLSID_WICXMPAltMetadataWriter",
    "CLSID_WICXMPBagMetadataReader",
    "CLSID_WICXMPBagMetadataWriter",
    "CLSID_WICXMPMetadataReader",
    "CLSID_WICXMPMetadataWriter",
    "CLSID_WICXMPSeqMetadataReader",
    "CLSID_WICXMPSeqMetadataWriter",
    "CLSID_WICXMPStructMetadataReader",
    "CLSID_WICXMPStructMetadataWriter",
    "FACILITY_WINCODEC_ERR",
    "GUID_ContainerFormatAdng",
    "GUID_ContainerFormatBmp",
    "GUID_ContainerFormatDds",
    "GUID_ContainerFormatGif",
    "GUID_ContainerFormatHeif",
    "GUID_ContainerFormatIco",
    "GUID_ContainerFormatJpeg",
    "GUID_ContainerFormatPng",
    "GUID_ContainerFormatRaw",
    "GUID_ContainerFormatTiff",
    "GUID_ContainerFormatWebp",
    "GUID_ContainerFormatWmp",
    "GUID_MetadataFormat8BIMIPTC",
    "GUID_MetadataFormat8BIMIPTCDigest",
    "GUID_MetadataFormat8BIMResolutionInfo",
    "GUID_MetadataFormatAPE",
    "GUID_MetadataFormatApp0",
    "GUID_MetadataFormatApp1",
    "GUID_MetadataFormatApp13",
    "GUID_MetadataFormatChunkbKGD",
    "GUID_MetadataFormatChunkcHRM",
    "GUID_MetadataFormatChunkgAMA",
    "GUID_MetadataFormatChunkhIST",
    "GUID_MetadataFormatChunkiCCP",
    "GUID_MetadataFormatChunkiTXt",
    "GUID_MetadataFormatChunksRGB",
    "GUID_MetadataFormatChunktEXt",
    "GUID_MetadataFormatChunktIME",
    "GUID_MetadataFormatDds",
    "GUID_MetadataFormatExif",
    "GUID_MetadataFormatGCE",
    "GUID_MetadataFormatGifComment",
    "GUID_MetadataFormatGps",
    "GUID_MetadataFormatHeif",
    "GUID_MetadataFormatHeifHDR",
    "GUID_MetadataFormatIMD",
    "GUID_MetadataFormatIPTC",
    "GUID_MetadataFormatIRB",
    "GUID_MetadataFormatIfd",
    "GUID_MetadataFormatInterop",
    "GUID_MetadataFormatJpegChrominance",
    "GUID_MetadataFormatJpegComment",
    "GUID_MetadataFormatJpegLuminance",
    "GUID_MetadataFormatLSD",
    "GUID_MetadataFormatSubIfd",
    "GUID_MetadataFormatThumbnail",
    "GUID_MetadataFormatUnknown",
    "GUID_MetadataFormatWebpANIM",
    "GUID_MetadataFormatWebpANMF",
    "GUID_MetadataFormatXMP",
    "GUID_MetadataFormatXMPAlt",
    "GUID_MetadataFormatXMPBag",
    "GUID_MetadataFormatXMPSeq",
    "GUID_MetadataFormatXMPStruct",
    "GUID_VendorMicrosoft",
    "GUID_VendorMicrosoftBuiltIn",
    "GUID_WICPixelFormat112bpp6ChannelsAlpha",
    "GUID_WICPixelFormat112bpp7Channels",
    "GUID_WICPixelFormat128bpp7ChannelsAlpha",
    "GUID_WICPixelFormat128bpp8Channels",
    "GUID_WICPixelFormat128bppPRGBAFloat",
    "GUID_WICPixelFormat128bppRGBAFixedPoint",
    "GUID_WICPixelFormat128bppRGBAFloat",
    "GUID_WICPixelFormat128bppRGBFixedPoint",
    "GUID_WICPixelFormat128bppRGBFloat",
    "GUID_WICPixelFormat144bpp8ChannelsAlpha",
    "GUID_WICPixelFormat16bppBGR555",
    "GUID_WICPixelFormat16bppBGR565",
    "GUID_WICPixelFormat16bppBGRA5551",
    "GUID_WICPixelFormat16bppCbCr",
    "GUID_WICPixelFormat16bppCbQuantizedDctCoefficients",
    "GUID_WICPixelFormat16bppCrQuantizedDctCoefficients",
    "GUID_WICPixelFormat16bppGray",
    "GUID_WICPixelFormat16bppGrayFixedPoint",
    "GUID_WICPixelFormat16bppGrayHalf",
    "GUID_WICPixelFormat16bppYQuantizedDctCoefficients",
    "GUID_WICPixelFormat1bppIndexed",
    "GUID_WICPixelFormat24bpp3Channels",
    "GUID_WICPixelFormat24bppBGR",
    "GUID_WICPixelFormat24bppRGB",
    "GUID_WICPixelFormat2bppGray",
    "GUID_WICPixelFormat2bppIndexed",
    "GUID_WICPixelFormat32bpp3ChannelsAlpha",
    "GUID_WICPixelFormat32bpp4Channels",
    "GUID_WICPixelFormat32bppBGR",
    "GUID_WICPixelFormat32bppBGR101010",
    "GUID_WICPixelFormat32bppBGRA",
    "GUID_WICPixelFormat32bppCMYK",
    "GUID_WICPixelFormat32bppGrayFixedPoint",
    "GUID_WICPixelFormat32bppGrayFloat",
    "GUID_WICPixelFormat32bppPBGRA",
    "GUID_WICPixelFormat32bppPRGBA",
    "GUID_WICPixelFormat32bppR10G10B10A2",
    "GUID_WICPixelFormat32bppR10G10B10A2HDR10",
    "GUID_WICPixelFormat32bppRGB",
    "GUID_WICPixelFormat32bppRGBA",
    "GUID_WICPixelFormat32bppRGBA1010102",
    "GUID_WICPixelFormat32bppRGBA1010102XR",
    "GUID_WICPixelFormat32bppRGBE",
    "GUID_WICPixelFormat40bpp4ChannelsAlpha",
    "GUID_WICPixelFormat40bpp5Channels",
    "GUID_WICPixelFormat40bppCMYKAlpha",
    "GUID_WICPixelFormat48bpp3Channels",
    "GUID_WICPixelFormat48bpp5ChannelsAlpha",
    "GUID_WICPixelFormat48bpp6Channels",
    "GUID_WICPixelFormat48bppBGR",
    "GUID_WICPixelFormat48bppBGRFixedPoint",
    "GUID_WICPixelFormat48bppRGB",
    "GUID_WICPixelFormat48bppRGBFixedPoint",
    "GUID_WICPixelFormat48bppRGBHalf",
    "GUID_WICPixelFormat4bppGray",
    "GUID_WICPixelFormat4bppIndexed",
    "GUID_WICPixelFormat56bpp6ChannelsAlpha",
    "GUID_WICPixelFormat56bpp7Channels",
    "GUID_WICPixelFormat64bpp3ChannelsAlpha",
    "GUID_WICPixelFormat64bpp4Channels",
    "GUID_WICPixelFormat64bpp7ChannelsAlpha",
    "GUID_WICPixelFormat64bpp8Channels",
    "GUID_WICPixelFormat64bppBGRA",
    "GUID_WICPixelFormat64bppBGRAFixedPoint",
    "GUID_WICPixelFormat64bppCMYK",
    "GUID_WICPixelFormat64bppPBGRA",
    "GUID_WICPixelFormat64bppPRGBA",
    "GUID_WICPixelFormat64bppPRGBAHalf",
    "GUID_WICPixelFormat64bppRGB",
    "GUID_WICPixelFormat64bppRGBA",
    "GUID_WICPixelFormat64bppRGBAFixedPoint",
    "GUID_WICPixelFormat64bppRGBAHalf",
    "GUID_WICPixelFormat64bppRGBFixedPoint",
    "GUID_WICPixelFormat64bppRGBHalf",
    "GUID_WICPixelFormat72bpp8ChannelsAlpha",
    "GUID_WICPixelFormat80bpp4ChannelsAlpha",
    "GUID_WICPixelFormat80bpp5Channels",
    "GUID_WICPixelFormat80bppCMYKAlpha",
    "GUID_WICPixelFormat8bppAlpha",
    "GUID_WICPixelFormat8bppCb",
    "GUID_WICPixelFormat8bppCr",
    "GUID_WICPixelFormat8bppGray",
    "GUID_WICPixelFormat8bppIndexed",
    "GUID_WICPixelFormat8bppY",
    "GUID_WICPixelFormat96bpp5ChannelsAlpha",
    "GUID_WICPixelFormat96bpp6Channels",
    "GUID_WICPixelFormat96bppRGBFixedPoint",
    "GUID_WICPixelFormat96bppRGBFloat",
    "GUID_WICPixelFormatBlackWhite",
    "GUID_WICPixelFormatDontCare",
    "IWICBitmap",
    "IWICBitmapClipper",
    "IWICBitmapCodecInfo",
    "IWICBitmapCodecProgressNotification",
    "IWICBitmapDecoder",
    "IWICBitmapDecoderInfo",
    "IWICBitmapEncoder",
    "IWICBitmapEncoderInfo",
    "IWICBitmapFlipRotator",
    "IWICBitmapFrameDecode",
    "IWICBitmapFrameEncode",
    "IWICBitmapLock",
    "IWICBitmapScaler",
    "IWICBitmapSource",
    "IWICBitmapSourceTransform",
    "IWICColorContext",
    "IWICColorTransform",
    "IWICComponentFactory",
    "IWICComponentInfo",
    "IWICDdsDecoder",
    "IWICDdsEncoder",
    "IWICDdsFrameDecode",
    "IWICDevelopRaw",
    "IWICDevelopRawNotificationCallback",
    "IWICEnumMetadataItem",
    "IWICFastMetadataEncoder",
    "IWICFormatConverter",
    "IWICFormatConverterInfo",
    "IWICImagingFactory",
    "IWICJpegFrameDecode",
    "IWICJpegFrameEncode",
    "IWICMetadataBlockReader",
    "IWICMetadataBlockWriter",
    "IWICMetadataHandlerInfo",
    "IWICMetadataQueryReader",
    "IWICMetadataQueryWriter",
    "IWICMetadataReader",
    "IWICMetadataReaderInfo",
    "IWICMetadataWriter",
    "IWICMetadataWriterInfo",
    "IWICPalette",
    "IWICPersistStream",
    "IWICPixelFormatInfo",
    "IWICPixelFormatInfo2",
    "IWICPlanarBitmapFrameEncode",
    "IWICPlanarBitmapSourceTransform",
    "IWICPlanarFormatConverter",
    "IWICProgressCallback",
    "IWICProgressiveLevelControl",
    "IWICStream",
    "IWICStreamProvider",
    "PFNProgressNotification",
    "WIC8BIMIptcDigestProperties",
    "WIC8BIMIptcDigestProperties_WIC8BIMIptcDigestIptcDigest",
    "WIC8BIMIptcDigestProperties_WIC8BIMIptcDigestPString",
    "WIC8BIMIptcDigestProperties_WIC8BIMIptcDigestProperties_FORCE_DWORD",
    "WIC8BIMIptcProperties",
    "WIC8BIMIptcProperties_WIC8BIMIptcEmbeddedIPTC",
    "WIC8BIMIptcProperties_WIC8BIMIptcPString",
    "WIC8BIMIptcProperties_WIC8BIMIptcProperties_FORCE_DWORD",
    "WIC8BIMResolutionInfoProperties",
    "WIC8BIMResolutionInfoProperties_WIC8BIMResolutionInfoHResolution",
    "WIC8BIMResolutionInfoProperties_WIC8BIMResolutionInfoHResolutionUnit",
    "WIC8BIMResolutionInfoProperties_WIC8BIMResolutionInfoHeightUnit",
    "WIC8BIMResolutionInfoProperties_WIC8BIMResolutionInfoPString",
    "WIC8BIMResolutionInfoProperties_WIC8BIMResolutionInfoProperties_FORCE_DWORD",
    "WIC8BIMResolutionInfoProperties_WIC8BIMResolutionInfoVResolution",
    "WIC8BIMResolutionInfoProperties_WIC8BIMResolutionInfoVResolutionUnit",
    "WIC8BIMResolutionInfoProperties_WIC8BIMResolutionInfoWidthUnit",
    "WICBitmapAlphaChannelOption",
    "WICBitmapAlphaChannelOption_WICBITMAPALPHACHANNELOPTIONS_FORCE_DWORD",
    "WICBitmapAlphaChannelOption_WICBitmapIgnoreAlpha",
    "WICBitmapAlphaChannelOption_WICBitmapUseAlpha",
    "WICBitmapAlphaChannelOption_WICBitmapUsePremultipliedAlpha",
    "WICBitmapCreateCacheOption",
    "WICBitmapCreateCacheOption_WICBITMAPCREATECACHEOPTION_FORCE_DWORD",
    "WICBitmapCreateCacheOption_WICBitmapCacheOnDemand",
    "WICBitmapCreateCacheOption_WICBitmapCacheOnLoad",
    "WICBitmapCreateCacheOption_WICBitmapNoCache",
    "WICBitmapDecoderCapabilities",
    "WICBitmapDecoderCapabilities_WICBITMAPDECODERCAPABILITIES_FORCE_DWORD",
    "WICBitmapDecoderCapabilities_WICBitmapDecoderCapabilityCanDecodeAllImages",
    "WICBitmapDecoderCapabilities_WICBitmapDecoderCapabilityCanDecodeSomeImages",
    "WICBitmapDecoderCapabilities_WICBitmapDecoderCapabilityCanDecodeThumbnail",
    "WICBitmapDecoderCapabilities_WICBitmapDecoderCapabilityCanEnumerateMetadata",
    "WICBitmapDecoderCapabilities_WICBitmapDecoderCapabilitySameEncoder",
    "WICBitmapDitherType",
    "WICBitmapDitherType_WICBITMAPDITHERTYPE_FORCE_DWORD",
    "WICBitmapDitherType_WICBitmapDitherTypeDualSpiral4x4",
    "WICBitmapDitherType_WICBitmapDitherTypeDualSpiral8x8",
    "WICBitmapDitherType_WICBitmapDitherTypeErrorDiffusion",
    "WICBitmapDitherType_WICBitmapDitherTypeNone",
    "WICBitmapDitherType_WICBitmapDitherTypeOrdered16x16",
    "WICBitmapDitherType_WICBitmapDitherTypeOrdered4x4",
    "WICBitmapDitherType_WICBitmapDitherTypeOrdered8x8",
    "WICBitmapDitherType_WICBitmapDitherTypeSolid",
    "WICBitmapDitherType_WICBitmapDitherTypeSpiral4x4",
    "WICBitmapDitherType_WICBitmapDitherTypeSpiral8x8",
    "WICBitmapEncoderCacheOption",
    "WICBitmapEncoderCacheOption_WICBITMAPENCODERCACHEOPTION_FORCE_DWORD",
    "WICBitmapEncoderCacheOption_WICBitmapEncoderCacheInMemory",
    "WICBitmapEncoderCacheOption_WICBitmapEncoderCacheTempFile",
    "WICBitmapEncoderCacheOption_WICBitmapEncoderNoCache",
    "WICBitmapInterpolationMode",
    "WICBitmapInterpolationMode_WICBITMAPINTERPOLATIONMODE_FORCE_DWORD",
    "WICBitmapInterpolationMode_WICBitmapInterpolationModeCubic",
    "WICBitmapInterpolationMode_WICBitmapInterpolationModeFant",
    "WICBitmapInterpolationMode_WICBitmapInterpolationModeHighQualityCubic",
    "WICBitmapInterpolationMode_WICBitmapInterpolationModeLinear",
    "WICBitmapInterpolationMode_WICBitmapInterpolationModeNearestNeighbor",
    "WICBitmapLockFlags",
    "WICBitmapLockFlags_WICBITMAPLOCKFLAGS_FORCE_DWORD",
    "WICBitmapLockFlags_WICBitmapLockRead",
    "WICBitmapLockFlags_WICBitmapLockWrite",
    "WICBitmapPaletteType",
    "WICBitmapPaletteType_WICBITMAPPALETTETYPE_FORCE_DWORD",
    "WICBitmapPaletteType_WICBitmapPaletteTypeCustom",
    "WICBitmapPaletteType_WICBitmapPaletteTypeFixedBW",
    "WICBitmapPaletteType_WICBitmapPaletteTypeFixedGray16",
    "WICBitmapPaletteType_WICBitmapPaletteTypeFixedGray256",
    "WICBitmapPaletteType_WICBitmapPaletteTypeFixedGray4",
    "WICBitmapPaletteType_WICBitmapPaletteTypeFixedHalftone125",
    "WICBitmapPaletteType_WICBitmapPaletteTypeFixedHalftone216",
    "WICBitmapPaletteType_WICBitmapPaletteTypeFixedHalftone252",
    "WICBitmapPaletteType_WICBitmapPaletteTypeFixedHalftone256",
    "WICBitmapPaletteType_WICBitmapPaletteTypeFixedHalftone27",
    "WICBitmapPaletteType_WICBitmapPaletteTypeFixedHalftone64",
    "WICBitmapPaletteType_WICBitmapPaletteTypeFixedHalftone8",
    "WICBitmapPaletteType_WICBitmapPaletteTypeFixedWebPalette",
    "WICBitmapPaletteType_WICBitmapPaletteTypeMedianCut",
    "WICBitmapPattern",
    "WICBitmapPlane",
    "WICBitmapPlaneDescription",
    "WICBitmapTransformOptions",
    "WICBitmapTransformOptions_WICBITMAPTRANSFORMOPTIONS_FORCE_DWORD",
    "WICBitmapTransformOptions_WICBitmapTransformFlipHorizontal",
    "WICBitmapTransformOptions_WICBitmapTransformFlipVertical",
    "WICBitmapTransformOptions_WICBitmapTransformRotate0",
    "WICBitmapTransformOptions_WICBitmapTransformRotate180",
    "WICBitmapTransformOptions_WICBitmapTransformRotate270",
    "WICBitmapTransformOptions_WICBitmapTransformRotate90",
    "WICColorContextType",
    "WICColorContextType_WICColorContextExifColorSpace",
    "WICColorContextType_WICColorContextProfile",
    "WICColorContextType_WICColorContextUninitialized",
    "WICComponentEnumerateOptions",
    "WICComponentEnumerateOptions_WICCOMPONENTENUMERATEOPTIONS_FORCE_DWORD",
    "WICComponentEnumerateOptions_WICComponentEnumerateBuiltInOnly",
    "WICComponentEnumerateOptions_WICComponentEnumerateDefault",
    "WICComponentEnumerateOptions_WICComponentEnumerateDisabled",
    "WICComponentEnumerateOptions_WICComponentEnumerateRefresh",
    "WICComponentEnumerateOptions_WICComponentEnumerateUnsigned",
    "WICComponentSigning",
    "WICComponentSigning_WICCOMPONENTSIGNING_FORCE_DWORD",
    "WICComponentSigning_WICComponentDisabled",
    "WICComponentSigning_WICComponentSafe",
    "WICComponentSigning_WICComponentSigned",
    "WICComponentSigning_WICComponentUnsigned",
    "WICComponentType",
    "WICComponentType_WICAllComponents",
    "WICComponentType_WICCOMPONENTTYPE_FORCE_DWORD",
    "WICComponentType_WICDecoder",
    "WICComponentType_WICEncoder",
    "WICComponentType_WICMetadataReader",
    "WICComponentType_WICMetadataWriter",
    "WICComponentType_WICPixelFormat",
    "WICComponentType_WICPixelFormatConverter",
    "WICConvertBitmapSource",
    "WICCreateBitmapFromSection",
    "WICCreateBitmapFromSectionEx",
    "WICDdsAlphaMode",
    "WICDdsAlphaMode_WICDDSALPHAMODE_FORCE_DWORD",
    "WICDdsAlphaMode_WICDdsAlphaModeCustom",
    "WICDdsAlphaMode_WICDdsAlphaModeOpaque",
    "WICDdsAlphaMode_WICDdsAlphaModePremultiplied",
    "WICDdsAlphaMode_WICDdsAlphaModeStraight",
    "WICDdsAlphaMode_WICDdsAlphaModeUnknown",
    "WICDdsDimension",
    "WICDdsDimension_WICDDSTEXTURE_FORCE_DWORD",
    "WICDdsDimension_WICDdsTexture1D",
    "WICDdsDimension_WICDdsTexture2D",
    "WICDdsDimension_WICDdsTexture3D",
    "WICDdsDimension_WICDdsTextureCube",
    "WICDdsFormatInfo",
    "WICDdsParameters",
    "WICDecodeOptions",
    "WICDecodeOptions_WICDecodeMetadataCacheOnDemand",
    "WICDecodeOptions_WICDecodeMetadataCacheOnLoad",
    "WICDecodeOptions_WICMETADATACACHEOPTION_FORCE_DWORD",
    "WICGetMetadataContentSize",
    "WICGifApplicationExtensionProperties",
    "WICGifApplicationExtensionProperties_WICGifApplicationExtensionApplication",
    "WICGifApplicationExtensionProperties_WICGifApplicationExtensionData",
    "WICGifApplicationExtensionProperties_WICGifApplicationExtensionProperties_FORCE_DWORD",
    "WICGifCommentExtensionProperties",
    "WICGifCommentExtensionProperties_WICGifCommentExtensionProperties_FORCE_DWORD",
    "WICGifCommentExtensionProperties_WICGifCommentExtensionText",
    "WICGifGraphicControlExtensionProperties",
    "WICGifGraphicControlExtensionProperties_WICGifGraphicControlExtensionDelay",
    "WICGifGraphicControlExtensionProperties_WICGifGraphicControlExtensionDisposal",
    "WICGifGraphicControlExtensionProperties_WICGifGraphicControlExtensionProperties_FORCE_DWORD",
    "WICGifGraphicControlExtensionProperties_WICGifGraphicControlExtensionTransparencyFlag",
    "WICGifGraphicControlExtensionProperties_WICGifGraphicControlExtensionTransparentColorIndex",
    "WICGifGraphicControlExtensionProperties_WICGifGraphicControlExtensionUserInputFlag",
    "WICGifImageDescriptorProperties",
    "WICGifImageDescriptorProperties_WICGifImageDescriptorHeight",
    "WICGifImageDescriptorProperties_WICGifImageDescriptorInterlaceFlag",
    "WICGifImageDescriptorProperties_WICGifImageDescriptorLeft",
    "WICGifImageDescriptorProperties_WICGifImageDescriptorLocalColorTableFlag",
    "WICGifImageDescriptorProperties_WICGifImageDescriptorLocalColorTableSize",
    "WICGifImageDescriptorProperties_WICGifImageDescriptorProperties_FORCE_DWORD",
    "WICGifImageDescriptorProperties_WICGifImageDescriptorSortFlag",
    "WICGifImageDescriptorProperties_WICGifImageDescriptorTop",
    "WICGifImageDescriptorProperties_WICGifImageDescriptorWidth",
    "WICGifLogicalScreenDescriptorProperties",
    "WICGifLogicalScreenDescriptorProperties_WICGifLogicalScreenDescriptorBackgroundColorIndex",
    "WICGifLogicalScreenDescriptorProperties_WICGifLogicalScreenDescriptorColorResolution",
    "WICGifLogicalScreenDescriptorProperties_WICGifLogicalScreenDescriptorGlobalColorTableFlag",
    "WICGifLogicalScreenDescriptorProperties_WICGifLogicalScreenDescriptorGlobalColorTableSize",
    "WICGifLogicalScreenDescriptorProperties_WICGifLogicalScreenDescriptorHeight",
    "WICGifLogicalScreenDescriptorProperties_WICGifLogicalScreenDescriptorPixelAspectRatio",
    "WICGifLogicalScreenDescriptorProperties_WICGifLogicalScreenDescriptorProperties_FORCE_DWORD",
    "WICGifLogicalScreenDescriptorProperties_WICGifLogicalScreenDescriptorSortFlag",
    "WICGifLogicalScreenDescriptorProperties_WICGifLogicalScreenDescriptorWidth",
    "WICGifLogicalScreenDescriptorProperties_WICGifLogicalScreenSignature",
    "WICHeifHdrProperties",
    "WICHeifHdrProperties_WICHeifHdrCustomVideoPrimaries",
    "WICHeifHdrProperties_WICHeifHdrMaximumFrameAverageLuminanceLevel",
    "WICHeifHdrProperties_WICHeifHdrMaximumLuminanceLevel",
    "WICHeifHdrProperties_WICHeifHdrMaximumMasteringDisplayLuminanceLevel",
    "WICHeifHdrProperties_WICHeifHdrMinimumMasteringDisplayLuminanceLevel",
    "WICHeifHdrProperties_WICHeifHdrProperties_FORCE_DWORD",
    "WICHeifProperties",
    "WICHeifProperties_WICHeifOrientation",
    "WICHeifProperties_WICHeifProperties_FORCE_DWORD",
    "WICImageParameters",
    "WICJpegChrominanceProperties",
    "WICJpegChrominanceProperties_WICJpegChrominanceProperties_FORCE_DWORD",
    "WICJpegChrominanceProperties_WICJpegChrominanceTable",
    "WICJpegCommentProperties",
    "WICJpegCommentProperties_WICJpegCommentProperties_FORCE_DWORD",
    "WICJpegCommentProperties_WICJpegCommentText",
    "WICJpegFrameHeader",
    "WICJpegIndexingOptions",
    "WICJpegIndexingOptions_WICJpegIndexingOptionsGenerateOnDemand",
    "WICJpegIndexingOptions_WICJpegIndexingOptionsGenerateOnLoad",
    "WICJpegIndexingOptions_WICJpegIndexingOptions_FORCE_DWORD",
    "WICJpegLuminanceProperties",
    "WICJpegLuminanceProperties_WICJpegLuminanceProperties_FORCE_DWORD",
    "WICJpegLuminanceProperties_WICJpegLuminanceTable",
    "WICJpegScanHeader",
    "WICJpegScanType",
    "WICJpegScanType_WICJpegScanTypeInterleaved",
    "WICJpegScanType_WICJpegScanTypePlanarComponents",
    "WICJpegScanType_WICJpegScanTypeProgressive",
    "WICJpegScanType_WICJpegScanType_FORCE_DWORD",
    "WICJpegTransferMatrix",
    "WICJpegTransferMatrix_WICJpegTransferMatrixBT601",
    "WICJpegTransferMatrix_WICJpegTransferMatrixIdentity",
    "WICJpegTransferMatrix_WICJpegTransferMatrix_FORCE_DWORD",
    "WICJpegYCrCbSubsamplingOption",
    "WICJpegYCrCbSubsamplingOption_WICJPEGYCRCBSUBSAMPLING_FORCE_DWORD",
    "WICJpegYCrCbSubsamplingOption_WICJpegYCrCbSubsampling420",
    "WICJpegYCrCbSubsamplingOption_WICJpegYCrCbSubsampling422",
    "WICJpegYCrCbSubsamplingOption_WICJpegYCrCbSubsampling440",
    "WICJpegYCrCbSubsamplingOption_WICJpegYCrCbSubsampling444",
    "WICJpegYCrCbSubsamplingOption_WICJpegYCrCbSubsamplingDefault",
    "WICMapGuidToShortName",
    "WICMapSchemaToName",
    "WICMapShortNameToGuid",
    "WICMatchMetadataContent",
    "WICMetadataCreationOptions",
    "WICMetadataCreationOptions_WICMetadataCreationAllowUnknown",
    "WICMetadataCreationOptions_WICMetadataCreationDefault",
    "WICMetadataCreationOptions_WICMetadataCreationFailUnknown",
    "WICMetadataCreationOptions_WICMetadataCreationMask",
    "WICMetadataHeader",
    "WICMetadataPattern",
    "WICNamedWhitePoint",
    "WICNamedWhitePoint_WICNAMEDWHITEPOINT_FORCE_DWORD",
    "WICNamedWhitePoint_WICWhitePointAsShot",
    "WICNamedWhitePoint_WICWhitePointAutoWhiteBalance",
    "WICNamedWhitePoint_WICWhitePointCloudy",
    "WICNamedWhitePoint_WICWhitePointCustom",
    "WICNamedWhitePoint_WICWhitePointDaylight",
    "WICNamedWhitePoint_WICWhitePointDefault",
    "WICNamedWhitePoint_WICWhitePointFlash",
    "WICNamedWhitePoint_WICWhitePointFluorescent",
    "WICNamedWhitePoint_WICWhitePointShade",
    "WICNamedWhitePoint_WICWhitePointTungsten",
    "WICNamedWhitePoint_WICWhitePointUnderwater",
    "WICPersistOptions",
    "WICPersistOptions_WICPersistOptionBigEndian",
    "WICPersistOptions_WICPersistOptionDefault",
    "WICPersistOptions_WICPersistOptionLittleEndian",
    "WICPersistOptions_WICPersistOptionMask",
    "WICPersistOptions_WICPersistOptionNoCacheStream",
    "WICPersistOptions_WICPersistOptionPreferUTF8",
    "WICPersistOptions_WICPersistOptionStrictFormat",
    "WICPixelFormatNumericRepresentation",
    "WICPixelFormatNumericRepresentation_WICPixelFormatNumericRepresentationFixed",
    "WICPixelFormatNumericRepresentation_WICPixelFormatNumericRepresentationFloat",
    "WICPixelFormatNumericRepresentation_WICPixelFormatNumericRepresentationIndexed",
    "WICPixelFormatNumericRepresentation_WICPixelFormatNumericRepresentationSignedInteger",
    "WICPixelFormatNumericRepresentation_WICPixelFormatNumericRepresentationUnsignedInteger",
    "WICPixelFormatNumericRepresentation_WICPixelFormatNumericRepresentationUnspecified",
    "WICPixelFormatNumericRepresentation_WICPixelFormatNumericRepresentation_FORCE_DWORD",
    "WICPlanarOptions",
    "WICPlanarOptions_WICPLANAROPTIONS_FORCE_DWORD",
    "WICPlanarOptions_WICPlanarOptionsDefault",
    "WICPlanarOptions_WICPlanarOptionsPreserveSubsampling",
    "WICPngBkgdProperties",
    "WICPngBkgdProperties_WICPngBkgdBackgroundColor",
    "WICPngBkgdProperties_WICPngBkgdProperties_FORCE_DWORD",
    "WICPngChrmProperties",
    "WICPngChrmProperties_WICPngChrmBlueX",
    "WICPngChrmProperties_WICPngChrmBlueY",
    "WICPngChrmProperties_WICPngChrmGreenX",
    "WICPngChrmProperties_WICPngChrmGreenY",
    "WICPngChrmProperties_WICPngChrmProperties_FORCE_DWORD",
    "WICPngChrmProperties_WICPngChrmRedX",
    "WICPngChrmProperties_WICPngChrmRedY",
    "WICPngChrmProperties_WICPngChrmWhitePointX",
    "WICPngChrmProperties_WICPngChrmWhitePointY",
    "WICPngFilterOption",
    "WICPngFilterOption_WICPNGFILTEROPTION_FORCE_DWORD",
    "WICPngFilterOption_WICPngFilterAdaptive",
    "WICPngFilterOption_WICPngFilterAverage",
    "WICPngFilterOption_WICPngFilterNone",
    "WICPngFilterOption_WICPngFilterPaeth",
    "WICPngFilterOption_WICPngFilterSub",
    "WICPngFilterOption_WICPngFilterUnspecified",
    "WICPngFilterOption_WICPngFilterUp",
    "WICPngGamaProperties",
    "WICPngGamaProperties_WICPngGamaGamma",
    "WICPngGamaProperties_WICPngGamaProperties_FORCE_DWORD",
    "WICPngHistProperties",
    "WICPngHistProperties_WICPngHistFrequencies",
    "WICPngHistProperties_WICPngHistProperties_FORCE_DWORD",
    "WICPngIccpProperties",
    "WICPngIccpProperties_WICPngIccpProfileData",
    "WICPngIccpProperties_WICPngIccpProfileName",
    "WICPngIccpProperties_WICPngIccpProperties_FORCE_DWORD",
    "WICPngItxtProperties",
    "WICPngItxtProperties_WICPngItxtCompressionFlag",
    "WICPngItxtProperties_WICPngItxtKeyword",
    "WICPngItxtProperties_WICPngItxtLanguageTag",
    "WICPngItxtProperties_WICPngItxtProperties_FORCE_DWORD",
    "WICPngItxtProperties_WICPngItxtText",
    "WICPngItxtProperties_WICPngItxtTranslatedKeyword",
    "WICPngSrgbProperties",
    "WICPngSrgbProperties_WICPngSrgbProperties_FORCE_DWORD",
    "WICPngSrgbProperties_WICPngSrgbRenderingIntent",
    "WICPngTimeProperties",
    "WICPngTimeProperties_WICPngTimeDay",
    "WICPngTimeProperties_WICPngTimeHour",
    "WICPngTimeProperties_WICPngTimeMinute",
    "WICPngTimeProperties_WICPngTimeMonth",
    "WICPngTimeProperties_WICPngTimeProperties_FORCE_DWORD",
    "WICPngTimeProperties_WICPngTimeSecond",
    "WICPngTimeProperties_WICPngTimeYear",
    "WICProgressNotification",
    "WICProgressNotification_WICPROGRESSNOTIFICATION_FORCE_DWORD",
    "WICProgressNotification_WICProgressNotificationAll",
    "WICProgressNotification_WICProgressNotificationBegin",
    "WICProgressNotification_WICProgressNotificationEnd",
    "WICProgressNotification_WICProgressNotificationFrequent",
    "WICProgressOperation",
    "WICProgressOperation_WICPROGRESSOPERATION_FORCE_DWORD",
    "WICProgressOperation_WICProgressOperationAll",
    "WICProgressOperation_WICProgressOperationCopyPixels",
    "WICProgressOperation_WICProgressOperationWritePixels",
    "WICRawCapabilities",
    "WICRawCapabilitiesInfo",
    "WICRawCapabilities_WICRAWCAPABILITIES_FORCE_DWORD",
    "WICRawCapabilities_WICRawCapabilityFullySupported",
    "WICRawCapabilities_WICRawCapabilityGetSupported",
    "WICRawCapabilities_WICRawCapabilityNotSupported",
    "WICRawChangeNotification_Contrast",
    "WICRawChangeNotification_DestinationColorContext",
    "WICRawChangeNotification_ExposureCompensation",
    "WICRawChangeNotification_Gamma",
    "WICRawChangeNotification_KelvinWhitePoint",
    "WICRawChangeNotification_NamedWhitePoint",
    "WICRawChangeNotification_NoiseReduction",
    "WICRawChangeNotification_RGBWhitePoint",
    "WICRawChangeNotification_RenderMode",
    "WICRawChangeNotification_Rotation",
    "WICRawChangeNotification_Saturation",
    "WICRawChangeNotification_Sharpness",
    "WICRawChangeNotification_Tint",
    "WICRawChangeNotification_ToneCurve",
    "WICRawParameterSet",
    "WICRawParameterSet_WICAsShotParameterSet",
    "WICRawParameterSet_WICAutoAdjustedParameterSet",
    "WICRawParameterSet_WICRAWPARAMETERSET_FORCE_DWORD",
    "WICRawParameterSet_WICUserAdjustedParameterSet",
    "WICRawRenderMode",
    "WICRawRenderMode_WICRAWRENDERMODE_FORCE_DWORD",
    "WICRawRenderMode_WICRawRenderModeBestQuality",
    "WICRawRenderMode_WICRawRenderModeDraft",
    "WICRawRenderMode_WICRawRenderModeNormal",
    "WICRawRotationCapabilities",
    "WICRawRotationCapabilities_WICRAWROTATIONCAPABILITIES_FORCE_DWORD",
    "WICRawRotationCapabilities_WICRawRotationCapabilityFullySupported",
    "WICRawRotationCapabilities_WICRawRotationCapabilityGetSupported",
    "WICRawRotationCapabilities_WICRawRotationCapabilityNinetyDegreesSupported",
    "WICRawRotationCapabilities_WICRawRotationCapabilityNotSupported",
    "WICRawToneCurve",
    "WICRawToneCurvePoint",
    "WICRect",
    "WICSectionAccessLevel",
    "WICSectionAccessLevel_WICSectionAccessLevelRead",
    "WICSectionAccessLevel_WICSectionAccessLevelReadWrite",
    "WICSectionAccessLevel_WICSectionAccessLevel_FORCE_DWORD",
    "WICSerializeMetadataContent",
    "WICTiffCompressionOption",
    "WICTiffCompressionOption_WICTIFFCOMPRESSIONOPTION_FORCE_DWORD",
    "WICTiffCompressionOption_WICTiffCompressionCCITT3",
    "WICTiffCompressionOption_WICTiffCompressionCCITT4",
    "WICTiffCompressionOption_WICTiffCompressionDontCare",
    "WICTiffCompressionOption_WICTiffCompressionLZW",
    "WICTiffCompressionOption_WICTiffCompressionLZWHDifferencing",
    "WICTiffCompressionOption_WICTiffCompressionNone",
    "WICTiffCompressionOption_WICTiffCompressionRLE",
    "WICTiffCompressionOption_WICTiffCompressionZIP",
    "WICWebpAnimProperties",
    "WICWebpAnimProperties_WICWebpAnimLoopCount",
    "WICWebpAnimProperties_WICWebpAnimProperties_FORCE_DWORD",
    "WICWebpAnmfProperties",
    "WICWebpAnmfProperties_WICWebpAnmfFrameDuration",
    "WICWebpAnmfProperties_WICWebpAnmfProperties_FORCE_DWORD",
    "WIC_JPEG_HUFFMAN_BASELINE_ONE",
    "WIC_JPEG_HUFFMAN_BASELINE_THREE",
    "WIC_JPEG_MAX_COMPONENT_COUNT",
    "WIC_JPEG_MAX_TABLE_INDEX",
    "WIC_JPEG_QUANTIZATION_BASELINE_ONE",
    "WIC_JPEG_QUANTIZATION_BASELINE_THREE",
    "WIC_JPEG_SAMPLE_FACTORS_ONE",
    "WIC_JPEG_SAMPLE_FACTORS_THREE_420",
    "WIC_JPEG_SAMPLE_FACTORS_THREE_422",
    "WIC_JPEG_SAMPLE_FACTORS_THREE_440",
    "WIC_JPEG_SAMPLE_FACTORS_THREE_444",
    "WINCODEC_ERR_ABORTED",
    "WINCODEC_ERR_ACCESSDENIED",
    "WINCODEC_ERR_BASE",
    "WINCODEC_ERR_GENERIC_ERROR",
    "WINCODEC_ERR_INVALIDPARAMETER",
    "WINCODEC_ERR_NOTIMPLEMENTED",
    "WINCODEC_ERR_OUTOFMEMORY",
    "WINCODEC_SDK_VERSION",
    "WINCODEC_SDK_VERSION1",
    "WINCODEC_SDK_VERSION2",
]
_arch_optional = [
]
