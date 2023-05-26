from __future__ import annotations
from ctypes import POINTER
from Windows import ARCH, Boolean, Byte, Bytes, Char, ComPtr, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, MissingType, SByte, SUCCEEDED, Single, String, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_head, press, winfunctype, winfunctype_pointer
import Windows.Win32.Foundation
import Windows.Win32.Graphics.Direct2D.Common
import Windows.Win32.Graphics.Dxgi.Common
import Windows.Win32.Graphics.Gdi
import Windows.Win32.Graphics.Imaging
import Windows.Win32.System.Com
import Windows.Win32.System.Com.StructuredStorage
import Windows.Win32.UI.WindowsAndMessaging
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
WINCODEC_SDK_VERSION1: UInt32 = 566
WINCODEC_SDK_VERSION2: UInt32 = 567
CLSID_WICImagingFactory: Guid = Guid('{cacaf262-9370-4615-a13b-9f5539da4c0a}')
CLSID_WICImagingFactory1: Guid = Guid('{cacaf262-9370-4615-a13b-9f5539da4c0a}')
CLSID_WICImagingFactory2: Guid = Guid('{317d06e8-5f24-433d-bdf7-79ce68d8abc2}')
WINCODEC_SDK_VERSION: UInt32 = 567
GUID_VendorMicrosoft: Guid = Guid('{f0e749ca-edef-4589-a73a-ee0e626a2a2b}')
GUID_VendorMicrosoftBuiltIn: Guid = Guid('{257a30fd-06b6-462b-aea4-63f70b86e533}')
CLSID_WICPngDecoder: Guid = Guid('{389ea17b-5078-4cde-b6ef-25c15175c751}')
CLSID_WICPngDecoder1: Guid = Guid('{389ea17b-5078-4cde-b6ef-25c15175c751}')
CLSID_WICPngDecoder2: Guid = Guid('{e018945b-aa86-4008-9bd4-6777a1e40c11}')
CLSID_WICBmpDecoder: Guid = Guid('{6b462062-7cbf-400d-9fdb-813dd10f2778}')
CLSID_WICIcoDecoder: Guid = Guid('{c61bfcdf-2e0f-4aad-a8d7-e06bafebcdfe}')
CLSID_WICJpegDecoder: Guid = Guid('{9456a480-e88b-43ea-9e73-0b2d9b71b1ca}')
CLSID_WICGifDecoder: Guid = Guid('{381dda3c-9ce9-4834-a23e-1f98f8fc52be}')
CLSID_WICTiffDecoder: Guid = Guid('{b54e85d9-fe23-499f-8b88-6acea713752b}')
CLSID_WICWmpDecoder: Guid = Guid('{a26cec36-234c-4950-ae16-e34aace71d0d}')
CLSID_WICDdsDecoder: Guid = Guid('{9053699f-a341-429d-9e90-ee437cf80c73}')
CLSID_WICBmpEncoder: Guid = Guid('{69be8bb4-d66d-47c8-865a-ed1589433782}')
CLSID_WICPngEncoder: Guid = Guid('{27949969-876a-41d7-9447-568f6a35a4dc}')
CLSID_WICJpegEncoder: Guid = Guid('{1a34f5c1-4a5a-46dc-b644-1f4567e7a676}')
CLSID_WICGifEncoder: Guid = Guid('{114f5598-0b22-40a0-86a1-c83ea495adbd}')
CLSID_WICTiffEncoder: Guid = Guid('{0131be10-2001-4c5f-a9b0-cc88fab64ce8}')
CLSID_WICWmpEncoder: Guid = Guid('{ac4ce3cb-e1c1-44cd-8215-5a1665509ec2}')
CLSID_WICDdsEncoder: Guid = Guid('{a61dde94-66ce-4ac1-881b-71680588895e}')
CLSID_WICAdngDecoder: Guid = Guid('{981d9411-909e-42a7-8f5d-a747ff052edb}')
CLSID_WICJpegQualcommPhoneEncoder: Guid = Guid('{68ed5c62-f534-4979-b2b3-686a12b2b34c}')
CLSID_WICHeifDecoder: Guid = Guid('{e9a4a80a-44fe-4de4-8971-7150b10a5199}')
CLSID_WICHeifEncoder: Guid = Guid('{0dbecec1-9eb3-4860-9c6f-ddbe86634575}')
CLSID_WICWebpDecoder: Guid = Guid('{7693e886-51c9-4070-8419-9f70738ec8fa}')
CLSID_WICRAWDecoder: Guid = Guid('{41945702-8302-44a6-9445-ac98e8afa086}')
GUID_ContainerFormatBmp: Guid = Guid('{0af1d87e-fcfe-4188-bdeb-a7906471cbe3}')
GUID_ContainerFormatPng: Guid = Guid('{1b7cfaf4-713f-473c-bbcd-6137425faeaf}')
GUID_ContainerFormatIco: Guid = Guid('{a3a860c4-338f-4c17-919a-fba4b5628f21}')
GUID_ContainerFormatJpeg: Guid = Guid('{19e4a5aa-5662-4fc5-a0c0-1758028e1057}')
GUID_ContainerFormatTiff: Guid = Guid('{163bcc30-e2e9-4f0b-961d-a3e9fdb788a3}')
GUID_ContainerFormatGif: Guid = Guid('{1f8a5601-7d4d-4cbd-9c82-1bc8d4eeb9a5}')
GUID_ContainerFormatWmp: Guid = Guid('{57a37caa-367a-4540-916b-f183c5093a4b}')
GUID_ContainerFormatDds: Guid = Guid('{9967cb95-2e85-4ac8-8ca2-83d7ccd425c9}')
GUID_ContainerFormatAdng: Guid = Guid('{f3ff6d0d-38c0-41c4-b1fe-1f3824f17b84}')
GUID_ContainerFormatHeif: Guid = Guid('{e1e62521-6787-405b-a339-500715b5763f}')
GUID_ContainerFormatWebp: Guid = Guid('{e094b0e2-67f2-45b3-b0ea-115337ca7cf3}')
GUID_ContainerFormatRaw: Guid = Guid('{fe99ce60-f19c-433c-a3ae-00acefa9ca21}')
CLSID_WICImagingCategories: Guid = Guid('{fae3d380-fea4-4623-8c75-c6b61110b681}')
CATID_WICBitmapDecoders: Guid = Guid('{7ed96837-96f0-4812-b211-f13c24117ed3}')
CATID_WICBitmapEncoders: Guid = Guid('{ac757296-3522-4e11-9862-c17be5a1767e}')
CATID_WICPixelFormats: Guid = Guid('{2b46e70f-cda7-473e-89f6-dc9630a2390b}')
CATID_WICFormatConverters: Guid = Guid('{7835eae8-bf14-49d1-93ce-533a407b2248}')
CATID_WICMetadataReader: Guid = Guid('{05af94d8-7174-4cd2-be4a-4124b80ee4b8}')
CATID_WICMetadataWriter: Guid = Guid('{abe3b9a4-257d-4b97-bd1a-294af496222e}')
CLSID_WICDefaultFormatConverter: Guid = Guid('{1a3f11dc-b514-4b17-8c5f-2154513852f1}')
CLSID_WICFormatConverterHighColor: Guid = Guid('{ac75d454-9f37-48f8-b972-4e19bc856011}')
CLSID_WICFormatConverterNChannel: Guid = Guid('{c17cabb2-d4a3-47d7-a557-339b2efbd4f1}')
CLSID_WICFormatConverterWMPhoto: Guid = Guid('{9cb5172b-d600-46ba-ab77-77bb7e3a00d9}')
CLSID_WICPlanarFormatConverter: Guid = Guid('{184132b8-32f8-4784-9131-dd7224b23438}')
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
GUID_WICPixelFormatDontCare: Guid = Guid('{6fddc324-4e03-4bfe-b185-3d77768dc900}')
GUID_WICPixelFormat1bppIndexed: Guid = Guid('{6fddc324-4e03-4bfe-b185-3d77768dc901}')
GUID_WICPixelFormat2bppIndexed: Guid = Guid('{6fddc324-4e03-4bfe-b185-3d77768dc902}')
GUID_WICPixelFormat4bppIndexed: Guid = Guid('{6fddc324-4e03-4bfe-b185-3d77768dc903}')
GUID_WICPixelFormat8bppIndexed: Guid = Guid('{6fddc324-4e03-4bfe-b185-3d77768dc904}')
GUID_WICPixelFormatBlackWhite: Guid = Guid('{6fddc324-4e03-4bfe-b185-3d77768dc905}')
GUID_WICPixelFormat2bppGray: Guid = Guid('{6fddc324-4e03-4bfe-b185-3d77768dc906}')
GUID_WICPixelFormat4bppGray: Guid = Guid('{6fddc324-4e03-4bfe-b185-3d77768dc907}')
GUID_WICPixelFormat8bppGray: Guid = Guid('{6fddc324-4e03-4bfe-b185-3d77768dc908}')
GUID_WICPixelFormat8bppAlpha: Guid = Guid('{e6cd0116-eeba-4161-aa85-27dd9fb3a895}')
GUID_WICPixelFormat16bppBGR555: Guid = Guid('{6fddc324-4e03-4bfe-b185-3d77768dc909}')
GUID_WICPixelFormat16bppBGR565: Guid = Guid('{6fddc324-4e03-4bfe-b185-3d77768dc90a}')
GUID_WICPixelFormat16bppBGRA5551: Guid = Guid('{05ec7c2b-f1e6-4961-ad46-e1cc810a87d2}')
GUID_WICPixelFormat16bppGray: Guid = Guid('{6fddc324-4e03-4bfe-b185-3d77768dc90b}')
GUID_WICPixelFormat24bppBGR: Guid = Guid('{6fddc324-4e03-4bfe-b185-3d77768dc90c}')
GUID_WICPixelFormat24bppRGB: Guid = Guid('{6fddc324-4e03-4bfe-b185-3d77768dc90d}')
GUID_WICPixelFormat32bppBGR: Guid = Guid('{6fddc324-4e03-4bfe-b185-3d77768dc90e}')
GUID_WICPixelFormat32bppBGRA: Guid = Guid('{6fddc324-4e03-4bfe-b185-3d77768dc90f}')
GUID_WICPixelFormat32bppPBGRA: Guid = Guid('{6fddc324-4e03-4bfe-b185-3d77768dc910}')
GUID_WICPixelFormat32bppGrayFloat: Guid = Guid('{6fddc324-4e03-4bfe-b185-3d77768dc911}')
GUID_WICPixelFormat32bppRGB: Guid = Guid('{d98c6b95-3efe-47d6-bb25-eb1748ab0cf1}')
GUID_WICPixelFormat32bppRGBA: Guid = Guid('{f5c7ad2d-6a8d-43dd-a7a8-a29935261ae9}')
GUID_WICPixelFormat32bppPRGBA: Guid = Guid('{3cc4a650-a527-4d37-a916-3142c7ebedba}')
GUID_WICPixelFormat48bppRGB: Guid = Guid('{6fddc324-4e03-4bfe-b185-3d77768dc915}')
GUID_WICPixelFormat48bppBGR: Guid = Guid('{e605a384-b468-46ce-bb2e-36f180e64313}')
GUID_WICPixelFormat64bppRGB: Guid = Guid('{a1182111-186d-4d42-bc6a-9c8303a8dff9}')
GUID_WICPixelFormat64bppRGBA: Guid = Guid('{6fddc324-4e03-4bfe-b185-3d77768dc916}')
GUID_WICPixelFormat64bppBGRA: Guid = Guid('{1562ff7c-d352-46f9-979e-42976b792246}')
GUID_WICPixelFormat64bppPRGBA: Guid = Guid('{6fddc324-4e03-4bfe-b185-3d77768dc917}')
GUID_WICPixelFormat64bppPBGRA: Guid = Guid('{8c518e8e-a4ec-468b-ae70-c9a35a9c5530}')
GUID_WICPixelFormat16bppGrayFixedPoint: Guid = Guid('{6fddc324-4e03-4bfe-b185-3d77768dc913}')
GUID_WICPixelFormat32bppBGR101010: Guid = Guid('{6fddc324-4e03-4bfe-b185-3d77768dc914}')
GUID_WICPixelFormat48bppRGBFixedPoint: Guid = Guid('{6fddc324-4e03-4bfe-b185-3d77768dc912}')
GUID_WICPixelFormat48bppBGRFixedPoint: Guid = Guid('{49ca140e-cab6-493b-9ddf-60187c37532a}')
GUID_WICPixelFormat96bppRGBFixedPoint: Guid = Guid('{6fddc324-4e03-4bfe-b185-3d77768dc918}')
GUID_WICPixelFormat96bppRGBFloat: Guid = Guid('{e3fed78f-e8db-4acf-84c1-e97f6136b327}')
GUID_WICPixelFormat128bppRGBAFloat: Guid = Guid('{6fddc324-4e03-4bfe-b185-3d77768dc919}')
GUID_WICPixelFormat128bppPRGBAFloat: Guid = Guid('{6fddc324-4e03-4bfe-b185-3d77768dc91a}')
GUID_WICPixelFormat128bppRGBFloat: Guid = Guid('{6fddc324-4e03-4bfe-b185-3d77768dc91b}')
GUID_WICPixelFormat32bppCMYK: Guid = Guid('{6fddc324-4e03-4bfe-b185-3d77768dc91c}')
GUID_WICPixelFormat64bppRGBAFixedPoint: Guid = Guid('{6fddc324-4e03-4bfe-b185-3d77768dc91d}')
GUID_WICPixelFormat64bppBGRAFixedPoint: Guid = Guid('{356de33c-54d2-4a23-bb04-9b7bf9b1d42d}')
GUID_WICPixelFormat64bppRGBFixedPoint: Guid = Guid('{6fddc324-4e03-4bfe-b185-3d77768dc940}')
GUID_WICPixelFormat128bppRGBAFixedPoint: Guid = Guid('{6fddc324-4e03-4bfe-b185-3d77768dc91e}')
GUID_WICPixelFormat128bppRGBFixedPoint: Guid = Guid('{6fddc324-4e03-4bfe-b185-3d77768dc941}')
GUID_WICPixelFormat64bppRGBAHalf: Guid = Guid('{6fddc324-4e03-4bfe-b185-3d77768dc93a}')
GUID_WICPixelFormat64bppPRGBAHalf: Guid = Guid('{58ad26c2-c623-4d9d-b320-387e49f8c442}')
GUID_WICPixelFormat64bppRGBHalf: Guid = Guid('{6fddc324-4e03-4bfe-b185-3d77768dc942}')
GUID_WICPixelFormat48bppRGBHalf: Guid = Guid('{6fddc324-4e03-4bfe-b185-3d77768dc93b}')
GUID_WICPixelFormat32bppRGBE: Guid = Guid('{6fddc324-4e03-4bfe-b185-3d77768dc93d}')
GUID_WICPixelFormat16bppGrayHalf: Guid = Guid('{6fddc324-4e03-4bfe-b185-3d77768dc93e}')
GUID_WICPixelFormat32bppGrayFixedPoint: Guid = Guid('{6fddc324-4e03-4bfe-b185-3d77768dc93f}')
GUID_WICPixelFormat32bppRGBA1010102: Guid = Guid('{25238d72-fcf9-4522-b514-5578e5ad55e0}')
GUID_WICPixelFormat32bppRGBA1010102XR: Guid = Guid('{00de6b9a-c101-434b-b502-d0165ee1122c}')
GUID_WICPixelFormat32bppR10G10B10A2: Guid = Guid('{604e1bb5-8a3c-4b65-b11c-bc0b8dd75b7f}')
GUID_WICPixelFormat32bppR10G10B10A2HDR10: Guid = Guid('{9c215c5d-1acc-4f0e-a4bc-70fb3ae8fd28}')
GUID_WICPixelFormat64bppCMYK: Guid = Guid('{6fddc324-4e03-4bfe-b185-3d77768dc91f}')
GUID_WICPixelFormat24bpp3Channels: Guid = Guid('{6fddc324-4e03-4bfe-b185-3d77768dc920}')
GUID_WICPixelFormat32bpp4Channels: Guid = Guid('{6fddc324-4e03-4bfe-b185-3d77768dc921}')
GUID_WICPixelFormat40bpp5Channels: Guid = Guid('{6fddc324-4e03-4bfe-b185-3d77768dc922}')
GUID_WICPixelFormat48bpp6Channels: Guid = Guid('{6fddc324-4e03-4bfe-b185-3d77768dc923}')
GUID_WICPixelFormat56bpp7Channels: Guid = Guid('{6fddc324-4e03-4bfe-b185-3d77768dc924}')
GUID_WICPixelFormat64bpp8Channels: Guid = Guid('{6fddc324-4e03-4bfe-b185-3d77768dc925}')
GUID_WICPixelFormat48bpp3Channels: Guid = Guid('{6fddc324-4e03-4bfe-b185-3d77768dc926}')
GUID_WICPixelFormat64bpp4Channels: Guid = Guid('{6fddc324-4e03-4bfe-b185-3d77768dc927}')
GUID_WICPixelFormat80bpp5Channels: Guid = Guid('{6fddc324-4e03-4bfe-b185-3d77768dc928}')
GUID_WICPixelFormat96bpp6Channels: Guid = Guid('{6fddc324-4e03-4bfe-b185-3d77768dc929}')
GUID_WICPixelFormat112bpp7Channels: Guid = Guid('{6fddc324-4e03-4bfe-b185-3d77768dc92a}')
GUID_WICPixelFormat128bpp8Channels: Guid = Guid('{6fddc324-4e03-4bfe-b185-3d77768dc92b}')
GUID_WICPixelFormat40bppCMYKAlpha: Guid = Guid('{6fddc324-4e03-4bfe-b185-3d77768dc92c}')
GUID_WICPixelFormat80bppCMYKAlpha: Guid = Guid('{6fddc324-4e03-4bfe-b185-3d77768dc92d}')
GUID_WICPixelFormat32bpp3ChannelsAlpha: Guid = Guid('{6fddc324-4e03-4bfe-b185-3d77768dc92e}')
GUID_WICPixelFormat40bpp4ChannelsAlpha: Guid = Guid('{6fddc324-4e03-4bfe-b185-3d77768dc92f}')
GUID_WICPixelFormat48bpp5ChannelsAlpha: Guid = Guid('{6fddc324-4e03-4bfe-b185-3d77768dc930}')
GUID_WICPixelFormat56bpp6ChannelsAlpha: Guid = Guid('{6fddc324-4e03-4bfe-b185-3d77768dc931}')
GUID_WICPixelFormat64bpp7ChannelsAlpha: Guid = Guid('{6fddc324-4e03-4bfe-b185-3d77768dc932}')
GUID_WICPixelFormat72bpp8ChannelsAlpha: Guid = Guid('{6fddc324-4e03-4bfe-b185-3d77768dc933}')
GUID_WICPixelFormat64bpp3ChannelsAlpha: Guid = Guid('{6fddc324-4e03-4bfe-b185-3d77768dc934}')
GUID_WICPixelFormat80bpp4ChannelsAlpha: Guid = Guid('{6fddc324-4e03-4bfe-b185-3d77768dc935}')
GUID_WICPixelFormat96bpp5ChannelsAlpha: Guid = Guid('{6fddc324-4e03-4bfe-b185-3d77768dc936}')
GUID_WICPixelFormat112bpp6ChannelsAlpha: Guid = Guid('{6fddc324-4e03-4bfe-b185-3d77768dc937}')
GUID_WICPixelFormat128bpp7ChannelsAlpha: Guid = Guid('{6fddc324-4e03-4bfe-b185-3d77768dc938}')
GUID_WICPixelFormat144bpp8ChannelsAlpha: Guid = Guid('{6fddc324-4e03-4bfe-b185-3d77768dc939}')
GUID_WICPixelFormat8bppY: Guid = Guid('{91b4db54-2df9-42f0-b449-2909bb3df88e}')
GUID_WICPixelFormat8bppCb: Guid = Guid('{1339f224-6bfe-4c3e-9302-e4f3a6d0ca2a}')
GUID_WICPixelFormat8bppCr: Guid = Guid('{b8145053-2116-49f0-8835-ed844b205c51}')
GUID_WICPixelFormat16bppCbCr: Guid = Guid('{ff95ba6e-11e0-4263-bb45-01721f3460a4}')
GUID_WICPixelFormat16bppYQuantizedDctCoefficients: Guid = Guid('{a355f433-48e8-4a42-84d8-e2aa26ca80a4}')
GUID_WICPixelFormat16bppCbQuantizedDctCoefficients: Guid = Guid('{d2c4ff61-56a5-49c2-8b5c-4c1925964837}')
GUID_WICPixelFormat16bppCrQuantizedDctCoefficients: Guid = Guid('{2fe354f0-1680-42d8-9231-e73c0565bfc1}')
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
GUID_MetadataFormatUnknown: Guid = Guid('{a45e592f-9078-4a7c-adb5-4edc4fd61b1f}')
GUID_MetadataFormatIfd: Guid = Guid('{537396c6-2d8a-4bb6-9bf8-2f0a8e2a3adf}')
GUID_MetadataFormatSubIfd: Guid = Guid('{58a2e128-2db9-4e57-bb14-5177891ed331}')
GUID_MetadataFormatExif: Guid = Guid('{1c3c4f9d-b84a-467d-9493-36cfbd59ea57}')
GUID_MetadataFormatGps: Guid = Guid('{7134ab8a-9351-44ad-af62-448db6b502ec}')
GUID_MetadataFormatInterop: Guid = Guid('{ed686f8e-681f-4c8b-bd41-a8addbf6b3fc}')
GUID_MetadataFormatApp0: Guid = Guid('{79007028-268d-45d6-a3c2-354e6a504bc9}')
GUID_MetadataFormatApp1: Guid = Guid('{8fd3dfc3-f951-492b-817f-69c2e6d9a5b0}')
GUID_MetadataFormatApp13: Guid = Guid('{326556a2-f502-4354-9cc0-8e3f48eaf6b5}')
GUID_MetadataFormatIPTC: Guid = Guid('{4fab0914-e129-4087-a1d1-bc812d45a7b5}')
GUID_MetadataFormatIRB: Guid = Guid('{16100d66-8570-4bb9-b92d-fda4b23ece67}')
GUID_MetadataFormat8BIMIPTC: Guid = Guid('{0010568c-0852-4e6a-b191-5c33ac5b0430}')
GUID_MetadataFormat8BIMResolutionInfo: Guid = Guid('{739f305d-81db-43cb-ac5e-55013ef9f003}')
GUID_MetadataFormat8BIMIPTCDigest: Guid = Guid('{1ca32285-9ccd-4786-8bd8-79539db6a006}')
GUID_MetadataFormatXMP: Guid = Guid('{bb5acc38-f216-4cec-a6c5-5f6e739763a9}')
GUID_MetadataFormatThumbnail: Guid = Guid('{243dcee9-8703-40ee-8ef0-22a600b8058c}')
GUID_MetadataFormatChunktEXt: Guid = Guid('{568d8936-c0a9-4923-905d-df2b38238fbc}')
GUID_MetadataFormatXMPStruct: Guid = Guid('{22383cf1-ed17-4e2e-af17-d85b8f6b30d0}')
GUID_MetadataFormatXMPBag: Guid = Guid('{833cca5f-dcb7-4516-806f-6596ab26dce4}')
GUID_MetadataFormatXMPSeq: Guid = Guid('{63e8df02-eb6c-456c-a224-b25e794fd648}')
GUID_MetadataFormatXMPAlt: Guid = Guid('{7b08a675-91aa-481b-a798-4da94908613b}')
GUID_MetadataFormatLSD: Guid = Guid('{e256031e-6299-4929-b98d-5ac884afba92}')
GUID_MetadataFormatIMD: Guid = Guid('{bd2bb086-4d52-48dd-9677-db483e85ae8f}')
GUID_MetadataFormatGCE: Guid = Guid('{2a25cad8-deeb-4c69-a788-0ec2266dcafd}')
GUID_MetadataFormatAPE: Guid = Guid('{2e043dc2-c967-4e05-875e-618bf67e85c3}')
GUID_MetadataFormatJpegChrominance: Guid = Guid('{f73d0dcf-cec6-4f85-9b0e-1c3956b1bef7}')
GUID_MetadataFormatJpegLuminance: Guid = Guid('{86908007-edfc-4860-8d4b-4ee6e83e6058}')
GUID_MetadataFormatJpegComment: Guid = Guid('{220e5f33-afd3-474e-9d31-7d4fe730f557}')
GUID_MetadataFormatGifComment: Guid = Guid('{c4b6e0e0-cfb4-4ad3-ab33-9aad2355a34a}')
GUID_MetadataFormatChunkgAMA: Guid = Guid('{f00935a5-1d5d-4cd1-81b2-9324d7eca781}')
GUID_MetadataFormatChunkbKGD: Guid = Guid('{e14d3571-6b47-4dea-b60a-87ce0a78dfb7}')
GUID_MetadataFormatChunkiTXt: Guid = Guid('{c2bec729-0b68-4b77-aa0e-6295a6ac1814}')
GUID_MetadataFormatChunkcHRM: Guid = Guid('{9db3655b-2842-44b3-8067-12e9b375556a}')
GUID_MetadataFormatChunkhIST: Guid = Guid('{c59a82da-db74-48a4-bd6a-b69c4931ef95}')
GUID_MetadataFormatChunkiCCP: Guid = Guid('{eb4349ab-b685-450f-91b5-e802e892536c}')
GUID_MetadataFormatChunksRGB: Guid = Guid('{c115fd36-cc6f-4e3f-8363-524b87c6b0d9}')
GUID_MetadataFormatChunktIME: Guid = Guid('{6b00ae2d-e24b-460a-98b6-878bd03072fd}')
GUID_MetadataFormatDds: Guid = Guid('{4a064603-8c33-4e60-9c29-136231702d08}')
GUID_MetadataFormatHeif: Guid = Guid('{817ef3e1-1288-45f4-a852-260d9e7cce83}')
GUID_MetadataFormatHeifHDR: Guid = Guid('{568b8d8a-1e65-438c-8968-d60e1012beb9}')
GUID_MetadataFormatWebpANIM: Guid = Guid('{6dc4fda6-78e6-4102-ae35-bcfa1edcc78b}')
GUID_MetadataFormatWebpANMF: Guid = Guid('{43c105ee-b93b-4abb-b003-a08c0d870471}')
CLSID_WICUnknownMetadataReader: Guid = Guid('{699745c2-5066-4b82-a8e3-d40478dbec8c}')
CLSID_WICUnknownMetadataWriter: Guid = Guid('{a09cca86-27ba-4f39-9053-121fa4dc08fc}')
CLSID_WICApp0MetadataWriter: Guid = Guid('{f3c633a2-46c8-498e-8fbb-cc6f721bbcde}')
CLSID_WICApp0MetadataReader: Guid = Guid('{43324b33-a78f-480f-9111-9638aaccc832}')
CLSID_WICApp1MetadataWriter: Guid = Guid('{ee366069-1832-420f-b381-0479ad066f19}')
CLSID_WICApp1MetadataReader: Guid = Guid('{dde33513-774e-4bcd-ae79-02f4adfe62fc}')
CLSID_WICApp13MetadataWriter: Guid = Guid('{7b19a919-a9d6-49e5-bd45-02c34e4e4cd5}')
CLSID_WICApp13MetadataReader: Guid = Guid('{aa7e3c50-864c-4604-bc04-8b0b76e637f6}')
CLSID_WICIfdMetadataReader: Guid = Guid('{8f914656-9d0a-4eb2-9019-0bf96d8a9ee6}')
CLSID_WICIfdMetadataWriter: Guid = Guid('{b1ebfc28-c9bd-47a2-8d33-b948769777a7}')
CLSID_WICSubIfdMetadataReader: Guid = Guid('{50d42f09-ecd1-4b41-b65d-da1fdaa75663}')
CLSID_WICSubIfdMetadataWriter: Guid = Guid('{8ade5386-8e9b-4f4c-acf2-f0008706b238}')
CLSID_WICExifMetadataReader: Guid = Guid('{d9403860-297f-4a49-bf9b-77898150a442}')
CLSID_WICExifMetadataWriter: Guid = Guid('{c9a14cda-c339-460b-9078-d4debcfabe91}')
CLSID_WICGpsMetadataReader: Guid = Guid('{3697790b-223b-484e-9925-c4869218f17a}')
CLSID_WICGpsMetadataWriter: Guid = Guid('{cb8c13e4-62b5-4c96-a48b-6ba6ace39c76}')
CLSID_WICInteropMetadataReader: Guid = Guid('{b5c8b898-0074-459f-b700-860d4651ea14}')
CLSID_WICInteropMetadataWriter: Guid = Guid('{122ec645-cd7e-44d8-b186-2c8c20c3b50f}')
CLSID_WICThumbnailMetadataReader: Guid = Guid('{fb012959-f4f6-44d7-9d09-daa087a9db57}')
CLSID_WICThumbnailMetadataWriter: Guid = Guid('{d049b20c-5dd0-44fe-b0b3-8f92c8e6d080}')
CLSID_WICIPTCMetadataReader: Guid = Guid('{03012959-f4f6-44d7-9d09-daa087a9db57}')
CLSID_WICIPTCMetadataWriter: Guid = Guid('{1249b20c-5dd0-44fe-b0b3-8f92c8e6d080}')
CLSID_WICIRBMetadataReader: Guid = Guid('{d4dcd3d7-b4c2-47d9-a6bf-b89ba396a4a3}')
CLSID_WICIRBMetadataWriter: Guid = Guid('{5c5c1935-0235-4434-80bc-251bc1ec39c6}')
CLSID_WIC8BIMIPTCMetadataReader: Guid = Guid('{0010668c-0801-4da6-a4a4-826522b6d28f}')
CLSID_WIC8BIMIPTCMetadataWriter: Guid = Guid('{00108226-ee41-44a2-9e9c-4be4d5b1d2cd}')
CLSID_WIC8BIMResolutionInfoMetadataReader: Guid = Guid('{5805137a-e348-4f7c-b3cc-6db9965a0599}')
CLSID_WIC8BIMResolutionInfoMetadataWriter: Guid = Guid('{4ff2fe0e-e74a-4b71-98c4-ab7dc16707ba}')
CLSID_WIC8BIMIPTCDigestMetadataReader: Guid = Guid('{02805f1e-d5aa-415b-82c5-61c033a988a6}')
CLSID_WIC8BIMIPTCDigestMetadataWriter: Guid = Guid('{2db5e62b-0d67-495f-8f9d-c2f0188647ac}')
CLSID_WICPngTextMetadataReader: Guid = Guid('{4b59afcc-b8c3-408a-b670-89e5fab6fda7}')
CLSID_WICPngTextMetadataWriter: Guid = Guid('{b5ebafb9-253e-4a72-a744-0762d2685683}')
CLSID_WICXMPMetadataReader: Guid = Guid('{72b624df-ae11-4948-a65c-351eb0829419}')
CLSID_WICXMPMetadataWriter: Guid = Guid('{1765e14e-1bd4-462e-b6b1-590bf1262ac6}')
CLSID_WICXMPStructMetadataReader: Guid = Guid('{01b90d9a-8209-47f7-9c52-e1244bf50ced}')
CLSID_WICXMPStructMetadataWriter: Guid = Guid('{22c21f93-7ddb-411c-9b17-c5b7bd064abc}')
CLSID_WICXMPBagMetadataReader: Guid = Guid('{e7e79a30-4f2c-4fab-8d00-394f2d6bbebe}')
CLSID_WICXMPBagMetadataWriter: Guid = Guid('{ed822c8c-d6be-4301-a631-0e1416bad28f}')
CLSID_WICXMPSeqMetadataReader: Guid = Guid('{7f12e753-fc71-43d7-a51d-92f35977abb5}')
CLSID_WICXMPSeqMetadataWriter: Guid = Guid('{6d68d1de-d432-4b0f-923a-091183a9bda7}')
CLSID_WICXMPAltMetadataReader: Guid = Guid('{aa94dcc2-b8b0-4898-b835-000aabd74393}')
CLSID_WICXMPAltMetadataWriter: Guid = Guid('{076c2a6c-f78f-4c46-a723-3583e70876ea}')
CLSID_WICLSDMetadataReader: Guid = Guid('{41070793-59e4-479a-a1f7-954adc2ef5fc}')
CLSID_WICLSDMetadataWriter: Guid = Guid('{73c037e7-e5d9-4954-876a-6da81d6e5768}')
CLSID_WICGCEMetadataReader: Guid = Guid('{b92e345d-f52d-41f3-b562-081bc772e3b9}')
CLSID_WICGCEMetadataWriter: Guid = Guid('{af95dc76-16b2-47f4-b3ea-3c31796693e7}')
CLSID_WICIMDMetadataReader: Guid = Guid('{7447a267-0015-42c8-a8f1-fb3b94c68361}')
CLSID_WICIMDMetadataWriter: Guid = Guid('{8c89071f-452e-4e95-9682-9d1024627172}')
CLSID_WICAPEMetadataReader: Guid = Guid('{1767b93a-b021-44ea-920f-863c11f4f768}')
CLSID_WICAPEMetadataWriter: Guid = Guid('{bd6edfca-2890-482f-b233-8d7339a1cf8d}')
CLSID_WICJpegChrominanceMetadataReader: Guid = Guid('{50b1904b-f28f-4574-93f4-0bade82c69e9}')
CLSID_WICJpegChrominanceMetadataWriter: Guid = Guid('{3ff566f0-6e6b-49d4-96e6-b78886692c62}')
CLSID_WICJpegLuminanceMetadataReader: Guid = Guid('{356f2f88-05a6-4728-b9a4-1bfbce04d838}')
CLSID_WICJpegLuminanceMetadataWriter: Guid = Guid('{1d583abc-8a0e-4657-9982-a380ca58fb4b}')
CLSID_WICJpegCommentMetadataReader: Guid = Guid('{9f66347c-60c4-4c4d-ab58-d2358685f607}')
CLSID_WICJpegCommentMetadataWriter: Guid = Guid('{e573236f-55b1-4eda-81ea-9f65db0290d3}')
CLSID_WICGifCommentMetadataReader: Guid = Guid('{32557d3b-69dc-4f95-836e-f5972b2f6159}')
CLSID_WICGifCommentMetadataWriter: Guid = Guid('{a02797fc-c4ae-418c-af95-e637c7ead2a1}')
CLSID_WICPngGamaMetadataReader: Guid = Guid('{3692ca39-e082-4350-9e1f-3704cb083cd5}')
CLSID_WICPngGamaMetadataWriter: Guid = Guid('{ff036d13-5d4b-46dd-b10f-106693d9fe4f}')
CLSID_WICPngBkgdMetadataReader: Guid = Guid('{0ce7a4a6-03e8-4a60-9d15-282ef32ee7da}')
CLSID_WICPngBkgdMetadataWriter: Guid = Guid('{68e3f2fd-31ae-4441-bb6a-fd7047525f90}')
CLSID_WICPngItxtMetadataReader: Guid = Guid('{aabfb2fa-3e1e-4a8f-8977-5556fb94ea23}')
CLSID_WICPngItxtMetadataWriter: Guid = Guid('{31879719-e751-4df8-981d-68dff67704ed}')
CLSID_WICPngChrmMetadataReader: Guid = Guid('{f90b5f36-367b-402a-9dd1-bc0fd59d8f62}')
CLSID_WICPngChrmMetadataWriter: Guid = Guid('{e23ce3eb-5608-4e83-bcef-27b1987e51d7}')
CLSID_WICPngHistMetadataReader: Guid = Guid('{877a0bb7-a313-4491-87b5-2e6d0594f520}')
CLSID_WICPngHistMetadataWriter: Guid = Guid('{8a03e749-672e-446e-bf1f-2c11d233b6ff}')
CLSID_WICPngIccpMetadataReader: Guid = Guid('{f5d3e63b-cb0f-4628-a478-6d8244be36b1}')
CLSID_WICPngIccpMetadataWriter: Guid = Guid('{16671e5f-0ce6-4cc4-9768-e89fe5018ade}')
CLSID_WICPngSrgbMetadataReader: Guid = Guid('{fb40360c-547e-4956-a3b9-d4418859ba66}')
CLSID_WICPngSrgbMetadataWriter: Guid = Guid('{a6ee35c6-87ec-47df-9f22-1d5aad840c82}')
CLSID_WICPngTimeMetadataReader: Guid = Guid('{d94edf02-efe5-4f0d-85c8-f5a68b3000b1}')
CLSID_WICPngTimeMetadataWriter: Guid = Guid('{1ab78400-b5a3-4d91-8ace-33fcd1499be6}')
CLSID_WICDdsMetadataReader: Guid = Guid('{276c88ca-7533-4a86-b676-66b36080d484}')
CLSID_WICDdsMetadataWriter: Guid = Guid('{fd688bbd-31ed-4db7-a723-934927d38367}')
CLSID_WICHeifMetadataReader: Guid = Guid('{acddfc3f-85ec-41bc-bdef-1bc262e4db05}')
CLSID_WICHeifMetadataWriter: Guid = Guid('{3ae45e79-40bc-4401-ace5-dd3cb16e6afe}')
CLSID_WICHeifHDRMetadataReader: Guid = Guid('{2438de3d-94d9-4be8-84a8-4de95a575e75}')
CLSID_WICWebpAnimMetadataReader: Guid = Guid('{076f9911-a348-465c-a807-a252f3f2d3de}')
CLSID_WICWebpAnmfMetadataReader: Guid = Guid('{85a10b03-c9f6-439f-be5e-c0fbef67807c}')
@winfunctype('WindowsCodecs.dll')
def WICConvertBitmapSource(dstFormat: POINTER(Guid), pISrc: Windows.Win32.Graphics.Imaging.IWICBitmapSource_head, ppIDst: POINTER(Windows.Win32.Graphics.Imaging.IWICBitmapSource_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WindowsCodecs.dll')
def WICCreateBitmapFromSection(width: UInt32, height: UInt32, pixelFormat: POINTER(Guid), hSection: Windows.Win32.Foundation.HANDLE, stride: UInt32, offset: UInt32, ppIBitmap: POINTER(Windows.Win32.Graphics.Imaging.IWICBitmap_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WindowsCodecs.dll')
def WICCreateBitmapFromSectionEx(width: UInt32, height: UInt32, pixelFormat: POINTER(Guid), hSection: Windows.Win32.Foundation.HANDLE, stride: UInt32, offset: UInt32, desiredAccessLevel: Windows.Win32.Graphics.Imaging.WICSectionAccessLevel, ppIBitmap: POINTER(Windows.Win32.Graphics.Imaging.IWICBitmap_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WindowsCodecs.dll')
def WICMapGuidToShortName(guid: POINTER(Guid), cchName: UInt32, wzName: Windows.Win32.Foundation.PWSTR, pcchActual: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WindowsCodecs.dll')
def WICMapShortNameToGuid(wzName: Windows.Win32.Foundation.PWSTR, pguid: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WindowsCodecs.dll')
def WICMapSchemaToName(guidMetadataFormat: POINTER(Guid), pwzSchema: Windows.Win32.Foundation.PWSTR, cchName: UInt32, wzName: Windows.Win32.Foundation.PWSTR, pcchActual: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WindowsCodecs.dll')
def WICMatchMetadataContent(guidContainerFormat: POINTER(Guid), pguidVendor: POINTER(Guid), pIStream: Windows.Win32.System.Com.IStream_head, pguidMetadataFormat: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WindowsCodecs.dll')
def WICSerializeMetadataContent(guidContainerFormat: POINTER(Guid), pIWriter: Windows.Win32.Graphics.Imaging.IWICMetadataWriter_head, dwPersistOptions: UInt32, pIStream: Windows.Win32.System.Com.IStream_head) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WindowsCodecs.dll')
def WICGetMetadataContentSize(guidContainerFormat: POINTER(Guid), pIWriter: Windows.Win32.Graphics.Imaging.IWICMetadataWriter_head, pcbSize: POINTER(UInt64)) -> Windows.Win32.Foundation.HRESULT: ...
class IWICBitmap(ComPtr):
    extends: Windows.Win32.Graphics.Imaging.IWICBitmapSource
    _iid_ = Guid('{00000121-a8f2-4877-ba0a-fd2b6645fb94}')
    @commethod(8)
    def Lock(self, prcLock: POINTER(Windows.Win32.Graphics.Imaging.WICRect_head), flags: UInt32, ppILock: POINTER(Windows.Win32.Graphics.Imaging.IWICBitmapLock_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SetPalette(self, pIPalette: Windows.Win32.Graphics.Imaging.IWICPalette_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SetResolution(self, dpiX: Double, dpiY: Double) -> Windows.Win32.Foundation.HRESULT: ...
class IWICBitmapClipper(ComPtr):
    extends: Windows.Win32.Graphics.Imaging.IWICBitmapSource
    _iid_ = Guid('{e4fbcf03-223d-4e81-9333-d635556dd1b5}')
    @commethod(8)
    def Initialize(self, pISource: Windows.Win32.Graphics.Imaging.IWICBitmapSource_head, prc: POINTER(Windows.Win32.Graphics.Imaging.WICRect_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IWICBitmapCodecInfo(ComPtr):
    extends: Windows.Win32.Graphics.Imaging.IWICComponentInfo
    _iid_ = Guid('{e87a44c4-b76e-4c47-8b09-298eb12a2714}')
    @commethod(11)
    def GetContainerFormat(self, pguidContainerFormat: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetPixelFormats(self, cFormats: UInt32, pguidPixelFormats: POINTER(Guid), pcActual: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetColorManagementVersion(self, cchColorManagementVersion: UInt32, wzColorManagementVersion: Windows.Win32.Foundation.PWSTR, pcchActual: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetDeviceManufacturer(self, cchDeviceManufacturer: UInt32, wzDeviceManufacturer: Windows.Win32.Foundation.PWSTR, pcchActual: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetDeviceModels(self, cchDeviceModels: UInt32, wzDeviceModels: Windows.Win32.Foundation.PWSTR, pcchActual: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def GetMimeTypes(self, cchMimeTypes: UInt32, wzMimeTypes: Windows.Win32.Foundation.PWSTR, pcchActual: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def GetFileExtensions(self, cchFileExtensions: UInt32, wzFileExtensions: Windows.Win32.Foundation.PWSTR, pcchActual: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def DoesSupportAnimation(self, pfSupportAnimation: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def DoesSupportChromakey(self, pfSupportChromakey: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def DoesSupportLossless(self, pfSupportLossless: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def DoesSupportMultiframe(self, pfSupportMultiframe: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def MatchesMimeType(self, wzMimeType: Windows.Win32.Foundation.PWSTR, pfMatches: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
class IWICBitmapCodecProgressNotification(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{64c1024e-c3cf-4462-8078-88c2b11c46d9}')
    @commethod(3)
    def RegisterProgressNotification(self, pfnProgressNotification: Windows.Win32.Graphics.Imaging.PFNProgressNotification, pvData: VoidPtr, dwProgressFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class IWICBitmapDecoder(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{9edde9e7-8dee-47ea-99df-e6faf2ed44bf}')
    @commethod(3)
    def QueryCapability(self, pIStream: Windows.Win32.System.Com.IStream_head, pdwCapability: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Initialize(self, pIStream: Windows.Win32.System.Com.IStream_head, cacheOptions: Windows.Win32.Graphics.Imaging.WICDecodeOptions) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetContainerFormat(self, pguidContainerFormat: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetDecoderInfo(self, ppIDecoderInfo: POINTER(Windows.Win32.Graphics.Imaging.IWICBitmapDecoderInfo_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def CopyPalette(self, pIPalette: Windows.Win32.Graphics.Imaging.IWICPalette_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetMetadataQueryReader(self, ppIMetadataQueryReader: POINTER(Windows.Win32.Graphics.Imaging.IWICMetadataQueryReader_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetPreview(self, ppIBitmapSource: POINTER(Windows.Win32.Graphics.Imaging.IWICBitmapSource_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetColorContexts(self, cCount: UInt32, ppIColorContexts: POINTER(Windows.Win32.Graphics.Imaging.IWICColorContext_head), pcActualCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetThumbnail(self, ppIThumbnail: POINTER(Windows.Win32.Graphics.Imaging.IWICBitmapSource_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetFrameCount(self, pCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetFrame(self, index: UInt32, ppIBitmapFrame: POINTER(Windows.Win32.Graphics.Imaging.IWICBitmapFrameDecode_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IWICBitmapDecoderInfo(ComPtr):
    extends: Windows.Win32.Graphics.Imaging.IWICBitmapCodecInfo
    _iid_ = Guid('{d8cd007f-d08f-4191-9bfc-236ea7f0e4b5}')
    @commethod(23)
    def GetPatterns(self, cbSizePatterns: UInt32, pPatterns: POINTER(Windows.Win32.Graphics.Imaging.WICBitmapPattern_head), pcPatterns: POINTER(UInt32), pcbPatternsActual: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def MatchesPattern(self, pIStream: Windows.Win32.System.Com.IStream_head, pfMatches: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def CreateInstance(self, ppIBitmapDecoder: POINTER(Windows.Win32.Graphics.Imaging.IWICBitmapDecoder_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IWICBitmapEncoder(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{00000103-a8f2-4877-ba0a-fd2b6645fb94}')
    @commethod(3)
    def Initialize(self, pIStream: Windows.Win32.System.Com.IStream_head, cacheOption: Windows.Win32.Graphics.Imaging.WICBitmapEncoderCacheOption) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetContainerFormat(self, pguidContainerFormat: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetEncoderInfo(self, ppIEncoderInfo: POINTER(Windows.Win32.Graphics.Imaging.IWICBitmapEncoderInfo_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetColorContexts(self, cCount: UInt32, ppIColorContext: POINTER(Windows.Win32.Graphics.Imaging.IWICColorContext_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetPalette(self, pIPalette: Windows.Win32.Graphics.Imaging.IWICPalette_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetThumbnail(self, pIThumbnail: Windows.Win32.Graphics.Imaging.IWICBitmapSource_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SetPreview(self, pIPreview: Windows.Win32.Graphics.Imaging.IWICBitmapSource_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def CreateNewFrame(self, ppIFrameEncode: POINTER(Windows.Win32.Graphics.Imaging.IWICBitmapFrameEncode_head), ppIEncoderOptions: POINTER(Windows.Win32.System.Com.StructuredStorage.IPropertyBag2_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Commit(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetMetadataQueryWriter(self, ppIMetadataQueryWriter: POINTER(Windows.Win32.Graphics.Imaging.IWICMetadataQueryWriter_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IWICBitmapEncoderInfo(ComPtr):
    extends: Windows.Win32.Graphics.Imaging.IWICBitmapCodecInfo
    _iid_ = Guid('{94c9b4ee-a09f-4f92-8a1e-4a9bce7e76fb}')
    @commethod(23)
    def CreateInstance(self, ppIBitmapEncoder: POINTER(Windows.Win32.Graphics.Imaging.IWICBitmapEncoder_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IWICBitmapFlipRotator(ComPtr):
    extends: Windows.Win32.Graphics.Imaging.IWICBitmapSource
    _iid_ = Guid('{5009834f-2d6a-41ce-9e1b-17c5aff7a782}')
    @commethod(8)
    def Initialize(self, pISource: Windows.Win32.Graphics.Imaging.IWICBitmapSource_head, options: Windows.Win32.Graphics.Imaging.WICBitmapTransformOptions) -> Windows.Win32.Foundation.HRESULT: ...
class IWICBitmapFrameDecode(ComPtr):
    extends: Windows.Win32.Graphics.Imaging.IWICBitmapSource
    _iid_ = Guid('{3b16811b-6a43-4ec9-a813-3d930c13b940}')
    @commethod(8)
    def GetMetadataQueryReader(self, ppIMetadataQueryReader: POINTER(Windows.Win32.Graphics.Imaging.IWICMetadataQueryReader_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetColorContexts(self, cCount: UInt32, ppIColorContexts: POINTER(Windows.Win32.Graphics.Imaging.IWICColorContext_head), pcActualCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetThumbnail(self, ppIThumbnail: POINTER(Windows.Win32.Graphics.Imaging.IWICBitmapSource_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IWICBitmapFrameEncode(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{00000105-a8f2-4877-ba0a-fd2b6645fb94}')
    @commethod(3)
    def Initialize(self, pIEncoderOptions: Windows.Win32.System.Com.StructuredStorage.IPropertyBag2_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetSize(self, uiWidth: UInt32, uiHeight: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetResolution(self, dpiX: Double, dpiY: Double) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetPixelFormat(self, pPixelFormat: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetColorContexts(self, cCount: UInt32, ppIColorContext: POINTER(Windows.Win32.Graphics.Imaging.IWICColorContext_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetPalette(self, pIPalette: Windows.Win32.Graphics.Imaging.IWICPalette_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SetThumbnail(self, pIThumbnail: Windows.Win32.Graphics.Imaging.IWICBitmapSource_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def WritePixels(self, lineCount: UInt32, cbStride: UInt32, cbBufferSize: UInt32, pbPixels: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def WriteSource(self, pIBitmapSource: Windows.Win32.Graphics.Imaging.IWICBitmapSource_head, prc: POINTER(Windows.Win32.Graphics.Imaging.WICRect_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def Commit(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetMetadataQueryWriter(self, ppIMetadataQueryWriter: POINTER(Windows.Win32.Graphics.Imaging.IWICMetadataQueryWriter_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IWICBitmapLock(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{00000123-a8f2-4877-ba0a-fd2b6645fb94}')
    @commethod(3)
    def GetSize(self, puiWidth: POINTER(UInt32), puiHeight: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetStride(self, pcbStride: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetDataPointer(self, pcbBufferSize: POINTER(UInt32), ppbData: POINTER(POINTER(Byte))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetPixelFormat(self, pPixelFormat: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
class IWICBitmapScaler(ComPtr):
    extends: Windows.Win32.Graphics.Imaging.IWICBitmapSource
    _iid_ = Guid('{00000302-a8f2-4877-ba0a-fd2b6645fb94}')
    @commethod(8)
    def Initialize(self, pISource: Windows.Win32.Graphics.Imaging.IWICBitmapSource_head, uiWidth: UInt32, uiHeight: UInt32, mode: Windows.Win32.Graphics.Imaging.WICBitmapInterpolationMode) -> Windows.Win32.Foundation.HRESULT: ...
class IWICBitmapSource(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{00000120-a8f2-4877-ba0a-fd2b6645fb94}')
    @commethod(3)
    def GetSize(self, puiWidth: POINTER(UInt32), puiHeight: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetPixelFormat(self, pPixelFormat: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetResolution(self, pDpiX: POINTER(Double), pDpiY: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def CopyPalette(self, pIPalette: Windows.Win32.Graphics.Imaging.IWICPalette_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def CopyPixels(self, prc: POINTER(Windows.Win32.Graphics.Imaging.WICRect_head), cbStride: UInt32, cbBufferSize: UInt32, pbBuffer: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
class IWICBitmapSourceTransform(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{3b16811b-6a43-4ec9-b713-3d5a0c13b940}')
    @commethod(3)
    def CopyPixels(self, prc: POINTER(Windows.Win32.Graphics.Imaging.WICRect_head), uiWidth: UInt32, uiHeight: UInt32, pguidDstFormat: POINTER(Guid), dstTransform: Windows.Win32.Graphics.Imaging.WICBitmapTransformOptions, nStride: UInt32, cbBufferSize: UInt32, pbBuffer: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetClosestSize(self, puiWidth: POINTER(UInt32), puiHeight: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetClosestPixelFormat(self, pguidDstFormat: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def DoesSupportTransform(self, dstTransform: Windows.Win32.Graphics.Imaging.WICBitmapTransformOptions, pfIsSupported: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
class IWICColorContext(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{3c613a02-34b2-44ea-9a7c-45aea9c6fd6d}')
    @commethod(3)
    def InitializeFromFilename(self, wzFilename: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def InitializeFromMemory(self, pbBuffer: POINTER(Byte), cbBufferSize: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def InitializeFromExifColorSpace(self, value: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetType(self, pType: POINTER(Windows.Win32.Graphics.Imaging.WICColorContextType)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetProfileBytes(self, cbBuffer: UInt32, pbBuffer: POINTER(Byte), pcbActual: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetExifColorSpace(self, pValue: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IWICColorTransform(ComPtr):
    extends: Windows.Win32.Graphics.Imaging.IWICBitmapSource
    _iid_ = Guid('{b66f034f-d0e2-40ab-b436-6de39e321a94}')
    @commethod(8)
    def Initialize(self, pIBitmapSource: Windows.Win32.Graphics.Imaging.IWICBitmapSource_head, pIContextSource: Windows.Win32.Graphics.Imaging.IWICColorContext_head, pIContextDest: Windows.Win32.Graphics.Imaging.IWICColorContext_head, pixelFmtDest: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
class IWICComponentFactory(ComPtr):
    extends: Windows.Win32.Graphics.Imaging.IWICImagingFactory
    _iid_ = Guid('{412d0c3a-9650-44fa-af5b-dd2a06c8e8fb}')
    @commethod(28)
    def CreateMetadataReader(self, guidMetadataFormat: POINTER(Guid), pguidVendor: POINTER(Guid), dwOptions: UInt32, pIStream: Windows.Win32.System.Com.IStream_head, ppIReader: POINTER(Windows.Win32.Graphics.Imaging.IWICMetadataReader_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def CreateMetadataReaderFromContainer(self, guidContainerFormat: POINTER(Guid), pguidVendor: POINTER(Guid), dwOptions: UInt32, pIStream: Windows.Win32.System.Com.IStream_head, ppIReader: POINTER(Windows.Win32.Graphics.Imaging.IWICMetadataReader_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def CreateMetadataWriter(self, guidMetadataFormat: POINTER(Guid), pguidVendor: POINTER(Guid), dwMetadataOptions: UInt32, ppIWriter: POINTER(Windows.Win32.Graphics.Imaging.IWICMetadataWriter_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def CreateMetadataWriterFromReader(self, pIReader: Windows.Win32.Graphics.Imaging.IWICMetadataReader_head, pguidVendor: POINTER(Guid), ppIWriter: POINTER(Windows.Win32.Graphics.Imaging.IWICMetadataWriter_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def CreateQueryReaderFromBlockReader(self, pIBlockReader: Windows.Win32.Graphics.Imaging.IWICMetadataBlockReader_head, ppIQueryReader: POINTER(Windows.Win32.Graphics.Imaging.IWICMetadataQueryReader_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def CreateQueryWriterFromBlockWriter(self, pIBlockWriter: Windows.Win32.Graphics.Imaging.IWICMetadataBlockWriter_head, ppIQueryWriter: POINTER(Windows.Win32.Graphics.Imaging.IWICMetadataQueryWriter_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def CreateEncoderPropertyBag(self, ppropOptions: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPBAG2_head), cCount: UInt32, ppIPropertyBag: POINTER(Windows.Win32.System.Com.StructuredStorage.IPropertyBag2_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IWICComponentInfo(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{23bc3f0a-698b-4357-886b-f24d50671334}')
    @commethod(3)
    def GetComponentType(self, pType: POINTER(Windows.Win32.Graphics.Imaging.WICComponentType)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetCLSID(self, pclsid: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetSigningStatus(self, pStatus: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetAuthor(self, cchAuthor: UInt32, wzAuthor: Windows.Win32.Foundation.PWSTR, pcchActual: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetVendorGUID(self, pguidVendor: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetVersion(self, cchVersion: UInt32, wzVersion: Windows.Win32.Foundation.PWSTR, pcchActual: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetSpecVersion(self, cchSpecVersion: UInt32, wzSpecVersion: Windows.Win32.Foundation.PWSTR, pcchActual: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetFriendlyName(self, cchFriendlyName: UInt32, wzFriendlyName: Windows.Win32.Foundation.PWSTR, pcchActual: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IWICDdsDecoder(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{409cd537-8532-40cb-9774-e2feb2df4e9c}')
    @commethod(3)
    def GetParameters(self, pParameters: POINTER(Windows.Win32.Graphics.Imaging.WICDdsParameters_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetFrame(self, arrayIndex: UInt32, mipLevel: UInt32, sliceIndex: UInt32, ppIBitmapFrame: POINTER(Windows.Win32.Graphics.Imaging.IWICBitmapFrameDecode_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IWICDdsEncoder(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{5cacdb4c-407e-41b3-b936-d0f010cd6732}')
    @commethod(3)
    def SetParameters(self, pParameters: POINTER(Windows.Win32.Graphics.Imaging.WICDdsParameters_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetParameters(self, pParameters: POINTER(Windows.Win32.Graphics.Imaging.WICDdsParameters_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def CreateNewFrame(self, ppIFrameEncode: POINTER(Windows.Win32.Graphics.Imaging.IWICBitmapFrameEncode_head), pArrayIndex: POINTER(UInt32), pMipLevel: POINTER(UInt32), pSliceIndex: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IWICDdsFrameDecode(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{3d4c0c61-18a4-41e4-bd80-481a4fc9f464}')
    @commethod(3)
    def GetSizeInBlocks(self, pWidthInBlocks: POINTER(UInt32), pHeightInBlocks: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetFormatInfo(self, pFormatInfo: POINTER(Windows.Win32.Graphics.Imaging.WICDdsFormatInfo_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def CopyBlocks(self, prcBoundsInBlocks: POINTER(Windows.Win32.Graphics.Imaging.WICRect_head), cbStride: UInt32, cbBufferSize: UInt32, pbBuffer: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
class IWICDevelopRaw(ComPtr):
    extends: Windows.Win32.Graphics.Imaging.IWICBitmapFrameDecode
    _iid_ = Guid('{fbec5e44-f7be-4b65-b7f8-c0c81fef026d}')
    @commethod(11)
    def QueryRawCapabilitiesInfo(self, pInfo: POINTER(Windows.Win32.Graphics.Imaging.WICRawCapabilitiesInfo_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def LoadParameterSet(self, ParameterSet: Windows.Win32.Graphics.Imaging.WICRawParameterSet) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetCurrentParameterSet(self, ppCurrentParameterSet: POINTER(Windows.Win32.System.Com.StructuredStorage.IPropertyBag2_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def SetExposureCompensation(self, ev: Double) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetExposureCompensation(self, pEV: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def SetWhitePointRGB(self, Red: UInt32, Green: UInt32, Blue: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def GetWhitePointRGB(self, pRed: POINTER(UInt32), pGreen: POINTER(UInt32), pBlue: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def SetNamedWhitePoint(self, WhitePoint: Windows.Win32.Graphics.Imaging.WICNamedWhitePoint) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def GetNamedWhitePoint(self, pWhitePoint: POINTER(Windows.Win32.Graphics.Imaging.WICNamedWhitePoint)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def SetWhitePointKelvin(self, WhitePointKelvin: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def GetWhitePointKelvin(self, pWhitePointKelvin: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def GetKelvinRangeInfo(self, pMinKelvinTemp: POINTER(UInt32), pMaxKelvinTemp: POINTER(UInt32), pKelvinTempStepValue: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def SetContrast(self, Contrast: Double) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def GetContrast(self, pContrast: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def SetGamma(self, Gamma: Double) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def GetGamma(self, pGamma: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def SetSharpness(self, Sharpness: Double) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def GetSharpness(self, pSharpness: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def SetSaturation(self, Saturation: Double) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def GetSaturation(self, pSaturation: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def SetTint(self, Tint: Double) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def GetTint(self, pTint: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def SetNoiseReduction(self, NoiseReduction: Double) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def GetNoiseReduction(self, pNoiseReduction: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def SetDestinationColorContext(self, pColorContext: Windows.Win32.Graphics.Imaging.IWICColorContext_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(36)
    def SetToneCurve(self, cbToneCurveSize: UInt32, pToneCurve: POINTER(Windows.Win32.Graphics.Imaging.WICRawToneCurve_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(37)
    def GetToneCurve(self, cbToneCurveBufferSize: UInt32, pToneCurve: POINTER(Windows.Win32.Graphics.Imaging.WICRawToneCurve_head), pcbActualToneCurveBufferSize: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(38)
    def SetRotation(self, Rotation: Double) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(39)
    def GetRotation(self, pRotation: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(40)
    def SetRenderMode(self, RenderMode: Windows.Win32.Graphics.Imaging.WICRawRenderMode) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(41)
    def GetRenderMode(self, pRenderMode: POINTER(Windows.Win32.Graphics.Imaging.WICRawRenderMode)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(42)
    def SetNotificationCallback(self, pCallback: Windows.Win32.Graphics.Imaging.IWICDevelopRawNotificationCallback_head) -> Windows.Win32.Foundation.HRESULT: ...
class IWICDevelopRawNotificationCallback(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{95c75a6e-3e8c-4ec2-85a8-aebcc551e59b}')
    @commethod(3)
    def Notify(self, NotificationMask: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class IWICEnumMetadataItem(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{dc2bb46d-3f07-481e-8625-220c4aedbb33}')
    @commethod(3)
    def Next(self, celt: UInt32, rgeltSchema: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), rgeltId: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), rgeltValue: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), pceltFetched: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(self, celt: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(self, ppIEnumMetadataItem: POINTER(Windows.Win32.Graphics.Imaging.IWICEnumMetadataItem_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IWICFastMetadataEncoder(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{b84e2c09-78c9-4ac4-8bd3-524ae1663a2f}')
    @commethod(3)
    def Commit(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetMetadataQueryWriter(self, ppIMetadataQueryWriter: POINTER(Windows.Win32.Graphics.Imaging.IWICMetadataQueryWriter_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IWICFormatConverter(ComPtr):
    extends: Windows.Win32.Graphics.Imaging.IWICBitmapSource
    _iid_ = Guid('{00000301-a8f2-4877-ba0a-fd2b6645fb94}')
    @commethod(8)
    def Initialize(self, pISource: Windows.Win32.Graphics.Imaging.IWICBitmapSource_head, dstFormat: POINTER(Guid), dither: Windows.Win32.Graphics.Imaging.WICBitmapDitherType, pIPalette: Windows.Win32.Graphics.Imaging.IWICPalette_head, alphaThresholdPercent: Double, paletteTranslate: Windows.Win32.Graphics.Imaging.WICBitmapPaletteType) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def CanConvert(self, srcPixelFormat: POINTER(Guid), dstPixelFormat: POINTER(Guid), pfCanConvert: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
class IWICFormatConverterInfo(ComPtr):
    extends: Windows.Win32.Graphics.Imaging.IWICComponentInfo
    _iid_ = Guid('{9f34fb65-13f4-4f15-bc57-3726b5e53d9f}')
    @commethod(11)
    def GetPixelFormats(self, cFormats: UInt32, pPixelFormatGUIDs: POINTER(Guid), pcActual: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def CreateInstance(self, ppIConverter: POINTER(Windows.Win32.Graphics.Imaging.IWICFormatConverter_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IWICImagingFactory(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{ec5ec8a9-c395-4314-9c77-54d7a935ff70}')
    @commethod(3)
    def CreateDecoderFromFilename(self, wzFilename: Windows.Win32.Foundation.PWSTR, pguidVendor: POINTER(Guid), dwDesiredAccess: Windows.Win32.Foundation.GENERIC_ACCESS_RIGHTS, metadataOptions: Windows.Win32.Graphics.Imaging.WICDecodeOptions, ppIDecoder: POINTER(Windows.Win32.Graphics.Imaging.IWICBitmapDecoder_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def CreateDecoderFromStream(self, pIStream: Windows.Win32.System.Com.IStream_head, pguidVendor: POINTER(Guid), metadataOptions: Windows.Win32.Graphics.Imaging.WICDecodeOptions, ppIDecoder: POINTER(Windows.Win32.Graphics.Imaging.IWICBitmapDecoder_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def CreateDecoderFromFileHandle(self, hFile: UIntPtr, pguidVendor: POINTER(Guid), metadataOptions: Windows.Win32.Graphics.Imaging.WICDecodeOptions, ppIDecoder: POINTER(Windows.Win32.Graphics.Imaging.IWICBitmapDecoder_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def CreateComponentInfo(self, clsidComponent: POINTER(Guid), ppIInfo: POINTER(Windows.Win32.Graphics.Imaging.IWICComponentInfo_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def CreateDecoder(self, guidContainerFormat: POINTER(Guid), pguidVendor: POINTER(Guid), ppIDecoder: POINTER(Windows.Win32.Graphics.Imaging.IWICBitmapDecoder_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def CreateEncoder(self, guidContainerFormat: POINTER(Guid), pguidVendor: POINTER(Guid), ppIEncoder: POINTER(Windows.Win32.Graphics.Imaging.IWICBitmapEncoder_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def CreatePalette(self, ppIPalette: POINTER(Windows.Win32.Graphics.Imaging.IWICPalette_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def CreateFormatConverter(self, ppIFormatConverter: POINTER(Windows.Win32.Graphics.Imaging.IWICFormatConverter_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def CreateBitmapScaler(self, ppIBitmapScaler: POINTER(Windows.Win32.Graphics.Imaging.IWICBitmapScaler_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def CreateBitmapClipper(self, ppIBitmapClipper: POINTER(Windows.Win32.Graphics.Imaging.IWICBitmapClipper_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def CreateBitmapFlipRotator(self, ppIBitmapFlipRotator: POINTER(Windows.Win32.Graphics.Imaging.IWICBitmapFlipRotator_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def CreateStream(self, ppIWICStream: POINTER(Windows.Win32.Graphics.Imaging.IWICStream_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def CreateColorContext(self, ppIWICColorContext: POINTER(Windows.Win32.Graphics.Imaging.IWICColorContext_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def CreateColorTransformer(self, ppIWICColorTransform: POINTER(Windows.Win32.Graphics.Imaging.IWICColorTransform_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def CreateBitmap(self, uiWidth: UInt32, uiHeight: UInt32, pixelFormat: POINTER(Guid), option: Windows.Win32.Graphics.Imaging.WICBitmapCreateCacheOption, ppIBitmap: POINTER(Windows.Win32.Graphics.Imaging.IWICBitmap_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def CreateBitmapFromSource(self, pIBitmapSource: Windows.Win32.Graphics.Imaging.IWICBitmapSource_head, option: Windows.Win32.Graphics.Imaging.WICBitmapCreateCacheOption, ppIBitmap: POINTER(Windows.Win32.Graphics.Imaging.IWICBitmap_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def CreateBitmapFromSourceRect(self, pIBitmapSource: Windows.Win32.Graphics.Imaging.IWICBitmapSource_head, x: UInt32, y: UInt32, width: UInt32, height: UInt32, ppIBitmap: POINTER(Windows.Win32.Graphics.Imaging.IWICBitmap_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def CreateBitmapFromMemory(self, uiWidth: UInt32, uiHeight: UInt32, pixelFormat: POINTER(Guid), cbStride: UInt32, cbBufferSize: UInt32, pbBuffer: POINTER(Byte), ppIBitmap: POINTER(Windows.Win32.Graphics.Imaging.IWICBitmap_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def CreateBitmapFromHBITMAP(self, hBitmap: Windows.Win32.Graphics.Gdi.HBITMAP, hPalette: Windows.Win32.Graphics.Gdi.HPALETTE, options: Windows.Win32.Graphics.Imaging.WICBitmapAlphaChannelOption, ppIBitmap: POINTER(Windows.Win32.Graphics.Imaging.IWICBitmap_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def CreateBitmapFromHICON(self, hIcon: Windows.Win32.UI.WindowsAndMessaging.HICON, ppIBitmap: POINTER(Windows.Win32.Graphics.Imaging.IWICBitmap_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def CreateComponentEnumerator(self, componentTypes: UInt32, options: UInt32, ppIEnumUnknown: POINTER(Windows.Win32.System.Com.IEnumUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def CreateFastMetadataEncoderFromDecoder(self, pIDecoder: Windows.Win32.Graphics.Imaging.IWICBitmapDecoder_head, ppIFastEncoder: POINTER(Windows.Win32.Graphics.Imaging.IWICFastMetadataEncoder_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def CreateFastMetadataEncoderFromFrameDecode(self, pIFrameDecoder: Windows.Win32.Graphics.Imaging.IWICBitmapFrameDecode_head, ppIFastEncoder: POINTER(Windows.Win32.Graphics.Imaging.IWICFastMetadataEncoder_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def CreateQueryWriter(self, guidMetadataFormat: POINTER(Guid), pguidVendor: POINTER(Guid), ppIQueryWriter: POINTER(Windows.Win32.Graphics.Imaging.IWICMetadataQueryWriter_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def CreateQueryWriterFromReader(self, pIQueryReader: Windows.Win32.Graphics.Imaging.IWICMetadataQueryReader_head, pguidVendor: POINTER(Guid), ppIQueryWriter: POINTER(Windows.Win32.Graphics.Imaging.IWICMetadataQueryWriter_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IWICJpegFrameDecode(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{8939f66e-c46a-4c21-a9d1-98b327ce1679}')
    @commethod(3)
    def DoesSupportIndexing(self, pfIndexingSupported: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetIndexing(self, options: Windows.Win32.Graphics.Imaging.WICJpegIndexingOptions, horizontalIntervalSize: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def ClearIndexing(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetAcHuffmanTable(self, scanIndex: UInt32, tableIndex: UInt32, pAcHuffmanTable: POINTER(Windows.Win32.Graphics.Dxgi.Common.DXGI_JPEG_AC_HUFFMAN_TABLE_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetDcHuffmanTable(self, scanIndex: UInt32, tableIndex: UInt32, pDcHuffmanTable: POINTER(Windows.Win32.Graphics.Dxgi.Common.DXGI_JPEG_DC_HUFFMAN_TABLE_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetQuantizationTable(self, scanIndex: UInt32, tableIndex: UInt32, pQuantizationTable: POINTER(Windows.Win32.Graphics.Dxgi.Common.DXGI_JPEG_QUANTIZATION_TABLE_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetFrameHeader(self, pFrameHeader: POINTER(Windows.Win32.Graphics.Imaging.WICJpegFrameHeader_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetScanHeader(self, scanIndex: UInt32, pScanHeader: POINTER(Windows.Win32.Graphics.Imaging.WICJpegScanHeader_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def CopyScan(self, scanIndex: UInt32, scanOffset: UInt32, cbScanData: UInt32, pbScanData: POINTER(Byte), pcbScanDataActual: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def CopyMinimalStream(self, streamOffset: UInt32, cbStreamData: UInt32, pbStreamData: POINTER(Byte), pcbStreamDataActual: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IWICJpegFrameEncode(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{2f0c601f-d2c6-468c-abfa-49495d983ed1}')
    @commethod(3)
    def GetAcHuffmanTable(self, scanIndex: UInt32, tableIndex: UInt32, pAcHuffmanTable: POINTER(Windows.Win32.Graphics.Dxgi.Common.DXGI_JPEG_AC_HUFFMAN_TABLE_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetDcHuffmanTable(self, scanIndex: UInt32, tableIndex: UInt32, pDcHuffmanTable: POINTER(Windows.Win32.Graphics.Dxgi.Common.DXGI_JPEG_DC_HUFFMAN_TABLE_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetQuantizationTable(self, scanIndex: UInt32, tableIndex: UInt32, pQuantizationTable: POINTER(Windows.Win32.Graphics.Dxgi.Common.DXGI_JPEG_QUANTIZATION_TABLE_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def WriteScan(self, cbScanData: UInt32, pbScanData: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
class IWICMetadataBlockReader(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{feaa2a8d-b3f3-43e4-b25c-d1de990a1ae1}')
    @commethod(3)
    def GetContainerFormat(self, pguidContainerFormat: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetCount(self, pcCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetReaderByIndex(self, nIndex: UInt32, ppIMetadataReader: POINTER(Windows.Win32.Graphics.Imaging.IWICMetadataReader_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetEnumerator(self, ppIEnumMetadata: POINTER(Windows.Win32.System.Com.IEnumUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IWICMetadataBlockWriter(ComPtr):
    extends: Windows.Win32.Graphics.Imaging.IWICMetadataBlockReader
    _iid_ = Guid('{08fb9676-b444-41e8-8dbe-6a53a542bff1}')
    @commethod(7)
    def InitializeFromBlockReader(self, pIMDBlockReader: Windows.Win32.Graphics.Imaging.IWICMetadataBlockReader_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetWriterByIndex(self, nIndex: UInt32, ppIMetadataWriter: POINTER(Windows.Win32.Graphics.Imaging.IWICMetadataWriter_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def AddWriter(self, pIMetadataWriter: Windows.Win32.Graphics.Imaging.IWICMetadataWriter_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SetWriterByIndex(self, nIndex: UInt32, pIMetadataWriter: Windows.Win32.Graphics.Imaging.IWICMetadataWriter_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def RemoveWriterByIndex(self, nIndex: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class IWICMetadataHandlerInfo(ComPtr):
    extends: Windows.Win32.Graphics.Imaging.IWICComponentInfo
    _iid_ = Guid('{aba958bf-c672-44d1-8d61-ce6df2e682c2}')
    @commethod(11)
    def GetMetadataFormat(self, pguidMetadataFormat: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetContainerFormats(self, cContainerFormats: UInt32, pguidContainerFormats: POINTER(Guid), pcchActual: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetDeviceManufacturer(self, cchDeviceManufacturer: UInt32, wzDeviceManufacturer: Windows.Win32.Foundation.PWSTR, pcchActual: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetDeviceModels(self, cchDeviceModels: UInt32, wzDeviceModels: Windows.Win32.Foundation.PWSTR, pcchActual: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def DoesRequireFullStream(self, pfRequiresFullStream: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def DoesSupportPadding(self, pfSupportsPadding: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def DoesRequireFixedSize(self, pfFixedSize: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
class IWICMetadataQueryReader(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{30989668-e1c9-4597-b395-458eedb808df}')
    @commethod(3)
    def GetContainerFormat(self, pguidContainerFormat: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetLocation(self, cchMaxLength: UInt32, wzNamespace: Windows.Win32.Foundation.PWSTR, pcchActualLength: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetMetadataByName(self, wzName: Windows.Win32.Foundation.PWSTR, pvarValue: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetEnumerator(self, ppIEnumString: POINTER(Windows.Win32.System.Com.IEnumString_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IWICMetadataQueryWriter(ComPtr):
    extends: Windows.Win32.Graphics.Imaging.IWICMetadataQueryReader
    _iid_ = Guid('{a721791a-0def-4d06-bd91-2118bf1db10b}')
    @commethod(7)
    def SetMetadataByName(self, wzName: Windows.Win32.Foundation.PWSTR, pvarValue: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def RemoveMetadataByName(self, wzName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
class IWICMetadataReader(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{9204fe99-d8fc-4fd5-a001-9536b067a899}')
    @commethod(3)
    def GetMetadataFormat(self, pguidMetadataFormat: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetMetadataHandlerInfo(self, ppIHandler: POINTER(Windows.Win32.Graphics.Imaging.IWICMetadataHandlerInfo_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetCount(self, pcCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetValueByIndex(self, nIndex: UInt32, pvarSchema: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), pvarId: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), pvarValue: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetValue(self, pvarSchema: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), pvarId: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), pvarValue: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetEnumerator(self, ppIEnumMetadata: POINTER(Windows.Win32.Graphics.Imaging.IWICEnumMetadataItem_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IWICMetadataReaderInfo(ComPtr):
    extends: Windows.Win32.Graphics.Imaging.IWICMetadataHandlerInfo
    _iid_ = Guid('{eebf1f5b-07c1-4447-a3ab-22acaf78a804}')
    @commethod(18)
    def GetPatterns(self, guidContainerFormat: POINTER(Guid), cbSize: UInt32, pPattern: POINTER(Windows.Win32.Graphics.Imaging.WICMetadataPattern_head), pcCount: POINTER(UInt32), pcbActual: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def MatchesPattern(self, guidContainerFormat: POINTER(Guid), pIStream: Windows.Win32.System.Com.IStream_head, pfMatches: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def CreateInstance(self, ppIReader: POINTER(Windows.Win32.Graphics.Imaging.IWICMetadataReader_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IWICMetadataWriter(ComPtr):
    extends: Windows.Win32.Graphics.Imaging.IWICMetadataReader
    _iid_ = Guid('{f7836e16-3be0-470b-86bb-160d0aecd7de}')
    @commethod(9)
    def SetValue(self, pvarSchema: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), pvarId: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), pvarValue: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SetValueByIndex(self, nIndex: UInt32, pvarSchema: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), pvarId: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), pvarValue: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def RemoveValue(self, pvarSchema: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), pvarId: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def RemoveValueByIndex(self, nIndex: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class IWICMetadataWriterInfo(ComPtr):
    extends: Windows.Win32.Graphics.Imaging.IWICMetadataHandlerInfo
    _iid_ = Guid('{b22e3fba-3925-4323-b5c1-9ebfc430f236}')
    @commethod(18)
    def GetHeader(self, guidContainerFormat: POINTER(Guid), cbSize: UInt32, pHeader: POINTER(Windows.Win32.Graphics.Imaging.WICMetadataHeader_head), pcbActual: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def CreateInstance(self, ppIWriter: POINTER(Windows.Win32.Graphics.Imaging.IWICMetadataWriter_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IWICPalette(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{00000040-a8f2-4877-ba0a-fd2b6645fb94}')
    @commethod(3)
    def InitializePredefined(self, ePaletteType: Windows.Win32.Graphics.Imaging.WICBitmapPaletteType, fAddTransparentColor: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def InitializeCustom(self, pColors: POINTER(UInt32), cCount: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def InitializeFromBitmap(self, pISurface: Windows.Win32.Graphics.Imaging.IWICBitmapSource_head, cCount: UInt32, fAddTransparentColor: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def InitializeFromPalette(self, pIPalette: Windows.Win32.Graphics.Imaging.IWICPalette_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetType(self, pePaletteType: POINTER(Windows.Win32.Graphics.Imaging.WICBitmapPaletteType)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetColorCount(self, pcCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetColors(self, cCount: UInt32, pColors: POINTER(UInt32), pcActualColors: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def IsBlackWhite(self, pfIsBlackWhite: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def IsGrayscale(self, pfIsGrayscale: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def HasAlpha(self, pfHasAlpha: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
class IWICPersistStream(ComPtr):
    extends: Windows.Win32.System.Com.IPersistStream
    _iid_ = Guid('{00675040-6908-45f8-86a3-49c7dfd6d9ad}')
    @commethod(8)
    def LoadEx(self, pIStream: Windows.Win32.System.Com.IStream_head, pguidPreferredVendor: POINTER(Guid), dwPersistOptions: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SaveEx(self, pIStream: Windows.Win32.System.Com.IStream_head, dwPersistOptions: UInt32, fClearDirty: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
class IWICPixelFormatInfo(ComPtr):
    extends: Windows.Win32.Graphics.Imaging.IWICComponentInfo
    _iid_ = Guid('{e8eda601-3d48-431a-ab44-69059be88bbe}')
    @commethod(11)
    def GetFormatGUID(self, pFormat: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetColorContext(self, ppIColorContext: POINTER(Windows.Win32.Graphics.Imaging.IWICColorContext_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetBitsPerPixel(self, puiBitsPerPixel: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetChannelCount(self, puiChannelCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetChannelMask(self, uiChannelIndex: UInt32, cbMaskBuffer: UInt32, pbMaskBuffer: POINTER(Byte), pcbActual: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IWICPixelFormatInfo2(ComPtr):
    extends: Windows.Win32.Graphics.Imaging.IWICPixelFormatInfo
    _iid_ = Guid('{a9db33a2-af5f-43c7-b679-74f5984b5aa4}')
    @commethod(16)
    def SupportsTransparency(self, pfSupportsTransparency: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def GetNumericRepresentation(self, pNumericRepresentation: POINTER(Windows.Win32.Graphics.Imaging.WICPixelFormatNumericRepresentation)) -> Windows.Win32.Foundation.HRESULT: ...
class IWICPlanarBitmapFrameEncode(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{f928b7b8-2221-40c1-b72e-7e82f1974d1a}')
    @commethod(3)
    def WritePixels(self, lineCount: UInt32, pPlanes: POINTER(Windows.Win32.Graphics.Imaging.WICBitmapPlane_head), cPlanes: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def WriteSource(self, ppPlanes: POINTER(Windows.Win32.Graphics.Imaging.IWICBitmapSource_head), cPlanes: UInt32, prcSource: POINTER(Windows.Win32.Graphics.Imaging.WICRect_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IWICPlanarBitmapSourceTransform(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{3aff9cce-be95-4303-b927-e7d16ff4a613}')
    @commethod(3)
    def DoesSupportTransform(self, puiWidth: POINTER(UInt32), puiHeight: POINTER(UInt32), dstTransform: Windows.Win32.Graphics.Imaging.WICBitmapTransformOptions, dstPlanarOptions: Windows.Win32.Graphics.Imaging.WICPlanarOptions, pguidDstFormats: POINTER(Guid), pPlaneDescriptions: POINTER(Windows.Win32.Graphics.Imaging.WICBitmapPlaneDescription_head), cPlanes: UInt32, pfIsSupported: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def CopyPixels(self, prcSource: POINTER(Windows.Win32.Graphics.Imaging.WICRect_head), uiWidth: UInt32, uiHeight: UInt32, dstTransform: Windows.Win32.Graphics.Imaging.WICBitmapTransformOptions, dstPlanarOptions: Windows.Win32.Graphics.Imaging.WICPlanarOptions, pDstPlanes: POINTER(Windows.Win32.Graphics.Imaging.WICBitmapPlane_head), cPlanes: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class IWICPlanarFormatConverter(ComPtr):
    extends: Windows.Win32.Graphics.Imaging.IWICBitmapSource
    _iid_ = Guid('{bebee9cb-83b0-4dcc-8132-b0aaa55eac96}')
    @commethod(8)
    def Initialize(self, ppPlanes: POINTER(Windows.Win32.Graphics.Imaging.IWICBitmapSource_head), cPlanes: UInt32, dstFormat: POINTER(Guid), dither: Windows.Win32.Graphics.Imaging.WICBitmapDitherType, pIPalette: Windows.Win32.Graphics.Imaging.IWICPalette_head, alphaThresholdPercent: Double, paletteTranslate: Windows.Win32.Graphics.Imaging.WICBitmapPaletteType) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def CanConvert(self, pSrcPixelFormats: POINTER(Guid), cSrcPlanes: UInt32, dstPixelFormat: POINTER(Guid), pfCanConvert: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
class IWICProgressCallback(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{4776f9cd-9517-45fa-bf24-e89c5ec5c60c}')
    @commethod(3)
    def Notify(self, uFrameNum: UInt32, operation: Windows.Win32.Graphics.Imaging.WICProgressOperation, dblProgress: Double) -> Windows.Win32.Foundation.HRESULT: ...
class IWICProgressiveLevelControl(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{daac296f-7aa5-4dbf-8d15-225c5976f891}')
    @commethod(3)
    def GetLevelCount(self, pcLevels: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetCurrentLevel(self, pnLevel: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetCurrentLevel(self, nLevel: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class IWICStream(ComPtr):
    extends: Windows.Win32.System.Com.IStream
    _iid_ = Guid('{135ff860-22b7-4ddf-b0f6-218f4f299a43}')
    @commethod(14)
    def InitializeFromIStream(self, pIStream: Windows.Win32.System.Com.IStream_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def InitializeFromFilename(self, wzFileName: Windows.Win32.Foundation.PWSTR, dwDesiredAccess: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def InitializeFromMemory(self, pbBuffer: POINTER(Byte), cbBufferSize: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def InitializeFromIStreamRegion(self, pIStream: Windows.Win32.System.Com.IStream_head, ulOffset: UInt64, ulMaxSize: UInt64) -> Windows.Win32.Foundation.HRESULT: ...
class IWICStreamProvider(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{449494bc-b468-4927-96d7-ba90d31ab505}')
    @commethod(3)
    def GetStream(self, ppIStream: POINTER(Windows.Win32.System.Com.IStream_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetPersistOptions(self, pdwPersistOptions: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetPreferredVendorGUID(self, pguidPreferredVendor: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def RefreshStream(self) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PFNProgressNotification(pvData: VoidPtr, uFrameNum: UInt32, operation: Windows.Win32.Graphics.Imaging.WICProgressOperation, dblProgress: Double) -> Windows.Win32.Foundation.HRESULT: ...
WIC8BIMIptcDigestProperties = UInt32
WIC8BIMIptcDigestProperties_WIC8BIMIptcDigestPString: WIC8BIMIptcDigestProperties = 1
WIC8BIMIptcDigestProperties_WIC8BIMIptcDigestIptcDigest: WIC8BIMIptcDigestProperties = 2
WIC8BIMIptcProperties = UInt32
WIC8BIMIptcProperties_WIC8BIMIptcPString: WIC8BIMIptcProperties = 0
WIC8BIMIptcProperties_WIC8BIMIptcEmbeddedIPTC: WIC8BIMIptcProperties = 1
WIC8BIMResolutionInfoProperties = UInt32
WIC8BIMResolutionInfoProperties_WIC8BIMResolutionInfoPString: WIC8BIMResolutionInfoProperties = 1
WIC8BIMResolutionInfoProperties_WIC8BIMResolutionInfoHResolution: WIC8BIMResolutionInfoProperties = 2
WIC8BIMResolutionInfoProperties_WIC8BIMResolutionInfoHResolutionUnit: WIC8BIMResolutionInfoProperties = 3
WIC8BIMResolutionInfoProperties_WIC8BIMResolutionInfoWidthUnit: WIC8BIMResolutionInfoProperties = 4
WIC8BIMResolutionInfoProperties_WIC8BIMResolutionInfoVResolution: WIC8BIMResolutionInfoProperties = 5
WIC8BIMResolutionInfoProperties_WIC8BIMResolutionInfoVResolutionUnit: WIC8BIMResolutionInfoProperties = 6
WIC8BIMResolutionInfoProperties_WIC8BIMResolutionInfoHeightUnit: WIC8BIMResolutionInfoProperties = 7
WICBitmapAlphaChannelOption = Int32
WICBitmapAlphaChannelOption_WICBitmapUseAlpha: WICBitmapAlphaChannelOption = 0
WICBitmapAlphaChannelOption_WICBitmapUsePremultipliedAlpha: WICBitmapAlphaChannelOption = 1
WICBitmapAlphaChannelOption_WICBitmapIgnoreAlpha: WICBitmapAlphaChannelOption = 2
WICBitmapCreateCacheOption = Int32
WICBitmapCreateCacheOption_WICBitmapNoCache: WICBitmapCreateCacheOption = 0
WICBitmapCreateCacheOption_WICBitmapCacheOnDemand: WICBitmapCreateCacheOption = 1
WICBitmapCreateCacheOption_WICBitmapCacheOnLoad: WICBitmapCreateCacheOption = 2
WICBitmapDecoderCapabilities = Int32
WICBitmapDecoderCapabilities_WICBitmapDecoderCapabilitySameEncoder: WICBitmapDecoderCapabilities = 1
WICBitmapDecoderCapabilities_WICBitmapDecoderCapabilityCanDecodeAllImages: WICBitmapDecoderCapabilities = 2
WICBitmapDecoderCapabilities_WICBitmapDecoderCapabilityCanDecodeSomeImages: WICBitmapDecoderCapabilities = 4
WICBitmapDecoderCapabilities_WICBitmapDecoderCapabilityCanEnumerateMetadata: WICBitmapDecoderCapabilities = 8
WICBitmapDecoderCapabilities_WICBitmapDecoderCapabilityCanDecodeThumbnail: WICBitmapDecoderCapabilities = 16
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
WICBitmapEncoderCacheOption = Int32
WICBitmapEncoderCacheOption_WICBitmapEncoderCacheInMemory: WICBitmapEncoderCacheOption = 0
WICBitmapEncoderCacheOption_WICBitmapEncoderCacheTempFile: WICBitmapEncoderCacheOption = 1
WICBitmapEncoderCacheOption_WICBitmapEncoderNoCache: WICBitmapEncoderCacheOption = 2
WICBitmapInterpolationMode = Int32
WICBitmapInterpolationMode_WICBitmapInterpolationModeNearestNeighbor: WICBitmapInterpolationMode = 0
WICBitmapInterpolationMode_WICBitmapInterpolationModeLinear: WICBitmapInterpolationMode = 1
WICBitmapInterpolationMode_WICBitmapInterpolationModeCubic: WICBitmapInterpolationMode = 2
WICBitmapInterpolationMode_WICBitmapInterpolationModeFant: WICBitmapInterpolationMode = 3
WICBitmapInterpolationMode_WICBitmapInterpolationModeHighQualityCubic: WICBitmapInterpolationMode = 4
WICBitmapLockFlags = Int32
WICBitmapLockFlags_WICBitmapLockRead: WICBitmapLockFlags = 1
WICBitmapLockFlags_WICBitmapLockWrite: WICBitmapLockFlags = 2
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
class WICBitmapPattern(EasyCastStructure):
    Position: UInt64
    Length: UInt32
    Pattern: POINTER(Byte)
    Mask: POINTER(Byte)
    EndOfStream: Windows.Win32.Foundation.BOOL
class WICBitmapPlane(EasyCastStructure):
    Format: Guid
    pbBuffer: POINTER(Byte)
    cbStride: UInt32
    cbBufferSize: UInt32
class WICBitmapPlaneDescription(EasyCastStructure):
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
WICComponentSigning = Int32
WICComponentSigning_WICComponentSigned: WICComponentSigning = 1
WICComponentSigning_WICComponentUnsigned: WICComponentSigning = 2
WICComponentSigning_WICComponentSafe: WICComponentSigning = 4
WICComponentSigning_WICComponentDisabled: WICComponentSigning = -2147483648
WICComponentType = Int32
WICComponentType_WICDecoder: WICComponentType = 1
WICComponentType_WICEncoder: WICComponentType = 2
WICComponentType_WICPixelFormatConverter: WICComponentType = 4
WICComponentType_WICMetadataReader: WICComponentType = 8
WICComponentType_WICMetadataWriter: WICComponentType = 16
WICComponentType_WICPixelFormat: WICComponentType = 32
WICComponentType_WICAllComponents: WICComponentType = 63
WICDdsAlphaMode = Int32
WICDdsAlphaMode_WICDdsAlphaModeUnknown: WICDdsAlphaMode = 0
WICDdsAlphaMode_WICDdsAlphaModeStraight: WICDdsAlphaMode = 1
WICDdsAlphaMode_WICDdsAlphaModePremultiplied: WICDdsAlphaMode = 2
WICDdsAlphaMode_WICDdsAlphaModeOpaque: WICDdsAlphaMode = 3
WICDdsAlphaMode_WICDdsAlphaModeCustom: WICDdsAlphaMode = 4
WICDdsDimension = Int32
WICDdsDimension_WICDdsTexture1D: WICDdsDimension = 0
WICDdsDimension_WICDdsTexture2D: WICDdsDimension = 1
WICDdsDimension_WICDdsTexture3D: WICDdsDimension = 2
WICDdsDimension_WICDdsTextureCube: WICDdsDimension = 3
class WICDdsFormatInfo(EasyCastStructure):
    DxgiFormat: Windows.Win32.Graphics.Dxgi.Common.DXGI_FORMAT
    BytesPerBlock: UInt32
    BlockWidth: UInt32
    BlockHeight: UInt32
class WICDdsParameters(EasyCastStructure):
    Width: UInt32
    Height: UInt32
    Depth: UInt32
    MipLevels: UInt32
    ArraySize: UInt32
    DxgiFormat: Windows.Win32.Graphics.Dxgi.Common.DXGI_FORMAT
    Dimension: Windows.Win32.Graphics.Imaging.WICDdsDimension
    AlphaMode: Windows.Win32.Graphics.Imaging.WICDdsAlphaMode
WICDecodeOptions = Int32
WICDecodeOptions_WICDecodeMetadataCacheOnDemand: WICDecodeOptions = 0
WICDecodeOptions_WICDecodeMetadataCacheOnLoad: WICDecodeOptions = 1
WICGifApplicationExtensionProperties = UInt32
WICGifApplicationExtensionProperties_WICGifApplicationExtensionApplication: WICGifApplicationExtensionProperties = 1
WICGifApplicationExtensionProperties_WICGifApplicationExtensionData: WICGifApplicationExtensionProperties = 2
WICGifCommentExtensionProperties = UInt32
WICGifCommentExtensionProperties_WICGifCommentExtensionText: WICGifCommentExtensionProperties = 1
WICGifGraphicControlExtensionProperties = UInt32
WICGifGraphicControlExtensionProperties_WICGifGraphicControlExtensionDisposal: WICGifGraphicControlExtensionProperties = 1
WICGifGraphicControlExtensionProperties_WICGifGraphicControlExtensionUserInputFlag: WICGifGraphicControlExtensionProperties = 2
WICGifGraphicControlExtensionProperties_WICGifGraphicControlExtensionTransparencyFlag: WICGifGraphicControlExtensionProperties = 3
WICGifGraphicControlExtensionProperties_WICGifGraphicControlExtensionDelay: WICGifGraphicControlExtensionProperties = 4
WICGifGraphicControlExtensionProperties_WICGifGraphicControlExtensionTransparentColorIndex: WICGifGraphicControlExtensionProperties = 5
WICGifImageDescriptorProperties = UInt32
WICGifImageDescriptorProperties_WICGifImageDescriptorLeft: WICGifImageDescriptorProperties = 1
WICGifImageDescriptorProperties_WICGifImageDescriptorTop: WICGifImageDescriptorProperties = 2
WICGifImageDescriptorProperties_WICGifImageDescriptorWidth: WICGifImageDescriptorProperties = 3
WICGifImageDescriptorProperties_WICGifImageDescriptorHeight: WICGifImageDescriptorProperties = 4
WICGifImageDescriptorProperties_WICGifImageDescriptorLocalColorTableFlag: WICGifImageDescriptorProperties = 5
WICGifImageDescriptorProperties_WICGifImageDescriptorInterlaceFlag: WICGifImageDescriptorProperties = 6
WICGifImageDescriptorProperties_WICGifImageDescriptorSortFlag: WICGifImageDescriptorProperties = 7
WICGifImageDescriptorProperties_WICGifImageDescriptorLocalColorTableSize: WICGifImageDescriptorProperties = 8
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
WICHeifHdrProperties = UInt32
WICHeifHdrProperties_WICHeifHdrMaximumLuminanceLevel: WICHeifHdrProperties = 1
WICHeifHdrProperties_WICHeifHdrMaximumFrameAverageLuminanceLevel: WICHeifHdrProperties = 2
WICHeifHdrProperties_WICHeifHdrMinimumMasteringDisplayLuminanceLevel: WICHeifHdrProperties = 3
WICHeifHdrProperties_WICHeifHdrMaximumMasteringDisplayLuminanceLevel: WICHeifHdrProperties = 4
WICHeifHdrProperties_WICHeifHdrCustomVideoPrimaries: WICHeifHdrProperties = 5
WICHeifProperties = UInt32
WICHeifProperties_WICHeifOrientation: WICHeifProperties = 1
class WICImageParameters(EasyCastStructure):
    PixelFormat: Windows.Win32.Graphics.Direct2D.Common.D2D1_PIXEL_FORMAT
    DpiX: Single
    DpiY: Single
    Top: Single
    Left: Single
    PixelWidth: UInt32
    PixelHeight: UInt32
WICJpegChrominanceProperties = UInt32
WICJpegChrominanceProperties_WICJpegChrominanceTable: WICJpegChrominanceProperties = 1
WICJpegCommentProperties = UInt32
WICJpegCommentProperties_WICJpegCommentText: WICJpegCommentProperties = 1
class WICJpegFrameHeader(EasyCastStructure):
    Width: UInt32
    Height: UInt32
    TransferMatrix: Windows.Win32.Graphics.Imaging.WICJpegTransferMatrix
    ScanType: Windows.Win32.Graphics.Imaging.WICJpegScanType
    cComponents: UInt32
    ComponentIdentifiers: UInt32
    SampleFactors: UInt32
    QuantizationTableIndices: UInt32
WICJpegIndexingOptions = UInt32
WICJpegIndexingOptions_WICJpegIndexingOptionsGenerateOnDemand: WICJpegIndexingOptions = 0
WICJpegIndexingOptions_WICJpegIndexingOptionsGenerateOnLoad: WICJpegIndexingOptions = 1
WICJpegLuminanceProperties = UInt32
WICJpegLuminanceProperties_WICJpegLuminanceTable: WICJpegLuminanceProperties = 1
class WICJpegScanHeader(EasyCastStructure):
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
WICJpegTransferMatrix = UInt32
WICJpegTransferMatrix_WICJpegTransferMatrixIdentity: WICJpegTransferMatrix = 0
WICJpegTransferMatrix_WICJpegTransferMatrixBT601: WICJpegTransferMatrix = 1
WICJpegYCrCbSubsamplingOption = Int32
WICJpegYCrCbSubsamplingOption_WICJpegYCrCbSubsamplingDefault: WICJpegYCrCbSubsamplingOption = 0
WICJpegYCrCbSubsamplingOption_WICJpegYCrCbSubsampling420: WICJpegYCrCbSubsamplingOption = 1
WICJpegYCrCbSubsamplingOption_WICJpegYCrCbSubsampling422: WICJpegYCrCbSubsamplingOption = 2
WICJpegYCrCbSubsamplingOption_WICJpegYCrCbSubsampling444: WICJpegYCrCbSubsamplingOption = 3
WICJpegYCrCbSubsamplingOption_WICJpegYCrCbSubsampling440: WICJpegYCrCbSubsamplingOption = 4
WICMetadataCreationOptions = Int32
WICMetadataCreationOptions_WICMetadataCreationDefault: WICMetadataCreationOptions = 0
WICMetadataCreationOptions_WICMetadataCreationAllowUnknown: WICMetadataCreationOptions = 0
WICMetadataCreationOptions_WICMetadataCreationFailUnknown: WICMetadataCreationOptions = 65536
WICMetadataCreationOptions_WICMetadataCreationMask: WICMetadataCreationOptions = -65536
class WICMetadataHeader(EasyCastStructure):
    Position: UInt64
    Length: UInt32
    Header: POINTER(Byte)
    DataOffset: UInt64
class WICMetadataPattern(EasyCastStructure):
    Position: UInt64
    Length: UInt32
    Pattern: POINTER(Byte)
    Mask: POINTER(Byte)
    DataOffset: UInt64
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
WICPlanarOptions = Int32
WICPlanarOptions_WICPlanarOptionsDefault: WICPlanarOptions = 0
WICPlanarOptions_WICPlanarOptionsPreserveSubsampling: WICPlanarOptions = 1
WICPngBkgdProperties = UInt32
WICPngBkgdProperties_WICPngBkgdBackgroundColor: WICPngBkgdProperties = 1
WICPngChrmProperties = UInt32
WICPngChrmProperties_WICPngChrmWhitePointX: WICPngChrmProperties = 1
WICPngChrmProperties_WICPngChrmWhitePointY: WICPngChrmProperties = 2
WICPngChrmProperties_WICPngChrmRedX: WICPngChrmProperties = 3
WICPngChrmProperties_WICPngChrmRedY: WICPngChrmProperties = 4
WICPngChrmProperties_WICPngChrmGreenX: WICPngChrmProperties = 5
WICPngChrmProperties_WICPngChrmGreenY: WICPngChrmProperties = 6
WICPngChrmProperties_WICPngChrmBlueX: WICPngChrmProperties = 7
WICPngChrmProperties_WICPngChrmBlueY: WICPngChrmProperties = 8
WICPngFilterOption = Int32
WICPngFilterOption_WICPngFilterUnspecified: WICPngFilterOption = 0
WICPngFilterOption_WICPngFilterNone: WICPngFilterOption = 1
WICPngFilterOption_WICPngFilterSub: WICPngFilterOption = 2
WICPngFilterOption_WICPngFilterUp: WICPngFilterOption = 3
WICPngFilterOption_WICPngFilterAverage: WICPngFilterOption = 4
WICPngFilterOption_WICPngFilterPaeth: WICPngFilterOption = 5
WICPngFilterOption_WICPngFilterAdaptive: WICPngFilterOption = 6
WICPngGamaProperties = UInt32
WICPngGamaProperties_WICPngGamaGamma: WICPngGamaProperties = 1
WICPngHistProperties = UInt32
WICPngHistProperties_WICPngHistFrequencies: WICPngHistProperties = 1
WICPngIccpProperties = UInt32
WICPngIccpProperties_WICPngIccpProfileName: WICPngIccpProperties = 1
WICPngIccpProperties_WICPngIccpProfileData: WICPngIccpProperties = 2
WICPngItxtProperties = UInt32
WICPngItxtProperties_WICPngItxtKeyword: WICPngItxtProperties = 1
WICPngItxtProperties_WICPngItxtCompressionFlag: WICPngItxtProperties = 2
WICPngItxtProperties_WICPngItxtLanguageTag: WICPngItxtProperties = 3
WICPngItxtProperties_WICPngItxtTranslatedKeyword: WICPngItxtProperties = 4
WICPngItxtProperties_WICPngItxtText: WICPngItxtProperties = 5
WICPngSrgbProperties = UInt32
WICPngSrgbProperties_WICPngSrgbRenderingIntent: WICPngSrgbProperties = 1
WICPngTimeProperties = UInt32
WICPngTimeProperties_WICPngTimeYear: WICPngTimeProperties = 1
WICPngTimeProperties_WICPngTimeMonth: WICPngTimeProperties = 2
WICPngTimeProperties_WICPngTimeDay: WICPngTimeProperties = 3
WICPngTimeProperties_WICPngTimeHour: WICPngTimeProperties = 4
WICPngTimeProperties_WICPngTimeMinute: WICPngTimeProperties = 5
WICPngTimeProperties_WICPngTimeSecond: WICPngTimeProperties = 6
WICProgressNotification = Int32
WICProgressNotification_WICProgressNotificationBegin: WICProgressNotification = 65536
WICProgressNotification_WICProgressNotificationEnd: WICProgressNotification = 131072
WICProgressNotification_WICProgressNotificationFrequent: WICProgressNotification = 262144
WICProgressNotification_WICProgressNotificationAll: WICProgressNotification = -65536
WICProgressOperation = Int32
WICProgressOperation_WICProgressOperationCopyPixels: WICProgressOperation = 1
WICProgressOperation_WICProgressOperationWritePixels: WICProgressOperation = 2
WICProgressOperation_WICProgressOperationAll: WICProgressOperation = 65535
WICRawCapabilities = Int32
WICRawCapabilities_WICRawCapabilityNotSupported: WICRawCapabilities = 0
WICRawCapabilities_WICRawCapabilityGetSupported: WICRawCapabilities = 1
WICRawCapabilities_WICRawCapabilityFullySupported: WICRawCapabilities = 2
class WICRawCapabilitiesInfo(EasyCastStructure):
    cbSize: UInt32
    CodecMajorVersion: UInt32
    CodecMinorVersion: UInt32
    ExposureCompensationSupport: Windows.Win32.Graphics.Imaging.WICRawCapabilities
    ContrastSupport: Windows.Win32.Graphics.Imaging.WICRawCapabilities
    RGBWhitePointSupport: Windows.Win32.Graphics.Imaging.WICRawCapabilities
    NamedWhitePointSupport: Windows.Win32.Graphics.Imaging.WICRawCapabilities
    NamedWhitePointSupportMask: UInt32
    KelvinWhitePointSupport: Windows.Win32.Graphics.Imaging.WICRawCapabilities
    GammaSupport: Windows.Win32.Graphics.Imaging.WICRawCapabilities
    TintSupport: Windows.Win32.Graphics.Imaging.WICRawCapabilities
    SaturationSupport: Windows.Win32.Graphics.Imaging.WICRawCapabilities
    SharpnessSupport: Windows.Win32.Graphics.Imaging.WICRawCapabilities
    NoiseReductionSupport: Windows.Win32.Graphics.Imaging.WICRawCapabilities
    DestinationColorProfileSupport: Windows.Win32.Graphics.Imaging.WICRawCapabilities
    ToneCurveSupport: Windows.Win32.Graphics.Imaging.WICRawCapabilities
    RotationSupport: Windows.Win32.Graphics.Imaging.WICRawRotationCapabilities
    RenderModeSupport: Windows.Win32.Graphics.Imaging.WICRawCapabilities
WICRawParameterSet = Int32
WICRawParameterSet_WICAsShotParameterSet: WICRawParameterSet = 1
WICRawParameterSet_WICUserAdjustedParameterSet: WICRawParameterSet = 2
WICRawParameterSet_WICAutoAdjustedParameterSet: WICRawParameterSet = 3
WICRawRenderMode = Int32
WICRawRenderMode_WICRawRenderModeDraft: WICRawRenderMode = 1
WICRawRenderMode_WICRawRenderModeNormal: WICRawRenderMode = 2
WICRawRenderMode_WICRawRenderModeBestQuality: WICRawRenderMode = 3
WICRawRotationCapabilities = Int32
WICRawRotationCapabilities_WICRawRotationCapabilityNotSupported: WICRawRotationCapabilities = 0
WICRawRotationCapabilities_WICRawRotationCapabilityGetSupported: WICRawRotationCapabilities = 1
WICRawRotationCapabilities_WICRawRotationCapabilityNinetyDegreesSupported: WICRawRotationCapabilities = 2
WICRawRotationCapabilities_WICRawRotationCapabilityFullySupported: WICRawRotationCapabilities = 3
class WICRawToneCurve(EasyCastStructure):
    cPoints: UInt32
    aPoints: Windows.Win32.Graphics.Imaging.WICRawToneCurvePoint * 1
class WICRawToneCurvePoint(EasyCastStructure):
    Input: Double
    Output: Double
class WICRect(EasyCastStructure):
    X: Int32
    Y: Int32
    Width: Int32
    Height: Int32
WICSectionAccessLevel = UInt32
WICSectionAccessLevel_WICSectionAccessLevelRead: WICSectionAccessLevel = 1
WICSectionAccessLevel_WICSectionAccessLevelReadWrite: WICSectionAccessLevel = 3
WICTiffCompressionOption = Int32
WICTiffCompressionOption_WICTiffCompressionDontCare: WICTiffCompressionOption = 0
WICTiffCompressionOption_WICTiffCompressionNone: WICTiffCompressionOption = 1
WICTiffCompressionOption_WICTiffCompressionCCITT3: WICTiffCompressionOption = 2
WICTiffCompressionOption_WICTiffCompressionCCITT4: WICTiffCompressionOption = 3
WICTiffCompressionOption_WICTiffCompressionLZW: WICTiffCompressionOption = 4
WICTiffCompressionOption_WICTiffCompressionRLE: WICTiffCompressionOption = 5
WICTiffCompressionOption_WICTiffCompressionZIP: WICTiffCompressionOption = 6
WICTiffCompressionOption_WICTiffCompressionLZWHDifferencing: WICTiffCompressionOption = 7
WICWebpAnimProperties = UInt32
WICWebpAnimProperties_WICWebpAnimLoopCount: WICWebpAnimProperties = 1
WICWebpAnmfProperties = UInt32
WICWebpAnmfProperties_WICWebpAnmfFrameDuration: WICWebpAnmfProperties = 1
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
