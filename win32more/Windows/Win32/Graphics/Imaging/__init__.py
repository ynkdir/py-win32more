from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.Graphics.Direct2D.Common
import win32more.Windows.Win32.Graphics.Dxgi.Common
import win32more.Windows.Win32.Graphics.Gdi
import win32more.Windows.Win32.Graphics.Imaging
import win32more.Windows.Win32.System.Com
import win32more.Windows.Win32.System.Com.StructuredStorage
import win32more.Windows.Win32.UI.WindowsAndMessaging
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
def WICConvertBitmapSource(dstFormat: POINTER(Guid), pISrc: win32more.Windows.Win32.Graphics.Imaging.IWICBitmapSource, ppIDst: POINTER(win32more.Windows.Win32.Graphics.Imaging.IWICBitmapSource)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WindowsCodecs.dll')
def WICCreateBitmapFromSection(width: UInt32, height: UInt32, pixelFormat: POINTER(Guid), hSection: win32more.Windows.Win32.Foundation.HANDLE, stride: UInt32, offset: UInt32, ppIBitmap: POINTER(win32more.Windows.Win32.Graphics.Imaging.IWICBitmap)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WindowsCodecs.dll')
def WICCreateBitmapFromSectionEx(width: UInt32, height: UInt32, pixelFormat: POINTER(Guid), hSection: win32more.Windows.Win32.Foundation.HANDLE, stride: UInt32, offset: UInt32, desiredAccessLevel: win32more.Windows.Win32.Graphics.Imaging.WICSectionAccessLevel, ppIBitmap: POINTER(win32more.Windows.Win32.Graphics.Imaging.IWICBitmap)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WindowsCodecs.dll')
def WICMapGuidToShortName(guid: POINTER(Guid), cchName: UInt32, wzName: win32more.Windows.Win32.Foundation.PWSTR, pcchActual: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WindowsCodecs.dll')
def WICMapShortNameToGuid(wzName: win32more.Windows.Win32.Foundation.PWSTR, pguid: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WindowsCodecs.dll')
def WICMapSchemaToName(guidMetadataFormat: POINTER(Guid), pwzSchema: win32more.Windows.Win32.Foundation.PWSTR, cchName: UInt32, wzName: win32more.Windows.Win32.Foundation.PWSTR, pcchActual: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WindowsCodecs.dll')
def WICMatchMetadataContent(guidContainerFormat: POINTER(Guid), pguidVendor: POINTER(Guid), pIStream: win32more.Windows.Win32.System.Com.IStream, pguidMetadataFormat: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WindowsCodecs.dll')
def WICSerializeMetadataContent(guidContainerFormat: POINTER(Guid), pIWriter: win32more.Windows.Win32.Graphics.Imaging.IWICMetadataWriter, dwPersistOptions: UInt32, pIStream: win32more.Windows.Win32.System.Com.IStream) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WindowsCodecs.dll')
def WICGetMetadataContentSize(guidContainerFormat: POINTER(Guid), pIWriter: win32more.Windows.Win32.Graphics.Imaging.IWICMetadataWriter, pcbSize: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWICBitmap(ComPtr):
    extends: win32more.Windows.Win32.Graphics.Imaging.IWICBitmapSource
    _iid_ = Guid('{00000121-a8f2-4877-ba0a-fd2b6645fb94}')
    @commethod(8)
    def Lock(self, prcLock: POINTER(win32more.Windows.Win32.Graphics.Imaging.WICRect), flags: UInt32, ppILock: POINTER(win32more.Windows.Win32.Graphics.Imaging.IWICBitmapLock)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SetPalette(self, pIPalette: win32more.Windows.Win32.Graphics.Imaging.IWICPalette) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SetResolution(self, dpiX: Double, dpiY: Double) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWICBitmapClipper(ComPtr):
    extends: win32more.Windows.Win32.Graphics.Imaging.IWICBitmapSource
    _iid_ = Guid('{e4fbcf03-223d-4e81-9333-d635556dd1b5}')
    @commethod(8)
    def Initialize(self, pISource: win32more.Windows.Win32.Graphics.Imaging.IWICBitmapSource, prc: POINTER(win32more.Windows.Win32.Graphics.Imaging.WICRect)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWICBitmapCodecInfo(ComPtr):
    extends: win32more.Windows.Win32.Graphics.Imaging.IWICComponentInfo
    _iid_ = Guid('{e87a44c4-b76e-4c47-8b09-298eb12a2714}')
    @commethod(11)
    def GetContainerFormat(self, pguidContainerFormat: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetPixelFormats(self, cFormats: UInt32, pguidPixelFormats: POINTER(Guid), pcActual: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetColorManagementVersion(self, cchColorManagementVersion: UInt32, wzColorManagementVersion: win32more.Windows.Win32.Foundation.PWSTR, pcchActual: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetDeviceManufacturer(self, cchDeviceManufacturer: UInt32, wzDeviceManufacturer: win32more.Windows.Win32.Foundation.PWSTR, pcchActual: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetDeviceModels(self, cchDeviceModels: UInt32, wzDeviceModels: win32more.Windows.Win32.Foundation.PWSTR, pcchActual: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def GetMimeTypes(self, cchMimeTypes: UInt32, wzMimeTypes: win32more.Windows.Win32.Foundation.PWSTR, pcchActual: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def GetFileExtensions(self, cchFileExtensions: UInt32, wzFileExtensions: win32more.Windows.Win32.Foundation.PWSTR, pcchActual: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def DoesSupportAnimation(self, pfSupportAnimation: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def DoesSupportChromakey(self, pfSupportChromakey: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def DoesSupportLossless(self, pfSupportLossless: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def DoesSupportMultiframe(self, pfSupportMultiframe: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def MatchesMimeType(self, wzMimeType: win32more.Windows.Win32.Foundation.PWSTR, pfMatches: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWICBitmapCodecProgressNotification(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{64c1024e-c3cf-4462-8078-88c2b11c46d9}')
    @commethod(3)
    def RegisterProgressNotification(self, pfnProgressNotification: win32more.Windows.Win32.Graphics.Imaging.PFNProgressNotification, pvData: VoidPtr, dwProgressFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWICBitmapDecoder(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{9edde9e7-8dee-47ea-99df-e6faf2ed44bf}')
    @commethod(3)
    def QueryCapability(self, pIStream: win32more.Windows.Win32.System.Com.IStream, pdwCapability: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Initialize(self, pIStream: win32more.Windows.Win32.System.Com.IStream, cacheOptions: win32more.Windows.Win32.Graphics.Imaging.WICDecodeOptions) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetContainerFormat(self, pguidContainerFormat: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetDecoderInfo(self, ppIDecoderInfo: POINTER(win32more.Windows.Win32.Graphics.Imaging.IWICBitmapDecoderInfo)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def CopyPalette(self, pIPalette: win32more.Windows.Win32.Graphics.Imaging.IWICPalette) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetMetadataQueryReader(self, ppIMetadataQueryReader: POINTER(win32more.Windows.Win32.Graphics.Imaging.IWICMetadataQueryReader)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetPreview(self, ppIBitmapSource: POINTER(win32more.Windows.Win32.Graphics.Imaging.IWICBitmapSource)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetColorContexts(self, cCount: UInt32, ppIColorContexts: POINTER(win32more.Windows.Win32.Graphics.Imaging.IWICColorContext), pcActualCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetThumbnail(self, ppIThumbnail: POINTER(win32more.Windows.Win32.Graphics.Imaging.IWICBitmapSource)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetFrameCount(self, pCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetFrame(self, index: UInt32, ppIBitmapFrame: POINTER(win32more.Windows.Win32.Graphics.Imaging.IWICBitmapFrameDecode)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWICBitmapDecoderInfo(ComPtr):
    extends: win32more.Windows.Win32.Graphics.Imaging.IWICBitmapCodecInfo
    _iid_ = Guid('{d8cd007f-d08f-4191-9bfc-236ea7f0e4b5}')
    @commethod(23)
    def GetPatterns(self, cbSizePatterns: UInt32, pPatterns: POINTER(win32more.Windows.Win32.Graphics.Imaging.WICBitmapPattern), pcPatterns: POINTER(UInt32), pcbPatternsActual: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def MatchesPattern(self, pIStream: win32more.Windows.Win32.System.Com.IStream, pfMatches: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def CreateInstance(self, ppIBitmapDecoder: POINTER(win32more.Windows.Win32.Graphics.Imaging.IWICBitmapDecoder)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWICBitmapEncoder(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{00000103-a8f2-4877-ba0a-fd2b6645fb94}')
    @commethod(3)
    def Initialize(self, pIStream: win32more.Windows.Win32.System.Com.IStream, cacheOption: win32more.Windows.Win32.Graphics.Imaging.WICBitmapEncoderCacheOption) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetContainerFormat(self, pguidContainerFormat: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetEncoderInfo(self, ppIEncoderInfo: POINTER(win32more.Windows.Win32.Graphics.Imaging.IWICBitmapEncoderInfo)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetColorContexts(self, cCount: UInt32, ppIColorContext: POINTER(win32more.Windows.Win32.Graphics.Imaging.IWICColorContext)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetPalette(self, pIPalette: win32more.Windows.Win32.Graphics.Imaging.IWICPalette) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetThumbnail(self, pIThumbnail: win32more.Windows.Win32.Graphics.Imaging.IWICBitmapSource) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SetPreview(self, pIPreview: win32more.Windows.Win32.Graphics.Imaging.IWICBitmapSource) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def CreateNewFrame(self, ppIFrameEncode: POINTER(win32more.Windows.Win32.Graphics.Imaging.IWICBitmapFrameEncode), ppIEncoderOptions: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.IPropertyBag2)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Commit(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetMetadataQueryWriter(self, ppIMetadataQueryWriter: POINTER(win32more.Windows.Win32.Graphics.Imaging.IWICMetadataQueryWriter)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWICBitmapEncoderInfo(ComPtr):
    extends: win32more.Windows.Win32.Graphics.Imaging.IWICBitmapCodecInfo
    _iid_ = Guid('{94c9b4ee-a09f-4f92-8a1e-4a9bce7e76fb}')
    @commethod(23)
    def CreateInstance(self, ppIBitmapEncoder: POINTER(win32more.Windows.Win32.Graphics.Imaging.IWICBitmapEncoder)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWICBitmapFlipRotator(ComPtr):
    extends: win32more.Windows.Win32.Graphics.Imaging.IWICBitmapSource
    _iid_ = Guid('{5009834f-2d6a-41ce-9e1b-17c5aff7a782}')
    @commethod(8)
    def Initialize(self, pISource: win32more.Windows.Win32.Graphics.Imaging.IWICBitmapSource, options: win32more.Windows.Win32.Graphics.Imaging.WICBitmapTransformOptions) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWICBitmapFrameDecode(ComPtr):
    extends: win32more.Windows.Win32.Graphics.Imaging.IWICBitmapSource
    _iid_ = Guid('{3b16811b-6a43-4ec9-a813-3d930c13b940}')
    @commethod(8)
    def GetMetadataQueryReader(self, ppIMetadataQueryReader: POINTER(win32more.Windows.Win32.Graphics.Imaging.IWICMetadataQueryReader)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetColorContexts(self, cCount: UInt32, ppIColorContexts: POINTER(win32more.Windows.Win32.Graphics.Imaging.IWICColorContext), pcActualCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetThumbnail(self, ppIThumbnail: POINTER(win32more.Windows.Win32.Graphics.Imaging.IWICBitmapSource)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWICBitmapFrameEncode(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{00000105-a8f2-4877-ba0a-fd2b6645fb94}')
    @commethod(3)
    def Initialize(self, pIEncoderOptions: win32more.Windows.Win32.System.Com.StructuredStorage.IPropertyBag2) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetSize(self, uiWidth: UInt32, uiHeight: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetResolution(self, dpiX: Double, dpiY: Double) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetPixelFormat(self, pPixelFormat: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetColorContexts(self, cCount: UInt32, ppIColorContext: POINTER(win32more.Windows.Win32.Graphics.Imaging.IWICColorContext)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetPalette(self, pIPalette: win32more.Windows.Win32.Graphics.Imaging.IWICPalette) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SetThumbnail(self, pIThumbnail: win32more.Windows.Win32.Graphics.Imaging.IWICBitmapSource) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def WritePixels(self, lineCount: UInt32, cbStride: UInt32, cbBufferSize: UInt32, pbPixels: POINTER(Byte)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def WriteSource(self, pIBitmapSource: win32more.Windows.Win32.Graphics.Imaging.IWICBitmapSource, prc: POINTER(win32more.Windows.Win32.Graphics.Imaging.WICRect)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def Commit(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetMetadataQueryWriter(self, ppIMetadataQueryWriter: POINTER(win32more.Windows.Win32.Graphics.Imaging.IWICMetadataQueryWriter)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWICBitmapLock(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{00000123-a8f2-4877-ba0a-fd2b6645fb94}')
    @commethod(3)
    def GetSize(self, puiWidth: POINTER(UInt32), puiHeight: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetStride(self, pcbStride: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetDataPointer(self, pcbBufferSize: POINTER(UInt32), ppbData: POINTER(POINTER(Byte))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetPixelFormat(self, pPixelFormat: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWICBitmapScaler(ComPtr):
    extends: win32more.Windows.Win32.Graphics.Imaging.IWICBitmapSource
    _iid_ = Guid('{00000302-a8f2-4877-ba0a-fd2b6645fb94}')
    @commethod(8)
    def Initialize(self, pISource: win32more.Windows.Win32.Graphics.Imaging.IWICBitmapSource, uiWidth: UInt32, uiHeight: UInt32, mode: win32more.Windows.Win32.Graphics.Imaging.WICBitmapInterpolationMode) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWICBitmapSource(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{00000120-a8f2-4877-ba0a-fd2b6645fb94}')
    @commethod(3)
    def GetSize(self, puiWidth: POINTER(UInt32), puiHeight: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetPixelFormat(self, pPixelFormat: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetResolution(self, pDpiX: POINTER(Double), pDpiY: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def CopyPalette(self, pIPalette: win32more.Windows.Win32.Graphics.Imaging.IWICPalette) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def CopyPixels(self, prc: POINTER(win32more.Windows.Win32.Graphics.Imaging.WICRect), cbStride: UInt32, cbBufferSize: UInt32, pbBuffer: POINTER(Byte)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWICBitmapSourceTransform(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{3b16811b-6a43-4ec9-b713-3d5a0c13b940}')
    @commethod(3)
    def CopyPixels(self, prc: POINTER(win32more.Windows.Win32.Graphics.Imaging.WICRect), uiWidth: UInt32, uiHeight: UInt32, pguidDstFormat: POINTER(Guid), dstTransform: win32more.Windows.Win32.Graphics.Imaging.WICBitmapTransformOptions, nStride: UInt32, cbBufferSize: UInt32, pbBuffer: POINTER(Byte)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetClosestSize(self, puiWidth: POINTER(UInt32), puiHeight: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetClosestPixelFormat(self, pguidDstFormat: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def DoesSupportTransform(self, dstTransform: win32more.Windows.Win32.Graphics.Imaging.WICBitmapTransformOptions, pfIsSupported: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWICColorContext(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{3c613a02-34b2-44ea-9a7c-45aea9c6fd6d}')
    @commethod(3)
    def InitializeFromFilename(self, wzFilename: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def InitializeFromMemory(self, pbBuffer: POINTER(Byte), cbBufferSize: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def InitializeFromExifColorSpace(self, value: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetType(self, pType: POINTER(win32more.Windows.Win32.Graphics.Imaging.WICColorContextType)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetProfileBytes(self, cbBuffer: UInt32, pbBuffer: POINTER(Byte), pcbActual: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetExifColorSpace(self, pValue: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWICColorTransform(ComPtr):
    extends: win32more.Windows.Win32.Graphics.Imaging.IWICBitmapSource
    _iid_ = Guid('{b66f034f-d0e2-40ab-b436-6de39e321a94}')
    @commethod(8)
    def Initialize(self, pIBitmapSource: win32more.Windows.Win32.Graphics.Imaging.IWICBitmapSource, pIContextSource: win32more.Windows.Win32.Graphics.Imaging.IWICColorContext, pIContextDest: win32more.Windows.Win32.Graphics.Imaging.IWICColorContext, pixelFmtDest: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWICComponentFactory(ComPtr):
    extends: win32more.Windows.Win32.Graphics.Imaging.IWICImagingFactory
    _iid_ = Guid('{412d0c3a-9650-44fa-af5b-dd2a06c8e8fb}')
    @commethod(28)
    def CreateMetadataReader(self, guidMetadataFormat: POINTER(Guid), pguidVendor: POINTER(Guid), dwOptions: UInt32, pIStream: win32more.Windows.Win32.System.Com.IStream, ppIReader: POINTER(win32more.Windows.Win32.Graphics.Imaging.IWICMetadataReader)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def CreateMetadataReaderFromContainer(self, guidContainerFormat: POINTER(Guid), pguidVendor: POINTER(Guid), dwOptions: UInt32, pIStream: win32more.Windows.Win32.System.Com.IStream, ppIReader: POINTER(win32more.Windows.Win32.Graphics.Imaging.IWICMetadataReader)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def CreateMetadataWriter(self, guidMetadataFormat: POINTER(Guid), pguidVendor: POINTER(Guid), dwMetadataOptions: UInt32, ppIWriter: POINTER(win32more.Windows.Win32.Graphics.Imaging.IWICMetadataWriter)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def CreateMetadataWriterFromReader(self, pIReader: win32more.Windows.Win32.Graphics.Imaging.IWICMetadataReader, pguidVendor: POINTER(Guid), ppIWriter: POINTER(win32more.Windows.Win32.Graphics.Imaging.IWICMetadataWriter)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def CreateQueryReaderFromBlockReader(self, pIBlockReader: win32more.Windows.Win32.Graphics.Imaging.IWICMetadataBlockReader, ppIQueryReader: POINTER(win32more.Windows.Win32.Graphics.Imaging.IWICMetadataQueryReader)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def CreateQueryWriterFromBlockWriter(self, pIBlockWriter: win32more.Windows.Win32.Graphics.Imaging.IWICMetadataBlockWriter, ppIQueryWriter: POINTER(win32more.Windows.Win32.Graphics.Imaging.IWICMetadataQueryWriter)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def CreateEncoderPropertyBag(self, ppropOptions: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPBAG2), cCount: UInt32, ppIPropertyBag: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.IPropertyBag2)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWICComponentInfo(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{23bc3f0a-698b-4357-886b-f24d50671334}')
    @commethod(3)
    def GetComponentType(self, pType: POINTER(win32more.Windows.Win32.Graphics.Imaging.WICComponentType)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetCLSID(self, pclsid: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetSigningStatus(self, pStatus: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetAuthor(self, cchAuthor: UInt32, wzAuthor: win32more.Windows.Win32.Foundation.PWSTR, pcchActual: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetVendorGUID(self, pguidVendor: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetVersion(self, cchVersion: UInt32, wzVersion: win32more.Windows.Win32.Foundation.PWSTR, pcchActual: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetSpecVersion(self, cchSpecVersion: UInt32, wzSpecVersion: win32more.Windows.Win32.Foundation.PWSTR, pcchActual: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetFriendlyName(self, cchFriendlyName: UInt32, wzFriendlyName: win32more.Windows.Win32.Foundation.PWSTR, pcchActual: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWICDdsDecoder(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{409cd537-8532-40cb-9774-e2feb2df4e9c}')
    @commethod(3)
    def GetParameters(self, pParameters: POINTER(win32more.Windows.Win32.Graphics.Imaging.WICDdsParameters)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetFrame(self, arrayIndex: UInt32, mipLevel: UInt32, sliceIndex: UInt32, ppIBitmapFrame: POINTER(win32more.Windows.Win32.Graphics.Imaging.IWICBitmapFrameDecode)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWICDdsEncoder(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{5cacdb4c-407e-41b3-b936-d0f010cd6732}')
    @commethod(3)
    def SetParameters(self, pParameters: POINTER(win32more.Windows.Win32.Graphics.Imaging.WICDdsParameters)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetParameters(self, pParameters: POINTER(win32more.Windows.Win32.Graphics.Imaging.WICDdsParameters)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def CreateNewFrame(self, ppIFrameEncode: POINTER(win32more.Windows.Win32.Graphics.Imaging.IWICBitmapFrameEncode), pArrayIndex: POINTER(UInt32), pMipLevel: POINTER(UInt32), pSliceIndex: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWICDdsFrameDecode(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{3d4c0c61-18a4-41e4-bd80-481a4fc9f464}')
    @commethod(3)
    def GetSizeInBlocks(self, pWidthInBlocks: POINTER(UInt32), pHeightInBlocks: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetFormatInfo(self, pFormatInfo: POINTER(win32more.Windows.Win32.Graphics.Imaging.WICDdsFormatInfo)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def CopyBlocks(self, prcBoundsInBlocks: POINTER(win32more.Windows.Win32.Graphics.Imaging.WICRect), cbStride: UInt32, cbBufferSize: UInt32, pbBuffer: POINTER(Byte)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWICDevelopRaw(ComPtr):
    extends: win32more.Windows.Win32.Graphics.Imaging.IWICBitmapFrameDecode
    _iid_ = Guid('{fbec5e44-f7be-4b65-b7f8-c0c81fef026d}')
    @commethod(11)
    def QueryRawCapabilitiesInfo(self, pInfo: POINTER(win32more.Windows.Win32.Graphics.Imaging.WICRawCapabilitiesInfo)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def LoadParameterSet(self, ParameterSet: win32more.Windows.Win32.Graphics.Imaging.WICRawParameterSet) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetCurrentParameterSet(self, ppCurrentParameterSet: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.IPropertyBag2)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def SetExposureCompensation(self, ev: Double) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetExposureCompensation(self, pEV: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def SetWhitePointRGB(self, Red: UInt32, Green: UInt32, Blue: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def GetWhitePointRGB(self, pRed: POINTER(UInt32), pGreen: POINTER(UInt32), pBlue: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def SetNamedWhitePoint(self, WhitePoint: win32more.Windows.Win32.Graphics.Imaging.WICNamedWhitePoint) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def GetNamedWhitePoint(self, pWhitePoint: POINTER(win32more.Windows.Win32.Graphics.Imaging.WICNamedWhitePoint)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def SetWhitePointKelvin(self, WhitePointKelvin: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def GetWhitePointKelvin(self, pWhitePointKelvin: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def GetKelvinRangeInfo(self, pMinKelvinTemp: POINTER(UInt32), pMaxKelvinTemp: POINTER(UInt32), pKelvinTempStepValue: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def SetContrast(self, Contrast: Double) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def GetContrast(self, pContrast: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def SetGamma(self, Gamma: Double) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def GetGamma(self, pGamma: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def SetSharpness(self, Sharpness: Double) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def GetSharpness(self, pSharpness: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def SetSaturation(self, Saturation: Double) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def GetSaturation(self, pSaturation: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def SetTint(self, Tint: Double) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def GetTint(self, pTint: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def SetNoiseReduction(self, NoiseReduction: Double) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def GetNoiseReduction(self, pNoiseReduction: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def SetDestinationColorContext(self, pColorContext: win32more.Windows.Win32.Graphics.Imaging.IWICColorContext) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(36)
    def SetToneCurve(self, cbToneCurveSize: UInt32, pToneCurve: POINTER(win32more.Windows.Win32.Graphics.Imaging.WICRawToneCurve)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(37)
    def GetToneCurve(self, cbToneCurveBufferSize: UInt32, pToneCurve: POINTER(win32more.Windows.Win32.Graphics.Imaging.WICRawToneCurve), pcbActualToneCurveBufferSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(38)
    def SetRotation(self, Rotation: Double) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(39)
    def GetRotation(self, pRotation: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(40)
    def SetRenderMode(self, RenderMode: win32more.Windows.Win32.Graphics.Imaging.WICRawRenderMode) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(41)
    def GetRenderMode(self, pRenderMode: POINTER(win32more.Windows.Win32.Graphics.Imaging.WICRawRenderMode)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(42)
    def SetNotificationCallback(self, pCallback: win32more.Windows.Win32.Graphics.Imaging.IWICDevelopRawNotificationCallback) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWICDevelopRawNotificationCallback(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{95c75a6e-3e8c-4ec2-85a8-aebcc551e59b}')
    @commethod(3)
    def Notify(self, NotificationMask: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWICEnumMetadataItem(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{dc2bb46d-3f07-481e-8625-220c4aedbb33}')
    @commethod(3)
    def Next(self, celt: UInt32, rgeltSchema: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT), rgeltId: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT), rgeltValue: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT), pceltFetched: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(self, celt: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(self, ppIEnumMetadataItem: POINTER(win32more.Windows.Win32.Graphics.Imaging.IWICEnumMetadataItem)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWICFastMetadataEncoder(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{b84e2c09-78c9-4ac4-8bd3-524ae1663a2f}')
    @commethod(3)
    def Commit(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetMetadataQueryWriter(self, ppIMetadataQueryWriter: POINTER(win32more.Windows.Win32.Graphics.Imaging.IWICMetadataQueryWriter)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWICFormatConverter(ComPtr):
    extends: win32more.Windows.Win32.Graphics.Imaging.IWICBitmapSource
    _iid_ = Guid('{00000301-a8f2-4877-ba0a-fd2b6645fb94}')
    @commethod(8)
    def Initialize(self, pISource: win32more.Windows.Win32.Graphics.Imaging.IWICBitmapSource, dstFormat: POINTER(Guid), dither: win32more.Windows.Win32.Graphics.Imaging.WICBitmapDitherType, pIPalette: win32more.Windows.Win32.Graphics.Imaging.IWICPalette, alphaThresholdPercent: Double, paletteTranslate: win32more.Windows.Win32.Graphics.Imaging.WICBitmapPaletteType) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def CanConvert(self, srcPixelFormat: POINTER(Guid), dstPixelFormat: POINTER(Guid), pfCanConvert: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWICFormatConverterInfo(ComPtr):
    extends: win32more.Windows.Win32.Graphics.Imaging.IWICComponentInfo
    _iid_ = Guid('{9f34fb65-13f4-4f15-bc57-3726b5e53d9f}')
    @commethod(11)
    def GetPixelFormats(self, cFormats: UInt32, pPixelFormatGUIDs: POINTER(Guid), pcActual: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def CreateInstance(self, ppIConverter: POINTER(win32more.Windows.Win32.Graphics.Imaging.IWICFormatConverter)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWICImagingFactory(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{ec5ec8a9-c395-4314-9c77-54d7a935ff70}')
    @commethod(3)
    def CreateDecoderFromFilename(self, wzFilename: win32more.Windows.Win32.Foundation.PWSTR, pguidVendor: POINTER(Guid), dwDesiredAccess: win32more.Windows.Win32.Foundation.GENERIC_ACCESS_RIGHTS, metadataOptions: win32more.Windows.Win32.Graphics.Imaging.WICDecodeOptions, ppIDecoder: POINTER(win32more.Windows.Win32.Graphics.Imaging.IWICBitmapDecoder)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def CreateDecoderFromStream(self, pIStream: win32more.Windows.Win32.System.Com.IStream, pguidVendor: POINTER(Guid), metadataOptions: win32more.Windows.Win32.Graphics.Imaging.WICDecodeOptions, ppIDecoder: POINTER(win32more.Windows.Win32.Graphics.Imaging.IWICBitmapDecoder)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def CreateDecoderFromFileHandle(self, hFile: UIntPtr, pguidVendor: POINTER(Guid), metadataOptions: win32more.Windows.Win32.Graphics.Imaging.WICDecodeOptions, ppIDecoder: POINTER(win32more.Windows.Win32.Graphics.Imaging.IWICBitmapDecoder)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def CreateComponentInfo(self, clsidComponent: POINTER(Guid), ppIInfo: POINTER(win32more.Windows.Win32.Graphics.Imaging.IWICComponentInfo)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def CreateDecoder(self, guidContainerFormat: POINTER(Guid), pguidVendor: POINTER(Guid), ppIDecoder: POINTER(win32more.Windows.Win32.Graphics.Imaging.IWICBitmapDecoder)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def CreateEncoder(self, guidContainerFormat: POINTER(Guid), pguidVendor: POINTER(Guid), ppIEncoder: POINTER(win32more.Windows.Win32.Graphics.Imaging.IWICBitmapEncoder)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def CreatePalette(self, ppIPalette: POINTER(win32more.Windows.Win32.Graphics.Imaging.IWICPalette)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def CreateFormatConverter(self, ppIFormatConverter: POINTER(win32more.Windows.Win32.Graphics.Imaging.IWICFormatConverter)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def CreateBitmapScaler(self, ppIBitmapScaler: POINTER(win32more.Windows.Win32.Graphics.Imaging.IWICBitmapScaler)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def CreateBitmapClipper(self, ppIBitmapClipper: POINTER(win32more.Windows.Win32.Graphics.Imaging.IWICBitmapClipper)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def CreateBitmapFlipRotator(self, ppIBitmapFlipRotator: POINTER(win32more.Windows.Win32.Graphics.Imaging.IWICBitmapFlipRotator)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def CreateStream(self, ppIWICStream: POINTER(win32more.Windows.Win32.Graphics.Imaging.IWICStream)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def CreateColorContext(self, ppIWICColorContext: POINTER(win32more.Windows.Win32.Graphics.Imaging.IWICColorContext)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def CreateColorTransformer(self, ppIWICColorTransform: POINTER(win32more.Windows.Win32.Graphics.Imaging.IWICColorTransform)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def CreateBitmap(self, uiWidth: UInt32, uiHeight: UInt32, pixelFormat: POINTER(Guid), option: win32more.Windows.Win32.Graphics.Imaging.WICBitmapCreateCacheOption, ppIBitmap: POINTER(win32more.Windows.Win32.Graphics.Imaging.IWICBitmap)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def CreateBitmapFromSource(self, pIBitmapSource: win32more.Windows.Win32.Graphics.Imaging.IWICBitmapSource, option: win32more.Windows.Win32.Graphics.Imaging.WICBitmapCreateCacheOption, ppIBitmap: POINTER(win32more.Windows.Win32.Graphics.Imaging.IWICBitmap)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def CreateBitmapFromSourceRect(self, pIBitmapSource: win32more.Windows.Win32.Graphics.Imaging.IWICBitmapSource, x: UInt32, y: UInt32, width: UInt32, height: UInt32, ppIBitmap: POINTER(win32more.Windows.Win32.Graphics.Imaging.IWICBitmap)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def CreateBitmapFromMemory(self, uiWidth: UInt32, uiHeight: UInt32, pixelFormat: POINTER(Guid), cbStride: UInt32, cbBufferSize: UInt32, pbBuffer: POINTER(Byte), ppIBitmap: POINTER(win32more.Windows.Win32.Graphics.Imaging.IWICBitmap)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def CreateBitmapFromHBITMAP(self, hBitmap: win32more.Windows.Win32.Graphics.Gdi.HBITMAP, hPalette: win32more.Windows.Win32.Graphics.Gdi.HPALETTE, options: win32more.Windows.Win32.Graphics.Imaging.WICBitmapAlphaChannelOption, ppIBitmap: POINTER(win32more.Windows.Win32.Graphics.Imaging.IWICBitmap)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def CreateBitmapFromHICON(self, hIcon: win32more.Windows.Win32.UI.WindowsAndMessaging.HICON, ppIBitmap: POINTER(win32more.Windows.Win32.Graphics.Imaging.IWICBitmap)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def CreateComponentEnumerator(self, componentTypes: UInt32, options: UInt32, ppIEnumUnknown: POINTER(win32more.Windows.Win32.System.Com.IEnumUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def CreateFastMetadataEncoderFromDecoder(self, pIDecoder: win32more.Windows.Win32.Graphics.Imaging.IWICBitmapDecoder, ppIFastEncoder: POINTER(win32more.Windows.Win32.Graphics.Imaging.IWICFastMetadataEncoder)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def CreateFastMetadataEncoderFromFrameDecode(self, pIFrameDecoder: win32more.Windows.Win32.Graphics.Imaging.IWICBitmapFrameDecode, ppIFastEncoder: POINTER(win32more.Windows.Win32.Graphics.Imaging.IWICFastMetadataEncoder)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def CreateQueryWriter(self, guidMetadataFormat: POINTER(Guid), pguidVendor: POINTER(Guid), ppIQueryWriter: POINTER(win32more.Windows.Win32.Graphics.Imaging.IWICMetadataQueryWriter)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def CreateQueryWriterFromReader(self, pIQueryReader: win32more.Windows.Win32.Graphics.Imaging.IWICMetadataQueryReader, pguidVendor: POINTER(Guid), ppIQueryWriter: POINTER(win32more.Windows.Win32.Graphics.Imaging.IWICMetadataQueryWriter)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWICJpegFrameDecode(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{8939f66e-c46a-4c21-a9d1-98b327ce1679}')
    @commethod(3)
    def DoesSupportIndexing(self, pfIndexingSupported: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetIndexing(self, options: win32more.Windows.Win32.Graphics.Imaging.WICJpegIndexingOptions, horizontalIntervalSize: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def ClearIndexing(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetAcHuffmanTable(self, scanIndex: UInt32, tableIndex: UInt32, pAcHuffmanTable: POINTER(win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_JPEG_AC_HUFFMAN_TABLE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetDcHuffmanTable(self, scanIndex: UInt32, tableIndex: UInt32, pDcHuffmanTable: POINTER(win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_JPEG_DC_HUFFMAN_TABLE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetQuantizationTable(self, scanIndex: UInt32, tableIndex: UInt32, pQuantizationTable: POINTER(win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_JPEG_QUANTIZATION_TABLE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetFrameHeader(self, pFrameHeader: POINTER(win32more.Windows.Win32.Graphics.Imaging.WICJpegFrameHeader)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetScanHeader(self, scanIndex: UInt32, pScanHeader: POINTER(win32more.Windows.Win32.Graphics.Imaging.WICJpegScanHeader)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def CopyScan(self, scanIndex: UInt32, scanOffset: UInt32, cbScanData: UInt32, pbScanData: POINTER(Byte), pcbScanDataActual: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def CopyMinimalStream(self, streamOffset: UInt32, cbStreamData: UInt32, pbStreamData: POINTER(Byte), pcbStreamDataActual: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWICJpegFrameEncode(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{2f0c601f-d2c6-468c-abfa-49495d983ed1}')
    @commethod(3)
    def GetAcHuffmanTable(self, scanIndex: UInt32, tableIndex: UInt32, pAcHuffmanTable: POINTER(win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_JPEG_AC_HUFFMAN_TABLE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetDcHuffmanTable(self, scanIndex: UInt32, tableIndex: UInt32, pDcHuffmanTable: POINTER(win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_JPEG_DC_HUFFMAN_TABLE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetQuantizationTable(self, scanIndex: UInt32, tableIndex: UInt32, pQuantizationTable: POINTER(win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_JPEG_QUANTIZATION_TABLE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def WriteScan(self, cbScanData: UInt32, pbScanData: POINTER(Byte)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWICMetadataBlockReader(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{feaa2a8d-b3f3-43e4-b25c-d1de990a1ae1}')
    @commethod(3)
    def GetContainerFormat(self, pguidContainerFormat: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetCount(self, pcCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetReaderByIndex(self, nIndex: UInt32, ppIMetadataReader: POINTER(win32more.Windows.Win32.Graphics.Imaging.IWICMetadataReader)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetEnumerator(self, ppIEnumMetadata: POINTER(win32more.Windows.Win32.System.Com.IEnumUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWICMetadataBlockWriter(ComPtr):
    extends: win32more.Windows.Win32.Graphics.Imaging.IWICMetadataBlockReader
    _iid_ = Guid('{08fb9676-b444-41e8-8dbe-6a53a542bff1}')
    @commethod(7)
    def InitializeFromBlockReader(self, pIMDBlockReader: win32more.Windows.Win32.Graphics.Imaging.IWICMetadataBlockReader) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetWriterByIndex(self, nIndex: UInt32, ppIMetadataWriter: POINTER(win32more.Windows.Win32.Graphics.Imaging.IWICMetadataWriter)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def AddWriter(self, pIMetadataWriter: win32more.Windows.Win32.Graphics.Imaging.IWICMetadataWriter) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SetWriterByIndex(self, nIndex: UInt32, pIMetadataWriter: win32more.Windows.Win32.Graphics.Imaging.IWICMetadataWriter) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def RemoveWriterByIndex(self, nIndex: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWICMetadataHandlerInfo(ComPtr):
    extends: win32more.Windows.Win32.Graphics.Imaging.IWICComponentInfo
    _iid_ = Guid('{aba958bf-c672-44d1-8d61-ce6df2e682c2}')
    @commethod(11)
    def GetMetadataFormat(self, pguidMetadataFormat: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetContainerFormats(self, cContainerFormats: UInt32, pguidContainerFormats: POINTER(Guid), pcchActual: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetDeviceManufacturer(self, cchDeviceManufacturer: UInt32, wzDeviceManufacturer: win32more.Windows.Win32.Foundation.PWSTR, pcchActual: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetDeviceModels(self, cchDeviceModels: UInt32, wzDeviceModels: win32more.Windows.Win32.Foundation.PWSTR, pcchActual: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def DoesRequireFullStream(self, pfRequiresFullStream: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def DoesSupportPadding(self, pfSupportsPadding: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def DoesRequireFixedSize(self, pfFixedSize: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWICMetadataQueryReader(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{30989668-e1c9-4597-b395-458eedb808df}')
    @commethod(3)
    def GetContainerFormat(self, pguidContainerFormat: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetLocation(self, cchMaxLength: UInt32, wzNamespace: win32more.Windows.Win32.Foundation.PWSTR, pcchActualLength: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetMetadataByName(self, wzName: win32more.Windows.Win32.Foundation.PWSTR, pvarValue: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetEnumerator(self, ppIEnumString: POINTER(win32more.Windows.Win32.System.Com.IEnumString)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWICMetadataQueryWriter(ComPtr):
    extends: win32more.Windows.Win32.Graphics.Imaging.IWICMetadataQueryReader
    _iid_ = Guid('{a721791a-0def-4d06-bd91-2118bf1db10b}')
    @commethod(7)
    def SetMetadataByName(self, wzName: win32more.Windows.Win32.Foundation.PWSTR, pvarValue: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def RemoveMetadataByName(self, wzName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWICMetadataReader(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{9204fe99-d8fc-4fd5-a001-9536b067a899}')
    @commethod(3)
    def GetMetadataFormat(self, pguidMetadataFormat: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetMetadataHandlerInfo(self, ppIHandler: POINTER(win32more.Windows.Win32.Graphics.Imaging.IWICMetadataHandlerInfo)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetCount(self, pcCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetValueByIndex(self, nIndex: UInt32, pvarSchema: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT), pvarId: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT), pvarValue: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetValue(self, pvarSchema: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT), pvarId: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT), pvarValue: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetEnumerator(self, ppIEnumMetadata: POINTER(win32more.Windows.Win32.Graphics.Imaging.IWICEnumMetadataItem)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWICMetadataReaderInfo(ComPtr):
    extends: win32more.Windows.Win32.Graphics.Imaging.IWICMetadataHandlerInfo
    _iid_ = Guid('{eebf1f5b-07c1-4447-a3ab-22acaf78a804}')
    @commethod(18)
    def GetPatterns(self, guidContainerFormat: POINTER(Guid), cbSize: UInt32, pPattern: POINTER(win32more.Windows.Win32.Graphics.Imaging.WICMetadataPattern), pcCount: POINTER(UInt32), pcbActual: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def MatchesPattern(self, guidContainerFormat: POINTER(Guid), pIStream: win32more.Windows.Win32.System.Com.IStream, pfMatches: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def CreateInstance(self, ppIReader: POINTER(win32more.Windows.Win32.Graphics.Imaging.IWICMetadataReader)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWICMetadataWriter(ComPtr):
    extends: win32more.Windows.Win32.Graphics.Imaging.IWICMetadataReader
    _iid_ = Guid('{f7836e16-3be0-470b-86bb-160d0aecd7de}')
    @commethod(9)
    def SetValue(self, pvarSchema: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT), pvarId: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT), pvarValue: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SetValueByIndex(self, nIndex: UInt32, pvarSchema: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT), pvarId: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT), pvarValue: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def RemoveValue(self, pvarSchema: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT), pvarId: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def RemoveValueByIndex(self, nIndex: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWICMetadataWriterInfo(ComPtr):
    extends: win32more.Windows.Win32.Graphics.Imaging.IWICMetadataHandlerInfo
    _iid_ = Guid('{b22e3fba-3925-4323-b5c1-9ebfc430f236}')
    @commethod(18)
    def GetHeader(self, guidContainerFormat: POINTER(Guid), cbSize: UInt32, pHeader: POINTER(win32more.Windows.Win32.Graphics.Imaging.WICMetadataHeader), pcbActual: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def CreateInstance(self, ppIWriter: POINTER(win32more.Windows.Win32.Graphics.Imaging.IWICMetadataWriter)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWICPalette(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{00000040-a8f2-4877-ba0a-fd2b6645fb94}')
    @commethod(3)
    def InitializePredefined(self, ePaletteType: win32more.Windows.Win32.Graphics.Imaging.WICBitmapPaletteType, fAddTransparentColor: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def InitializeCustom(self, pColors: POINTER(UInt32), cCount: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def InitializeFromBitmap(self, pISurface: win32more.Windows.Win32.Graphics.Imaging.IWICBitmapSource, cCount: UInt32, fAddTransparentColor: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def InitializeFromPalette(self, pIPalette: win32more.Windows.Win32.Graphics.Imaging.IWICPalette) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetType(self, pePaletteType: POINTER(win32more.Windows.Win32.Graphics.Imaging.WICBitmapPaletteType)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetColorCount(self, pcCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetColors(self, cCount: UInt32, pColors: POINTER(UInt32), pcActualColors: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def IsBlackWhite(self, pfIsBlackWhite: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def IsGrayscale(self, pfIsGrayscale: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def HasAlpha(self, pfHasAlpha: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWICPersistStream(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IPersistStream
    _iid_ = Guid('{00675040-6908-45f8-86a3-49c7dfd6d9ad}')
    @commethod(8)
    def LoadEx(self, pIStream: win32more.Windows.Win32.System.Com.IStream, pguidPreferredVendor: POINTER(Guid), dwPersistOptions: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SaveEx(self, pIStream: win32more.Windows.Win32.System.Com.IStream, dwPersistOptions: UInt32, fClearDirty: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWICPixelFormatInfo(ComPtr):
    extends: win32more.Windows.Win32.Graphics.Imaging.IWICComponentInfo
    _iid_ = Guid('{e8eda601-3d48-431a-ab44-69059be88bbe}')
    @commethod(11)
    def GetFormatGUID(self, pFormat: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetColorContext(self, ppIColorContext: POINTER(win32more.Windows.Win32.Graphics.Imaging.IWICColorContext)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetBitsPerPixel(self, puiBitsPerPixel: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetChannelCount(self, puiChannelCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetChannelMask(self, uiChannelIndex: UInt32, cbMaskBuffer: UInt32, pbMaskBuffer: POINTER(Byte), pcbActual: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWICPixelFormatInfo2(ComPtr):
    extends: win32more.Windows.Win32.Graphics.Imaging.IWICPixelFormatInfo
    _iid_ = Guid('{a9db33a2-af5f-43c7-b679-74f5984b5aa4}')
    @commethod(16)
    def SupportsTransparency(self, pfSupportsTransparency: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def GetNumericRepresentation(self, pNumericRepresentation: POINTER(win32more.Windows.Win32.Graphics.Imaging.WICPixelFormatNumericRepresentation)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWICPlanarBitmapFrameEncode(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{f928b7b8-2221-40c1-b72e-7e82f1974d1a}')
    @commethod(3)
    def WritePixels(self, lineCount: UInt32, pPlanes: POINTER(win32more.Windows.Win32.Graphics.Imaging.WICBitmapPlane), cPlanes: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def WriteSource(self, ppPlanes: POINTER(win32more.Windows.Win32.Graphics.Imaging.IWICBitmapSource), cPlanes: UInt32, prcSource: POINTER(win32more.Windows.Win32.Graphics.Imaging.WICRect)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWICPlanarBitmapSourceTransform(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{3aff9cce-be95-4303-b927-e7d16ff4a613}')
    @commethod(3)
    def DoesSupportTransform(self, puiWidth: POINTER(UInt32), puiHeight: POINTER(UInt32), dstTransform: win32more.Windows.Win32.Graphics.Imaging.WICBitmapTransformOptions, dstPlanarOptions: win32more.Windows.Win32.Graphics.Imaging.WICPlanarOptions, pguidDstFormats: POINTER(Guid), pPlaneDescriptions: POINTER(win32more.Windows.Win32.Graphics.Imaging.WICBitmapPlaneDescription), cPlanes: UInt32, pfIsSupported: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def CopyPixels(self, prcSource: POINTER(win32more.Windows.Win32.Graphics.Imaging.WICRect), uiWidth: UInt32, uiHeight: UInt32, dstTransform: win32more.Windows.Win32.Graphics.Imaging.WICBitmapTransformOptions, dstPlanarOptions: win32more.Windows.Win32.Graphics.Imaging.WICPlanarOptions, pDstPlanes: POINTER(win32more.Windows.Win32.Graphics.Imaging.WICBitmapPlane), cPlanes: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWICPlanarFormatConverter(ComPtr):
    extends: win32more.Windows.Win32.Graphics.Imaging.IWICBitmapSource
    _iid_ = Guid('{bebee9cb-83b0-4dcc-8132-b0aaa55eac96}')
    @commethod(8)
    def Initialize(self, ppPlanes: POINTER(win32more.Windows.Win32.Graphics.Imaging.IWICBitmapSource), cPlanes: UInt32, dstFormat: POINTER(Guid), dither: win32more.Windows.Win32.Graphics.Imaging.WICBitmapDitherType, pIPalette: win32more.Windows.Win32.Graphics.Imaging.IWICPalette, alphaThresholdPercent: Double, paletteTranslate: win32more.Windows.Win32.Graphics.Imaging.WICBitmapPaletteType) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def CanConvert(self, pSrcPixelFormats: POINTER(Guid), cSrcPlanes: UInt32, dstPixelFormat: POINTER(Guid), pfCanConvert: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWICProgressCallback(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{4776f9cd-9517-45fa-bf24-e89c5ec5c60c}')
    @commethod(3)
    def Notify(self, uFrameNum: UInt32, operation: win32more.Windows.Win32.Graphics.Imaging.WICProgressOperation, dblProgress: Double) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWICProgressiveLevelControl(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{daac296f-7aa5-4dbf-8d15-225c5976f891}')
    @commethod(3)
    def GetLevelCount(self, pcLevels: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetCurrentLevel(self, pnLevel: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetCurrentLevel(self, nLevel: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWICStream(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IStream
    _iid_ = Guid('{135ff860-22b7-4ddf-b0f6-218f4f299a43}')
    @commethod(14)
    def InitializeFromIStream(self, pIStream: win32more.Windows.Win32.System.Com.IStream) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def InitializeFromFilename(self, wzFileName: win32more.Windows.Win32.Foundation.PWSTR, dwDesiredAccess: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def InitializeFromMemory(self, pbBuffer: POINTER(Byte), cbBufferSize: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def InitializeFromIStreamRegion(self, pIStream: win32more.Windows.Win32.System.Com.IStream, ulOffset: UInt64, ulMaxSize: UInt64) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWICStreamProvider(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{449494bc-b468-4927-96d7-ba90d31ab505}')
    @commethod(3)
    def GetStream(self, ppIStream: POINTER(win32more.Windows.Win32.System.Com.IStream)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetPersistOptions(self, pdwPersistOptions: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetPreferredVendorGUID(self, pguidPreferredVendor: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def RefreshStream(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PFNProgressNotification(pvData: VoidPtr, uFrameNum: UInt32, operation: win32more.Windows.Win32.Graphics.Imaging.WICProgressOperation, dblProgress: Double) -> win32more.Windows.Win32.Foundation.HRESULT: ...
WIC8BIMIptcDigestProperties = Int32
WIC8BIMIptcDigestPString: win32more.Windows.Win32.Graphics.Imaging.WIC8BIMIptcDigestProperties = 1
WIC8BIMIptcDigestIptcDigest: win32more.Windows.Win32.Graphics.Imaging.WIC8BIMIptcDigestProperties = 2
WIC8BIMIptcProperties = Int32
WIC8BIMIptcPString: win32more.Windows.Win32.Graphics.Imaging.WIC8BIMIptcProperties = 0
WIC8BIMIptcEmbeddedIPTC: win32more.Windows.Win32.Graphics.Imaging.WIC8BIMIptcProperties = 1
WIC8BIMResolutionInfoProperties = Int32
WIC8BIMResolutionInfoPString: win32more.Windows.Win32.Graphics.Imaging.WIC8BIMResolutionInfoProperties = 1
WIC8BIMResolutionInfoHResolution: win32more.Windows.Win32.Graphics.Imaging.WIC8BIMResolutionInfoProperties = 2
WIC8BIMResolutionInfoHResolutionUnit: win32more.Windows.Win32.Graphics.Imaging.WIC8BIMResolutionInfoProperties = 3
WIC8BIMResolutionInfoWidthUnit: win32more.Windows.Win32.Graphics.Imaging.WIC8BIMResolutionInfoProperties = 4
WIC8BIMResolutionInfoVResolution: win32more.Windows.Win32.Graphics.Imaging.WIC8BIMResolutionInfoProperties = 5
WIC8BIMResolutionInfoVResolutionUnit: win32more.Windows.Win32.Graphics.Imaging.WIC8BIMResolutionInfoProperties = 6
WIC8BIMResolutionInfoHeightUnit: win32more.Windows.Win32.Graphics.Imaging.WIC8BIMResolutionInfoProperties = 7
WICBitmapAlphaChannelOption = Int32
WICBitmapUseAlpha: win32more.Windows.Win32.Graphics.Imaging.WICBitmapAlphaChannelOption = 0
WICBitmapUsePremultipliedAlpha: win32more.Windows.Win32.Graphics.Imaging.WICBitmapAlphaChannelOption = 1
WICBitmapIgnoreAlpha: win32more.Windows.Win32.Graphics.Imaging.WICBitmapAlphaChannelOption = 2
WICBitmapCreateCacheOption = Int32
WICBitmapNoCache: win32more.Windows.Win32.Graphics.Imaging.WICBitmapCreateCacheOption = 0
WICBitmapCacheOnDemand: win32more.Windows.Win32.Graphics.Imaging.WICBitmapCreateCacheOption = 1
WICBitmapCacheOnLoad: win32more.Windows.Win32.Graphics.Imaging.WICBitmapCreateCacheOption = 2
WICBitmapDecoderCapabilities = Int32
WICBitmapDecoderCapabilitySameEncoder: win32more.Windows.Win32.Graphics.Imaging.WICBitmapDecoderCapabilities = 1
WICBitmapDecoderCapabilityCanDecodeAllImages: win32more.Windows.Win32.Graphics.Imaging.WICBitmapDecoderCapabilities = 2
WICBitmapDecoderCapabilityCanDecodeSomeImages: win32more.Windows.Win32.Graphics.Imaging.WICBitmapDecoderCapabilities = 4
WICBitmapDecoderCapabilityCanEnumerateMetadata: win32more.Windows.Win32.Graphics.Imaging.WICBitmapDecoderCapabilities = 8
WICBitmapDecoderCapabilityCanDecodeThumbnail: win32more.Windows.Win32.Graphics.Imaging.WICBitmapDecoderCapabilities = 16
WICBitmapDitherType = Int32
WICBitmapDitherTypeNone: win32more.Windows.Win32.Graphics.Imaging.WICBitmapDitherType = 0
WICBitmapDitherTypeSolid: win32more.Windows.Win32.Graphics.Imaging.WICBitmapDitherType = 0
WICBitmapDitherTypeOrdered4x4: win32more.Windows.Win32.Graphics.Imaging.WICBitmapDitherType = 1
WICBitmapDitherTypeOrdered8x8: win32more.Windows.Win32.Graphics.Imaging.WICBitmapDitherType = 2
WICBitmapDitherTypeOrdered16x16: win32more.Windows.Win32.Graphics.Imaging.WICBitmapDitherType = 3
WICBitmapDitherTypeSpiral4x4: win32more.Windows.Win32.Graphics.Imaging.WICBitmapDitherType = 4
WICBitmapDitherTypeSpiral8x8: win32more.Windows.Win32.Graphics.Imaging.WICBitmapDitherType = 5
WICBitmapDitherTypeDualSpiral4x4: win32more.Windows.Win32.Graphics.Imaging.WICBitmapDitherType = 6
WICBitmapDitherTypeDualSpiral8x8: win32more.Windows.Win32.Graphics.Imaging.WICBitmapDitherType = 7
WICBitmapDitherTypeErrorDiffusion: win32more.Windows.Win32.Graphics.Imaging.WICBitmapDitherType = 8
WICBitmapEncoderCacheOption = Int32
WICBitmapEncoderCacheInMemory: win32more.Windows.Win32.Graphics.Imaging.WICBitmapEncoderCacheOption = 0
WICBitmapEncoderCacheTempFile: win32more.Windows.Win32.Graphics.Imaging.WICBitmapEncoderCacheOption = 1
WICBitmapEncoderNoCache: win32more.Windows.Win32.Graphics.Imaging.WICBitmapEncoderCacheOption = 2
WICBitmapInterpolationMode = Int32
WICBitmapInterpolationModeNearestNeighbor: win32more.Windows.Win32.Graphics.Imaging.WICBitmapInterpolationMode = 0
WICBitmapInterpolationModeLinear: win32more.Windows.Win32.Graphics.Imaging.WICBitmapInterpolationMode = 1
WICBitmapInterpolationModeCubic: win32more.Windows.Win32.Graphics.Imaging.WICBitmapInterpolationMode = 2
WICBitmapInterpolationModeFant: win32more.Windows.Win32.Graphics.Imaging.WICBitmapInterpolationMode = 3
WICBitmapInterpolationModeHighQualityCubic: win32more.Windows.Win32.Graphics.Imaging.WICBitmapInterpolationMode = 4
WICBitmapLockFlags = Int32
WICBitmapLockRead: win32more.Windows.Win32.Graphics.Imaging.WICBitmapLockFlags = 1
WICBitmapLockWrite: win32more.Windows.Win32.Graphics.Imaging.WICBitmapLockFlags = 2
WICBitmapPaletteType = Int32
WICBitmapPaletteTypeCustom: win32more.Windows.Win32.Graphics.Imaging.WICBitmapPaletteType = 0
WICBitmapPaletteTypeMedianCut: win32more.Windows.Win32.Graphics.Imaging.WICBitmapPaletteType = 1
WICBitmapPaletteTypeFixedBW: win32more.Windows.Win32.Graphics.Imaging.WICBitmapPaletteType = 2
WICBitmapPaletteTypeFixedHalftone8: win32more.Windows.Win32.Graphics.Imaging.WICBitmapPaletteType = 3
WICBitmapPaletteTypeFixedHalftone27: win32more.Windows.Win32.Graphics.Imaging.WICBitmapPaletteType = 4
WICBitmapPaletteTypeFixedHalftone64: win32more.Windows.Win32.Graphics.Imaging.WICBitmapPaletteType = 5
WICBitmapPaletteTypeFixedHalftone125: win32more.Windows.Win32.Graphics.Imaging.WICBitmapPaletteType = 6
WICBitmapPaletteTypeFixedHalftone216: win32more.Windows.Win32.Graphics.Imaging.WICBitmapPaletteType = 7
WICBitmapPaletteTypeFixedWebPalette: win32more.Windows.Win32.Graphics.Imaging.WICBitmapPaletteType = 7
WICBitmapPaletteTypeFixedHalftone252: win32more.Windows.Win32.Graphics.Imaging.WICBitmapPaletteType = 8
WICBitmapPaletteTypeFixedHalftone256: win32more.Windows.Win32.Graphics.Imaging.WICBitmapPaletteType = 9
WICBitmapPaletteTypeFixedGray4: win32more.Windows.Win32.Graphics.Imaging.WICBitmapPaletteType = 10
WICBitmapPaletteTypeFixedGray16: win32more.Windows.Win32.Graphics.Imaging.WICBitmapPaletteType = 11
WICBitmapPaletteTypeFixedGray256: win32more.Windows.Win32.Graphics.Imaging.WICBitmapPaletteType = 12
class WICBitmapPattern(Structure):
    Position: UInt64
    Length: UInt32
    Pattern: POINTER(Byte)
    Mask: POINTER(Byte)
    EndOfStream: win32more.Windows.Win32.Foundation.BOOL
class WICBitmapPlane(Structure):
    Format: Guid
    pbBuffer: POINTER(Byte)
    cbStride: UInt32
    cbBufferSize: UInt32
class WICBitmapPlaneDescription(Structure):
    Format: Guid
    Width: UInt32
    Height: UInt32
WICBitmapTransformOptions = Int32
WICBitmapTransformRotate0: win32more.Windows.Win32.Graphics.Imaging.WICBitmapTransformOptions = 0
WICBitmapTransformRotate90: win32more.Windows.Win32.Graphics.Imaging.WICBitmapTransformOptions = 1
WICBitmapTransformRotate180: win32more.Windows.Win32.Graphics.Imaging.WICBitmapTransformOptions = 2
WICBitmapTransformRotate270: win32more.Windows.Win32.Graphics.Imaging.WICBitmapTransformOptions = 3
WICBitmapTransformFlipHorizontal: win32more.Windows.Win32.Graphics.Imaging.WICBitmapTransformOptions = 8
WICBitmapTransformFlipVertical: win32more.Windows.Win32.Graphics.Imaging.WICBitmapTransformOptions = 16
WICColorContextType = Int32
WICColorContextUninitialized: win32more.Windows.Win32.Graphics.Imaging.WICColorContextType = 0
WICColorContextProfile: win32more.Windows.Win32.Graphics.Imaging.WICColorContextType = 1
WICColorContextExifColorSpace: win32more.Windows.Win32.Graphics.Imaging.WICColorContextType = 2
WICComponentEnumerateOptions = Int32
WICComponentEnumerateDefault: win32more.Windows.Win32.Graphics.Imaging.WICComponentEnumerateOptions = 0
WICComponentEnumerateRefresh: win32more.Windows.Win32.Graphics.Imaging.WICComponentEnumerateOptions = 1
WICComponentEnumerateDisabled: win32more.Windows.Win32.Graphics.Imaging.WICComponentEnumerateOptions = -2147483648
WICComponentEnumerateUnsigned: win32more.Windows.Win32.Graphics.Imaging.WICComponentEnumerateOptions = 1073741824
WICComponentEnumerateBuiltInOnly: win32more.Windows.Win32.Graphics.Imaging.WICComponentEnumerateOptions = 536870912
WICComponentSigning = Int32
WICComponentSigned: win32more.Windows.Win32.Graphics.Imaging.WICComponentSigning = 1
WICComponentUnsigned: win32more.Windows.Win32.Graphics.Imaging.WICComponentSigning = 2
WICComponentSafe: win32more.Windows.Win32.Graphics.Imaging.WICComponentSigning = 4
WICComponentDisabled: win32more.Windows.Win32.Graphics.Imaging.WICComponentSigning = -2147483648
WICComponentType = Int32
WICDecoder: win32more.Windows.Win32.Graphics.Imaging.WICComponentType = 1
WICEncoder: win32more.Windows.Win32.Graphics.Imaging.WICComponentType = 2
WICPixelFormatConverter: win32more.Windows.Win32.Graphics.Imaging.WICComponentType = 4
WICMetadataReader: win32more.Windows.Win32.Graphics.Imaging.WICComponentType = 8
WICMetadataWriter: win32more.Windows.Win32.Graphics.Imaging.WICComponentType = 16
WICPixelFormat: win32more.Windows.Win32.Graphics.Imaging.WICComponentType = 32
WICAllComponents: win32more.Windows.Win32.Graphics.Imaging.WICComponentType = 63
WICDdsAlphaMode = Int32
WICDdsAlphaModeUnknown: win32more.Windows.Win32.Graphics.Imaging.WICDdsAlphaMode = 0
WICDdsAlphaModeStraight: win32more.Windows.Win32.Graphics.Imaging.WICDdsAlphaMode = 1
WICDdsAlphaModePremultiplied: win32more.Windows.Win32.Graphics.Imaging.WICDdsAlphaMode = 2
WICDdsAlphaModeOpaque: win32more.Windows.Win32.Graphics.Imaging.WICDdsAlphaMode = 3
WICDdsAlphaModeCustom: win32more.Windows.Win32.Graphics.Imaging.WICDdsAlphaMode = 4
WICDdsDimension = Int32
WICDdsTexture1D: win32more.Windows.Win32.Graphics.Imaging.WICDdsDimension = 0
WICDdsTexture2D: win32more.Windows.Win32.Graphics.Imaging.WICDdsDimension = 1
WICDdsTexture3D: win32more.Windows.Win32.Graphics.Imaging.WICDdsDimension = 2
WICDdsTextureCube: win32more.Windows.Win32.Graphics.Imaging.WICDdsDimension = 3
class WICDdsFormatInfo(Structure):
    DxgiFormat: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_FORMAT
    BytesPerBlock: UInt32
    BlockWidth: UInt32
    BlockHeight: UInt32
class WICDdsParameters(Structure):
    Width: UInt32
    Height: UInt32
    Depth: UInt32
    MipLevels: UInt32
    ArraySize: UInt32
    DxgiFormat: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_FORMAT
    Dimension: win32more.Windows.Win32.Graphics.Imaging.WICDdsDimension
    AlphaMode: win32more.Windows.Win32.Graphics.Imaging.WICDdsAlphaMode
WICDecodeOptions = Int32
WICDecodeMetadataCacheOnDemand: win32more.Windows.Win32.Graphics.Imaging.WICDecodeOptions = 0
WICDecodeMetadataCacheOnLoad: win32more.Windows.Win32.Graphics.Imaging.WICDecodeOptions = 1
WICGifApplicationExtensionProperties = Int32
WICGifApplicationExtensionApplication: win32more.Windows.Win32.Graphics.Imaging.WICGifApplicationExtensionProperties = 1
WICGifApplicationExtensionData: win32more.Windows.Win32.Graphics.Imaging.WICGifApplicationExtensionProperties = 2
WICGifCommentExtensionProperties = Int32
WICGifCommentExtensionText: win32more.Windows.Win32.Graphics.Imaging.WICGifCommentExtensionProperties = 1
WICGifGraphicControlExtensionProperties = Int32
WICGifGraphicControlExtensionDisposal: win32more.Windows.Win32.Graphics.Imaging.WICGifGraphicControlExtensionProperties = 1
WICGifGraphicControlExtensionUserInputFlag: win32more.Windows.Win32.Graphics.Imaging.WICGifGraphicControlExtensionProperties = 2
WICGifGraphicControlExtensionTransparencyFlag: win32more.Windows.Win32.Graphics.Imaging.WICGifGraphicControlExtensionProperties = 3
WICGifGraphicControlExtensionDelay: win32more.Windows.Win32.Graphics.Imaging.WICGifGraphicControlExtensionProperties = 4
WICGifGraphicControlExtensionTransparentColorIndex: win32more.Windows.Win32.Graphics.Imaging.WICGifGraphicControlExtensionProperties = 5
WICGifImageDescriptorProperties = Int32
WICGifImageDescriptorLeft: win32more.Windows.Win32.Graphics.Imaging.WICGifImageDescriptorProperties = 1
WICGifImageDescriptorTop: win32more.Windows.Win32.Graphics.Imaging.WICGifImageDescriptorProperties = 2
WICGifImageDescriptorWidth: win32more.Windows.Win32.Graphics.Imaging.WICGifImageDescriptorProperties = 3
WICGifImageDescriptorHeight: win32more.Windows.Win32.Graphics.Imaging.WICGifImageDescriptorProperties = 4
WICGifImageDescriptorLocalColorTableFlag: win32more.Windows.Win32.Graphics.Imaging.WICGifImageDescriptorProperties = 5
WICGifImageDescriptorInterlaceFlag: win32more.Windows.Win32.Graphics.Imaging.WICGifImageDescriptorProperties = 6
WICGifImageDescriptorSortFlag: win32more.Windows.Win32.Graphics.Imaging.WICGifImageDescriptorProperties = 7
WICGifImageDescriptorLocalColorTableSize: win32more.Windows.Win32.Graphics.Imaging.WICGifImageDescriptorProperties = 8
WICGifLogicalScreenDescriptorProperties = Int32
WICGifLogicalScreenSignature: win32more.Windows.Win32.Graphics.Imaging.WICGifLogicalScreenDescriptorProperties = 1
WICGifLogicalScreenDescriptorWidth: win32more.Windows.Win32.Graphics.Imaging.WICGifLogicalScreenDescriptorProperties = 2
WICGifLogicalScreenDescriptorHeight: win32more.Windows.Win32.Graphics.Imaging.WICGifLogicalScreenDescriptorProperties = 3
WICGifLogicalScreenDescriptorGlobalColorTableFlag: win32more.Windows.Win32.Graphics.Imaging.WICGifLogicalScreenDescriptorProperties = 4
WICGifLogicalScreenDescriptorColorResolution: win32more.Windows.Win32.Graphics.Imaging.WICGifLogicalScreenDescriptorProperties = 5
WICGifLogicalScreenDescriptorSortFlag: win32more.Windows.Win32.Graphics.Imaging.WICGifLogicalScreenDescriptorProperties = 6
WICGifLogicalScreenDescriptorGlobalColorTableSize: win32more.Windows.Win32.Graphics.Imaging.WICGifLogicalScreenDescriptorProperties = 7
WICGifLogicalScreenDescriptorBackgroundColorIndex: win32more.Windows.Win32.Graphics.Imaging.WICGifLogicalScreenDescriptorProperties = 8
WICGifLogicalScreenDescriptorPixelAspectRatio: win32more.Windows.Win32.Graphics.Imaging.WICGifLogicalScreenDescriptorProperties = 9
WICHeifHdrProperties = Int32
WICHeifHdrMaximumLuminanceLevel: win32more.Windows.Win32.Graphics.Imaging.WICHeifHdrProperties = 1
WICHeifHdrMaximumFrameAverageLuminanceLevel: win32more.Windows.Win32.Graphics.Imaging.WICHeifHdrProperties = 2
WICHeifHdrMinimumMasteringDisplayLuminanceLevel: win32more.Windows.Win32.Graphics.Imaging.WICHeifHdrProperties = 3
WICHeifHdrMaximumMasteringDisplayLuminanceLevel: win32more.Windows.Win32.Graphics.Imaging.WICHeifHdrProperties = 4
WICHeifHdrCustomVideoPrimaries: win32more.Windows.Win32.Graphics.Imaging.WICHeifHdrProperties = 5
WICHeifProperties = Int32
WICHeifOrientation: win32more.Windows.Win32.Graphics.Imaging.WICHeifProperties = 1
class WICImageParameters(Structure):
    PixelFormat: win32more.Windows.Win32.Graphics.Direct2D.Common.D2D1_PIXEL_FORMAT
    DpiX: Single
    DpiY: Single
    Top: Single
    Left: Single
    PixelWidth: UInt32
    PixelHeight: UInt32
WICJpegChrominanceProperties = Int32
WICJpegChrominanceTable: win32more.Windows.Win32.Graphics.Imaging.WICJpegChrominanceProperties = 1
WICJpegCommentProperties = Int32
WICJpegCommentText: win32more.Windows.Win32.Graphics.Imaging.WICJpegCommentProperties = 1
class WICJpegFrameHeader(Structure):
    Width: UInt32
    Height: UInt32
    TransferMatrix: win32more.Windows.Win32.Graphics.Imaging.WICJpegTransferMatrix
    ScanType: win32more.Windows.Win32.Graphics.Imaging.WICJpegScanType
    cComponents: UInt32
    ComponentIdentifiers: UInt32
    SampleFactors: UInt32
    QuantizationTableIndices: UInt32
WICJpegIndexingOptions = Int32
WICJpegIndexingOptionsGenerateOnDemand: win32more.Windows.Win32.Graphics.Imaging.WICJpegIndexingOptions = 0
WICJpegIndexingOptionsGenerateOnLoad: win32more.Windows.Win32.Graphics.Imaging.WICJpegIndexingOptions = 1
WICJpegLuminanceProperties = Int32
WICJpegLuminanceTable: win32more.Windows.Win32.Graphics.Imaging.WICJpegLuminanceProperties = 1
class WICJpegScanHeader(Structure):
    cComponents: UInt32
    RestartInterval: UInt32
    ComponentSelectors: UInt32
    HuffmanTableIndices: UInt32
    StartSpectralSelection: Byte
    EndSpectralSelection: Byte
    SuccessiveApproximationHigh: Byte
    SuccessiveApproximationLow: Byte
WICJpegScanType = Int32
WICJpegScanTypeInterleaved: win32more.Windows.Win32.Graphics.Imaging.WICJpegScanType = 0
WICJpegScanTypePlanarComponents: win32more.Windows.Win32.Graphics.Imaging.WICJpegScanType = 1
WICJpegScanTypeProgressive: win32more.Windows.Win32.Graphics.Imaging.WICJpegScanType = 2
WICJpegTransferMatrix = Int32
WICJpegTransferMatrixIdentity: win32more.Windows.Win32.Graphics.Imaging.WICJpegTransferMatrix = 0
WICJpegTransferMatrixBT601: win32more.Windows.Win32.Graphics.Imaging.WICJpegTransferMatrix = 1
WICJpegYCrCbSubsamplingOption = Int32
WICJpegYCrCbSubsamplingDefault: win32more.Windows.Win32.Graphics.Imaging.WICJpegYCrCbSubsamplingOption = 0
WICJpegYCrCbSubsampling420: win32more.Windows.Win32.Graphics.Imaging.WICJpegYCrCbSubsamplingOption = 1
WICJpegYCrCbSubsampling422: win32more.Windows.Win32.Graphics.Imaging.WICJpegYCrCbSubsamplingOption = 2
WICJpegYCrCbSubsampling444: win32more.Windows.Win32.Graphics.Imaging.WICJpegYCrCbSubsamplingOption = 3
WICJpegYCrCbSubsampling440: win32more.Windows.Win32.Graphics.Imaging.WICJpegYCrCbSubsamplingOption = 4
WICMetadataCreationOptions = Int32
WICMetadataCreationDefault: win32more.Windows.Win32.Graphics.Imaging.WICMetadataCreationOptions = 0
WICMetadataCreationAllowUnknown: win32more.Windows.Win32.Graphics.Imaging.WICMetadataCreationOptions = 0
WICMetadataCreationFailUnknown: win32more.Windows.Win32.Graphics.Imaging.WICMetadataCreationOptions = 65536
WICMetadataCreationMask: win32more.Windows.Win32.Graphics.Imaging.WICMetadataCreationOptions = -65536
class WICMetadataHeader(Structure):
    Position: UInt64
    Length: UInt32
    Header: POINTER(Byte)
    DataOffset: UInt64
class WICMetadataPattern(Structure):
    Position: UInt64
    Length: UInt32
    Pattern: POINTER(Byte)
    Mask: POINTER(Byte)
    DataOffset: UInt64
WICNamedWhitePoint = Int32
WICWhitePointDefault: win32more.Windows.Win32.Graphics.Imaging.WICNamedWhitePoint = 1
WICWhitePointDaylight: win32more.Windows.Win32.Graphics.Imaging.WICNamedWhitePoint = 2
WICWhitePointCloudy: win32more.Windows.Win32.Graphics.Imaging.WICNamedWhitePoint = 4
WICWhitePointShade: win32more.Windows.Win32.Graphics.Imaging.WICNamedWhitePoint = 8
WICWhitePointTungsten: win32more.Windows.Win32.Graphics.Imaging.WICNamedWhitePoint = 16
WICWhitePointFluorescent: win32more.Windows.Win32.Graphics.Imaging.WICNamedWhitePoint = 32
WICWhitePointFlash: win32more.Windows.Win32.Graphics.Imaging.WICNamedWhitePoint = 64
WICWhitePointUnderwater: win32more.Windows.Win32.Graphics.Imaging.WICNamedWhitePoint = 128
WICWhitePointCustom: win32more.Windows.Win32.Graphics.Imaging.WICNamedWhitePoint = 256
WICWhitePointAutoWhiteBalance: win32more.Windows.Win32.Graphics.Imaging.WICNamedWhitePoint = 512
WICWhitePointAsShot: win32more.Windows.Win32.Graphics.Imaging.WICNamedWhitePoint = 1
WICPersistOptions = Int32
WICPersistOptionDefault: win32more.Windows.Win32.Graphics.Imaging.WICPersistOptions = 0
WICPersistOptionLittleEndian: win32more.Windows.Win32.Graphics.Imaging.WICPersistOptions = 0
WICPersistOptionBigEndian: win32more.Windows.Win32.Graphics.Imaging.WICPersistOptions = 1
WICPersistOptionStrictFormat: win32more.Windows.Win32.Graphics.Imaging.WICPersistOptions = 2
WICPersistOptionNoCacheStream: win32more.Windows.Win32.Graphics.Imaging.WICPersistOptions = 4
WICPersistOptionPreferUTF8: win32more.Windows.Win32.Graphics.Imaging.WICPersistOptions = 8
WICPersistOptionMask: win32more.Windows.Win32.Graphics.Imaging.WICPersistOptions = 65535
WICPixelFormatNumericRepresentation = Int32
WICPixelFormatNumericRepresentationUnspecified: win32more.Windows.Win32.Graphics.Imaging.WICPixelFormatNumericRepresentation = 0
WICPixelFormatNumericRepresentationIndexed: win32more.Windows.Win32.Graphics.Imaging.WICPixelFormatNumericRepresentation = 1
WICPixelFormatNumericRepresentationUnsignedInteger: win32more.Windows.Win32.Graphics.Imaging.WICPixelFormatNumericRepresentation = 2
WICPixelFormatNumericRepresentationSignedInteger: win32more.Windows.Win32.Graphics.Imaging.WICPixelFormatNumericRepresentation = 3
WICPixelFormatNumericRepresentationFixed: win32more.Windows.Win32.Graphics.Imaging.WICPixelFormatNumericRepresentation = 4
WICPixelFormatNumericRepresentationFloat: win32more.Windows.Win32.Graphics.Imaging.WICPixelFormatNumericRepresentation = 5
WICPlanarOptions = Int32
WICPlanarOptionsDefault: win32more.Windows.Win32.Graphics.Imaging.WICPlanarOptions = 0
WICPlanarOptionsPreserveSubsampling: win32more.Windows.Win32.Graphics.Imaging.WICPlanarOptions = 1
WICPngBkgdProperties = Int32
WICPngBkgdBackgroundColor: win32more.Windows.Win32.Graphics.Imaging.WICPngBkgdProperties = 1
WICPngChrmProperties = Int32
WICPngChrmWhitePointX: win32more.Windows.Win32.Graphics.Imaging.WICPngChrmProperties = 1
WICPngChrmWhitePointY: win32more.Windows.Win32.Graphics.Imaging.WICPngChrmProperties = 2
WICPngChrmRedX: win32more.Windows.Win32.Graphics.Imaging.WICPngChrmProperties = 3
WICPngChrmRedY: win32more.Windows.Win32.Graphics.Imaging.WICPngChrmProperties = 4
WICPngChrmGreenX: win32more.Windows.Win32.Graphics.Imaging.WICPngChrmProperties = 5
WICPngChrmGreenY: win32more.Windows.Win32.Graphics.Imaging.WICPngChrmProperties = 6
WICPngChrmBlueX: win32more.Windows.Win32.Graphics.Imaging.WICPngChrmProperties = 7
WICPngChrmBlueY: win32more.Windows.Win32.Graphics.Imaging.WICPngChrmProperties = 8
WICPngFilterOption = Int32
WICPngFilterUnspecified: win32more.Windows.Win32.Graphics.Imaging.WICPngFilterOption = 0
WICPngFilterNone: win32more.Windows.Win32.Graphics.Imaging.WICPngFilterOption = 1
WICPngFilterSub: win32more.Windows.Win32.Graphics.Imaging.WICPngFilterOption = 2
WICPngFilterUp: win32more.Windows.Win32.Graphics.Imaging.WICPngFilterOption = 3
WICPngFilterAverage: win32more.Windows.Win32.Graphics.Imaging.WICPngFilterOption = 4
WICPngFilterPaeth: win32more.Windows.Win32.Graphics.Imaging.WICPngFilterOption = 5
WICPngFilterAdaptive: win32more.Windows.Win32.Graphics.Imaging.WICPngFilterOption = 6
WICPngGamaProperties = Int32
WICPngGamaGamma: win32more.Windows.Win32.Graphics.Imaging.WICPngGamaProperties = 1
WICPngHistProperties = Int32
WICPngHistFrequencies: win32more.Windows.Win32.Graphics.Imaging.WICPngHistProperties = 1
WICPngIccpProperties = Int32
WICPngIccpProfileName: win32more.Windows.Win32.Graphics.Imaging.WICPngIccpProperties = 1
WICPngIccpProfileData: win32more.Windows.Win32.Graphics.Imaging.WICPngIccpProperties = 2
WICPngItxtProperties = Int32
WICPngItxtKeyword: win32more.Windows.Win32.Graphics.Imaging.WICPngItxtProperties = 1
WICPngItxtCompressionFlag: win32more.Windows.Win32.Graphics.Imaging.WICPngItxtProperties = 2
WICPngItxtLanguageTag: win32more.Windows.Win32.Graphics.Imaging.WICPngItxtProperties = 3
WICPngItxtTranslatedKeyword: win32more.Windows.Win32.Graphics.Imaging.WICPngItxtProperties = 4
WICPngItxtText: win32more.Windows.Win32.Graphics.Imaging.WICPngItxtProperties = 5
WICPngSrgbProperties = Int32
WICPngSrgbRenderingIntent: win32more.Windows.Win32.Graphics.Imaging.WICPngSrgbProperties = 1
WICPngTimeProperties = Int32
WICPngTimeYear: win32more.Windows.Win32.Graphics.Imaging.WICPngTimeProperties = 1
WICPngTimeMonth: win32more.Windows.Win32.Graphics.Imaging.WICPngTimeProperties = 2
WICPngTimeDay: win32more.Windows.Win32.Graphics.Imaging.WICPngTimeProperties = 3
WICPngTimeHour: win32more.Windows.Win32.Graphics.Imaging.WICPngTimeProperties = 4
WICPngTimeMinute: win32more.Windows.Win32.Graphics.Imaging.WICPngTimeProperties = 5
WICPngTimeSecond: win32more.Windows.Win32.Graphics.Imaging.WICPngTimeProperties = 6
WICProgressNotification = Int32
WICProgressNotificationBegin: win32more.Windows.Win32.Graphics.Imaging.WICProgressNotification = 65536
WICProgressNotificationEnd: win32more.Windows.Win32.Graphics.Imaging.WICProgressNotification = 131072
WICProgressNotificationFrequent: win32more.Windows.Win32.Graphics.Imaging.WICProgressNotification = 262144
WICProgressNotificationAll: win32more.Windows.Win32.Graphics.Imaging.WICProgressNotification = -65536
WICProgressOperation = Int32
WICProgressOperationCopyPixels: win32more.Windows.Win32.Graphics.Imaging.WICProgressOperation = 1
WICProgressOperationWritePixels: win32more.Windows.Win32.Graphics.Imaging.WICProgressOperation = 2
WICProgressOperationAll: win32more.Windows.Win32.Graphics.Imaging.WICProgressOperation = 65535
WICRawCapabilities = Int32
WICRawCapabilityNotSupported: win32more.Windows.Win32.Graphics.Imaging.WICRawCapabilities = 0
WICRawCapabilityGetSupported: win32more.Windows.Win32.Graphics.Imaging.WICRawCapabilities = 1
WICRawCapabilityFullySupported: win32more.Windows.Win32.Graphics.Imaging.WICRawCapabilities = 2
class WICRawCapabilitiesInfo(Structure):
    cbSize: UInt32
    CodecMajorVersion: UInt32
    CodecMinorVersion: UInt32
    ExposureCompensationSupport: win32more.Windows.Win32.Graphics.Imaging.WICRawCapabilities
    ContrastSupport: win32more.Windows.Win32.Graphics.Imaging.WICRawCapabilities
    RGBWhitePointSupport: win32more.Windows.Win32.Graphics.Imaging.WICRawCapabilities
    NamedWhitePointSupport: win32more.Windows.Win32.Graphics.Imaging.WICRawCapabilities
    NamedWhitePointSupportMask: UInt32
    KelvinWhitePointSupport: win32more.Windows.Win32.Graphics.Imaging.WICRawCapabilities
    GammaSupport: win32more.Windows.Win32.Graphics.Imaging.WICRawCapabilities
    TintSupport: win32more.Windows.Win32.Graphics.Imaging.WICRawCapabilities
    SaturationSupport: win32more.Windows.Win32.Graphics.Imaging.WICRawCapabilities
    SharpnessSupport: win32more.Windows.Win32.Graphics.Imaging.WICRawCapabilities
    NoiseReductionSupport: win32more.Windows.Win32.Graphics.Imaging.WICRawCapabilities
    DestinationColorProfileSupport: win32more.Windows.Win32.Graphics.Imaging.WICRawCapabilities
    ToneCurveSupport: win32more.Windows.Win32.Graphics.Imaging.WICRawCapabilities
    RotationSupport: win32more.Windows.Win32.Graphics.Imaging.WICRawRotationCapabilities
    RenderModeSupport: win32more.Windows.Win32.Graphics.Imaging.WICRawCapabilities
WICRawParameterSet = Int32
WICAsShotParameterSet: win32more.Windows.Win32.Graphics.Imaging.WICRawParameterSet = 1
WICUserAdjustedParameterSet: win32more.Windows.Win32.Graphics.Imaging.WICRawParameterSet = 2
WICAutoAdjustedParameterSet: win32more.Windows.Win32.Graphics.Imaging.WICRawParameterSet = 3
WICRawRenderMode = Int32
WICRawRenderModeDraft: win32more.Windows.Win32.Graphics.Imaging.WICRawRenderMode = 1
WICRawRenderModeNormal: win32more.Windows.Win32.Graphics.Imaging.WICRawRenderMode = 2
WICRawRenderModeBestQuality: win32more.Windows.Win32.Graphics.Imaging.WICRawRenderMode = 3
WICRawRotationCapabilities = Int32
WICRawRotationCapabilityNotSupported: win32more.Windows.Win32.Graphics.Imaging.WICRawRotationCapabilities = 0
WICRawRotationCapabilityGetSupported: win32more.Windows.Win32.Graphics.Imaging.WICRawRotationCapabilities = 1
WICRawRotationCapabilityNinetyDegreesSupported: win32more.Windows.Win32.Graphics.Imaging.WICRawRotationCapabilities = 2
WICRawRotationCapabilityFullySupported: win32more.Windows.Win32.Graphics.Imaging.WICRawRotationCapabilities = 3
class WICRawToneCurve(Structure):
    cPoints: UInt32
    aPoints: win32more.Windows.Win32.Graphics.Imaging.WICRawToneCurvePoint * 1
class WICRawToneCurvePoint(Structure):
    Input: Double
    Output: Double
class WICRect(Structure):
    X: Int32
    Y: Int32
    Width: Int32
    Height: Int32
WICSectionAccessLevel = Int32
WICSectionAccessLevelRead: win32more.Windows.Win32.Graphics.Imaging.WICSectionAccessLevel = 1
WICSectionAccessLevelReadWrite: win32more.Windows.Win32.Graphics.Imaging.WICSectionAccessLevel = 3
WICTiffCompressionOption = Int32
WICTiffCompressionDontCare: win32more.Windows.Win32.Graphics.Imaging.WICTiffCompressionOption = 0
WICTiffCompressionNone: win32more.Windows.Win32.Graphics.Imaging.WICTiffCompressionOption = 1
WICTiffCompressionCCITT3: win32more.Windows.Win32.Graphics.Imaging.WICTiffCompressionOption = 2
WICTiffCompressionCCITT4: win32more.Windows.Win32.Graphics.Imaging.WICTiffCompressionOption = 3
WICTiffCompressionLZW: win32more.Windows.Win32.Graphics.Imaging.WICTiffCompressionOption = 4
WICTiffCompressionRLE: win32more.Windows.Win32.Graphics.Imaging.WICTiffCompressionOption = 5
WICTiffCompressionZIP: win32more.Windows.Win32.Graphics.Imaging.WICTiffCompressionOption = 6
WICTiffCompressionLZWHDifferencing: win32more.Windows.Win32.Graphics.Imaging.WICTiffCompressionOption = 7
WICWebpAnimProperties = Int32
WICWebpAnimLoopCount: win32more.Windows.Win32.Graphics.Imaging.WICWebpAnimProperties = 1
WICWebpAnmfProperties = Int32
WICWebpAnmfFrameDuration: win32more.Windows.Win32.Graphics.Imaging.WICWebpAnmfProperties = 1


make_ready(__name__)
