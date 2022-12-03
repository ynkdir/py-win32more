from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, COMMETHOD, SUCCEEDED, FAILED
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
        f = globals()[f'_define_{name}']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, f())
    return getattr(_module, name)
def __dir__():
    return __all__
WINCODEC_SDK_VERSION1 = 566
WINCODEC_SDK_VERSION2 = 567
def _define_CLSID_WICImagingFactory():
    return Guid('cacaf262-9370-4615-a1-3b-9f-55-39-da-4c-0a')
def _define_CLSID_WICImagingFactory1():
    return Guid('cacaf262-9370-4615-a1-3b-9f-55-39-da-4c-0a')
def _define_CLSID_WICImagingFactory2():
    return Guid('317d06e8-5f24-433d-bd-f7-79-ce-68-d8-ab-c2')
WINCODEC_SDK_VERSION = 567
def _define_GUID_VendorMicrosoft():
    return Guid('f0e749ca-edef-4589-a7-3a-ee-0e-62-6a-2a-2b')
def _define_GUID_VendorMicrosoftBuiltIn():
    return Guid('257a30fd-06b6-462b-ae-a4-63-f7-0b-86-e5-33')
def _define_CLSID_WICPngDecoder():
    return Guid('389ea17b-5078-4cde-b6-ef-25-c1-51-75-c7-51')
def _define_CLSID_WICPngDecoder1():
    return Guid('389ea17b-5078-4cde-b6-ef-25-c1-51-75-c7-51')
def _define_CLSID_WICPngDecoder2():
    return Guid('e018945b-aa86-4008-9b-d4-67-77-a1-e4-0c-11')
def _define_CLSID_WICBmpDecoder():
    return Guid('6b462062-7cbf-400d-9f-db-81-3d-d1-0f-27-78')
def _define_CLSID_WICIcoDecoder():
    return Guid('c61bfcdf-2e0f-4aad-a8-d7-e0-6b-af-eb-cd-fe')
def _define_CLSID_WICJpegDecoder():
    return Guid('9456a480-e88b-43ea-9e-73-0b-2d-9b-71-b1-ca')
def _define_CLSID_WICGifDecoder():
    return Guid('381dda3c-9ce9-4834-a2-3e-1f-98-f8-fc-52-be')
def _define_CLSID_WICTiffDecoder():
    return Guid('b54e85d9-fe23-499f-8b-88-6a-ce-a7-13-75-2b')
def _define_CLSID_WICWmpDecoder():
    return Guid('a26cec36-234c-4950-ae-16-e3-4a-ac-e7-1d-0d')
def _define_CLSID_WICDdsDecoder():
    return Guid('9053699f-a341-429d-9e-90-ee-43-7c-f8-0c-73')
def _define_CLSID_WICBmpEncoder():
    return Guid('69be8bb4-d66d-47c8-86-5a-ed-15-89-43-37-82')
def _define_CLSID_WICPngEncoder():
    return Guid('27949969-876a-41d7-94-47-56-8f-6a-35-a4-dc')
def _define_CLSID_WICJpegEncoder():
    return Guid('1a34f5c1-4a5a-46dc-b6-44-1f-45-67-e7-a6-76')
def _define_CLSID_WICGifEncoder():
    return Guid('114f5598-0b22-40a0-86-a1-c8-3e-a4-95-ad-bd')
def _define_CLSID_WICTiffEncoder():
    return Guid('0131be10-2001-4c5f-a9-b0-cc-88-fa-b6-4c-e8')
def _define_CLSID_WICWmpEncoder():
    return Guid('ac4ce3cb-e1c1-44cd-82-15-5a-16-65-50-9e-c2')
def _define_CLSID_WICDdsEncoder():
    return Guid('a61dde94-66ce-4ac1-88-1b-71-68-05-88-89-5e')
def _define_CLSID_WICAdngDecoder():
    return Guid('981d9411-909e-42a7-8f-5d-a7-47-ff-05-2e-db')
def _define_CLSID_WICJpegQualcommPhoneEncoder():
    return Guid('68ed5c62-f534-4979-b2-b3-68-6a-12-b2-b3-4c')
def _define_CLSID_WICHeifDecoder():
    return Guid('e9a4a80a-44fe-4de4-89-71-71-50-b1-0a-51-99')
def _define_CLSID_WICHeifEncoder():
    return Guid('0dbecec1-9eb3-4860-9c-6f-dd-be-86-63-45-75')
def _define_CLSID_WICWebpDecoder():
    return Guid('7693e886-51c9-4070-84-19-9f-70-73-8e-c8-fa')
def _define_CLSID_WICRAWDecoder():
    return Guid('41945702-8302-44a6-94-45-ac-98-e8-af-a0-86')
def _define_GUID_ContainerFormatBmp():
    return Guid('0af1d87e-fcfe-4188-bd-eb-a7-90-64-71-cb-e3')
def _define_GUID_ContainerFormatPng():
    return Guid('1b7cfaf4-713f-473c-bb-cd-61-37-42-5f-ae-af')
def _define_GUID_ContainerFormatIco():
    return Guid('a3a860c4-338f-4c17-91-9a-fb-a4-b5-62-8f-21')
def _define_GUID_ContainerFormatJpeg():
    return Guid('19e4a5aa-5662-4fc5-a0-c0-17-58-02-8e-10-57')
def _define_GUID_ContainerFormatTiff():
    return Guid('163bcc30-e2e9-4f0b-96-1d-a3-e9-fd-b7-88-a3')
def _define_GUID_ContainerFormatGif():
    return Guid('1f8a5601-7d4d-4cbd-9c-82-1b-c8-d4-ee-b9-a5')
def _define_GUID_ContainerFormatWmp():
    return Guid('57a37caa-367a-4540-91-6b-f1-83-c5-09-3a-4b')
def _define_GUID_ContainerFormatDds():
    return Guid('9967cb95-2e85-4ac8-8c-a2-83-d7-cc-d4-25-c9')
def _define_GUID_ContainerFormatAdng():
    return Guid('f3ff6d0d-38c0-41c4-b1-fe-1f-38-24-f1-7b-84')
def _define_GUID_ContainerFormatHeif():
    return Guid('e1e62521-6787-405b-a3-39-50-07-15-b5-76-3f')
def _define_GUID_ContainerFormatWebp():
    return Guid('e094b0e2-67f2-45b3-b0-ea-11-53-37-ca-7c-f3')
def _define_GUID_ContainerFormatRaw():
    return Guid('fe99ce60-f19c-433c-a3-ae-00-ac-ef-a9-ca-21')
def _define_CLSID_WICImagingCategories():
    return Guid('fae3d380-fea4-4623-8c-75-c6-b6-11-10-b6-81')
def _define_CATID_WICBitmapDecoders():
    return Guid('7ed96837-96f0-4812-b2-11-f1-3c-24-11-7e-d3')
def _define_CATID_WICBitmapEncoders():
    return Guid('ac757296-3522-4e11-98-62-c1-7b-e5-a1-76-7e')
def _define_CATID_WICPixelFormats():
    return Guid('2b46e70f-cda7-473e-89-f6-dc-96-30-a2-39-0b')
def _define_CATID_WICFormatConverters():
    return Guid('7835eae8-bf14-49d1-93-ce-53-3a-40-7b-22-48')
def _define_CATID_WICMetadataReader():
    return Guid('05af94d8-7174-4cd2-be-4a-41-24-b8-0e-e4-b8')
def _define_CATID_WICMetadataWriter():
    return Guid('abe3b9a4-257d-4b97-bd-1a-29-4a-f4-96-22-2e')
def _define_CLSID_WICDefaultFormatConverter():
    return Guid('1a3f11dc-b514-4b17-8c-5f-21-54-51-38-52-f1')
def _define_CLSID_WICFormatConverterHighColor():
    return Guid('ac75d454-9f37-48f8-b9-72-4e-19-bc-85-60-11')
def _define_CLSID_WICFormatConverterNChannel():
    return Guid('c17cabb2-d4a3-47d7-a5-57-33-9b-2e-fb-d4-f1')
def _define_CLSID_WICFormatConverterWMPhoto():
    return Guid('9cb5172b-d600-46ba-ab-77-77-bb-7e-3a-00-d9')
def _define_CLSID_WICPlanarFormatConverter():
    return Guid('184132b8-32f8-4784-91-31-dd-72-24-b2-34-38')
WIC_JPEG_MAX_COMPONENT_COUNT = 4
WIC_JPEG_MAX_TABLE_INDEX = 3
WIC_JPEG_SAMPLE_FACTORS_ONE = 17
WIC_JPEG_SAMPLE_FACTORS_THREE_420 = 1118498
WIC_JPEG_SAMPLE_FACTORS_THREE_422 = 1118497
WIC_JPEG_SAMPLE_FACTORS_THREE_440 = 1118482
WIC_JPEG_SAMPLE_FACTORS_THREE_444 = 1118481
WIC_JPEG_QUANTIZATION_BASELINE_ONE = 0
WIC_JPEG_QUANTIZATION_BASELINE_THREE = 65792
WIC_JPEG_HUFFMAN_BASELINE_ONE = 0
WIC_JPEG_HUFFMAN_BASELINE_THREE = 1118464
def _define_GUID_WICPixelFormatDontCare():
    return Guid('6fddc324-4e03-4bfe-b1-85-3d-77-76-8d-c9-00')
def _define_GUID_WICPixelFormat1bppIndexed():
    return Guid('6fddc324-4e03-4bfe-b1-85-3d-77-76-8d-c9-01')
def _define_GUID_WICPixelFormat2bppIndexed():
    return Guid('6fddc324-4e03-4bfe-b1-85-3d-77-76-8d-c9-02')
def _define_GUID_WICPixelFormat4bppIndexed():
    return Guid('6fddc324-4e03-4bfe-b1-85-3d-77-76-8d-c9-03')
def _define_GUID_WICPixelFormat8bppIndexed():
    return Guid('6fddc324-4e03-4bfe-b1-85-3d-77-76-8d-c9-04')
def _define_GUID_WICPixelFormatBlackWhite():
    return Guid('6fddc324-4e03-4bfe-b1-85-3d-77-76-8d-c9-05')
def _define_GUID_WICPixelFormat2bppGray():
    return Guid('6fddc324-4e03-4bfe-b1-85-3d-77-76-8d-c9-06')
def _define_GUID_WICPixelFormat4bppGray():
    return Guid('6fddc324-4e03-4bfe-b1-85-3d-77-76-8d-c9-07')
def _define_GUID_WICPixelFormat8bppGray():
    return Guid('6fddc324-4e03-4bfe-b1-85-3d-77-76-8d-c9-08')
def _define_GUID_WICPixelFormat8bppAlpha():
    return Guid('e6cd0116-eeba-4161-aa-85-27-dd-9f-b3-a8-95')
def _define_GUID_WICPixelFormat16bppBGR555():
    return Guid('6fddc324-4e03-4bfe-b1-85-3d-77-76-8d-c9-09')
def _define_GUID_WICPixelFormat16bppBGR565():
    return Guid('6fddc324-4e03-4bfe-b1-85-3d-77-76-8d-c9-0a')
def _define_GUID_WICPixelFormat16bppBGRA5551():
    return Guid('05ec7c2b-f1e6-4961-ad-46-e1-cc-81-0a-87-d2')
def _define_GUID_WICPixelFormat16bppGray():
    return Guid('6fddc324-4e03-4bfe-b1-85-3d-77-76-8d-c9-0b')
def _define_GUID_WICPixelFormat24bppBGR():
    return Guid('6fddc324-4e03-4bfe-b1-85-3d-77-76-8d-c9-0c')
def _define_GUID_WICPixelFormat24bppRGB():
    return Guid('6fddc324-4e03-4bfe-b1-85-3d-77-76-8d-c9-0d')
def _define_GUID_WICPixelFormat32bppBGR():
    return Guid('6fddc324-4e03-4bfe-b1-85-3d-77-76-8d-c9-0e')
def _define_GUID_WICPixelFormat32bppBGRA():
    return Guid('6fddc324-4e03-4bfe-b1-85-3d-77-76-8d-c9-0f')
def _define_GUID_WICPixelFormat32bppPBGRA():
    return Guid('6fddc324-4e03-4bfe-b1-85-3d-77-76-8d-c9-10')
def _define_GUID_WICPixelFormat32bppGrayFloat():
    return Guid('6fddc324-4e03-4bfe-b1-85-3d-77-76-8d-c9-11')
def _define_GUID_WICPixelFormat32bppRGB():
    return Guid('d98c6b95-3efe-47d6-bb-25-eb-17-48-ab-0c-f1')
def _define_GUID_WICPixelFormat32bppRGBA():
    return Guid('f5c7ad2d-6a8d-43dd-a7-a8-a2-99-35-26-1a-e9')
def _define_GUID_WICPixelFormat32bppPRGBA():
    return Guid('3cc4a650-a527-4d37-a9-16-31-42-c7-eb-ed-ba')
def _define_GUID_WICPixelFormat48bppRGB():
    return Guid('6fddc324-4e03-4bfe-b1-85-3d-77-76-8d-c9-15')
def _define_GUID_WICPixelFormat48bppBGR():
    return Guid('e605a384-b468-46ce-bb-2e-36-f1-80-e6-43-13')
def _define_GUID_WICPixelFormat64bppRGB():
    return Guid('a1182111-186d-4d42-bc-6a-9c-83-03-a8-df-f9')
def _define_GUID_WICPixelFormat64bppRGBA():
    return Guid('6fddc324-4e03-4bfe-b1-85-3d-77-76-8d-c9-16')
def _define_GUID_WICPixelFormat64bppBGRA():
    return Guid('1562ff7c-d352-46f9-97-9e-42-97-6b-79-22-46')
def _define_GUID_WICPixelFormat64bppPRGBA():
    return Guid('6fddc324-4e03-4bfe-b1-85-3d-77-76-8d-c9-17')
def _define_GUID_WICPixelFormat64bppPBGRA():
    return Guid('8c518e8e-a4ec-468b-ae-70-c9-a3-5a-9c-55-30')
def _define_GUID_WICPixelFormat16bppGrayFixedPoint():
    return Guid('6fddc324-4e03-4bfe-b1-85-3d-77-76-8d-c9-13')
def _define_GUID_WICPixelFormat32bppBGR101010():
    return Guid('6fddc324-4e03-4bfe-b1-85-3d-77-76-8d-c9-14')
def _define_GUID_WICPixelFormat48bppRGBFixedPoint():
    return Guid('6fddc324-4e03-4bfe-b1-85-3d-77-76-8d-c9-12')
def _define_GUID_WICPixelFormat48bppBGRFixedPoint():
    return Guid('49ca140e-cab6-493b-9d-df-60-18-7c-37-53-2a')
def _define_GUID_WICPixelFormat96bppRGBFixedPoint():
    return Guid('6fddc324-4e03-4bfe-b1-85-3d-77-76-8d-c9-18')
def _define_GUID_WICPixelFormat96bppRGBFloat():
    return Guid('e3fed78f-e8db-4acf-84-c1-e9-7f-61-36-b3-27')
def _define_GUID_WICPixelFormat128bppRGBAFloat():
    return Guid('6fddc324-4e03-4bfe-b1-85-3d-77-76-8d-c9-19')
def _define_GUID_WICPixelFormat128bppPRGBAFloat():
    return Guid('6fddc324-4e03-4bfe-b1-85-3d-77-76-8d-c9-1a')
def _define_GUID_WICPixelFormat128bppRGBFloat():
    return Guid('6fddc324-4e03-4bfe-b1-85-3d-77-76-8d-c9-1b')
def _define_GUID_WICPixelFormat32bppCMYK():
    return Guid('6fddc324-4e03-4bfe-b1-85-3d-77-76-8d-c9-1c')
def _define_GUID_WICPixelFormat64bppRGBAFixedPoint():
    return Guid('6fddc324-4e03-4bfe-b1-85-3d-77-76-8d-c9-1d')
def _define_GUID_WICPixelFormat64bppBGRAFixedPoint():
    return Guid('356de33c-54d2-4a23-bb-04-9b-7b-f9-b1-d4-2d')
def _define_GUID_WICPixelFormat64bppRGBFixedPoint():
    return Guid('6fddc324-4e03-4bfe-b1-85-3d-77-76-8d-c9-40')
def _define_GUID_WICPixelFormat128bppRGBAFixedPoint():
    return Guid('6fddc324-4e03-4bfe-b1-85-3d-77-76-8d-c9-1e')
def _define_GUID_WICPixelFormat128bppRGBFixedPoint():
    return Guid('6fddc324-4e03-4bfe-b1-85-3d-77-76-8d-c9-41')
def _define_GUID_WICPixelFormat64bppRGBAHalf():
    return Guid('6fddc324-4e03-4bfe-b1-85-3d-77-76-8d-c9-3a')
def _define_GUID_WICPixelFormat64bppPRGBAHalf():
    return Guid('58ad26c2-c623-4d9d-b3-20-38-7e-49-f8-c4-42')
def _define_GUID_WICPixelFormat64bppRGBHalf():
    return Guid('6fddc324-4e03-4bfe-b1-85-3d-77-76-8d-c9-42')
def _define_GUID_WICPixelFormat48bppRGBHalf():
    return Guid('6fddc324-4e03-4bfe-b1-85-3d-77-76-8d-c9-3b')
def _define_GUID_WICPixelFormat32bppRGBE():
    return Guid('6fddc324-4e03-4bfe-b1-85-3d-77-76-8d-c9-3d')
def _define_GUID_WICPixelFormat16bppGrayHalf():
    return Guid('6fddc324-4e03-4bfe-b1-85-3d-77-76-8d-c9-3e')
def _define_GUID_WICPixelFormat32bppGrayFixedPoint():
    return Guid('6fddc324-4e03-4bfe-b1-85-3d-77-76-8d-c9-3f')
def _define_GUID_WICPixelFormat32bppRGBA1010102():
    return Guid('25238d72-fcf9-4522-b5-14-55-78-e5-ad-55-e0')
def _define_GUID_WICPixelFormat32bppRGBA1010102XR():
    return Guid('00de6b9a-c101-434b-b5-02-d0-16-5e-e1-12-2c')
def _define_GUID_WICPixelFormat32bppR10G10B10A2():
    return Guid('604e1bb5-8a3c-4b65-b1-1c-bc-0b-8d-d7-5b-7f')
def _define_GUID_WICPixelFormat32bppR10G10B10A2HDR10():
    return Guid('9c215c5d-1acc-4f0e-a4-bc-70-fb-3a-e8-fd-28')
def _define_GUID_WICPixelFormat64bppCMYK():
    return Guid('6fddc324-4e03-4bfe-b1-85-3d-77-76-8d-c9-1f')
def _define_GUID_WICPixelFormat24bpp3Channels():
    return Guid('6fddc324-4e03-4bfe-b1-85-3d-77-76-8d-c9-20')
def _define_GUID_WICPixelFormat32bpp4Channels():
    return Guid('6fddc324-4e03-4bfe-b1-85-3d-77-76-8d-c9-21')
def _define_GUID_WICPixelFormat40bpp5Channels():
    return Guid('6fddc324-4e03-4bfe-b1-85-3d-77-76-8d-c9-22')
def _define_GUID_WICPixelFormat48bpp6Channels():
    return Guid('6fddc324-4e03-4bfe-b1-85-3d-77-76-8d-c9-23')
def _define_GUID_WICPixelFormat56bpp7Channels():
    return Guid('6fddc324-4e03-4bfe-b1-85-3d-77-76-8d-c9-24')
def _define_GUID_WICPixelFormat64bpp8Channels():
    return Guid('6fddc324-4e03-4bfe-b1-85-3d-77-76-8d-c9-25')
def _define_GUID_WICPixelFormat48bpp3Channels():
    return Guid('6fddc324-4e03-4bfe-b1-85-3d-77-76-8d-c9-26')
def _define_GUID_WICPixelFormat64bpp4Channels():
    return Guid('6fddc324-4e03-4bfe-b1-85-3d-77-76-8d-c9-27')
def _define_GUID_WICPixelFormat80bpp5Channels():
    return Guid('6fddc324-4e03-4bfe-b1-85-3d-77-76-8d-c9-28')
def _define_GUID_WICPixelFormat96bpp6Channels():
    return Guid('6fddc324-4e03-4bfe-b1-85-3d-77-76-8d-c9-29')
def _define_GUID_WICPixelFormat112bpp7Channels():
    return Guid('6fddc324-4e03-4bfe-b1-85-3d-77-76-8d-c9-2a')
def _define_GUID_WICPixelFormat128bpp8Channels():
    return Guid('6fddc324-4e03-4bfe-b1-85-3d-77-76-8d-c9-2b')
def _define_GUID_WICPixelFormat40bppCMYKAlpha():
    return Guid('6fddc324-4e03-4bfe-b1-85-3d-77-76-8d-c9-2c')
def _define_GUID_WICPixelFormat80bppCMYKAlpha():
    return Guid('6fddc324-4e03-4bfe-b1-85-3d-77-76-8d-c9-2d')
def _define_GUID_WICPixelFormat32bpp3ChannelsAlpha():
    return Guid('6fddc324-4e03-4bfe-b1-85-3d-77-76-8d-c9-2e')
def _define_GUID_WICPixelFormat40bpp4ChannelsAlpha():
    return Guid('6fddc324-4e03-4bfe-b1-85-3d-77-76-8d-c9-2f')
def _define_GUID_WICPixelFormat48bpp5ChannelsAlpha():
    return Guid('6fddc324-4e03-4bfe-b1-85-3d-77-76-8d-c9-30')
def _define_GUID_WICPixelFormat56bpp6ChannelsAlpha():
    return Guid('6fddc324-4e03-4bfe-b1-85-3d-77-76-8d-c9-31')
def _define_GUID_WICPixelFormat64bpp7ChannelsAlpha():
    return Guid('6fddc324-4e03-4bfe-b1-85-3d-77-76-8d-c9-32')
def _define_GUID_WICPixelFormat72bpp8ChannelsAlpha():
    return Guid('6fddc324-4e03-4bfe-b1-85-3d-77-76-8d-c9-33')
def _define_GUID_WICPixelFormat64bpp3ChannelsAlpha():
    return Guid('6fddc324-4e03-4bfe-b1-85-3d-77-76-8d-c9-34')
def _define_GUID_WICPixelFormat80bpp4ChannelsAlpha():
    return Guid('6fddc324-4e03-4bfe-b1-85-3d-77-76-8d-c9-35')
def _define_GUID_WICPixelFormat96bpp5ChannelsAlpha():
    return Guid('6fddc324-4e03-4bfe-b1-85-3d-77-76-8d-c9-36')
def _define_GUID_WICPixelFormat112bpp6ChannelsAlpha():
    return Guid('6fddc324-4e03-4bfe-b1-85-3d-77-76-8d-c9-37')
def _define_GUID_WICPixelFormat128bpp7ChannelsAlpha():
    return Guid('6fddc324-4e03-4bfe-b1-85-3d-77-76-8d-c9-38')
def _define_GUID_WICPixelFormat144bpp8ChannelsAlpha():
    return Guid('6fddc324-4e03-4bfe-b1-85-3d-77-76-8d-c9-39')
def _define_GUID_WICPixelFormat8bppY():
    return Guid('91b4db54-2df9-42f0-b4-49-29-09-bb-3d-f8-8e')
def _define_GUID_WICPixelFormat8bppCb():
    return Guid('1339f224-6bfe-4c3e-93-02-e4-f3-a6-d0-ca-2a')
def _define_GUID_WICPixelFormat8bppCr():
    return Guid('b8145053-2116-49f0-88-35-ed-84-4b-20-5c-51')
def _define_GUID_WICPixelFormat16bppCbCr():
    return Guid('ff95ba6e-11e0-4263-bb-45-01-72-1f-34-60-a4')
def _define_GUID_WICPixelFormat16bppYQuantizedDctCoefficients():
    return Guid('a355f433-48e8-4a42-84-d8-e2-aa-26-ca-80-a4')
def _define_GUID_WICPixelFormat16bppCbQuantizedDctCoefficients():
    return Guid('d2c4ff61-56a5-49c2-8b-5c-4c-19-25-96-48-37')
def _define_GUID_WICPixelFormat16bppCrQuantizedDctCoefficients():
    return Guid('2fe354f0-1680-42d8-92-31-e7-3c-05-65-bf-c1')
FACILITY_WINCODEC_ERR = 2200
WINCODEC_ERR_BASE = 8192
WINCODEC_ERR_GENERIC_ERROR = -2147467259
WINCODEC_ERR_INVALIDPARAMETER = -2147024809
WINCODEC_ERR_OUTOFMEMORY = -2147024882
WINCODEC_ERR_NOTIMPLEMENTED = -2147467263
WINCODEC_ERR_ABORTED = -2147467260
WINCODEC_ERR_ACCESSDENIED = -2147024891
WICRawChangeNotification_ExposureCompensation = 1
WICRawChangeNotification_NamedWhitePoint = 2
WICRawChangeNotification_KelvinWhitePoint = 4
WICRawChangeNotification_RGBWhitePoint = 8
WICRawChangeNotification_Contrast = 16
WICRawChangeNotification_Gamma = 32
WICRawChangeNotification_Sharpness = 64
WICRawChangeNotification_Saturation = 128
WICRawChangeNotification_Tint = 256
WICRawChangeNotification_NoiseReduction = 512
WICRawChangeNotification_DestinationColorContext = 1024
WICRawChangeNotification_ToneCurve = 2048
WICRawChangeNotification_Rotation = 4096
WICRawChangeNotification_RenderMode = 8192
def _define_GUID_MetadataFormatUnknown():
    return Guid('a45e592f-9078-4a7c-ad-b5-4e-dc-4f-d6-1b-1f')
def _define_GUID_MetadataFormatIfd():
    return Guid('537396c6-2d8a-4bb6-9b-f8-2f-0a-8e-2a-3a-df')
def _define_GUID_MetadataFormatSubIfd():
    return Guid('58a2e128-2db9-4e57-bb-14-51-77-89-1e-d3-31')
def _define_GUID_MetadataFormatExif():
    return Guid('1c3c4f9d-b84a-467d-94-93-36-cf-bd-59-ea-57')
def _define_GUID_MetadataFormatGps():
    return Guid('7134ab8a-9351-44ad-af-62-44-8d-b6-b5-02-ec')
def _define_GUID_MetadataFormatInterop():
    return Guid('ed686f8e-681f-4c8b-bd-41-a8-ad-db-f6-b3-fc')
def _define_GUID_MetadataFormatApp0():
    return Guid('79007028-268d-45d6-a3-c2-35-4e-6a-50-4b-c9')
def _define_GUID_MetadataFormatApp1():
    return Guid('8fd3dfc3-f951-492b-81-7f-69-c2-e6-d9-a5-b0')
def _define_GUID_MetadataFormatApp13():
    return Guid('326556a2-f502-4354-9c-c0-8e-3f-48-ea-f6-b5')
def _define_GUID_MetadataFormatIPTC():
    return Guid('4fab0914-e129-4087-a1-d1-bc-81-2d-45-a7-b5')
def _define_GUID_MetadataFormatIRB():
    return Guid('16100d66-8570-4bb9-b9-2d-fd-a4-b2-3e-ce-67')
def _define_GUID_MetadataFormat8BIMIPTC():
    return Guid('0010568c-0852-4e6a-b1-91-5c-33-ac-5b-04-30')
def _define_GUID_MetadataFormat8BIMResolutionInfo():
    return Guid('739f305d-81db-43cb-ac-5e-55-01-3e-f9-f0-03')
def _define_GUID_MetadataFormat8BIMIPTCDigest():
    return Guid('1ca32285-9ccd-4786-8b-d8-79-53-9d-b6-a0-06')
def _define_GUID_MetadataFormatXMP():
    return Guid('bb5acc38-f216-4cec-a6-c5-5f-6e-73-97-63-a9')
def _define_GUID_MetadataFormatThumbnail():
    return Guid('243dcee9-8703-40ee-8e-f0-22-a6-00-b8-05-8c')
def _define_GUID_MetadataFormatChunktEXt():
    return Guid('568d8936-c0a9-4923-90-5d-df-2b-38-23-8f-bc')
def _define_GUID_MetadataFormatXMPStruct():
    return Guid('22383cf1-ed17-4e2e-af-17-d8-5b-8f-6b-30-d0')
def _define_GUID_MetadataFormatXMPBag():
    return Guid('833cca5f-dcb7-4516-80-6f-65-96-ab-26-dc-e4')
def _define_GUID_MetadataFormatXMPSeq():
    return Guid('63e8df02-eb6c-456c-a2-24-b2-5e-79-4f-d6-48')
def _define_GUID_MetadataFormatXMPAlt():
    return Guid('7b08a675-91aa-481b-a7-98-4d-a9-49-08-61-3b')
def _define_GUID_MetadataFormatLSD():
    return Guid('e256031e-6299-4929-b9-8d-5a-c8-84-af-ba-92')
def _define_GUID_MetadataFormatIMD():
    return Guid('bd2bb086-4d52-48dd-96-77-db-48-3e-85-ae-8f')
def _define_GUID_MetadataFormatGCE():
    return Guid('2a25cad8-deeb-4c69-a7-88-0e-c2-26-6d-ca-fd')
def _define_GUID_MetadataFormatAPE():
    return Guid('2e043dc2-c967-4e05-87-5e-61-8b-f6-7e-85-c3')
def _define_GUID_MetadataFormatJpegChrominance():
    return Guid('f73d0dcf-cec6-4f85-9b-0e-1c-39-56-b1-be-f7')
def _define_GUID_MetadataFormatJpegLuminance():
    return Guid('86908007-edfc-4860-8d-4b-4e-e6-e8-3e-60-58')
def _define_GUID_MetadataFormatJpegComment():
    return Guid('220e5f33-afd3-474e-9d-31-7d-4f-e7-30-f5-57')
def _define_GUID_MetadataFormatGifComment():
    return Guid('c4b6e0e0-cfb4-4ad3-ab-33-9a-ad-23-55-a3-4a')
def _define_GUID_MetadataFormatChunkgAMA():
    return Guid('f00935a5-1d5d-4cd1-81-b2-93-24-d7-ec-a7-81')
def _define_GUID_MetadataFormatChunkbKGD():
    return Guid('e14d3571-6b47-4dea-b6-0a-87-ce-0a-78-df-b7')
def _define_GUID_MetadataFormatChunkiTXt():
    return Guid('c2bec729-0b68-4b77-aa-0e-62-95-a6-ac-18-14')
def _define_GUID_MetadataFormatChunkcHRM():
    return Guid('9db3655b-2842-44b3-80-67-12-e9-b3-75-55-6a')
def _define_GUID_MetadataFormatChunkhIST():
    return Guid('c59a82da-db74-48a4-bd-6a-b6-9c-49-31-ef-95')
def _define_GUID_MetadataFormatChunkiCCP():
    return Guid('eb4349ab-b685-450f-91-b5-e8-02-e8-92-53-6c')
def _define_GUID_MetadataFormatChunksRGB():
    return Guid('c115fd36-cc6f-4e3f-83-63-52-4b-87-c6-b0-d9')
def _define_GUID_MetadataFormatChunktIME():
    return Guid('6b00ae2d-e24b-460a-98-b6-87-8b-d0-30-72-fd')
def _define_GUID_MetadataFormatDds():
    return Guid('4a064603-8c33-4e60-9c-29-13-62-31-70-2d-08')
def _define_GUID_MetadataFormatHeif():
    return Guid('817ef3e1-1288-45f4-a8-52-26-0d-9e-7c-ce-83')
def _define_GUID_MetadataFormatHeifHDR():
    return Guid('568b8d8a-1e65-438c-89-68-d6-0e-10-12-be-b9')
def _define_GUID_MetadataFormatWebpANIM():
    return Guid('6dc4fda6-78e6-4102-ae-35-bc-fa-1e-dc-c7-8b')
def _define_GUID_MetadataFormatWebpANMF():
    return Guid('43c105ee-b93b-4abb-b0-03-a0-8c-0d-87-04-71')
def _define_CLSID_WICUnknownMetadataReader():
    return Guid('699745c2-5066-4b82-a8-e3-d4-04-78-db-ec-8c')
def _define_CLSID_WICUnknownMetadataWriter():
    return Guid('a09cca86-27ba-4f39-90-53-12-1f-a4-dc-08-fc')
def _define_CLSID_WICApp0MetadataWriter():
    return Guid('f3c633a2-46c8-498e-8f-bb-cc-6f-72-1b-bc-de')
def _define_CLSID_WICApp0MetadataReader():
    return Guid('43324b33-a78f-480f-91-11-96-38-aa-cc-c8-32')
def _define_CLSID_WICApp1MetadataWriter():
    return Guid('ee366069-1832-420f-b3-81-04-79-ad-06-6f-19')
def _define_CLSID_WICApp1MetadataReader():
    return Guid('dde33513-774e-4bcd-ae-79-02-f4-ad-fe-62-fc')
def _define_CLSID_WICApp13MetadataWriter():
    return Guid('7b19a919-a9d6-49e5-bd-45-02-c3-4e-4e-4c-d5')
def _define_CLSID_WICApp13MetadataReader():
    return Guid('aa7e3c50-864c-4604-bc-04-8b-0b-76-e6-37-f6')
def _define_CLSID_WICIfdMetadataReader():
    return Guid('8f914656-9d0a-4eb2-90-19-0b-f9-6d-8a-9e-e6')
def _define_CLSID_WICIfdMetadataWriter():
    return Guid('b1ebfc28-c9bd-47a2-8d-33-b9-48-76-97-77-a7')
def _define_CLSID_WICSubIfdMetadataReader():
    return Guid('50d42f09-ecd1-4b41-b6-5d-da-1f-da-a7-56-63')
def _define_CLSID_WICSubIfdMetadataWriter():
    return Guid('8ade5386-8e9b-4f4c-ac-f2-f0-00-87-06-b2-38')
def _define_CLSID_WICExifMetadataReader():
    return Guid('d9403860-297f-4a49-bf-9b-77-89-81-50-a4-42')
def _define_CLSID_WICExifMetadataWriter():
    return Guid('c9a14cda-c339-460b-90-78-d4-de-bc-fa-be-91')
def _define_CLSID_WICGpsMetadataReader():
    return Guid('3697790b-223b-484e-99-25-c4-86-92-18-f1-7a')
def _define_CLSID_WICGpsMetadataWriter():
    return Guid('cb8c13e4-62b5-4c96-a4-8b-6b-a6-ac-e3-9c-76')
def _define_CLSID_WICInteropMetadataReader():
    return Guid('b5c8b898-0074-459f-b7-00-86-0d-46-51-ea-14')
def _define_CLSID_WICInteropMetadataWriter():
    return Guid('122ec645-cd7e-44d8-b1-86-2c-8c-20-c3-b5-0f')
def _define_CLSID_WICThumbnailMetadataReader():
    return Guid('fb012959-f4f6-44d7-9d-09-da-a0-87-a9-db-57')
def _define_CLSID_WICThumbnailMetadataWriter():
    return Guid('d049b20c-5dd0-44fe-b0-b3-8f-92-c8-e6-d0-80')
def _define_CLSID_WICIPTCMetadataReader():
    return Guid('03012959-f4f6-44d7-9d-09-da-a0-87-a9-db-57')
def _define_CLSID_WICIPTCMetadataWriter():
    return Guid('1249b20c-5dd0-44fe-b0-b3-8f-92-c8-e6-d0-80')
def _define_CLSID_WICIRBMetadataReader():
    return Guid('d4dcd3d7-b4c2-47d9-a6-bf-b8-9b-a3-96-a4-a3')
def _define_CLSID_WICIRBMetadataWriter():
    return Guid('5c5c1935-0235-4434-80-bc-25-1b-c1-ec-39-c6')
def _define_CLSID_WIC8BIMIPTCMetadataReader():
    return Guid('0010668c-0801-4da6-a4-a4-82-65-22-b6-d2-8f')
def _define_CLSID_WIC8BIMIPTCMetadataWriter():
    return Guid('00108226-ee41-44a2-9e-9c-4b-e4-d5-b1-d2-cd')
def _define_CLSID_WIC8BIMResolutionInfoMetadataReader():
    return Guid('5805137a-e348-4f7c-b3-cc-6d-b9-96-5a-05-99')
def _define_CLSID_WIC8BIMResolutionInfoMetadataWriter():
    return Guid('4ff2fe0e-e74a-4b71-98-c4-ab-7d-c1-67-07-ba')
def _define_CLSID_WIC8BIMIPTCDigestMetadataReader():
    return Guid('02805f1e-d5aa-415b-82-c5-61-c0-33-a9-88-a6')
def _define_CLSID_WIC8BIMIPTCDigestMetadataWriter():
    return Guid('2db5e62b-0d67-495f-8f-9d-c2-f0-18-86-47-ac')
def _define_CLSID_WICPngTextMetadataReader():
    return Guid('4b59afcc-b8c3-408a-b6-70-89-e5-fa-b6-fd-a7')
def _define_CLSID_WICPngTextMetadataWriter():
    return Guid('b5ebafb9-253e-4a72-a7-44-07-62-d2-68-56-83')
def _define_CLSID_WICXMPMetadataReader():
    return Guid('72b624df-ae11-4948-a6-5c-35-1e-b0-82-94-19')
def _define_CLSID_WICXMPMetadataWriter():
    return Guid('1765e14e-1bd4-462e-b6-b1-59-0b-f1-26-2a-c6')
def _define_CLSID_WICXMPStructMetadataReader():
    return Guid('01b90d9a-8209-47f7-9c-52-e1-24-4b-f5-0c-ed')
def _define_CLSID_WICXMPStructMetadataWriter():
    return Guid('22c21f93-7ddb-411c-9b-17-c5-b7-bd-06-4a-bc')
def _define_CLSID_WICXMPBagMetadataReader():
    return Guid('e7e79a30-4f2c-4fab-8d-00-39-4f-2d-6b-be-be')
def _define_CLSID_WICXMPBagMetadataWriter():
    return Guid('ed822c8c-d6be-4301-a6-31-0e-14-16-ba-d2-8f')
def _define_CLSID_WICXMPSeqMetadataReader():
    return Guid('7f12e753-fc71-43d7-a5-1d-92-f3-59-77-ab-b5')
def _define_CLSID_WICXMPSeqMetadataWriter():
    return Guid('6d68d1de-d432-4b0f-92-3a-09-11-83-a9-bd-a7')
def _define_CLSID_WICXMPAltMetadataReader():
    return Guid('aa94dcc2-b8b0-4898-b8-35-00-0a-ab-d7-43-93')
def _define_CLSID_WICXMPAltMetadataWriter():
    return Guid('076c2a6c-f78f-4c46-a7-23-35-83-e7-08-76-ea')
def _define_CLSID_WICLSDMetadataReader():
    return Guid('41070793-59e4-479a-a1-f7-95-4a-dc-2e-f5-fc')
def _define_CLSID_WICLSDMetadataWriter():
    return Guid('73c037e7-e5d9-4954-87-6a-6d-a8-1d-6e-57-68')
def _define_CLSID_WICGCEMetadataReader():
    return Guid('b92e345d-f52d-41f3-b5-62-08-1b-c7-72-e3-b9')
def _define_CLSID_WICGCEMetadataWriter():
    return Guid('af95dc76-16b2-47f4-b3-ea-3c-31-79-66-93-e7')
def _define_CLSID_WICIMDMetadataReader():
    return Guid('7447a267-0015-42c8-a8-f1-fb-3b-94-c6-83-61')
def _define_CLSID_WICIMDMetadataWriter():
    return Guid('8c89071f-452e-4e95-96-82-9d-10-24-62-71-72')
def _define_CLSID_WICAPEMetadataReader():
    return Guid('1767b93a-b021-44ea-92-0f-86-3c-11-f4-f7-68')
def _define_CLSID_WICAPEMetadataWriter():
    return Guid('bd6edfca-2890-482f-b2-33-8d-73-39-a1-cf-8d')
def _define_CLSID_WICJpegChrominanceMetadataReader():
    return Guid('50b1904b-f28f-4574-93-f4-0b-ad-e8-2c-69-e9')
def _define_CLSID_WICJpegChrominanceMetadataWriter():
    return Guid('3ff566f0-6e6b-49d4-96-e6-b7-88-86-69-2c-62')
def _define_CLSID_WICJpegLuminanceMetadataReader():
    return Guid('356f2f88-05a6-4728-b9-a4-1b-fb-ce-04-d8-38')
def _define_CLSID_WICJpegLuminanceMetadataWriter():
    return Guid('1d583abc-8a0e-4657-99-82-a3-80-ca-58-fb-4b')
def _define_CLSID_WICJpegCommentMetadataReader():
    return Guid('9f66347c-60c4-4c4d-ab-58-d2-35-86-85-f6-07')
def _define_CLSID_WICJpegCommentMetadataWriter():
    return Guid('e573236f-55b1-4eda-81-ea-9f-65-db-02-90-d3')
def _define_CLSID_WICGifCommentMetadataReader():
    return Guid('32557d3b-69dc-4f95-83-6e-f5-97-2b-2f-61-59')
def _define_CLSID_WICGifCommentMetadataWriter():
    return Guid('a02797fc-c4ae-418c-af-95-e6-37-c7-ea-d2-a1')
def _define_CLSID_WICPngGamaMetadataReader():
    return Guid('3692ca39-e082-4350-9e-1f-37-04-cb-08-3c-d5')
def _define_CLSID_WICPngGamaMetadataWriter():
    return Guid('ff036d13-5d4b-46dd-b1-0f-10-66-93-d9-fe-4f')
def _define_CLSID_WICPngBkgdMetadataReader():
    return Guid('0ce7a4a6-03e8-4a60-9d-15-28-2e-f3-2e-e7-da')
def _define_CLSID_WICPngBkgdMetadataWriter():
    return Guid('68e3f2fd-31ae-4441-bb-6a-fd-70-47-52-5f-90')
def _define_CLSID_WICPngItxtMetadataReader():
    return Guid('aabfb2fa-3e1e-4a8f-89-77-55-56-fb-94-ea-23')
def _define_CLSID_WICPngItxtMetadataWriter():
    return Guid('31879719-e751-4df8-98-1d-68-df-f6-77-04-ed')
def _define_CLSID_WICPngChrmMetadataReader():
    return Guid('f90b5f36-367b-402a-9d-d1-bc-0f-d5-9d-8f-62')
def _define_CLSID_WICPngChrmMetadataWriter():
    return Guid('e23ce3eb-5608-4e83-bc-ef-27-b1-98-7e-51-d7')
def _define_CLSID_WICPngHistMetadataReader():
    return Guid('877a0bb7-a313-4491-87-b5-2e-6d-05-94-f5-20')
def _define_CLSID_WICPngHistMetadataWriter():
    return Guid('8a03e749-672e-446e-bf-1f-2c-11-d2-33-b6-ff')
def _define_CLSID_WICPngIccpMetadataReader():
    return Guid('f5d3e63b-cb0f-4628-a4-78-6d-82-44-be-36-b1')
def _define_CLSID_WICPngIccpMetadataWriter():
    return Guid('16671e5f-0ce6-4cc4-97-68-e8-9f-e5-01-8a-de')
def _define_CLSID_WICPngSrgbMetadataReader():
    return Guid('fb40360c-547e-4956-a3-b9-d4-41-88-59-ba-66')
def _define_CLSID_WICPngSrgbMetadataWriter():
    return Guid('a6ee35c6-87ec-47df-9f-22-1d-5a-ad-84-0c-82')
def _define_CLSID_WICPngTimeMetadataReader():
    return Guid('d94edf02-efe5-4f0d-85-c8-f5-a6-8b-30-00-b1')
def _define_CLSID_WICPngTimeMetadataWriter():
    return Guid('1ab78400-b5a3-4d91-8a-ce-33-fc-d1-49-9b-e6')
def _define_CLSID_WICDdsMetadataReader():
    return Guid('276c88ca-7533-4a86-b6-76-66-b3-60-80-d4-84')
def _define_CLSID_WICDdsMetadataWriter():
    return Guid('fd688bbd-31ed-4db7-a7-23-93-49-27-d3-83-67')
def _define_CLSID_WICHeifMetadataReader():
    return Guid('acddfc3f-85ec-41bc-bd-ef-1b-c2-62-e4-db-05')
def _define_CLSID_WICHeifMetadataWriter():
    return Guid('3ae45e79-40bc-4401-ac-e5-dd-3c-b1-6e-6a-fe')
def _define_CLSID_WICHeifHDRMetadataReader():
    return Guid('2438de3d-94d9-4be8-84-a8-4d-e9-5a-57-5e-75')
def _define_CLSID_WICWebpAnimMetadataReader():
    return Guid('076f9911-a348-465c-a8-07-a2-52-f3-f2-d3-de')
def _define_CLSID_WICWebpAnmfMetadataReader():
    return Guid('85a10b03-c9f6-439f-be-5e-c0-fb-ef-67-80-7c')
def _define_WICConvertBitmapSource():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),win32more.Graphics.Imaging.IWICBitmapSource_head,POINTER(win32more.Graphics.Imaging.IWICBitmapSource_head))(('WICConvertBitmapSource', windll['WindowsCodecs.dll']), ((1, 'dstFormat'),(1, 'pISrc'),(1, 'ppIDst'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WICCreateBitmapFromSection():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,POINTER(Guid),win32more.Foundation.HANDLE,UInt32,UInt32,POINTER(win32more.Graphics.Imaging.IWICBitmap_head))(('WICCreateBitmapFromSection', windll['WindowsCodecs.dll']), ((1, 'width'),(1, 'height'),(1, 'pixelFormat'),(1, 'hSection'),(1, 'stride'),(1, 'offset'),(1, 'ppIBitmap'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WICCreateBitmapFromSectionEx():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,POINTER(Guid),win32more.Foundation.HANDLE,UInt32,UInt32,win32more.Graphics.Imaging.WICSectionAccessLevel,POINTER(win32more.Graphics.Imaging.IWICBitmap_head))(('WICCreateBitmapFromSectionEx', windll['WindowsCodecs.dll']), ((1, 'width'),(1, 'height'),(1, 'pixelFormat'),(1, 'hSection'),(1, 'stride'),(1, 'offset'),(1, 'desiredAccessLevel'),(1, 'ppIBitmap'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WICMapGuidToShortName():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),UInt32,win32more.Foundation.PWSTR,POINTER(UInt32))(('WICMapGuidToShortName', windll['WindowsCodecs.dll']), ((1, 'guid'),(1, 'cchName'),(1, 'wzName'),(1, 'pcchActual'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WICMapShortNameToGuid():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(Guid))(('WICMapShortNameToGuid', windll['WindowsCodecs.dll']), ((1, 'wzName'),(1, 'pguid'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WICMapSchemaToName():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),win32more.Foundation.PWSTR,UInt32,win32more.Foundation.PWSTR,POINTER(UInt32))(('WICMapSchemaToName', windll['WindowsCodecs.dll']), ((1, 'guidMetadataFormat'),(1, 'pwzSchema'),(1, 'cchName'),(1, 'wzName'),(1, 'pcchActual'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WICMatchMetadataContent():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(Guid),win32more.System.Com.IStream_head,POINTER(Guid))(('WICMatchMetadataContent', windll['WindowsCodecs.dll']), ((1, 'guidContainerFormat'),(1, 'pguidVendor'),(1, 'pIStream'),(1, 'pguidMetadataFormat'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WICSerializeMetadataContent():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),win32more.Graphics.Imaging.IWICMetadataWriter_head,UInt32,win32more.System.Com.IStream_head)(('WICSerializeMetadataContent', windll['WindowsCodecs.dll']), ((1, 'guidContainerFormat'),(1, 'pIWriter'),(1, 'dwPersistOptions'),(1, 'pIStream'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WICGetMetadataContentSize():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),win32more.Graphics.Imaging.IWICMetadataWriter_head,POINTER(win32more.Foundation.ULARGE_INTEGER_head))(('WICGetMetadataContentSize', windll['WindowsCodecs.dll']), ((1, 'guidContainerFormat'),(1, 'pIWriter'),(1, 'pcbSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_IWICBitmap_head():
    class IWICBitmap(win32more.Graphics.Imaging.IWICBitmapSource_head):
        Guid = Guid('00000121-a8f2-4877-ba-0a-fd-2b-66-45-fb-94')
    return IWICBitmap
def _define_IWICBitmap():
    IWICBitmap = win32more.Graphics.Imaging.IWICBitmap_head
    IWICBitmap.Lock = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Imaging.WICRect_head),UInt32,POINTER(win32more.Graphics.Imaging.IWICBitmapLock_head))(8, 'Lock', ((1, 'prcLock'),(1, 'flags'),(1, 'ppILock'),)))
    IWICBitmap.SetPalette = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Imaging.IWICPalette_head)(9, 'SetPalette', ((1, 'pIPalette'),)))
    IWICBitmap.SetResolution = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Double,Double)(10, 'SetResolution', ((1, 'dpiX'),(1, 'dpiY'),)))
    win32more.Graphics.Imaging.IWICBitmapSource
    return IWICBitmap
def _define_IWICBitmapClipper_head():
    class IWICBitmapClipper(win32more.Graphics.Imaging.IWICBitmapSource_head):
        Guid = Guid('e4fbcf03-223d-4e81-93-33-d6-35-55-6d-d1-b5')
    return IWICBitmapClipper
def _define_IWICBitmapClipper():
    IWICBitmapClipper = win32more.Graphics.Imaging.IWICBitmapClipper_head
    IWICBitmapClipper.Initialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Imaging.IWICBitmapSource_head,POINTER(win32more.Graphics.Imaging.WICRect_head))(8, 'Initialize', ((1, 'pISource'),(1, 'prc'),)))
    win32more.Graphics.Imaging.IWICBitmapSource
    return IWICBitmapClipper
def _define_IWICBitmapCodecInfo_head():
    class IWICBitmapCodecInfo(win32more.Graphics.Imaging.IWICComponentInfo_head):
        Guid = Guid('e87a44c4-b76e-4c47-8b-09-29-8e-b1-2a-27-14')
    return IWICBitmapCodecInfo
def _define_IWICBitmapCodecInfo():
    IWICBitmapCodecInfo = win32more.Graphics.Imaging.IWICBitmapCodecInfo_head
    IWICBitmapCodecInfo.GetContainerFormat = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid))(11, 'GetContainerFormat', ((1, 'pguidContainerFormat'),)))
    IWICBitmapCodecInfo.GetPixelFormats = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(Guid),POINTER(UInt32))(12, 'GetPixelFormats', ((1, 'cFormats'),(1, 'pguidPixelFormats'),(1, 'pcActual'),)))
    IWICBitmapCodecInfo.GetColorManagementVersion = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Foundation.PWSTR,POINTER(UInt32))(13, 'GetColorManagementVersion', ((1, 'cchColorManagementVersion'),(1, 'wzColorManagementVersion'),(1, 'pcchActual'),)))
    IWICBitmapCodecInfo.GetDeviceManufacturer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Foundation.PWSTR,POINTER(UInt32))(14, 'GetDeviceManufacturer', ((1, 'cchDeviceManufacturer'),(1, 'wzDeviceManufacturer'),(1, 'pcchActual'),)))
    IWICBitmapCodecInfo.GetDeviceModels = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Foundation.PWSTR,POINTER(UInt32))(15, 'GetDeviceModels', ((1, 'cchDeviceModels'),(1, 'wzDeviceModels'),(1, 'pcchActual'),)))
    IWICBitmapCodecInfo.GetMimeTypes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Foundation.PWSTR,POINTER(UInt32))(16, 'GetMimeTypes', ((1, 'cchMimeTypes'),(1, 'wzMimeTypes'),(1, 'pcchActual'),)))
    IWICBitmapCodecInfo.GetFileExtensions = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Foundation.PWSTR,POINTER(UInt32))(17, 'GetFileExtensions', ((1, 'cchFileExtensions'),(1, 'wzFileExtensions'),(1, 'pcchActual'),)))
    IWICBitmapCodecInfo.DoesSupportAnimation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL))(18, 'DoesSupportAnimation', ((1, 'pfSupportAnimation'),)))
    IWICBitmapCodecInfo.DoesSupportChromakey = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL))(19, 'DoesSupportChromakey', ((1, 'pfSupportChromakey'),)))
    IWICBitmapCodecInfo.DoesSupportLossless = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL))(20, 'DoesSupportLossless', ((1, 'pfSupportLossless'),)))
    IWICBitmapCodecInfo.DoesSupportMultiframe = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL))(21, 'DoesSupportMultiframe', ((1, 'pfSupportMultiframe'),)))
    IWICBitmapCodecInfo.MatchesMimeType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.BOOL))(22, 'MatchesMimeType', ((1, 'wzMimeType'),(1, 'pfMatches'),)))
    win32more.Graphics.Imaging.IWICComponentInfo
    return IWICBitmapCodecInfo
def _define_IWICBitmapCodecProgressNotification_head():
    class IWICBitmapCodecProgressNotification(win32more.System.Com.IUnknown_head):
        Guid = Guid('64c1024e-c3cf-4462-80-78-88-c2-b1-1c-46-d9')
    return IWICBitmapCodecProgressNotification
def _define_IWICBitmapCodecProgressNotification():
    IWICBitmapCodecProgressNotification = win32more.Graphics.Imaging.IWICBitmapCodecProgressNotification_head
    IWICBitmapCodecProgressNotification.RegisterProgressNotification = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Imaging.PFNProgressNotification,c_void_p,UInt32)(3, 'RegisterProgressNotification', ((1, 'pfnProgressNotification'),(1, 'pvData'),(1, 'dwProgressFlags'),)))
    win32more.System.Com.IUnknown
    return IWICBitmapCodecProgressNotification
def _define_IWICBitmapDecoder_head():
    class IWICBitmapDecoder(win32more.System.Com.IUnknown_head):
        Guid = Guid('9edde9e7-8dee-47ea-99-df-e6-fa-f2-ed-44-bf')
    return IWICBitmapDecoder
def _define_IWICBitmapDecoder():
    IWICBitmapDecoder = win32more.Graphics.Imaging.IWICBitmapDecoder_head
    IWICBitmapDecoder.QueryCapability = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IStream_head,POINTER(UInt32))(3, 'QueryCapability', ((1, 'pIStream'),(1, 'pdwCapability'),)))
    IWICBitmapDecoder.Initialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IStream_head,win32more.Graphics.Imaging.WICDecodeOptions)(4, 'Initialize', ((1, 'pIStream'),(1, 'cacheOptions'),)))
    IWICBitmapDecoder.GetContainerFormat = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid))(5, 'GetContainerFormat', ((1, 'pguidContainerFormat'),)))
    IWICBitmapDecoder.GetDecoderInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Imaging.IWICBitmapDecoderInfo_head))(6, 'GetDecoderInfo', ((1, 'ppIDecoderInfo'),)))
    IWICBitmapDecoder.CopyPalette = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Imaging.IWICPalette_head)(7, 'CopyPalette', ((1, 'pIPalette'),)))
    IWICBitmapDecoder.GetMetadataQueryReader = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Imaging.IWICMetadataQueryReader_head))(8, 'GetMetadataQueryReader', ((1, 'ppIMetadataQueryReader'),)))
    IWICBitmapDecoder.GetPreview = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Imaging.IWICBitmapSource_head))(9, 'GetPreview', ((1, 'ppIBitmapSource'),)))
    IWICBitmapDecoder.GetColorContexts = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Graphics.Imaging.IWICColorContext_head),POINTER(UInt32))(10, 'GetColorContexts', ((1, 'cCount'),(1, 'ppIColorContexts'),(1, 'pcActualCount'),)))
    IWICBitmapDecoder.GetThumbnail = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Imaging.IWICBitmapSource_head))(11, 'GetThumbnail', ((1, 'ppIThumbnail'),)))
    IWICBitmapDecoder.GetFrameCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(12, 'GetFrameCount', ((1, 'pCount'),)))
    IWICBitmapDecoder.GetFrame = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Graphics.Imaging.IWICBitmapFrameDecode_head))(13, 'GetFrame', ((1, 'index'),(1, 'ppIBitmapFrame'),)))
    win32more.System.Com.IUnknown
    return IWICBitmapDecoder
def _define_IWICBitmapDecoderInfo_head():
    class IWICBitmapDecoderInfo(win32more.Graphics.Imaging.IWICBitmapCodecInfo_head):
        Guid = Guid('d8cd007f-d08f-4191-9b-fc-23-6e-a7-f0-e4-b5')
    return IWICBitmapDecoderInfo
def _define_IWICBitmapDecoderInfo():
    IWICBitmapDecoderInfo = win32more.Graphics.Imaging.IWICBitmapDecoderInfo_head
    IWICBitmapDecoderInfo.GetPatterns = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Graphics.Imaging.WICBitmapPattern_head),POINTER(UInt32),POINTER(UInt32))(23, 'GetPatterns', ((1, 'cbSizePatterns'),(1, 'pPatterns'),(1, 'pcPatterns'),(1, 'pcbPatternsActual'),)))
    IWICBitmapDecoderInfo.MatchesPattern = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IStream_head,POINTER(win32more.Foundation.BOOL))(24, 'MatchesPattern', ((1, 'pIStream'),(1, 'pfMatches'),)))
    IWICBitmapDecoderInfo.CreateInstance = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Imaging.IWICBitmapDecoder_head))(25, 'CreateInstance', ((1, 'ppIBitmapDecoder'),)))
    win32more.Graphics.Imaging.IWICBitmapCodecInfo
    return IWICBitmapDecoderInfo
def _define_IWICBitmapEncoder_head():
    class IWICBitmapEncoder(win32more.System.Com.IUnknown_head):
        Guid = Guid('00000103-a8f2-4877-ba-0a-fd-2b-66-45-fb-94')
    return IWICBitmapEncoder
def _define_IWICBitmapEncoder():
    IWICBitmapEncoder = win32more.Graphics.Imaging.IWICBitmapEncoder_head
    IWICBitmapEncoder.Initialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IStream_head,win32more.Graphics.Imaging.WICBitmapEncoderCacheOption)(3, 'Initialize', ((1, 'pIStream'),(1, 'cacheOption'),)))
    IWICBitmapEncoder.GetContainerFormat = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid))(4, 'GetContainerFormat', ((1, 'pguidContainerFormat'),)))
    IWICBitmapEncoder.GetEncoderInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Imaging.IWICBitmapEncoderInfo_head))(5, 'GetEncoderInfo', ((1, 'ppIEncoderInfo'),)))
    IWICBitmapEncoder.SetColorContexts = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Graphics.Imaging.IWICColorContext_head))(6, 'SetColorContexts', ((1, 'cCount'),(1, 'ppIColorContext'),)))
    IWICBitmapEncoder.SetPalette = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Imaging.IWICPalette_head)(7, 'SetPalette', ((1, 'pIPalette'),)))
    IWICBitmapEncoder.SetThumbnail = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Imaging.IWICBitmapSource_head)(8, 'SetThumbnail', ((1, 'pIThumbnail'),)))
    IWICBitmapEncoder.SetPreview = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Imaging.IWICBitmapSource_head)(9, 'SetPreview', ((1, 'pIPreview'),)))
    IWICBitmapEncoder.CreateNewFrame = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Imaging.IWICBitmapFrameEncode_head),POINTER(win32more.System.Com.StructuredStorage.IPropertyBag2_head))(10, 'CreateNewFrame', ((1, 'ppIFrameEncode'),(1, 'ppIEncoderOptions'),)))
    IWICBitmapEncoder.Commit = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(11, 'Commit', ()))
    IWICBitmapEncoder.GetMetadataQueryWriter = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Imaging.IWICMetadataQueryWriter_head))(12, 'GetMetadataQueryWriter', ((1, 'ppIMetadataQueryWriter'),)))
    win32more.System.Com.IUnknown
    return IWICBitmapEncoder
def _define_IWICBitmapEncoderInfo_head():
    class IWICBitmapEncoderInfo(win32more.Graphics.Imaging.IWICBitmapCodecInfo_head):
        Guid = Guid('94c9b4ee-a09f-4f92-8a-1e-4a-9b-ce-7e-76-fb')
    return IWICBitmapEncoderInfo
def _define_IWICBitmapEncoderInfo():
    IWICBitmapEncoderInfo = win32more.Graphics.Imaging.IWICBitmapEncoderInfo_head
    IWICBitmapEncoderInfo.CreateInstance = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Imaging.IWICBitmapEncoder_head))(23, 'CreateInstance', ((1, 'ppIBitmapEncoder'),)))
    win32more.Graphics.Imaging.IWICBitmapCodecInfo
    return IWICBitmapEncoderInfo
def _define_IWICBitmapFlipRotator_head():
    class IWICBitmapFlipRotator(win32more.Graphics.Imaging.IWICBitmapSource_head):
        Guid = Guid('5009834f-2d6a-41ce-9e-1b-17-c5-af-f7-a7-82')
    return IWICBitmapFlipRotator
def _define_IWICBitmapFlipRotator():
    IWICBitmapFlipRotator = win32more.Graphics.Imaging.IWICBitmapFlipRotator_head
    IWICBitmapFlipRotator.Initialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Imaging.IWICBitmapSource_head,win32more.Graphics.Imaging.WICBitmapTransformOptions)(8, 'Initialize', ((1, 'pISource'),(1, 'options'),)))
    win32more.Graphics.Imaging.IWICBitmapSource
    return IWICBitmapFlipRotator
def _define_IWICBitmapFrameDecode_head():
    class IWICBitmapFrameDecode(win32more.Graphics.Imaging.IWICBitmapSource_head):
        Guid = Guid('3b16811b-6a43-4ec9-a8-13-3d-93-0c-13-b9-40')
    return IWICBitmapFrameDecode
def _define_IWICBitmapFrameDecode():
    IWICBitmapFrameDecode = win32more.Graphics.Imaging.IWICBitmapFrameDecode_head
    IWICBitmapFrameDecode.GetMetadataQueryReader = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Imaging.IWICMetadataQueryReader_head))(8, 'GetMetadataQueryReader', ((1, 'ppIMetadataQueryReader'),)))
    IWICBitmapFrameDecode.GetColorContexts = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Graphics.Imaging.IWICColorContext_head),POINTER(UInt32))(9, 'GetColorContexts', ((1, 'cCount'),(1, 'ppIColorContexts'),(1, 'pcActualCount'),)))
    IWICBitmapFrameDecode.GetThumbnail = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Imaging.IWICBitmapSource_head))(10, 'GetThumbnail', ((1, 'ppIThumbnail'),)))
    win32more.Graphics.Imaging.IWICBitmapSource
    return IWICBitmapFrameDecode
def _define_IWICBitmapFrameEncode_head():
    class IWICBitmapFrameEncode(win32more.System.Com.IUnknown_head):
        Guid = Guid('00000105-a8f2-4877-ba-0a-fd-2b-66-45-fb-94')
    return IWICBitmapFrameEncode
def _define_IWICBitmapFrameEncode():
    IWICBitmapFrameEncode = win32more.Graphics.Imaging.IWICBitmapFrameEncode_head
    IWICBitmapFrameEncode.Initialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.StructuredStorage.IPropertyBag2_head)(3, 'Initialize', ((1, 'pIEncoderOptions'),)))
    IWICBitmapFrameEncode.SetSize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32)(4, 'SetSize', ((1, 'uiWidth'),(1, 'uiHeight'),)))
    IWICBitmapFrameEncode.SetResolution = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Double,Double)(5, 'SetResolution', ((1, 'dpiX'),(1, 'dpiY'),)))
    IWICBitmapFrameEncode.SetPixelFormat = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid))(6, 'SetPixelFormat', ((1, 'pPixelFormat'),)))
    IWICBitmapFrameEncode.SetColorContexts = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Graphics.Imaging.IWICColorContext_head))(7, 'SetColorContexts', ((1, 'cCount'),(1, 'ppIColorContext'),)))
    IWICBitmapFrameEncode.SetPalette = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Imaging.IWICPalette_head)(8, 'SetPalette', ((1, 'pIPalette'),)))
    IWICBitmapFrameEncode.SetThumbnail = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Imaging.IWICBitmapSource_head)(9, 'SetThumbnail', ((1, 'pIThumbnail'),)))
    IWICBitmapFrameEncode.WritePixels = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,UInt32,c_char_p_no)(10, 'WritePixels', ((1, 'lineCount'),(1, 'cbStride'),(1, 'cbBufferSize'),(1, 'pbPixels'),)))
    IWICBitmapFrameEncode.WriteSource = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Imaging.IWICBitmapSource_head,POINTER(win32more.Graphics.Imaging.WICRect_head))(11, 'WriteSource', ((1, 'pIBitmapSource'),(1, 'prc'),)))
    IWICBitmapFrameEncode.Commit = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(12, 'Commit', ()))
    IWICBitmapFrameEncode.GetMetadataQueryWriter = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Imaging.IWICMetadataQueryWriter_head))(13, 'GetMetadataQueryWriter', ((1, 'ppIMetadataQueryWriter'),)))
    win32more.System.Com.IUnknown
    return IWICBitmapFrameEncode
def _define_IWICBitmapLock_head():
    class IWICBitmapLock(win32more.System.Com.IUnknown_head):
        Guid = Guid('00000123-a8f2-4877-ba-0a-fd-2b-66-45-fb-94')
    return IWICBitmapLock
def _define_IWICBitmapLock():
    IWICBitmapLock = win32more.Graphics.Imaging.IWICBitmapLock_head
    IWICBitmapLock.GetSize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32),POINTER(UInt32))(3, 'GetSize', ((1, 'puiWidth'),(1, 'puiHeight'),)))
    IWICBitmapLock.GetStride = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(4, 'GetStride', ((1, 'pcbStride'),)))
    IWICBitmapLock.GetDataPointer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32),POINTER(c_char_p_no))(5, 'GetDataPointer', ((1, 'pcbBufferSize'),(1, 'ppbData'),)))
    IWICBitmapLock.GetPixelFormat = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid))(6, 'GetPixelFormat', ((1, 'pPixelFormat'),)))
    win32more.System.Com.IUnknown
    return IWICBitmapLock
def _define_IWICBitmapScaler_head():
    class IWICBitmapScaler(win32more.Graphics.Imaging.IWICBitmapSource_head):
        Guid = Guid('00000302-a8f2-4877-ba-0a-fd-2b-66-45-fb-94')
    return IWICBitmapScaler
def _define_IWICBitmapScaler():
    IWICBitmapScaler = win32more.Graphics.Imaging.IWICBitmapScaler_head
    IWICBitmapScaler.Initialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Imaging.IWICBitmapSource_head,UInt32,UInt32,win32more.Graphics.Imaging.WICBitmapInterpolationMode)(8, 'Initialize', ((1, 'pISource'),(1, 'uiWidth'),(1, 'uiHeight'),(1, 'mode'),)))
    win32more.Graphics.Imaging.IWICBitmapSource
    return IWICBitmapScaler
def _define_IWICBitmapSource_head():
    class IWICBitmapSource(win32more.System.Com.IUnknown_head):
        Guid = Guid('00000120-a8f2-4877-ba-0a-fd-2b-66-45-fb-94')
    return IWICBitmapSource
def _define_IWICBitmapSource():
    IWICBitmapSource = win32more.Graphics.Imaging.IWICBitmapSource_head
    IWICBitmapSource.GetSize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32),POINTER(UInt32))(3, 'GetSize', ((1, 'puiWidth'),(1, 'puiHeight'),)))
    IWICBitmapSource.GetPixelFormat = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid))(4, 'GetPixelFormat', ((1, 'pPixelFormat'),)))
    IWICBitmapSource.GetResolution = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double),POINTER(Double))(5, 'GetResolution', ((1, 'pDpiX'),(1, 'pDpiY'),)))
    IWICBitmapSource.CopyPalette = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Imaging.IWICPalette_head)(6, 'CopyPalette', ((1, 'pIPalette'),)))
    IWICBitmapSource.CopyPixels = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Imaging.WICRect_head),UInt32,UInt32,c_char_p_no)(7, 'CopyPixels', ((1, 'prc'),(1, 'cbStride'),(1, 'cbBufferSize'),(1, 'pbBuffer'),)))
    win32more.System.Com.IUnknown
    return IWICBitmapSource
def _define_IWICBitmapSourceTransform_head():
    class IWICBitmapSourceTransform(win32more.System.Com.IUnknown_head):
        Guid = Guid('3b16811b-6a43-4ec9-b7-13-3d-5a-0c-13-b9-40')
    return IWICBitmapSourceTransform
def _define_IWICBitmapSourceTransform():
    IWICBitmapSourceTransform = win32more.Graphics.Imaging.IWICBitmapSourceTransform_head
    IWICBitmapSourceTransform.CopyPixels = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Imaging.WICRect_head),UInt32,UInt32,POINTER(Guid),win32more.Graphics.Imaging.WICBitmapTransformOptions,UInt32,UInt32,c_char_p_no)(3, 'CopyPixels', ((1, 'prc'),(1, 'uiWidth'),(1, 'uiHeight'),(1, 'pguidDstFormat'),(1, 'dstTransform'),(1, 'nStride'),(1, 'cbBufferSize'),(1, 'pbBuffer'),)))
    IWICBitmapSourceTransform.GetClosestSize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32),POINTER(UInt32))(4, 'GetClosestSize', ((1, 'puiWidth'),(1, 'puiHeight'),)))
    IWICBitmapSourceTransform.GetClosestPixelFormat = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid))(5, 'GetClosestPixelFormat', ((1, 'pguidDstFormat'),)))
    IWICBitmapSourceTransform.DoesSupportTransform = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Imaging.WICBitmapTransformOptions,POINTER(win32more.Foundation.BOOL))(6, 'DoesSupportTransform', ((1, 'dstTransform'),(1, 'pfIsSupported'),)))
    win32more.System.Com.IUnknown
    return IWICBitmapSourceTransform
def _define_IWICColorContext_head():
    class IWICColorContext(win32more.System.Com.IUnknown_head):
        Guid = Guid('3c613a02-34b2-44ea-9a-7c-45-ae-a9-c6-fd-6d')
    return IWICColorContext
def _define_IWICColorContext():
    IWICColorContext = win32more.Graphics.Imaging.IWICColorContext_head
    IWICColorContext.InitializeFromFilename = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR)(3, 'InitializeFromFilename', ((1, 'wzFilename'),)))
    IWICColorContext.InitializeFromMemory = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_char_p_no,UInt32)(4, 'InitializeFromMemory', ((1, 'pbBuffer'),(1, 'cbBufferSize'),)))
    IWICColorContext.InitializeFromExifColorSpace = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(5, 'InitializeFromExifColorSpace', ((1, 'value'),)))
    IWICColorContext.GetType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Imaging.WICColorContextType))(6, 'GetType', ((1, 'pType'),)))
    IWICColorContext.GetProfileBytes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,c_char_p_no,POINTER(UInt32))(7, 'GetProfileBytes', ((1, 'cbBuffer'),(1, 'pbBuffer'),(1, 'pcbActual'),)))
    IWICColorContext.GetExifColorSpace = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(8, 'GetExifColorSpace', ((1, 'pValue'),)))
    win32more.System.Com.IUnknown
    return IWICColorContext
def _define_IWICColorTransform_head():
    class IWICColorTransform(win32more.Graphics.Imaging.IWICBitmapSource_head):
        Guid = Guid('b66f034f-d0e2-40ab-b4-36-6d-e3-9e-32-1a-94')
    return IWICColorTransform
def _define_IWICColorTransform():
    IWICColorTransform = win32more.Graphics.Imaging.IWICColorTransform_head
    IWICColorTransform.Initialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Imaging.IWICBitmapSource_head,win32more.Graphics.Imaging.IWICColorContext_head,win32more.Graphics.Imaging.IWICColorContext_head,POINTER(Guid))(8, 'Initialize', ((1, 'pIBitmapSource'),(1, 'pIContextSource'),(1, 'pIContextDest'),(1, 'pixelFmtDest'),)))
    win32more.Graphics.Imaging.IWICBitmapSource
    return IWICColorTransform
def _define_IWICComponentFactory_head():
    class IWICComponentFactory(win32more.Graphics.Imaging.IWICImagingFactory_head):
        Guid = Guid('412d0c3a-9650-44fa-af-5b-dd-2a-06-c8-e8-fb')
    return IWICComponentFactory
def _define_IWICComponentFactory():
    IWICComponentFactory = win32more.Graphics.Imaging.IWICComponentFactory_head
    IWICComponentFactory.CreateMetadataReader = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(Guid),UInt32,win32more.System.Com.IStream_head,POINTER(win32more.Graphics.Imaging.IWICMetadataReader_head))(28, 'CreateMetadataReader', ((1, 'guidMetadataFormat'),(1, 'pguidVendor'),(1, 'dwOptions'),(1, 'pIStream'),(1, 'ppIReader'),)))
    IWICComponentFactory.CreateMetadataReaderFromContainer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(Guid),UInt32,win32more.System.Com.IStream_head,POINTER(win32more.Graphics.Imaging.IWICMetadataReader_head))(29, 'CreateMetadataReaderFromContainer', ((1, 'guidContainerFormat'),(1, 'pguidVendor'),(1, 'dwOptions'),(1, 'pIStream'),(1, 'ppIReader'),)))
    IWICComponentFactory.CreateMetadataWriter = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(Guid),UInt32,POINTER(win32more.Graphics.Imaging.IWICMetadataWriter_head))(30, 'CreateMetadataWriter', ((1, 'guidMetadataFormat'),(1, 'pguidVendor'),(1, 'dwMetadataOptions'),(1, 'ppIWriter'),)))
    IWICComponentFactory.CreateMetadataWriterFromReader = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Imaging.IWICMetadataReader_head,POINTER(Guid),POINTER(win32more.Graphics.Imaging.IWICMetadataWriter_head))(31, 'CreateMetadataWriterFromReader', ((1, 'pIReader'),(1, 'pguidVendor'),(1, 'ppIWriter'),)))
    IWICComponentFactory.CreateQueryReaderFromBlockReader = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Imaging.IWICMetadataBlockReader_head,POINTER(win32more.Graphics.Imaging.IWICMetadataQueryReader_head))(32, 'CreateQueryReaderFromBlockReader', ((1, 'pIBlockReader'),(1, 'ppIQueryReader'),)))
    IWICComponentFactory.CreateQueryWriterFromBlockWriter = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Imaging.IWICMetadataBlockWriter_head,POINTER(win32more.Graphics.Imaging.IWICMetadataQueryWriter_head))(33, 'CreateQueryWriterFromBlockWriter', ((1, 'pIBlockWriter'),(1, 'ppIQueryWriter'),)))
    IWICComponentFactory.CreateEncoderPropertyBag = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.StructuredStorage.PROPBAG2_head),UInt32,POINTER(win32more.System.Com.StructuredStorage.IPropertyBag2_head))(34, 'CreateEncoderPropertyBag', ((1, 'ppropOptions'),(1, 'cCount'),(1, 'ppIPropertyBag'),)))
    win32more.Graphics.Imaging.IWICImagingFactory
    return IWICComponentFactory
def _define_IWICComponentInfo_head():
    class IWICComponentInfo(win32more.System.Com.IUnknown_head):
        Guid = Guid('23bc3f0a-698b-4357-88-6b-f2-4d-50-67-13-34')
    return IWICComponentInfo
def _define_IWICComponentInfo():
    IWICComponentInfo = win32more.Graphics.Imaging.IWICComponentInfo_head
    IWICComponentInfo.GetComponentType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Imaging.WICComponentType))(3, 'GetComponentType', ((1, 'pType'),)))
    IWICComponentInfo.GetCLSID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid))(4, 'GetCLSID', ((1, 'pclsid'),)))
    IWICComponentInfo.GetSigningStatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(5, 'GetSigningStatus', ((1, 'pStatus'),)))
    IWICComponentInfo.GetAuthor = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Foundation.PWSTR,POINTER(UInt32))(6, 'GetAuthor', ((1, 'cchAuthor'),(1, 'wzAuthor'),(1, 'pcchActual'),)))
    IWICComponentInfo.GetVendorGUID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid))(7, 'GetVendorGUID', ((1, 'pguidVendor'),)))
    IWICComponentInfo.GetVersion = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Foundation.PWSTR,POINTER(UInt32))(8, 'GetVersion', ((1, 'cchVersion'),(1, 'wzVersion'),(1, 'pcchActual'),)))
    IWICComponentInfo.GetSpecVersion = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Foundation.PWSTR,POINTER(UInt32))(9, 'GetSpecVersion', ((1, 'cchSpecVersion'),(1, 'wzSpecVersion'),(1, 'pcchActual'),)))
    IWICComponentInfo.GetFriendlyName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Foundation.PWSTR,POINTER(UInt32))(10, 'GetFriendlyName', ((1, 'cchFriendlyName'),(1, 'wzFriendlyName'),(1, 'pcchActual'),)))
    win32more.System.Com.IUnknown
    return IWICComponentInfo
def _define_IWICDdsDecoder_head():
    class IWICDdsDecoder(win32more.System.Com.IUnknown_head):
        Guid = Guid('409cd537-8532-40cb-97-74-e2-fe-b2-df-4e-9c')
    return IWICDdsDecoder
def _define_IWICDdsDecoder():
    IWICDdsDecoder = win32more.Graphics.Imaging.IWICDdsDecoder_head
    IWICDdsDecoder.GetParameters = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Imaging.WICDdsParameters_head))(3, 'GetParameters', ((1, 'pParameters'),)))
    IWICDdsDecoder.GetFrame = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,UInt32,POINTER(win32more.Graphics.Imaging.IWICBitmapFrameDecode_head))(4, 'GetFrame', ((1, 'arrayIndex'),(1, 'mipLevel'),(1, 'sliceIndex'),(1, 'ppIBitmapFrame'),)))
    win32more.System.Com.IUnknown
    return IWICDdsDecoder
def _define_IWICDdsEncoder_head():
    class IWICDdsEncoder(win32more.System.Com.IUnknown_head):
        Guid = Guid('5cacdb4c-407e-41b3-b9-36-d0-f0-10-cd-67-32')
    return IWICDdsEncoder
def _define_IWICDdsEncoder():
    IWICDdsEncoder = win32more.Graphics.Imaging.IWICDdsEncoder_head
    IWICDdsEncoder.SetParameters = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Imaging.WICDdsParameters_head))(3, 'SetParameters', ((1, 'pParameters'),)))
    IWICDdsEncoder.GetParameters = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Imaging.WICDdsParameters_head))(4, 'GetParameters', ((1, 'pParameters'),)))
    IWICDdsEncoder.CreateNewFrame = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Imaging.IWICBitmapFrameEncode_head),POINTER(UInt32),POINTER(UInt32),POINTER(UInt32))(5, 'CreateNewFrame', ((1, 'ppIFrameEncode'),(1, 'pArrayIndex'),(1, 'pMipLevel'),(1, 'pSliceIndex'),)))
    win32more.System.Com.IUnknown
    return IWICDdsEncoder
def _define_IWICDdsFrameDecode_head():
    class IWICDdsFrameDecode(win32more.System.Com.IUnknown_head):
        Guid = Guid('3d4c0c61-18a4-41e4-bd-80-48-1a-4f-c9-f4-64')
    return IWICDdsFrameDecode
def _define_IWICDdsFrameDecode():
    IWICDdsFrameDecode = win32more.Graphics.Imaging.IWICDdsFrameDecode_head
    IWICDdsFrameDecode.GetSizeInBlocks = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32),POINTER(UInt32))(3, 'GetSizeInBlocks', ((1, 'pWidthInBlocks'),(1, 'pHeightInBlocks'),)))
    IWICDdsFrameDecode.GetFormatInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Imaging.WICDdsFormatInfo_head))(4, 'GetFormatInfo', ((1, 'pFormatInfo'),)))
    IWICDdsFrameDecode.CopyBlocks = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Imaging.WICRect_head),UInt32,UInt32,c_char_p_no)(5, 'CopyBlocks', ((1, 'prcBoundsInBlocks'),(1, 'cbStride'),(1, 'cbBufferSize'),(1, 'pbBuffer'),)))
    win32more.System.Com.IUnknown
    return IWICDdsFrameDecode
def _define_IWICDevelopRaw_head():
    class IWICDevelopRaw(win32more.Graphics.Imaging.IWICBitmapFrameDecode_head):
        Guid = Guid('fbec5e44-f7be-4b65-b7-f8-c0-c8-1f-ef-02-6d')
    return IWICDevelopRaw
def _define_IWICDevelopRaw():
    IWICDevelopRaw = win32more.Graphics.Imaging.IWICDevelopRaw_head
    IWICDevelopRaw.QueryRawCapabilitiesInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Imaging.WICRawCapabilitiesInfo_head))(11, 'QueryRawCapabilitiesInfo', ((1, 'pInfo'),)))
    IWICDevelopRaw.LoadParameterSet = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Imaging.WICRawParameterSet)(12, 'LoadParameterSet', ((1, 'ParameterSet'),)))
    IWICDevelopRaw.GetCurrentParameterSet = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.StructuredStorage.IPropertyBag2_head))(13, 'GetCurrentParameterSet', ((1, 'ppCurrentParameterSet'),)))
    IWICDevelopRaw.SetExposureCompensation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Double)(14, 'SetExposureCompensation', ((1, 'ev'),)))
    IWICDevelopRaw.GetExposureCompensation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double))(15, 'GetExposureCompensation', ((1, 'pEV'),)))
    IWICDevelopRaw.SetWhitePointRGB = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,UInt32)(16, 'SetWhitePointRGB', ((1, 'Red'),(1, 'Green'),(1, 'Blue'),)))
    IWICDevelopRaw.GetWhitePointRGB = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32),POINTER(UInt32),POINTER(UInt32))(17, 'GetWhitePointRGB', ((1, 'pRed'),(1, 'pGreen'),(1, 'pBlue'),)))
    IWICDevelopRaw.SetNamedWhitePoint = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Imaging.WICNamedWhitePoint)(18, 'SetNamedWhitePoint', ((1, 'WhitePoint'),)))
    IWICDevelopRaw.GetNamedWhitePoint = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Imaging.WICNamedWhitePoint))(19, 'GetNamedWhitePoint', ((1, 'pWhitePoint'),)))
    IWICDevelopRaw.SetWhitePointKelvin = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(20, 'SetWhitePointKelvin', ((1, 'WhitePointKelvin'),)))
    IWICDevelopRaw.GetWhitePointKelvin = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(21, 'GetWhitePointKelvin', ((1, 'pWhitePointKelvin'),)))
    IWICDevelopRaw.GetKelvinRangeInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32),POINTER(UInt32),POINTER(UInt32))(22, 'GetKelvinRangeInfo', ((1, 'pMinKelvinTemp'),(1, 'pMaxKelvinTemp'),(1, 'pKelvinTempStepValue'),)))
    IWICDevelopRaw.SetContrast = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Double)(23, 'SetContrast', ((1, 'Contrast'),)))
    IWICDevelopRaw.GetContrast = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double))(24, 'GetContrast', ((1, 'pContrast'),)))
    IWICDevelopRaw.SetGamma = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Double)(25, 'SetGamma', ((1, 'Gamma'),)))
    IWICDevelopRaw.GetGamma = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double))(26, 'GetGamma', ((1, 'pGamma'),)))
    IWICDevelopRaw.SetSharpness = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Double)(27, 'SetSharpness', ((1, 'Sharpness'),)))
    IWICDevelopRaw.GetSharpness = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double))(28, 'GetSharpness', ((1, 'pSharpness'),)))
    IWICDevelopRaw.SetSaturation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Double)(29, 'SetSaturation', ((1, 'Saturation'),)))
    IWICDevelopRaw.GetSaturation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double))(30, 'GetSaturation', ((1, 'pSaturation'),)))
    IWICDevelopRaw.SetTint = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Double)(31, 'SetTint', ((1, 'Tint'),)))
    IWICDevelopRaw.GetTint = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double))(32, 'GetTint', ((1, 'pTint'),)))
    IWICDevelopRaw.SetNoiseReduction = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Double)(33, 'SetNoiseReduction', ((1, 'NoiseReduction'),)))
    IWICDevelopRaw.GetNoiseReduction = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double))(34, 'GetNoiseReduction', ((1, 'pNoiseReduction'),)))
    IWICDevelopRaw.SetDestinationColorContext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Imaging.IWICColorContext_head)(35, 'SetDestinationColorContext', ((1, 'pColorContext'),)))
    IWICDevelopRaw.SetToneCurve = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Graphics.Imaging.WICRawToneCurve_head))(36, 'SetToneCurve', ((1, 'cbToneCurveSize'),(1, 'pToneCurve'),)))
    IWICDevelopRaw.GetToneCurve = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Graphics.Imaging.WICRawToneCurve_head),POINTER(UInt32))(37, 'GetToneCurve', ((1, 'cbToneCurveBufferSize'),(1, 'pToneCurve'),(1, 'pcbActualToneCurveBufferSize'),)))
    IWICDevelopRaw.SetRotation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Double)(38, 'SetRotation', ((1, 'Rotation'),)))
    IWICDevelopRaw.GetRotation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double))(39, 'GetRotation', ((1, 'pRotation'),)))
    IWICDevelopRaw.SetRenderMode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Imaging.WICRawRenderMode)(40, 'SetRenderMode', ((1, 'RenderMode'),)))
    IWICDevelopRaw.GetRenderMode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Imaging.WICRawRenderMode))(41, 'GetRenderMode', ((1, 'pRenderMode'),)))
    IWICDevelopRaw.SetNotificationCallback = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Imaging.IWICDevelopRawNotificationCallback_head)(42, 'SetNotificationCallback', ((1, 'pCallback'),)))
    win32more.Graphics.Imaging.IWICBitmapFrameDecode
    return IWICDevelopRaw
def _define_IWICDevelopRawNotificationCallback_head():
    class IWICDevelopRawNotificationCallback(win32more.System.Com.IUnknown_head):
        Guid = Guid('95c75a6e-3e8c-4ec2-85-a8-ae-bc-c5-51-e5-9b')
    return IWICDevelopRawNotificationCallback
def _define_IWICDevelopRawNotificationCallback():
    IWICDevelopRawNotificationCallback = win32more.Graphics.Imaging.IWICDevelopRawNotificationCallback_head
    IWICDevelopRawNotificationCallback.Notify = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(3, 'Notify', ((1, 'NotificationMask'),)))
    win32more.System.Com.IUnknown
    return IWICDevelopRawNotificationCallback
def _define_IWICEnumMetadataItem_head():
    class IWICEnumMetadataItem(win32more.System.Com.IUnknown_head):
        Guid = Guid('dc2bb46d-3f07-481e-86-25-22-0c-4a-ed-bb-33')
    return IWICEnumMetadataItem
def _define_IWICEnumMetadataItem():
    IWICEnumMetadataItem = win32more.Graphics.Imaging.IWICEnumMetadataItem_head
    IWICEnumMetadataItem.Next = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),POINTER(UInt32))(3, 'Next', ((1, 'celt'),(1, 'rgeltSchema'),(1, 'rgeltId'),(1, 'rgeltValue'),(1, 'pceltFetched'),)))
    IWICEnumMetadataItem.Skip = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(4, 'Skip', ((1, 'celt'),)))
    IWICEnumMetadataItem.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(5, 'Reset', ()))
    IWICEnumMetadataItem.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Imaging.IWICEnumMetadataItem_head))(6, 'Clone', ((1, 'ppIEnumMetadataItem'),)))
    win32more.System.Com.IUnknown
    return IWICEnumMetadataItem
def _define_IWICFastMetadataEncoder_head():
    class IWICFastMetadataEncoder(win32more.System.Com.IUnknown_head):
        Guid = Guid('b84e2c09-78c9-4ac4-8b-d3-52-4a-e1-66-3a-2f')
    return IWICFastMetadataEncoder
def _define_IWICFastMetadataEncoder():
    IWICFastMetadataEncoder = win32more.Graphics.Imaging.IWICFastMetadataEncoder_head
    IWICFastMetadataEncoder.Commit = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(3, 'Commit', ()))
    IWICFastMetadataEncoder.GetMetadataQueryWriter = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Imaging.IWICMetadataQueryWriter_head))(4, 'GetMetadataQueryWriter', ((1, 'ppIMetadataQueryWriter'),)))
    win32more.System.Com.IUnknown
    return IWICFastMetadataEncoder
def _define_IWICFormatConverter_head():
    class IWICFormatConverter(win32more.Graphics.Imaging.IWICBitmapSource_head):
        Guid = Guid('00000301-a8f2-4877-ba-0a-fd-2b-66-45-fb-94')
    return IWICFormatConverter
def _define_IWICFormatConverter():
    IWICFormatConverter = win32more.Graphics.Imaging.IWICFormatConverter_head
    IWICFormatConverter.Initialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Imaging.IWICBitmapSource_head,POINTER(Guid),win32more.Graphics.Imaging.WICBitmapDitherType,win32more.Graphics.Imaging.IWICPalette_head,Double,win32more.Graphics.Imaging.WICBitmapPaletteType)(8, 'Initialize', ((1, 'pISource'),(1, 'dstFormat'),(1, 'dither'),(1, 'pIPalette'),(1, 'alphaThresholdPercent'),(1, 'paletteTranslate'),)))
    IWICFormatConverter.CanConvert = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(Guid),POINTER(win32more.Foundation.BOOL))(9, 'CanConvert', ((1, 'srcPixelFormat'),(1, 'dstPixelFormat'),(1, 'pfCanConvert'),)))
    win32more.Graphics.Imaging.IWICBitmapSource
    return IWICFormatConverter
def _define_IWICFormatConverterInfo_head():
    class IWICFormatConverterInfo(win32more.Graphics.Imaging.IWICComponentInfo_head):
        Guid = Guid('9f34fb65-13f4-4f15-bc-57-37-26-b5-e5-3d-9f')
    return IWICFormatConverterInfo
def _define_IWICFormatConverterInfo():
    IWICFormatConverterInfo = win32more.Graphics.Imaging.IWICFormatConverterInfo_head
    IWICFormatConverterInfo.GetPixelFormats = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(Guid),POINTER(UInt32))(11, 'GetPixelFormats', ((1, 'cFormats'),(1, 'pPixelFormatGUIDs'),(1, 'pcActual'),)))
    IWICFormatConverterInfo.CreateInstance = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Imaging.IWICFormatConverter_head))(12, 'CreateInstance', ((1, 'ppIConverter'),)))
    win32more.Graphics.Imaging.IWICComponentInfo
    return IWICFormatConverterInfo
def _define_IWICImagingFactory_head():
    class IWICImagingFactory(win32more.System.Com.IUnknown_head):
        Guid = Guid('ec5ec8a9-c395-4314-9c-77-54-d7-a9-35-ff-70')
    return IWICImagingFactory
def _define_IWICImagingFactory():
    IWICImagingFactory = win32more.Graphics.Imaging.IWICImagingFactory_head
    IWICImagingFactory.CreateDecoderFromFilename = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(Guid),UInt32,win32more.Graphics.Imaging.WICDecodeOptions,POINTER(win32more.Graphics.Imaging.IWICBitmapDecoder_head))(3, 'CreateDecoderFromFilename', ((1, 'wzFilename'),(1, 'pguidVendor'),(1, 'dwDesiredAccess'),(1, 'metadataOptions'),(1, 'ppIDecoder'),)))
    IWICImagingFactory.CreateDecoderFromStream = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IStream_head,POINTER(Guid),win32more.Graphics.Imaging.WICDecodeOptions,POINTER(win32more.Graphics.Imaging.IWICBitmapDecoder_head))(4, 'CreateDecoderFromStream', ((1, 'pIStream'),(1, 'pguidVendor'),(1, 'metadataOptions'),(1, 'ppIDecoder'),)))
    IWICImagingFactory.CreateDecoderFromFileHandle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UIntPtr,POINTER(Guid),win32more.Graphics.Imaging.WICDecodeOptions,POINTER(win32more.Graphics.Imaging.IWICBitmapDecoder_head))(5, 'CreateDecoderFromFileHandle', ((1, 'hFile'),(1, 'pguidVendor'),(1, 'metadataOptions'),(1, 'ppIDecoder'),)))
    IWICImagingFactory.CreateComponentInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(win32more.Graphics.Imaging.IWICComponentInfo_head))(6, 'CreateComponentInfo', ((1, 'clsidComponent'),(1, 'ppIInfo'),)))
    IWICImagingFactory.CreateDecoder = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(Guid),POINTER(win32more.Graphics.Imaging.IWICBitmapDecoder_head))(7, 'CreateDecoder', ((1, 'guidContainerFormat'),(1, 'pguidVendor'),(1, 'ppIDecoder'),)))
    IWICImagingFactory.CreateEncoder = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(Guid),POINTER(win32more.Graphics.Imaging.IWICBitmapEncoder_head))(8, 'CreateEncoder', ((1, 'guidContainerFormat'),(1, 'pguidVendor'),(1, 'ppIEncoder'),)))
    IWICImagingFactory.CreatePalette = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Imaging.IWICPalette_head))(9, 'CreatePalette', ((1, 'ppIPalette'),)))
    IWICImagingFactory.CreateFormatConverter = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Imaging.IWICFormatConverter_head))(10, 'CreateFormatConverter', ((1, 'ppIFormatConverter'),)))
    IWICImagingFactory.CreateBitmapScaler = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Imaging.IWICBitmapScaler_head))(11, 'CreateBitmapScaler', ((1, 'ppIBitmapScaler'),)))
    IWICImagingFactory.CreateBitmapClipper = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Imaging.IWICBitmapClipper_head))(12, 'CreateBitmapClipper', ((1, 'ppIBitmapClipper'),)))
    IWICImagingFactory.CreateBitmapFlipRotator = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Imaging.IWICBitmapFlipRotator_head))(13, 'CreateBitmapFlipRotator', ((1, 'ppIBitmapFlipRotator'),)))
    IWICImagingFactory.CreateStream = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Imaging.IWICStream_head))(14, 'CreateStream', ((1, 'ppIWICStream'),)))
    IWICImagingFactory.CreateColorContext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Imaging.IWICColorContext_head))(15, 'CreateColorContext', ((1, 'ppIWICColorContext'),)))
    IWICImagingFactory.CreateColorTransformer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Imaging.IWICColorTransform_head))(16, 'CreateColorTransformer', ((1, 'ppIWICColorTransform'),)))
    IWICImagingFactory.CreateBitmap = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,POINTER(Guid),win32more.Graphics.Imaging.WICBitmapCreateCacheOption,POINTER(win32more.Graphics.Imaging.IWICBitmap_head))(17, 'CreateBitmap', ((1, 'uiWidth'),(1, 'uiHeight'),(1, 'pixelFormat'),(1, 'option'),(1, 'ppIBitmap'),)))
    IWICImagingFactory.CreateBitmapFromSource = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Imaging.IWICBitmapSource_head,win32more.Graphics.Imaging.WICBitmapCreateCacheOption,POINTER(win32more.Graphics.Imaging.IWICBitmap_head))(18, 'CreateBitmapFromSource', ((1, 'pIBitmapSource'),(1, 'option'),(1, 'ppIBitmap'),)))
    IWICImagingFactory.CreateBitmapFromSourceRect = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Imaging.IWICBitmapSource_head,UInt32,UInt32,UInt32,UInt32,POINTER(win32more.Graphics.Imaging.IWICBitmap_head))(19, 'CreateBitmapFromSourceRect', ((1, 'pIBitmapSource'),(1, 'x'),(1, 'y'),(1, 'width'),(1, 'height'),(1, 'ppIBitmap'),)))
    IWICImagingFactory.CreateBitmapFromMemory = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,POINTER(Guid),UInt32,UInt32,c_char_p_no,POINTER(win32more.Graphics.Imaging.IWICBitmap_head))(20, 'CreateBitmapFromMemory', ((1, 'uiWidth'),(1, 'uiHeight'),(1, 'pixelFormat'),(1, 'cbStride'),(1, 'cbBufferSize'),(1, 'pbBuffer'),(1, 'ppIBitmap'),)))
    IWICImagingFactory.CreateBitmapFromHBITMAP = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Gdi.HBITMAP,win32more.Graphics.Gdi.HPALETTE,win32more.Graphics.Imaging.WICBitmapAlphaChannelOption,POINTER(win32more.Graphics.Imaging.IWICBitmap_head))(21, 'CreateBitmapFromHBITMAP', ((1, 'hBitmap'),(1, 'hPalette'),(1, 'options'),(1, 'ppIBitmap'),)))
    IWICImagingFactory.CreateBitmapFromHICON = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.WindowsAndMessaging.HICON,POINTER(win32more.Graphics.Imaging.IWICBitmap_head))(22, 'CreateBitmapFromHICON', ((1, 'hIcon'),(1, 'ppIBitmap'),)))
    IWICImagingFactory.CreateComponentEnumerator = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,POINTER(win32more.System.Com.IEnumUnknown_head))(23, 'CreateComponentEnumerator', ((1, 'componentTypes'),(1, 'options'),(1, 'ppIEnumUnknown'),)))
    IWICImagingFactory.CreateFastMetadataEncoderFromDecoder = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Imaging.IWICBitmapDecoder_head,POINTER(win32more.Graphics.Imaging.IWICFastMetadataEncoder_head))(24, 'CreateFastMetadataEncoderFromDecoder', ((1, 'pIDecoder'),(1, 'ppIFastEncoder'),)))
    IWICImagingFactory.CreateFastMetadataEncoderFromFrameDecode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Imaging.IWICBitmapFrameDecode_head,POINTER(win32more.Graphics.Imaging.IWICFastMetadataEncoder_head))(25, 'CreateFastMetadataEncoderFromFrameDecode', ((1, 'pIFrameDecoder'),(1, 'ppIFastEncoder'),)))
    IWICImagingFactory.CreateQueryWriter = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(Guid),POINTER(win32more.Graphics.Imaging.IWICMetadataQueryWriter_head))(26, 'CreateQueryWriter', ((1, 'guidMetadataFormat'),(1, 'pguidVendor'),(1, 'ppIQueryWriter'),)))
    IWICImagingFactory.CreateQueryWriterFromReader = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Imaging.IWICMetadataQueryReader_head,POINTER(Guid),POINTER(win32more.Graphics.Imaging.IWICMetadataQueryWriter_head))(27, 'CreateQueryWriterFromReader', ((1, 'pIQueryReader'),(1, 'pguidVendor'),(1, 'ppIQueryWriter'),)))
    win32more.System.Com.IUnknown
    return IWICImagingFactory
def _define_IWICJpegFrameDecode_head():
    class IWICJpegFrameDecode(win32more.System.Com.IUnknown_head):
        Guid = Guid('8939f66e-c46a-4c21-a9-d1-98-b3-27-ce-16-79')
    return IWICJpegFrameDecode
def _define_IWICJpegFrameDecode():
    IWICJpegFrameDecode = win32more.Graphics.Imaging.IWICJpegFrameDecode_head
    IWICJpegFrameDecode.DoesSupportIndexing = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL))(3, 'DoesSupportIndexing', ((1, 'pfIndexingSupported'),)))
    IWICJpegFrameDecode.SetIndexing = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Imaging.WICJpegIndexingOptions,UInt32)(4, 'SetIndexing', ((1, 'options'),(1, 'horizontalIntervalSize'),)))
    IWICJpegFrameDecode.ClearIndexing = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(5, 'ClearIndexing', ()))
    IWICJpegFrameDecode.GetAcHuffmanTable = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,POINTER(win32more.Graphics.Dxgi.Common.DXGI_JPEG_AC_HUFFMAN_TABLE_head))(6, 'GetAcHuffmanTable', ((1, 'scanIndex'),(1, 'tableIndex'),(1, 'pAcHuffmanTable'),)))
    IWICJpegFrameDecode.GetDcHuffmanTable = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,POINTER(win32more.Graphics.Dxgi.Common.DXGI_JPEG_DC_HUFFMAN_TABLE_head))(7, 'GetDcHuffmanTable', ((1, 'scanIndex'),(1, 'tableIndex'),(1, 'pDcHuffmanTable'),)))
    IWICJpegFrameDecode.GetQuantizationTable = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,POINTER(win32more.Graphics.Dxgi.Common.DXGI_JPEG_QUANTIZATION_TABLE_head))(8, 'GetQuantizationTable', ((1, 'scanIndex'),(1, 'tableIndex'),(1, 'pQuantizationTable'),)))
    IWICJpegFrameDecode.GetFrameHeader = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Imaging.WICJpegFrameHeader_head))(9, 'GetFrameHeader', ((1, 'pFrameHeader'),)))
    IWICJpegFrameDecode.GetScanHeader = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Graphics.Imaging.WICJpegScanHeader_head))(10, 'GetScanHeader', ((1, 'scanIndex'),(1, 'pScanHeader'),)))
    IWICJpegFrameDecode.CopyScan = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,UInt32,c_char_p_no,POINTER(UInt32))(11, 'CopyScan', ((1, 'scanIndex'),(1, 'scanOffset'),(1, 'cbScanData'),(1, 'pbScanData'),(1, 'pcbScanDataActual'),)))
    IWICJpegFrameDecode.CopyMinimalStream = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,c_char_p_no,POINTER(UInt32))(12, 'CopyMinimalStream', ((1, 'streamOffset'),(1, 'cbStreamData'),(1, 'pbStreamData'),(1, 'pcbStreamDataActual'),)))
    win32more.System.Com.IUnknown
    return IWICJpegFrameDecode
def _define_IWICJpegFrameEncode_head():
    class IWICJpegFrameEncode(win32more.System.Com.IUnknown_head):
        Guid = Guid('2f0c601f-d2c6-468c-ab-fa-49-49-5d-98-3e-d1')
    return IWICJpegFrameEncode
def _define_IWICJpegFrameEncode():
    IWICJpegFrameEncode = win32more.Graphics.Imaging.IWICJpegFrameEncode_head
    IWICJpegFrameEncode.GetAcHuffmanTable = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,POINTER(win32more.Graphics.Dxgi.Common.DXGI_JPEG_AC_HUFFMAN_TABLE_head))(3, 'GetAcHuffmanTable', ((1, 'scanIndex'),(1, 'tableIndex'),(1, 'pAcHuffmanTable'),)))
    IWICJpegFrameEncode.GetDcHuffmanTable = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,POINTER(win32more.Graphics.Dxgi.Common.DXGI_JPEG_DC_HUFFMAN_TABLE_head))(4, 'GetDcHuffmanTable', ((1, 'scanIndex'),(1, 'tableIndex'),(1, 'pDcHuffmanTable'),)))
    IWICJpegFrameEncode.GetQuantizationTable = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,POINTER(win32more.Graphics.Dxgi.Common.DXGI_JPEG_QUANTIZATION_TABLE_head))(5, 'GetQuantizationTable', ((1, 'scanIndex'),(1, 'tableIndex'),(1, 'pQuantizationTable'),)))
    IWICJpegFrameEncode.WriteScan = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,c_char_p_no)(6, 'WriteScan', ((1, 'cbScanData'),(1, 'pbScanData'),)))
    win32more.System.Com.IUnknown
    return IWICJpegFrameEncode
def _define_IWICMetadataBlockReader_head():
    class IWICMetadataBlockReader(win32more.System.Com.IUnknown_head):
        Guid = Guid('feaa2a8d-b3f3-43e4-b2-5c-d1-de-99-0a-1a-e1')
    return IWICMetadataBlockReader
def _define_IWICMetadataBlockReader():
    IWICMetadataBlockReader = win32more.Graphics.Imaging.IWICMetadataBlockReader_head
    IWICMetadataBlockReader.GetContainerFormat = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid))(3, 'GetContainerFormat', ((1, 'pguidContainerFormat'),)))
    IWICMetadataBlockReader.GetCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(4, 'GetCount', ((1, 'pcCount'),)))
    IWICMetadataBlockReader.GetReaderByIndex = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Graphics.Imaging.IWICMetadataReader_head))(5, 'GetReaderByIndex', ((1, 'nIndex'),(1, 'ppIMetadataReader'),)))
    IWICMetadataBlockReader.GetEnumerator = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IEnumUnknown_head))(6, 'GetEnumerator', ((1, 'ppIEnumMetadata'),)))
    win32more.System.Com.IUnknown
    return IWICMetadataBlockReader
def _define_IWICMetadataBlockWriter_head():
    class IWICMetadataBlockWriter(win32more.Graphics.Imaging.IWICMetadataBlockReader_head):
        Guid = Guid('08fb9676-b444-41e8-8d-be-6a-53-a5-42-bf-f1')
    return IWICMetadataBlockWriter
def _define_IWICMetadataBlockWriter():
    IWICMetadataBlockWriter = win32more.Graphics.Imaging.IWICMetadataBlockWriter_head
    IWICMetadataBlockWriter.InitializeFromBlockReader = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Imaging.IWICMetadataBlockReader_head)(7, 'InitializeFromBlockReader', ((1, 'pIMDBlockReader'),)))
    IWICMetadataBlockWriter.GetWriterByIndex = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Graphics.Imaging.IWICMetadataWriter_head))(8, 'GetWriterByIndex', ((1, 'nIndex'),(1, 'ppIMetadataWriter'),)))
    IWICMetadataBlockWriter.AddWriter = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Imaging.IWICMetadataWriter_head)(9, 'AddWriter', ((1, 'pIMetadataWriter'),)))
    IWICMetadataBlockWriter.SetWriterByIndex = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Graphics.Imaging.IWICMetadataWriter_head)(10, 'SetWriterByIndex', ((1, 'nIndex'),(1, 'pIMetadataWriter'),)))
    IWICMetadataBlockWriter.RemoveWriterByIndex = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(11, 'RemoveWriterByIndex', ((1, 'nIndex'),)))
    win32more.Graphics.Imaging.IWICMetadataBlockReader
    return IWICMetadataBlockWriter
def _define_IWICMetadataHandlerInfo_head():
    class IWICMetadataHandlerInfo(win32more.Graphics.Imaging.IWICComponentInfo_head):
        Guid = Guid('aba958bf-c672-44d1-8d-61-ce-6d-f2-e6-82-c2')
    return IWICMetadataHandlerInfo
def _define_IWICMetadataHandlerInfo():
    IWICMetadataHandlerInfo = win32more.Graphics.Imaging.IWICMetadataHandlerInfo_head
    IWICMetadataHandlerInfo.GetMetadataFormat = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid))(11, 'GetMetadataFormat', ((1, 'pguidMetadataFormat'),)))
    IWICMetadataHandlerInfo.GetContainerFormats = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(Guid),POINTER(UInt32))(12, 'GetContainerFormats', ((1, 'cContainerFormats'),(1, 'pguidContainerFormats'),(1, 'pcchActual'),)))
    IWICMetadataHandlerInfo.GetDeviceManufacturer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Foundation.PWSTR,POINTER(UInt32))(13, 'GetDeviceManufacturer', ((1, 'cchDeviceManufacturer'),(1, 'wzDeviceManufacturer'),(1, 'pcchActual'),)))
    IWICMetadataHandlerInfo.GetDeviceModels = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Foundation.PWSTR,POINTER(UInt32))(14, 'GetDeviceModels', ((1, 'cchDeviceModels'),(1, 'wzDeviceModels'),(1, 'pcchActual'),)))
    IWICMetadataHandlerInfo.DoesRequireFullStream = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL))(15, 'DoesRequireFullStream', ((1, 'pfRequiresFullStream'),)))
    IWICMetadataHandlerInfo.DoesSupportPadding = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL))(16, 'DoesSupportPadding', ((1, 'pfSupportsPadding'),)))
    IWICMetadataHandlerInfo.DoesRequireFixedSize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL))(17, 'DoesRequireFixedSize', ((1, 'pfFixedSize'),)))
    win32more.Graphics.Imaging.IWICComponentInfo
    return IWICMetadataHandlerInfo
def _define_IWICMetadataQueryReader_head():
    class IWICMetadataQueryReader(win32more.System.Com.IUnknown_head):
        Guid = Guid('30989668-e1c9-4597-b3-95-45-8e-ed-b8-08-df')
    return IWICMetadataQueryReader
def _define_IWICMetadataQueryReader():
    IWICMetadataQueryReader = win32more.Graphics.Imaging.IWICMetadataQueryReader_head
    IWICMetadataQueryReader.GetContainerFormat = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid))(3, 'GetContainerFormat', ((1, 'pguidContainerFormat'),)))
    IWICMetadataQueryReader.GetLocation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Foundation.PWSTR,POINTER(UInt32))(4, 'GetLocation', ((1, 'cchMaxLength'),(1, 'wzNamespace'),(1, 'pcchActualLength'),)))
    IWICMetadataQueryReader.GetMetadataByName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head))(5, 'GetMetadataByName', ((1, 'wzName'),(1, 'pvarValue'),)))
    IWICMetadataQueryReader.GetEnumerator = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IEnumString_head))(6, 'GetEnumerator', ((1, 'ppIEnumString'),)))
    win32more.System.Com.IUnknown
    return IWICMetadataQueryReader
def _define_IWICMetadataQueryWriter_head():
    class IWICMetadataQueryWriter(win32more.Graphics.Imaging.IWICMetadataQueryReader_head):
        Guid = Guid('a721791a-0def-4d06-bd-91-21-18-bf-1d-b1-0b')
    return IWICMetadataQueryWriter
def _define_IWICMetadataQueryWriter():
    IWICMetadataQueryWriter = win32more.Graphics.Imaging.IWICMetadataQueryWriter_head
    IWICMetadataQueryWriter.SetMetadataByName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head))(7, 'SetMetadataByName', ((1, 'wzName'),(1, 'pvarValue'),)))
    IWICMetadataQueryWriter.RemoveMetadataByName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR)(8, 'RemoveMetadataByName', ((1, 'wzName'),)))
    win32more.Graphics.Imaging.IWICMetadataQueryReader
    return IWICMetadataQueryWriter
def _define_IWICMetadataReader_head():
    class IWICMetadataReader(win32more.System.Com.IUnknown_head):
        Guid = Guid('9204fe99-d8fc-4fd5-a0-01-95-36-b0-67-a8-99')
    return IWICMetadataReader
def _define_IWICMetadataReader():
    IWICMetadataReader = win32more.Graphics.Imaging.IWICMetadataReader_head
    IWICMetadataReader.GetMetadataFormat = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid))(3, 'GetMetadataFormat', ((1, 'pguidMetadataFormat'),)))
    IWICMetadataReader.GetMetadataHandlerInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Imaging.IWICMetadataHandlerInfo_head))(4, 'GetMetadataHandlerInfo', ((1, 'ppIHandler'),)))
    IWICMetadataReader.GetCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(5, 'GetCount', ((1, 'pcCount'),)))
    IWICMetadataReader.GetValueByIndex = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head))(6, 'GetValueByIndex', ((1, 'nIndex'),(1, 'pvarSchema'),(1, 'pvarId'),(1, 'pvarValue'),)))
    IWICMetadataReader.GetValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head))(7, 'GetValue', ((1, 'pvarSchema'),(1, 'pvarId'),(1, 'pvarValue'),)))
    IWICMetadataReader.GetEnumerator = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Imaging.IWICEnumMetadataItem_head))(8, 'GetEnumerator', ((1, 'ppIEnumMetadata'),)))
    win32more.System.Com.IUnknown
    return IWICMetadataReader
def _define_IWICMetadataReaderInfo_head():
    class IWICMetadataReaderInfo(win32more.Graphics.Imaging.IWICMetadataHandlerInfo_head):
        Guid = Guid('eebf1f5b-07c1-4447-a3-ab-22-ac-af-78-a8-04')
    return IWICMetadataReaderInfo
def _define_IWICMetadataReaderInfo():
    IWICMetadataReaderInfo = win32more.Graphics.Imaging.IWICMetadataReaderInfo_head
    IWICMetadataReaderInfo.GetPatterns = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),UInt32,POINTER(win32more.Graphics.Imaging.WICMetadataPattern_head),POINTER(UInt32),POINTER(UInt32))(18, 'GetPatterns', ((1, 'guidContainerFormat'),(1, 'cbSize'),(1, 'pPattern'),(1, 'pcCount'),(1, 'pcbActual'),)))
    IWICMetadataReaderInfo.MatchesPattern = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),win32more.System.Com.IStream_head,POINTER(win32more.Foundation.BOOL))(19, 'MatchesPattern', ((1, 'guidContainerFormat'),(1, 'pIStream'),(1, 'pfMatches'),)))
    IWICMetadataReaderInfo.CreateInstance = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Imaging.IWICMetadataReader_head))(20, 'CreateInstance', ((1, 'ppIReader'),)))
    win32more.Graphics.Imaging.IWICMetadataHandlerInfo
    return IWICMetadataReaderInfo
def _define_IWICMetadataWriter_head():
    class IWICMetadataWriter(win32more.Graphics.Imaging.IWICMetadataReader_head):
        Guid = Guid('f7836e16-3be0-470b-86-bb-16-0d-0a-ec-d7-de')
    return IWICMetadataWriter
def _define_IWICMetadataWriter():
    IWICMetadataWriter = win32more.Graphics.Imaging.IWICMetadataWriter_head
    IWICMetadataWriter.SetValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head))(9, 'SetValue', ((1, 'pvarSchema'),(1, 'pvarId'),(1, 'pvarValue'),)))
    IWICMetadataWriter.SetValueByIndex = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head))(10, 'SetValueByIndex', ((1, 'nIndex'),(1, 'pvarSchema'),(1, 'pvarId'),(1, 'pvarValue'),)))
    IWICMetadataWriter.RemoveValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head))(11, 'RemoveValue', ((1, 'pvarSchema'),(1, 'pvarId'),)))
    IWICMetadataWriter.RemoveValueByIndex = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(12, 'RemoveValueByIndex', ((1, 'nIndex'),)))
    win32more.Graphics.Imaging.IWICMetadataReader
    return IWICMetadataWriter
def _define_IWICMetadataWriterInfo_head():
    class IWICMetadataWriterInfo(win32more.Graphics.Imaging.IWICMetadataHandlerInfo_head):
        Guid = Guid('b22e3fba-3925-4323-b5-c1-9e-bf-c4-30-f2-36')
    return IWICMetadataWriterInfo
def _define_IWICMetadataWriterInfo():
    IWICMetadataWriterInfo = win32more.Graphics.Imaging.IWICMetadataWriterInfo_head
    IWICMetadataWriterInfo.GetHeader = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),UInt32,POINTER(win32more.Graphics.Imaging.WICMetadataHeader_head),POINTER(UInt32))(18, 'GetHeader', ((1, 'guidContainerFormat'),(1, 'cbSize'),(1, 'pHeader'),(1, 'pcbActual'),)))
    IWICMetadataWriterInfo.CreateInstance = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Imaging.IWICMetadataWriter_head))(19, 'CreateInstance', ((1, 'ppIWriter'),)))
    win32more.Graphics.Imaging.IWICMetadataHandlerInfo
    return IWICMetadataWriterInfo
def _define_IWICPalette_head():
    class IWICPalette(win32more.System.Com.IUnknown_head):
        Guid = Guid('00000040-a8f2-4877-ba-0a-fd-2b-66-45-fb-94')
    return IWICPalette
def _define_IWICPalette():
    IWICPalette = win32more.Graphics.Imaging.IWICPalette_head
    IWICPalette.InitializePredefined = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Imaging.WICBitmapPaletteType,win32more.Foundation.BOOL)(3, 'InitializePredefined', ((1, 'ePaletteType'),(1, 'fAddTransparentColor'),)))
    IWICPalette.InitializeCustom = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32),UInt32)(4, 'InitializeCustom', ((1, 'pColors'),(1, 'cCount'),)))
    IWICPalette.InitializeFromBitmap = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Imaging.IWICBitmapSource_head,UInt32,win32more.Foundation.BOOL)(5, 'InitializeFromBitmap', ((1, 'pISurface'),(1, 'cCount'),(1, 'fAddTransparentColor'),)))
    IWICPalette.InitializeFromPalette = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Imaging.IWICPalette_head)(6, 'InitializeFromPalette', ((1, 'pIPalette'),)))
    IWICPalette.GetType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Imaging.WICBitmapPaletteType))(7, 'GetType', ((1, 'pePaletteType'),)))
    IWICPalette.GetColorCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(8, 'GetColorCount', ((1, 'pcCount'),)))
    IWICPalette.GetColors = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(UInt32),POINTER(UInt32))(9, 'GetColors', ((1, 'cCount'),(1, 'pColors'),(1, 'pcActualColors'),)))
    IWICPalette.IsBlackWhite = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL))(10, 'IsBlackWhite', ((1, 'pfIsBlackWhite'),)))
    IWICPalette.IsGrayscale = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL))(11, 'IsGrayscale', ((1, 'pfIsGrayscale'),)))
    IWICPalette.HasAlpha = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL))(12, 'HasAlpha', ((1, 'pfHasAlpha'),)))
    win32more.System.Com.IUnknown
    return IWICPalette
def _define_IWICPersistStream_head():
    class IWICPersistStream(win32more.System.Com.IPersistStream_head):
        Guid = Guid('00675040-6908-45f8-86-a3-49-c7-df-d6-d9-ad')
    return IWICPersistStream
def _define_IWICPersistStream():
    IWICPersistStream = win32more.Graphics.Imaging.IWICPersistStream_head
    IWICPersistStream.LoadEx = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IStream_head,POINTER(Guid),UInt32)(8, 'LoadEx', ((1, 'pIStream'),(1, 'pguidPreferredVendor'),(1, 'dwPersistOptions'),)))
    IWICPersistStream.SaveEx = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IStream_head,UInt32,win32more.Foundation.BOOL)(9, 'SaveEx', ((1, 'pIStream'),(1, 'dwPersistOptions'),(1, 'fClearDirty'),)))
    win32more.System.Com.IPersistStream
    return IWICPersistStream
def _define_IWICPixelFormatInfo_head():
    class IWICPixelFormatInfo(win32more.Graphics.Imaging.IWICComponentInfo_head):
        Guid = Guid('e8eda601-3d48-431a-ab-44-69-05-9b-e8-8b-be')
    return IWICPixelFormatInfo
def _define_IWICPixelFormatInfo():
    IWICPixelFormatInfo = win32more.Graphics.Imaging.IWICPixelFormatInfo_head
    IWICPixelFormatInfo.GetFormatGUID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid))(11, 'GetFormatGUID', ((1, 'pFormat'),)))
    IWICPixelFormatInfo.GetColorContext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Imaging.IWICColorContext_head))(12, 'GetColorContext', ((1, 'ppIColorContext'),)))
    IWICPixelFormatInfo.GetBitsPerPixel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(13, 'GetBitsPerPixel', ((1, 'puiBitsPerPixel'),)))
    IWICPixelFormatInfo.GetChannelCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(14, 'GetChannelCount', ((1, 'puiChannelCount'),)))
    IWICPixelFormatInfo.GetChannelMask = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,c_char_p_no,POINTER(UInt32))(15, 'GetChannelMask', ((1, 'uiChannelIndex'),(1, 'cbMaskBuffer'),(1, 'pbMaskBuffer'),(1, 'pcbActual'),)))
    win32more.Graphics.Imaging.IWICComponentInfo
    return IWICPixelFormatInfo
def _define_IWICPixelFormatInfo2_head():
    class IWICPixelFormatInfo2(win32more.Graphics.Imaging.IWICPixelFormatInfo_head):
        Guid = Guid('a9db33a2-af5f-43c7-b6-79-74-f5-98-4b-5a-a4')
    return IWICPixelFormatInfo2
def _define_IWICPixelFormatInfo2():
    IWICPixelFormatInfo2 = win32more.Graphics.Imaging.IWICPixelFormatInfo2_head
    IWICPixelFormatInfo2.SupportsTransparency = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL))(16, 'SupportsTransparency', ((1, 'pfSupportsTransparency'),)))
    IWICPixelFormatInfo2.GetNumericRepresentation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Imaging.WICPixelFormatNumericRepresentation))(17, 'GetNumericRepresentation', ((1, 'pNumericRepresentation'),)))
    win32more.Graphics.Imaging.IWICPixelFormatInfo
    return IWICPixelFormatInfo2
def _define_IWICPlanarBitmapFrameEncode_head():
    class IWICPlanarBitmapFrameEncode(win32more.System.Com.IUnknown_head):
        Guid = Guid('f928b7b8-2221-40c1-b7-2e-7e-82-f1-97-4d-1a')
    return IWICPlanarBitmapFrameEncode
def _define_IWICPlanarBitmapFrameEncode():
    IWICPlanarBitmapFrameEncode = win32more.Graphics.Imaging.IWICPlanarBitmapFrameEncode_head
    IWICPlanarBitmapFrameEncode.WritePixels = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Graphics.Imaging.WICBitmapPlane_head),UInt32)(3, 'WritePixels', ((1, 'lineCount'),(1, 'pPlanes'),(1, 'cPlanes'),)))
    IWICPlanarBitmapFrameEncode.WriteSource = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Imaging.IWICBitmapSource_head),UInt32,POINTER(win32more.Graphics.Imaging.WICRect_head))(4, 'WriteSource', ((1, 'ppPlanes'),(1, 'cPlanes'),(1, 'prcSource'),)))
    win32more.System.Com.IUnknown
    return IWICPlanarBitmapFrameEncode
def _define_IWICPlanarBitmapSourceTransform_head():
    class IWICPlanarBitmapSourceTransform(win32more.System.Com.IUnknown_head):
        Guid = Guid('3aff9cce-be95-4303-b9-27-e7-d1-6f-f4-a6-13')
    return IWICPlanarBitmapSourceTransform
def _define_IWICPlanarBitmapSourceTransform():
    IWICPlanarBitmapSourceTransform = win32more.Graphics.Imaging.IWICPlanarBitmapSourceTransform_head
    IWICPlanarBitmapSourceTransform.DoesSupportTransform = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32),POINTER(UInt32),win32more.Graphics.Imaging.WICBitmapTransformOptions,win32more.Graphics.Imaging.WICPlanarOptions,POINTER(Guid),POINTER(win32more.Graphics.Imaging.WICBitmapPlaneDescription_head),UInt32,POINTER(win32more.Foundation.BOOL))(3, 'DoesSupportTransform', ((1, 'puiWidth'),(1, 'puiHeight'),(1, 'dstTransform'),(1, 'dstPlanarOptions'),(1, 'pguidDstFormats'),(1, 'pPlaneDescriptions'),(1, 'cPlanes'),(1, 'pfIsSupported'),)))
    IWICPlanarBitmapSourceTransform.CopyPixels = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Imaging.WICRect_head),UInt32,UInt32,win32more.Graphics.Imaging.WICBitmapTransformOptions,win32more.Graphics.Imaging.WICPlanarOptions,POINTER(win32more.Graphics.Imaging.WICBitmapPlane_head),UInt32)(4, 'CopyPixels', ((1, 'prcSource'),(1, 'uiWidth'),(1, 'uiHeight'),(1, 'dstTransform'),(1, 'dstPlanarOptions'),(1, 'pDstPlanes'),(1, 'cPlanes'),)))
    win32more.System.Com.IUnknown
    return IWICPlanarBitmapSourceTransform
def _define_IWICPlanarFormatConverter_head():
    class IWICPlanarFormatConverter(win32more.Graphics.Imaging.IWICBitmapSource_head):
        Guid = Guid('bebee9cb-83b0-4dcc-81-32-b0-aa-a5-5e-ac-96')
    return IWICPlanarFormatConverter
def _define_IWICPlanarFormatConverter():
    IWICPlanarFormatConverter = win32more.Graphics.Imaging.IWICPlanarFormatConverter_head
    IWICPlanarFormatConverter.Initialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Imaging.IWICBitmapSource_head),UInt32,POINTER(Guid),win32more.Graphics.Imaging.WICBitmapDitherType,win32more.Graphics.Imaging.IWICPalette_head,Double,win32more.Graphics.Imaging.WICBitmapPaletteType)(8, 'Initialize', ((1, 'ppPlanes'),(1, 'cPlanes'),(1, 'dstFormat'),(1, 'dither'),(1, 'pIPalette'),(1, 'alphaThresholdPercent'),(1, 'paletteTranslate'),)))
    IWICPlanarFormatConverter.CanConvert = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),UInt32,POINTER(Guid),POINTER(win32more.Foundation.BOOL))(9, 'CanConvert', ((1, 'pSrcPixelFormats'),(1, 'cSrcPlanes'),(1, 'dstPixelFormat'),(1, 'pfCanConvert'),)))
    win32more.Graphics.Imaging.IWICBitmapSource
    return IWICPlanarFormatConverter
def _define_IWICProgressCallback_head():
    class IWICProgressCallback(win32more.System.Com.IUnknown_head):
        Guid = Guid('4776f9cd-9517-45fa-bf-24-e8-9c-5e-c5-c6-0c')
    return IWICProgressCallback
def _define_IWICProgressCallback():
    IWICProgressCallback = win32more.Graphics.Imaging.IWICProgressCallback_head
    IWICProgressCallback.Notify = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Graphics.Imaging.WICProgressOperation,Double)(3, 'Notify', ((1, 'uFrameNum'),(1, 'operation'),(1, 'dblProgress'),)))
    win32more.System.Com.IUnknown
    return IWICProgressCallback
def _define_IWICProgressiveLevelControl_head():
    class IWICProgressiveLevelControl(win32more.System.Com.IUnknown_head):
        Guid = Guid('daac296f-7aa5-4dbf-8d-15-22-5c-59-76-f8-91')
    return IWICProgressiveLevelControl
def _define_IWICProgressiveLevelControl():
    IWICProgressiveLevelControl = win32more.Graphics.Imaging.IWICProgressiveLevelControl_head
    IWICProgressiveLevelControl.GetLevelCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(3, 'GetLevelCount', ((1, 'pcLevels'),)))
    IWICProgressiveLevelControl.GetCurrentLevel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(4, 'GetCurrentLevel', ((1, 'pnLevel'),)))
    IWICProgressiveLevelControl.SetCurrentLevel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(5, 'SetCurrentLevel', ((1, 'nLevel'),)))
    win32more.System.Com.IUnknown
    return IWICProgressiveLevelControl
def _define_IWICStream_head():
    class IWICStream(win32more.System.Com.IStream_head):
        Guid = Guid('135ff860-22b7-4ddf-b0-f6-21-8f-4f-29-9a-43')
    return IWICStream
def _define_IWICStream():
    IWICStream = win32more.Graphics.Imaging.IWICStream_head
    IWICStream.InitializeFromIStream = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IStream_head)(14, 'InitializeFromIStream', ((1, 'pIStream'),)))
    IWICStream.InitializeFromFilename = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32)(15, 'InitializeFromFilename', ((1, 'wzFileName'),(1, 'dwDesiredAccess'),)))
    IWICStream.InitializeFromMemory = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_char_p_no,UInt32)(16, 'InitializeFromMemory', ((1, 'pbBuffer'),(1, 'cbBufferSize'),)))
    IWICStream.InitializeFromIStreamRegion = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IStream_head,win32more.Foundation.ULARGE_INTEGER,win32more.Foundation.ULARGE_INTEGER)(17, 'InitializeFromIStreamRegion', ((1, 'pIStream'),(1, 'ulOffset'),(1, 'ulMaxSize'),)))
    win32more.System.Com.IStream
    return IWICStream
def _define_IWICStreamProvider_head():
    class IWICStreamProvider(win32more.System.Com.IUnknown_head):
        Guid = Guid('449494bc-b468-4927-96-d7-ba-90-d3-1a-b5-05')
    return IWICStreamProvider
def _define_IWICStreamProvider():
    IWICStreamProvider = win32more.Graphics.Imaging.IWICStreamProvider_head
    IWICStreamProvider.GetStream = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IStream_head))(3, 'GetStream', ((1, 'ppIStream'),)))
    IWICStreamProvider.GetPersistOptions = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(4, 'GetPersistOptions', ((1, 'pdwPersistOptions'),)))
    IWICStreamProvider.GetPreferredVendorGUID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid))(5, 'GetPreferredVendorGUID', ((1, 'pguidPreferredVendor'),)))
    IWICStreamProvider.RefreshStream = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(6, 'RefreshStream', ()))
    win32more.System.Com.IUnknown
    return IWICStreamProvider
def _define_PFNProgressNotification():
    return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,UInt32,win32more.Graphics.Imaging.WICProgressOperation,Double)
WIC8BIMIptcDigestProperties = UInt32
WIC8BIMIptcDigestProperties_WIC8BIMIptcDigestPString = 1
WIC8BIMIptcDigestProperties_WIC8BIMIptcDigestIptcDigest = 2
WIC8BIMIptcDigestProperties_WIC8BIMIptcDigestProperties_FORCE_DWORD = 2147483647
WIC8BIMIptcProperties = UInt32
WIC8BIMIptcProperties_WIC8BIMIptcPString = 0
WIC8BIMIptcProperties_WIC8BIMIptcEmbeddedIPTC = 1
WIC8BIMIptcProperties_WIC8BIMIptcProperties_FORCE_DWORD = 2147483647
WIC8BIMResolutionInfoProperties = UInt32
WIC8BIMResolutionInfoProperties_WIC8BIMResolutionInfoPString = 1
WIC8BIMResolutionInfoProperties_WIC8BIMResolutionInfoHResolution = 2
WIC8BIMResolutionInfoProperties_WIC8BIMResolutionInfoHResolutionUnit = 3
WIC8BIMResolutionInfoProperties_WIC8BIMResolutionInfoWidthUnit = 4
WIC8BIMResolutionInfoProperties_WIC8BIMResolutionInfoVResolution = 5
WIC8BIMResolutionInfoProperties_WIC8BIMResolutionInfoVResolutionUnit = 6
WIC8BIMResolutionInfoProperties_WIC8BIMResolutionInfoHeightUnit = 7
WIC8BIMResolutionInfoProperties_WIC8BIMResolutionInfoProperties_FORCE_DWORD = 2147483647
WICBitmapAlphaChannelOption = Int32
WICBitmapAlphaChannelOption_WICBitmapUseAlpha = 0
WICBitmapAlphaChannelOption_WICBitmapUsePremultipliedAlpha = 1
WICBitmapAlphaChannelOption_WICBitmapIgnoreAlpha = 2
WICBitmapAlphaChannelOption_WICBITMAPALPHACHANNELOPTIONS_FORCE_DWORD = 2147483647
WICBitmapCreateCacheOption = Int32
WICBitmapCreateCacheOption_WICBitmapNoCache = 0
WICBitmapCreateCacheOption_WICBitmapCacheOnDemand = 1
WICBitmapCreateCacheOption_WICBitmapCacheOnLoad = 2
WICBitmapCreateCacheOption_WICBITMAPCREATECACHEOPTION_FORCE_DWORD = 2147483647
WICBitmapDecoderCapabilities = Int32
WICBitmapDecoderCapabilities_WICBitmapDecoderCapabilitySameEncoder = 1
WICBitmapDecoderCapabilities_WICBitmapDecoderCapabilityCanDecodeAllImages = 2
WICBitmapDecoderCapabilities_WICBitmapDecoderCapabilityCanDecodeSomeImages = 4
WICBitmapDecoderCapabilities_WICBitmapDecoderCapabilityCanEnumerateMetadata = 8
WICBitmapDecoderCapabilities_WICBitmapDecoderCapabilityCanDecodeThumbnail = 16
WICBitmapDecoderCapabilities_WICBITMAPDECODERCAPABILITIES_FORCE_DWORD = 2147483647
WICBitmapDitherType = Int32
WICBitmapDitherType_WICBitmapDitherTypeNone = 0
WICBitmapDitherType_WICBitmapDitherTypeSolid = 0
WICBitmapDitherType_WICBitmapDitherTypeOrdered4x4 = 1
WICBitmapDitherType_WICBitmapDitherTypeOrdered8x8 = 2
WICBitmapDitherType_WICBitmapDitherTypeOrdered16x16 = 3
WICBitmapDitherType_WICBitmapDitherTypeSpiral4x4 = 4
WICBitmapDitherType_WICBitmapDitherTypeSpiral8x8 = 5
WICBitmapDitherType_WICBitmapDitherTypeDualSpiral4x4 = 6
WICBitmapDitherType_WICBitmapDitherTypeDualSpiral8x8 = 7
WICBitmapDitherType_WICBitmapDitherTypeErrorDiffusion = 8
WICBitmapDitherType_WICBITMAPDITHERTYPE_FORCE_DWORD = 2147483647
WICBitmapEncoderCacheOption = Int32
WICBitmapEncoderCacheOption_WICBitmapEncoderCacheInMemory = 0
WICBitmapEncoderCacheOption_WICBitmapEncoderCacheTempFile = 1
WICBitmapEncoderCacheOption_WICBitmapEncoderNoCache = 2
WICBitmapEncoderCacheOption_WICBITMAPENCODERCACHEOPTION_FORCE_DWORD = 2147483647
WICBitmapInterpolationMode = Int32
WICBitmapInterpolationMode_WICBitmapInterpolationModeNearestNeighbor = 0
WICBitmapInterpolationMode_WICBitmapInterpolationModeLinear = 1
WICBitmapInterpolationMode_WICBitmapInterpolationModeCubic = 2
WICBitmapInterpolationMode_WICBitmapInterpolationModeFant = 3
WICBitmapInterpolationMode_WICBitmapInterpolationModeHighQualityCubic = 4
WICBitmapInterpolationMode_WICBITMAPINTERPOLATIONMODE_FORCE_DWORD = 2147483647
WICBitmapLockFlags = Int32
WICBitmapLockFlags_WICBitmapLockRead = 1
WICBitmapLockFlags_WICBitmapLockWrite = 2
WICBitmapLockFlags_WICBITMAPLOCKFLAGS_FORCE_DWORD = 2147483647
WICBitmapPaletteType = Int32
WICBitmapPaletteType_WICBitmapPaletteTypeCustom = 0
WICBitmapPaletteType_WICBitmapPaletteTypeMedianCut = 1
WICBitmapPaletteType_WICBitmapPaletteTypeFixedBW = 2
WICBitmapPaletteType_WICBitmapPaletteTypeFixedHalftone8 = 3
WICBitmapPaletteType_WICBitmapPaletteTypeFixedHalftone27 = 4
WICBitmapPaletteType_WICBitmapPaletteTypeFixedHalftone64 = 5
WICBitmapPaletteType_WICBitmapPaletteTypeFixedHalftone125 = 6
WICBitmapPaletteType_WICBitmapPaletteTypeFixedHalftone216 = 7
WICBitmapPaletteType_WICBitmapPaletteTypeFixedWebPalette = 7
WICBitmapPaletteType_WICBitmapPaletteTypeFixedHalftone252 = 8
WICBitmapPaletteType_WICBitmapPaletteTypeFixedHalftone256 = 9
WICBitmapPaletteType_WICBitmapPaletteTypeFixedGray4 = 10
WICBitmapPaletteType_WICBitmapPaletteTypeFixedGray16 = 11
WICBitmapPaletteType_WICBitmapPaletteTypeFixedGray256 = 12
WICBitmapPaletteType_WICBITMAPPALETTETYPE_FORCE_DWORD = 2147483647
def _define_WICBitmapPattern_head():
    class WICBitmapPattern(Structure):
        pass
    return WICBitmapPattern
def _define_WICBitmapPattern():
    WICBitmapPattern = win32more.Graphics.Imaging.WICBitmapPattern_head
    WICBitmapPattern._fields_ = [
        ('Position', win32more.Foundation.ULARGE_INTEGER),
        ('Length', UInt32),
        ('Pattern', c_char_p_no),
        ('Mask', c_char_p_no),
        ('EndOfStream', win32more.Foundation.BOOL),
    ]
    return WICBitmapPattern
def _define_WICBitmapPlane_head():
    class WICBitmapPlane(Structure):
        pass
    return WICBitmapPlane
def _define_WICBitmapPlane():
    WICBitmapPlane = win32more.Graphics.Imaging.WICBitmapPlane_head
    WICBitmapPlane._fields_ = [
        ('Format', Guid),
        ('pbBuffer', c_char_p_no),
        ('cbStride', UInt32),
        ('cbBufferSize', UInt32),
    ]
    return WICBitmapPlane
def _define_WICBitmapPlaneDescription_head():
    class WICBitmapPlaneDescription(Structure):
        pass
    return WICBitmapPlaneDescription
def _define_WICBitmapPlaneDescription():
    WICBitmapPlaneDescription = win32more.Graphics.Imaging.WICBitmapPlaneDescription_head
    WICBitmapPlaneDescription._fields_ = [
        ('Format', Guid),
        ('Width', UInt32),
        ('Height', UInt32),
    ]
    return WICBitmapPlaneDescription
WICBitmapTransformOptions = Int32
WICBitmapTransformOptions_WICBitmapTransformRotate0 = 0
WICBitmapTransformOptions_WICBitmapTransformRotate90 = 1
WICBitmapTransformOptions_WICBitmapTransformRotate180 = 2
WICBitmapTransformOptions_WICBitmapTransformRotate270 = 3
WICBitmapTransformOptions_WICBitmapTransformFlipHorizontal = 8
WICBitmapTransformOptions_WICBitmapTransformFlipVertical = 16
WICBitmapTransformOptions_WICBITMAPTRANSFORMOPTIONS_FORCE_DWORD = 2147483647
WICColorContextType = Int32
WICColorContextType_WICColorContextUninitialized = 0
WICColorContextType_WICColorContextProfile = 1
WICColorContextType_WICColorContextExifColorSpace = 2
WICComponentEnumerateOptions = Int32
WICComponentEnumerateOptions_WICComponentEnumerateDefault = 0
WICComponentEnumerateOptions_WICComponentEnumerateRefresh = 1
WICComponentEnumerateOptions_WICComponentEnumerateDisabled = -2147483648
WICComponentEnumerateOptions_WICComponentEnumerateUnsigned = 1073741824
WICComponentEnumerateOptions_WICComponentEnumerateBuiltInOnly = 536870912
WICComponentEnumerateOptions_WICCOMPONENTENUMERATEOPTIONS_FORCE_DWORD = 2147483647
WICComponentSigning = Int32
WICComponentSigning_WICComponentSigned = 1
WICComponentSigning_WICComponentUnsigned = 2
WICComponentSigning_WICComponentSafe = 4
WICComponentSigning_WICComponentDisabled = -2147483648
WICComponentSigning_WICCOMPONENTSIGNING_FORCE_DWORD = 2147483647
WICComponentType = Int32
WICComponentType_WICDecoder = 1
WICComponentType_WICEncoder = 2
WICComponentType_WICPixelFormatConverter = 4
WICComponentType_WICMetadataReader = 8
WICComponentType_WICMetadataWriter = 16
WICComponentType_WICPixelFormat = 32
WICComponentType_WICAllComponents = 63
WICComponentType_WICCOMPONENTTYPE_FORCE_DWORD = 2147483647
WICDdsAlphaMode = Int32
WICDdsAlphaMode_WICDdsAlphaModeUnknown = 0
WICDdsAlphaMode_WICDdsAlphaModeStraight = 1
WICDdsAlphaMode_WICDdsAlphaModePremultiplied = 2
WICDdsAlphaMode_WICDdsAlphaModeOpaque = 3
WICDdsAlphaMode_WICDdsAlphaModeCustom = 4
WICDdsAlphaMode_WICDDSALPHAMODE_FORCE_DWORD = 2147483647
WICDdsDimension = Int32
WICDdsDimension_WICDdsTexture1D = 0
WICDdsDimension_WICDdsTexture2D = 1
WICDdsDimension_WICDdsTexture3D = 2
WICDdsDimension_WICDdsTextureCube = 3
WICDdsDimension_WICDDSTEXTURE_FORCE_DWORD = 2147483647
def _define_WICDdsFormatInfo_head():
    class WICDdsFormatInfo(Structure):
        pass
    return WICDdsFormatInfo
def _define_WICDdsFormatInfo():
    WICDdsFormatInfo = win32more.Graphics.Imaging.WICDdsFormatInfo_head
    WICDdsFormatInfo._fields_ = [
        ('DxgiFormat', win32more.Graphics.Dxgi.Common.DXGI_FORMAT),
        ('BytesPerBlock', UInt32),
        ('BlockWidth', UInt32),
        ('BlockHeight', UInt32),
    ]
    return WICDdsFormatInfo
def _define_WICDdsParameters_head():
    class WICDdsParameters(Structure):
        pass
    return WICDdsParameters
def _define_WICDdsParameters():
    WICDdsParameters = win32more.Graphics.Imaging.WICDdsParameters_head
    WICDdsParameters._fields_ = [
        ('Width', UInt32),
        ('Height', UInt32),
        ('Depth', UInt32),
        ('MipLevels', UInt32),
        ('ArraySize', UInt32),
        ('DxgiFormat', win32more.Graphics.Dxgi.Common.DXGI_FORMAT),
        ('Dimension', win32more.Graphics.Imaging.WICDdsDimension),
        ('AlphaMode', win32more.Graphics.Imaging.WICDdsAlphaMode),
    ]
    return WICDdsParameters
WICDecodeOptions = Int32
WICDecodeOptions_WICDecodeMetadataCacheOnDemand = 0
WICDecodeOptions_WICDecodeMetadataCacheOnLoad = 1
WICDecodeOptions_WICMETADATACACHEOPTION_FORCE_DWORD = 2147483647
WICGifApplicationExtensionProperties = UInt32
WICGifApplicationExtensionProperties_WICGifApplicationExtensionApplication = 1
WICGifApplicationExtensionProperties_WICGifApplicationExtensionData = 2
WICGifApplicationExtensionProperties_WICGifApplicationExtensionProperties_FORCE_DWORD = 2147483647
WICGifCommentExtensionProperties = UInt32
WICGifCommentExtensionProperties_WICGifCommentExtensionText = 1
WICGifCommentExtensionProperties_WICGifCommentExtensionProperties_FORCE_DWORD = 2147483647
WICGifGraphicControlExtensionProperties = UInt32
WICGifGraphicControlExtensionProperties_WICGifGraphicControlExtensionDisposal = 1
WICGifGraphicControlExtensionProperties_WICGifGraphicControlExtensionUserInputFlag = 2
WICGifGraphicControlExtensionProperties_WICGifGraphicControlExtensionTransparencyFlag = 3
WICGifGraphicControlExtensionProperties_WICGifGraphicControlExtensionDelay = 4
WICGifGraphicControlExtensionProperties_WICGifGraphicControlExtensionTransparentColorIndex = 5
WICGifGraphicControlExtensionProperties_WICGifGraphicControlExtensionProperties_FORCE_DWORD = 2147483647
WICGifImageDescriptorProperties = UInt32
WICGifImageDescriptorProperties_WICGifImageDescriptorLeft = 1
WICGifImageDescriptorProperties_WICGifImageDescriptorTop = 2
WICGifImageDescriptorProperties_WICGifImageDescriptorWidth = 3
WICGifImageDescriptorProperties_WICGifImageDescriptorHeight = 4
WICGifImageDescriptorProperties_WICGifImageDescriptorLocalColorTableFlag = 5
WICGifImageDescriptorProperties_WICGifImageDescriptorInterlaceFlag = 6
WICGifImageDescriptorProperties_WICGifImageDescriptorSortFlag = 7
WICGifImageDescriptorProperties_WICGifImageDescriptorLocalColorTableSize = 8
WICGifImageDescriptorProperties_WICGifImageDescriptorProperties_FORCE_DWORD = 2147483647
WICGifLogicalScreenDescriptorProperties = UInt32
WICGifLogicalScreenDescriptorProperties_WICGifLogicalScreenSignature = 1
WICGifLogicalScreenDescriptorProperties_WICGifLogicalScreenDescriptorWidth = 2
WICGifLogicalScreenDescriptorProperties_WICGifLogicalScreenDescriptorHeight = 3
WICGifLogicalScreenDescriptorProperties_WICGifLogicalScreenDescriptorGlobalColorTableFlag = 4
WICGifLogicalScreenDescriptorProperties_WICGifLogicalScreenDescriptorColorResolution = 5
WICGifLogicalScreenDescriptorProperties_WICGifLogicalScreenDescriptorSortFlag = 6
WICGifLogicalScreenDescriptorProperties_WICGifLogicalScreenDescriptorGlobalColorTableSize = 7
WICGifLogicalScreenDescriptorProperties_WICGifLogicalScreenDescriptorBackgroundColorIndex = 8
WICGifLogicalScreenDescriptorProperties_WICGifLogicalScreenDescriptorPixelAspectRatio = 9
WICGifLogicalScreenDescriptorProperties_WICGifLogicalScreenDescriptorProperties_FORCE_DWORD = 2147483647
WICHeifHdrProperties = UInt32
WICHeifHdrProperties_WICHeifHdrMaximumLuminanceLevel = 1
WICHeifHdrProperties_WICHeifHdrMaximumFrameAverageLuminanceLevel = 2
WICHeifHdrProperties_WICHeifHdrMinimumMasteringDisplayLuminanceLevel = 3
WICHeifHdrProperties_WICHeifHdrMaximumMasteringDisplayLuminanceLevel = 4
WICHeifHdrProperties_WICHeifHdrCustomVideoPrimaries = 5
WICHeifHdrProperties_WICHeifHdrProperties_FORCE_DWORD = 2147483647
WICHeifProperties = UInt32
WICHeifProperties_WICHeifOrientation = 1
WICHeifProperties_WICHeifProperties_FORCE_DWORD = 2147483647
def _define_WICImageParameters_head():
    class WICImageParameters(Structure):
        pass
    return WICImageParameters
def _define_WICImageParameters():
    WICImageParameters = win32more.Graphics.Imaging.WICImageParameters_head
    WICImageParameters._fields_ = [
        ('PixelFormat', win32more.Graphics.Direct2D.Common.D2D1_PIXEL_FORMAT),
        ('DpiX', Single),
        ('DpiY', Single),
        ('Top', Single),
        ('Left', Single),
        ('PixelWidth', UInt32),
        ('PixelHeight', UInt32),
    ]
    return WICImageParameters
WICJpegChrominanceProperties = UInt32
WICJpegChrominanceProperties_WICJpegChrominanceTable = 1
WICJpegChrominanceProperties_WICJpegChrominanceProperties_FORCE_DWORD = 2147483647
WICJpegCommentProperties = UInt32
WICJpegCommentProperties_WICJpegCommentText = 1
WICJpegCommentProperties_WICJpegCommentProperties_FORCE_DWORD = 2147483647
def _define_WICJpegFrameHeader_head():
    class WICJpegFrameHeader(Structure):
        pass
    return WICJpegFrameHeader
def _define_WICJpegFrameHeader():
    WICJpegFrameHeader = win32more.Graphics.Imaging.WICJpegFrameHeader_head
    WICJpegFrameHeader._fields_ = [
        ('Width', UInt32),
        ('Height', UInt32),
        ('TransferMatrix', win32more.Graphics.Imaging.WICJpegTransferMatrix),
        ('ScanType', win32more.Graphics.Imaging.WICJpegScanType),
        ('cComponents', UInt32),
        ('ComponentIdentifiers', UInt32),
        ('SampleFactors', UInt32),
        ('QuantizationTableIndices', UInt32),
    ]
    return WICJpegFrameHeader
WICJpegIndexingOptions = UInt32
WICJpegIndexingOptions_WICJpegIndexingOptionsGenerateOnDemand = 0
WICJpegIndexingOptions_WICJpegIndexingOptionsGenerateOnLoad = 1
WICJpegIndexingOptions_WICJpegIndexingOptions_FORCE_DWORD = 2147483647
WICJpegLuminanceProperties = UInt32
WICJpegLuminanceProperties_WICJpegLuminanceTable = 1
WICJpegLuminanceProperties_WICJpegLuminanceProperties_FORCE_DWORD = 2147483647
def _define_WICJpegScanHeader_head():
    class WICJpegScanHeader(Structure):
        pass
    return WICJpegScanHeader
def _define_WICJpegScanHeader():
    WICJpegScanHeader = win32more.Graphics.Imaging.WICJpegScanHeader_head
    WICJpegScanHeader._fields_ = [
        ('cComponents', UInt32),
        ('RestartInterval', UInt32),
        ('ComponentSelectors', UInt32),
        ('HuffmanTableIndices', UInt32),
        ('StartSpectralSelection', Byte),
        ('EndSpectralSelection', Byte),
        ('SuccessiveApproximationHigh', Byte),
        ('SuccessiveApproximationLow', Byte),
    ]
    return WICJpegScanHeader
WICJpegScanType = UInt32
WICJpegScanType_WICJpegScanTypeInterleaved = 0
WICJpegScanType_WICJpegScanTypePlanarComponents = 1
WICJpegScanType_WICJpegScanTypeProgressive = 2
WICJpegScanType_WICJpegScanType_FORCE_DWORD = 2147483647
WICJpegTransferMatrix = UInt32
WICJpegTransferMatrix_WICJpegTransferMatrixIdentity = 0
WICJpegTransferMatrix_WICJpegTransferMatrixBT601 = 1
WICJpegTransferMatrix_WICJpegTransferMatrix_FORCE_DWORD = 2147483647
WICJpegYCrCbSubsamplingOption = Int32
WICJpegYCrCbSubsamplingOption_WICJpegYCrCbSubsamplingDefault = 0
WICJpegYCrCbSubsamplingOption_WICJpegYCrCbSubsampling420 = 1
WICJpegYCrCbSubsamplingOption_WICJpegYCrCbSubsampling422 = 2
WICJpegYCrCbSubsamplingOption_WICJpegYCrCbSubsampling444 = 3
WICJpegYCrCbSubsamplingOption_WICJpegYCrCbSubsampling440 = 4
WICJpegYCrCbSubsamplingOption_WICJPEGYCRCBSUBSAMPLING_FORCE_DWORD = 2147483647
WICMetadataCreationOptions = Int32
WICMetadataCreationOptions_WICMetadataCreationDefault = 0
WICMetadataCreationOptions_WICMetadataCreationAllowUnknown = 0
WICMetadataCreationOptions_WICMetadataCreationFailUnknown = 65536
WICMetadataCreationOptions_WICMetadataCreationMask = -65536
def _define_WICMetadataHeader_head():
    class WICMetadataHeader(Structure):
        pass
    return WICMetadataHeader
def _define_WICMetadataHeader():
    WICMetadataHeader = win32more.Graphics.Imaging.WICMetadataHeader_head
    WICMetadataHeader._fields_ = [
        ('Position', win32more.Foundation.ULARGE_INTEGER),
        ('Length', UInt32),
        ('Header', c_char_p_no),
        ('DataOffset', win32more.Foundation.ULARGE_INTEGER),
    ]
    return WICMetadataHeader
def _define_WICMetadataPattern_head():
    class WICMetadataPattern(Structure):
        pass
    return WICMetadataPattern
def _define_WICMetadataPattern():
    WICMetadataPattern = win32more.Graphics.Imaging.WICMetadataPattern_head
    WICMetadataPattern._fields_ = [
        ('Position', win32more.Foundation.ULARGE_INTEGER),
        ('Length', UInt32),
        ('Pattern', c_char_p_no),
        ('Mask', c_char_p_no),
        ('DataOffset', win32more.Foundation.ULARGE_INTEGER),
    ]
    return WICMetadataPattern
WICNamedWhitePoint = Int32
WICNamedWhitePoint_WICWhitePointDefault = 1
WICNamedWhitePoint_WICWhitePointDaylight = 2
WICNamedWhitePoint_WICWhitePointCloudy = 4
WICNamedWhitePoint_WICWhitePointShade = 8
WICNamedWhitePoint_WICWhitePointTungsten = 16
WICNamedWhitePoint_WICWhitePointFluorescent = 32
WICNamedWhitePoint_WICWhitePointFlash = 64
WICNamedWhitePoint_WICWhitePointUnderwater = 128
WICNamedWhitePoint_WICWhitePointCustom = 256
WICNamedWhitePoint_WICWhitePointAutoWhiteBalance = 512
WICNamedWhitePoint_WICWhitePointAsShot = 1
WICNamedWhitePoint_WICNAMEDWHITEPOINT_FORCE_DWORD = 2147483647
WICPersistOptions = Int32
WICPersistOptions_WICPersistOptionDefault = 0
WICPersistOptions_WICPersistOptionLittleEndian = 0
WICPersistOptions_WICPersistOptionBigEndian = 1
WICPersistOptions_WICPersistOptionStrictFormat = 2
WICPersistOptions_WICPersistOptionNoCacheStream = 4
WICPersistOptions_WICPersistOptionPreferUTF8 = 8
WICPersistOptions_WICPersistOptionMask = 65535
WICPixelFormatNumericRepresentation = UInt32
WICPixelFormatNumericRepresentation_WICPixelFormatNumericRepresentationUnspecified = 0
WICPixelFormatNumericRepresentation_WICPixelFormatNumericRepresentationIndexed = 1
WICPixelFormatNumericRepresentation_WICPixelFormatNumericRepresentationUnsignedInteger = 2
WICPixelFormatNumericRepresentation_WICPixelFormatNumericRepresentationSignedInteger = 3
WICPixelFormatNumericRepresentation_WICPixelFormatNumericRepresentationFixed = 4
WICPixelFormatNumericRepresentation_WICPixelFormatNumericRepresentationFloat = 5
WICPixelFormatNumericRepresentation_WICPixelFormatNumericRepresentation_FORCE_DWORD = 2147483647
WICPlanarOptions = Int32
WICPlanarOptions_WICPlanarOptionsDefault = 0
WICPlanarOptions_WICPlanarOptionsPreserveSubsampling = 1
WICPlanarOptions_WICPLANAROPTIONS_FORCE_DWORD = 2147483647
WICPngBkgdProperties = UInt32
WICPngBkgdProperties_WICPngBkgdBackgroundColor = 1
WICPngBkgdProperties_WICPngBkgdProperties_FORCE_DWORD = 2147483647
WICPngChrmProperties = UInt32
WICPngChrmProperties_WICPngChrmWhitePointX = 1
WICPngChrmProperties_WICPngChrmWhitePointY = 2
WICPngChrmProperties_WICPngChrmRedX = 3
WICPngChrmProperties_WICPngChrmRedY = 4
WICPngChrmProperties_WICPngChrmGreenX = 5
WICPngChrmProperties_WICPngChrmGreenY = 6
WICPngChrmProperties_WICPngChrmBlueX = 7
WICPngChrmProperties_WICPngChrmBlueY = 8
WICPngChrmProperties_WICPngChrmProperties_FORCE_DWORD = 2147483647
WICPngFilterOption = Int32
WICPngFilterOption_WICPngFilterUnspecified = 0
WICPngFilterOption_WICPngFilterNone = 1
WICPngFilterOption_WICPngFilterSub = 2
WICPngFilterOption_WICPngFilterUp = 3
WICPngFilterOption_WICPngFilterAverage = 4
WICPngFilterOption_WICPngFilterPaeth = 5
WICPngFilterOption_WICPngFilterAdaptive = 6
WICPngFilterOption_WICPNGFILTEROPTION_FORCE_DWORD = 2147483647
WICPngGamaProperties = UInt32
WICPngGamaProperties_WICPngGamaGamma = 1
WICPngGamaProperties_WICPngGamaProperties_FORCE_DWORD = 2147483647
WICPngHistProperties = UInt32
WICPngHistProperties_WICPngHistFrequencies = 1
WICPngHistProperties_WICPngHistProperties_FORCE_DWORD = 2147483647
WICPngIccpProperties = UInt32
WICPngIccpProperties_WICPngIccpProfileName = 1
WICPngIccpProperties_WICPngIccpProfileData = 2
WICPngIccpProperties_WICPngIccpProperties_FORCE_DWORD = 2147483647
WICPngItxtProperties = UInt32
WICPngItxtProperties_WICPngItxtKeyword = 1
WICPngItxtProperties_WICPngItxtCompressionFlag = 2
WICPngItxtProperties_WICPngItxtLanguageTag = 3
WICPngItxtProperties_WICPngItxtTranslatedKeyword = 4
WICPngItxtProperties_WICPngItxtText = 5
WICPngItxtProperties_WICPngItxtProperties_FORCE_DWORD = 2147483647
WICPngSrgbProperties = UInt32
WICPngSrgbProperties_WICPngSrgbRenderingIntent = 1
WICPngSrgbProperties_WICPngSrgbProperties_FORCE_DWORD = 2147483647
WICPngTimeProperties = UInt32
WICPngTimeProperties_WICPngTimeYear = 1
WICPngTimeProperties_WICPngTimeMonth = 2
WICPngTimeProperties_WICPngTimeDay = 3
WICPngTimeProperties_WICPngTimeHour = 4
WICPngTimeProperties_WICPngTimeMinute = 5
WICPngTimeProperties_WICPngTimeSecond = 6
WICPngTimeProperties_WICPngTimeProperties_FORCE_DWORD = 2147483647
WICProgressNotification = Int32
WICProgressNotification_WICProgressNotificationBegin = 65536
WICProgressNotification_WICProgressNotificationEnd = 131072
WICProgressNotification_WICProgressNotificationFrequent = 262144
WICProgressNotification_WICProgressNotificationAll = -65536
WICProgressNotification_WICPROGRESSNOTIFICATION_FORCE_DWORD = 2147483647
WICProgressOperation = Int32
WICProgressOperation_WICProgressOperationCopyPixels = 1
WICProgressOperation_WICProgressOperationWritePixels = 2
WICProgressOperation_WICProgressOperationAll = 65535
WICProgressOperation_WICPROGRESSOPERATION_FORCE_DWORD = 2147483647
WICRawCapabilities = Int32
WICRawCapabilities_WICRawCapabilityNotSupported = 0
WICRawCapabilities_WICRawCapabilityGetSupported = 1
WICRawCapabilities_WICRawCapabilityFullySupported = 2
WICRawCapabilities_WICRAWCAPABILITIES_FORCE_DWORD = 2147483647
def _define_WICRawCapabilitiesInfo_head():
    class WICRawCapabilitiesInfo(Structure):
        pass
    return WICRawCapabilitiesInfo
def _define_WICRawCapabilitiesInfo():
    WICRawCapabilitiesInfo = win32more.Graphics.Imaging.WICRawCapabilitiesInfo_head
    WICRawCapabilitiesInfo._fields_ = [
        ('cbSize', UInt32),
        ('CodecMajorVersion', UInt32),
        ('CodecMinorVersion', UInt32),
        ('ExposureCompensationSupport', win32more.Graphics.Imaging.WICRawCapabilities),
        ('ContrastSupport', win32more.Graphics.Imaging.WICRawCapabilities),
        ('RGBWhitePointSupport', win32more.Graphics.Imaging.WICRawCapabilities),
        ('NamedWhitePointSupport', win32more.Graphics.Imaging.WICRawCapabilities),
        ('NamedWhitePointSupportMask', UInt32),
        ('KelvinWhitePointSupport', win32more.Graphics.Imaging.WICRawCapabilities),
        ('GammaSupport', win32more.Graphics.Imaging.WICRawCapabilities),
        ('TintSupport', win32more.Graphics.Imaging.WICRawCapabilities),
        ('SaturationSupport', win32more.Graphics.Imaging.WICRawCapabilities),
        ('SharpnessSupport', win32more.Graphics.Imaging.WICRawCapabilities),
        ('NoiseReductionSupport', win32more.Graphics.Imaging.WICRawCapabilities),
        ('DestinationColorProfileSupport', win32more.Graphics.Imaging.WICRawCapabilities),
        ('ToneCurveSupport', win32more.Graphics.Imaging.WICRawCapabilities),
        ('RotationSupport', win32more.Graphics.Imaging.WICRawRotationCapabilities),
        ('RenderModeSupport', win32more.Graphics.Imaging.WICRawCapabilities),
    ]
    return WICRawCapabilitiesInfo
WICRawParameterSet = Int32
WICRawParameterSet_WICAsShotParameterSet = 1
WICRawParameterSet_WICUserAdjustedParameterSet = 2
WICRawParameterSet_WICAutoAdjustedParameterSet = 3
WICRawParameterSet_WICRAWPARAMETERSET_FORCE_DWORD = 2147483647
WICRawRenderMode = Int32
WICRawRenderMode_WICRawRenderModeDraft = 1
WICRawRenderMode_WICRawRenderModeNormal = 2
WICRawRenderMode_WICRawRenderModeBestQuality = 3
WICRawRenderMode_WICRAWRENDERMODE_FORCE_DWORD = 2147483647
WICRawRotationCapabilities = Int32
WICRawRotationCapabilities_WICRawRotationCapabilityNotSupported = 0
WICRawRotationCapabilities_WICRawRotationCapabilityGetSupported = 1
WICRawRotationCapabilities_WICRawRotationCapabilityNinetyDegreesSupported = 2
WICRawRotationCapabilities_WICRawRotationCapabilityFullySupported = 3
WICRawRotationCapabilities_WICRAWROTATIONCAPABILITIES_FORCE_DWORD = 2147483647
def _define_WICRawToneCurve_head():
    class WICRawToneCurve(Structure):
        pass
    return WICRawToneCurve
def _define_WICRawToneCurve():
    WICRawToneCurve = win32more.Graphics.Imaging.WICRawToneCurve_head
    WICRawToneCurve._fields_ = [
        ('cPoints', UInt32),
        ('aPoints', win32more.Graphics.Imaging.WICRawToneCurvePoint * 1),
    ]
    return WICRawToneCurve
def _define_WICRawToneCurvePoint_head():
    class WICRawToneCurvePoint(Structure):
        pass
    return WICRawToneCurvePoint
def _define_WICRawToneCurvePoint():
    WICRawToneCurvePoint = win32more.Graphics.Imaging.WICRawToneCurvePoint_head
    WICRawToneCurvePoint._fields_ = [
        ('Input', Double),
        ('Output', Double),
    ]
    return WICRawToneCurvePoint
def _define_WICRect_head():
    class WICRect(Structure):
        pass
    return WICRect
def _define_WICRect():
    WICRect = win32more.Graphics.Imaging.WICRect_head
    WICRect._fields_ = [
        ('X', Int32),
        ('Y', Int32),
        ('Width', Int32),
        ('Height', Int32),
    ]
    return WICRect
WICSectionAccessLevel = UInt32
WICSectionAccessLevel_WICSectionAccessLevelRead = 1
WICSectionAccessLevel_WICSectionAccessLevelReadWrite = 3
WICSectionAccessLevel_WICSectionAccessLevel_FORCE_DWORD = 2147483647
WICTiffCompressionOption = Int32
WICTiffCompressionOption_WICTiffCompressionDontCare = 0
WICTiffCompressionOption_WICTiffCompressionNone = 1
WICTiffCompressionOption_WICTiffCompressionCCITT3 = 2
WICTiffCompressionOption_WICTiffCompressionCCITT4 = 3
WICTiffCompressionOption_WICTiffCompressionLZW = 4
WICTiffCompressionOption_WICTiffCompressionRLE = 5
WICTiffCompressionOption_WICTiffCompressionZIP = 6
WICTiffCompressionOption_WICTiffCompressionLZWHDifferencing = 7
WICTiffCompressionOption_WICTIFFCOMPRESSIONOPTION_FORCE_DWORD = 2147483647
WICWebpAnimProperties = UInt32
WICWebpAnimProperties_WICWebpAnimLoopCount = 1
WICWebpAnimProperties_WICWebpAnimProperties_FORCE_DWORD = 2147483647
WICWebpAnmfProperties = UInt32
WICWebpAnmfProperties_WICWebpAnmfFrameDuration = 1
WICWebpAnmfProperties_WICWebpAnmfProperties_FORCE_DWORD = 2147483647
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
