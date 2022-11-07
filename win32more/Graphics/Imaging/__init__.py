from win32more import *
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
        f = globals()[f"_define_{name}"]
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, f())
    return getattr(_module, name)
def __dir__():
    return __all__
WINCODEC_SDK_VERSION1 = 566
WINCODEC_SDK_VERSION2 = 567
CLSID_WICImagingFactory = 'cacaf262-9370-4615-a13b-9f5539da4c0a'
CLSID_WICImagingFactory1 = 'cacaf262-9370-4615-a13b-9f5539da4c0a'
CLSID_WICImagingFactory2 = '317d06e8-5f24-433d-bdf7-79ce68d8abc2'
WINCODEC_SDK_VERSION = 567
GUID_VendorMicrosoft = 'f0e749ca-edef-4589-a73a-ee0e626a2a2b'
GUID_VendorMicrosoftBuiltIn = '257a30fd-06b6-462b-aea4-63f70b86e533'
CLSID_WICPngDecoder = '389ea17b-5078-4cde-b6ef-25c15175c751'
CLSID_WICPngDecoder1 = '389ea17b-5078-4cde-b6ef-25c15175c751'
CLSID_WICPngDecoder2 = 'e018945b-aa86-4008-9bd4-6777a1e40c11'
CLSID_WICBmpDecoder = '6b462062-7cbf-400d-9fdb-813dd10f2778'
CLSID_WICIcoDecoder = 'c61bfcdf-2e0f-4aad-a8d7-e06bafebcdfe'
CLSID_WICJpegDecoder = '9456a480-e88b-43ea-9e73-0b2d9b71b1ca'
CLSID_WICGifDecoder = '381dda3c-9ce9-4834-a23e-1f98f8fc52be'
CLSID_WICTiffDecoder = 'b54e85d9-fe23-499f-8b88-6acea713752b'
CLSID_WICWmpDecoder = 'a26cec36-234c-4950-ae16-e34aace71d0d'
CLSID_WICDdsDecoder = '9053699f-a341-429d-9e90-ee437cf80c73'
CLSID_WICBmpEncoder = '69be8bb4-d66d-47c8-865a-ed1589433782'
CLSID_WICPngEncoder = '27949969-876a-41d7-9447-568f6a35a4dc'
CLSID_WICJpegEncoder = '1a34f5c1-4a5a-46dc-b644-1f4567e7a676'
CLSID_WICGifEncoder = '114f5598-0b22-40a0-86a1-c83ea495adbd'
CLSID_WICTiffEncoder = '0131be10-2001-4c5f-a9b0-cc88fab64ce8'
CLSID_WICWmpEncoder = 'ac4ce3cb-e1c1-44cd-8215-5a1665509ec2'
CLSID_WICDdsEncoder = 'a61dde94-66ce-4ac1-881b-71680588895e'
CLSID_WICAdngDecoder = '981d9411-909e-42a7-8f5d-a747ff052edb'
CLSID_WICJpegQualcommPhoneEncoder = '68ed5c62-f534-4979-b2b3-686a12b2b34c'
CLSID_WICHeifDecoder = 'e9a4a80a-44fe-4de4-8971-7150b10a5199'
CLSID_WICHeifEncoder = '0dbecec1-9eb3-4860-9c6f-ddbe86634575'
CLSID_WICWebpDecoder = '7693e886-51c9-4070-8419-9f70738ec8fa'
CLSID_WICRAWDecoder = '41945702-8302-44a6-9445-ac98e8afa086'
GUID_ContainerFormatBmp = '0af1d87e-fcfe-4188-bdeb-a7906471cbe3'
GUID_ContainerFormatPng = '1b7cfaf4-713f-473c-bbcd-6137425faeaf'
GUID_ContainerFormatIco = 'a3a860c4-338f-4c17-919a-fba4b5628f21'
GUID_ContainerFormatJpeg = '19e4a5aa-5662-4fc5-a0c0-1758028e1057'
GUID_ContainerFormatTiff = '163bcc30-e2e9-4f0b-961d-a3e9fdb788a3'
GUID_ContainerFormatGif = '1f8a5601-7d4d-4cbd-9c82-1bc8d4eeb9a5'
GUID_ContainerFormatWmp = '57a37caa-367a-4540-916b-f183c5093a4b'
GUID_ContainerFormatDds = '9967cb95-2e85-4ac8-8ca2-83d7ccd425c9'
GUID_ContainerFormatAdng = 'f3ff6d0d-38c0-41c4-b1fe-1f3824f17b84'
GUID_ContainerFormatHeif = 'e1e62521-6787-405b-a339-500715b5763f'
GUID_ContainerFormatWebp = 'e094b0e2-67f2-45b3-b0ea-115337ca7cf3'
GUID_ContainerFormatRaw = 'fe99ce60-f19c-433c-a3ae-00acefa9ca21'
CLSID_WICImagingCategories = 'fae3d380-fea4-4623-8c75-c6b61110b681'
CATID_WICBitmapDecoders = '7ed96837-96f0-4812-b211-f13c24117ed3'
CATID_WICBitmapEncoders = 'ac757296-3522-4e11-9862-c17be5a1767e'
CATID_WICPixelFormats = '2b46e70f-cda7-473e-89f6-dc9630a2390b'
CATID_WICFormatConverters = '7835eae8-bf14-49d1-93ce-533a407b2248'
CATID_WICMetadataReader = '05af94d8-7174-4cd2-be4a-4124b80ee4b8'
CATID_WICMetadataWriter = 'abe3b9a4-257d-4b97-bd1a-294af496222e'
CLSID_WICDefaultFormatConverter = '1a3f11dc-b514-4b17-8c5f-2154513852f1'
CLSID_WICFormatConverterHighColor = 'ac75d454-9f37-48f8-b972-4e19bc856011'
CLSID_WICFormatConverterNChannel = 'c17cabb2-d4a3-47d7-a557-339b2efbd4f1'
CLSID_WICFormatConverterWMPhoto = '9cb5172b-d600-46ba-ab77-77bb7e3a00d9'
CLSID_WICPlanarFormatConverter = '184132b8-32f8-4784-9131-dd7224b23438'
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
GUID_WICPixelFormatDontCare = '6fddc324-4e03-4bfe-b185-3d77768dc900'
GUID_WICPixelFormat1bppIndexed = '6fddc324-4e03-4bfe-b185-3d77768dc901'
GUID_WICPixelFormat2bppIndexed = '6fddc324-4e03-4bfe-b185-3d77768dc902'
GUID_WICPixelFormat4bppIndexed = '6fddc324-4e03-4bfe-b185-3d77768dc903'
GUID_WICPixelFormat8bppIndexed = '6fddc324-4e03-4bfe-b185-3d77768dc904'
GUID_WICPixelFormatBlackWhite = '6fddc324-4e03-4bfe-b185-3d77768dc905'
GUID_WICPixelFormat2bppGray = '6fddc324-4e03-4bfe-b185-3d77768dc906'
GUID_WICPixelFormat4bppGray = '6fddc324-4e03-4bfe-b185-3d77768dc907'
GUID_WICPixelFormat8bppGray = '6fddc324-4e03-4bfe-b185-3d77768dc908'
GUID_WICPixelFormat8bppAlpha = 'e6cd0116-eeba-4161-aa85-27dd9fb3a895'
GUID_WICPixelFormat16bppBGR555 = '6fddc324-4e03-4bfe-b185-3d77768dc909'
GUID_WICPixelFormat16bppBGR565 = '6fddc324-4e03-4bfe-b185-3d77768dc90a'
GUID_WICPixelFormat16bppBGRA5551 = '05ec7c2b-f1e6-4961-ad46-e1cc810a87d2'
GUID_WICPixelFormat16bppGray = '6fddc324-4e03-4bfe-b185-3d77768dc90b'
GUID_WICPixelFormat24bppBGR = '6fddc324-4e03-4bfe-b185-3d77768dc90c'
GUID_WICPixelFormat24bppRGB = '6fddc324-4e03-4bfe-b185-3d77768dc90d'
GUID_WICPixelFormat32bppBGR = '6fddc324-4e03-4bfe-b185-3d77768dc90e'
GUID_WICPixelFormat32bppBGRA = '6fddc324-4e03-4bfe-b185-3d77768dc90f'
GUID_WICPixelFormat32bppPBGRA = '6fddc324-4e03-4bfe-b185-3d77768dc910'
GUID_WICPixelFormat32bppGrayFloat = '6fddc324-4e03-4bfe-b185-3d77768dc911'
GUID_WICPixelFormat32bppRGB = 'd98c6b95-3efe-47d6-bb25-eb1748ab0cf1'
GUID_WICPixelFormat32bppRGBA = 'f5c7ad2d-6a8d-43dd-a7a8-a29935261ae9'
GUID_WICPixelFormat32bppPRGBA = '3cc4a650-a527-4d37-a916-3142c7ebedba'
GUID_WICPixelFormat48bppRGB = '6fddc324-4e03-4bfe-b185-3d77768dc915'
GUID_WICPixelFormat48bppBGR = 'e605a384-b468-46ce-bb2e-36f180e64313'
GUID_WICPixelFormat64bppRGB = 'a1182111-186d-4d42-bc6a-9c8303a8dff9'
GUID_WICPixelFormat64bppRGBA = '6fddc324-4e03-4bfe-b185-3d77768dc916'
GUID_WICPixelFormat64bppBGRA = '1562ff7c-d352-46f9-979e-42976b792246'
GUID_WICPixelFormat64bppPRGBA = '6fddc324-4e03-4bfe-b185-3d77768dc917'
GUID_WICPixelFormat64bppPBGRA = '8c518e8e-a4ec-468b-ae70-c9a35a9c5530'
GUID_WICPixelFormat16bppGrayFixedPoint = '6fddc324-4e03-4bfe-b185-3d77768dc913'
GUID_WICPixelFormat32bppBGR101010 = '6fddc324-4e03-4bfe-b185-3d77768dc914'
GUID_WICPixelFormat48bppRGBFixedPoint = '6fddc324-4e03-4bfe-b185-3d77768dc912'
GUID_WICPixelFormat48bppBGRFixedPoint = '49ca140e-cab6-493b-9ddf-60187c37532a'
GUID_WICPixelFormat96bppRGBFixedPoint = '6fddc324-4e03-4bfe-b185-3d77768dc918'
GUID_WICPixelFormat96bppRGBFloat = 'e3fed78f-e8db-4acf-84c1-e97f6136b327'
GUID_WICPixelFormat128bppRGBAFloat = '6fddc324-4e03-4bfe-b185-3d77768dc919'
GUID_WICPixelFormat128bppPRGBAFloat = '6fddc324-4e03-4bfe-b185-3d77768dc91a'
GUID_WICPixelFormat128bppRGBFloat = '6fddc324-4e03-4bfe-b185-3d77768dc91b'
GUID_WICPixelFormat32bppCMYK = '6fddc324-4e03-4bfe-b185-3d77768dc91c'
GUID_WICPixelFormat64bppRGBAFixedPoint = '6fddc324-4e03-4bfe-b185-3d77768dc91d'
GUID_WICPixelFormat64bppBGRAFixedPoint = '356de33c-54d2-4a23-bb04-9b7bf9b1d42d'
GUID_WICPixelFormat64bppRGBFixedPoint = '6fddc324-4e03-4bfe-b185-3d77768dc940'
GUID_WICPixelFormat128bppRGBAFixedPoint = '6fddc324-4e03-4bfe-b185-3d77768dc91e'
GUID_WICPixelFormat128bppRGBFixedPoint = '6fddc324-4e03-4bfe-b185-3d77768dc941'
GUID_WICPixelFormat64bppRGBAHalf = '6fddc324-4e03-4bfe-b185-3d77768dc93a'
GUID_WICPixelFormat64bppPRGBAHalf = '58ad26c2-c623-4d9d-b320-387e49f8c442'
GUID_WICPixelFormat64bppRGBHalf = '6fddc324-4e03-4bfe-b185-3d77768dc942'
GUID_WICPixelFormat48bppRGBHalf = '6fddc324-4e03-4bfe-b185-3d77768dc93b'
GUID_WICPixelFormat32bppRGBE = '6fddc324-4e03-4bfe-b185-3d77768dc93d'
GUID_WICPixelFormat16bppGrayHalf = '6fddc324-4e03-4bfe-b185-3d77768dc93e'
GUID_WICPixelFormat32bppGrayFixedPoint = '6fddc324-4e03-4bfe-b185-3d77768dc93f'
GUID_WICPixelFormat32bppRGBA1010102 = '25238d72-fcf9-4522-b514-5578e5ad55e0'
GUID_WICPixelFormat32bppRGBA1010102XR = '00de6b9a-c101-434b-b502-d0165ee1122c'
GUID_WICPixelFormat32bppR10G10B10A2 = '604e1bb5-8a3c-4b65-b11c-bc0b8dd75b7f'
GUID_WICPixelFormat32bppR10G10B10A2HDR10 = '9c215c5d-1acc-4f0e-a4bc-70fb3ae8fd28'
GUID_WICPixelFormat64bppCMYK = '6fddc324-4e03-4bfe-b185-3d77768dc91f'
GUID_WICPixelFormat24bpp3Channels = '6fddc324-4e03-4bfe-b185-3d77768dc920'
GUID_WICPixelFormat32bpp4Channels = '6fddc324-4e03-4bfe-b185-3d77768dc921'
GUID_WICPixelFormat40bpp5Channels = '6fddc324-4e03-4bfe-b185-3d77768dc922'
GUID_WICPixelFormat48bpp6Channels = '6fddc324-4e03-4bfe-b185-3d77768dc923'
GUID_WICPixelFormat56bpp7Channels = '6fddc324-4e03-4bfe-b185-3d77768dc924'
GUID_WICPixelFormat64bpp8Channels = '6fddc324-4e03-4bfe-b185-3d77768dc925'
GUID_WICPixelFormat48bpp3Channels = '6fddc324-4e03-4bfe-b185-3d77768dc926'
GUID_WICPixelFormat64bpp4Channels = '6fddc324-4e03-4bfe-b185-3d77768dc927'
GUID_WICPixelFormat80bpp5Channels = '6fddc324-4e03-4bfe-b185-3d77768dc928'
GUID_WICPixelFormat96bpp6Channels = '6fddc324-4e03-4bfe-b185-3d77768dc929'
GUID_WICPixelFormat112bpp7Channels = '6fddc324-4e03-4bfe-b185-3d77768dc92a'
GUID_WICPixelFormat128bpp8Channels = '6fddc324-4e03-4bfe-b185-3d77768dc92b'
GUID_WICPixelFormat40bppCMYKAlpha = '6fddc324-4e03-4bfe-b185-3d77768dc92c'
GUID_WICPixelFormat80bppCMYKAlpha = '6fddc324-4e03-4bfe-b185-3d77768dc92d'
GUID_WICPixelFormat32bpp3ChannelsAlpha = '6fddc324-4e03-4bfe-b185-3d77768dc92e'
GUID_WICPixelFormat40bpp4ChannelsAlpha = '6fddc324-4e03-4bfe-b185-3d77768dc92f'
GUID_WICPixelFormat48bpp5ChannelsAlpha = '6fddc324-4e03-4bfe-b185-3d77768dc930'
GUID_WICPixelFormat56bpp6ChannelsAlpha = '6fddc324-4e03-4bfe-b185-3d77768dc931'
GUID_WICPixelFormat64bpp7ChannelsAlpha = '6fddc324-4e03-4bfe-b185-3d77768dc932'
GUID_WICPixelFormat72bpp8ChannelsAlpha = '6fddc324-4e03-4bfe-b185-3d77768dc933'
GUID_WICPixelFormat64bpp3ChannelsAlpha = '6fddc324-4e03-4bfe-b185-3d77768dc934'
GUID_WICPixelFormat80bpp4ChannelsAlpha = '6fddc324-4e03-4bfe-b185-3d77768dc935'
GUID_WICPixelFormat96bpp5ChannelsAlpha = '6fddc324-4e03-4bfe-b185-3d77768dc936'
GUID_WICPixelFormat112bpp6ChannelsAlpha = '6fddc324-4e03-4bfe-b185-3d77768dc937'
GUID_WICPixelFormat128bpp7ChannelsAlpha = '6fddc324-4e03-4bfe-b185-3d77768dc938'
GUID_WICPixelFormat144bpp8ChannelsAlpha = '6fddc324-4e03-4bfe-b185-3d77768dc939'
GUID_WICPixelFormat8bppY = '91b4db54-2df9-42f0-b449-2909bb3df88e'
GUID_WICPixelFormat8bppCb = '1339f224-6bfe-4c3e-9302-e4f3a6d0ca2a'
GUID_WICPixelFormat8bppCr = 'b8145053-2116-49f0-8835-ed844b205c51'
GUID_WICPixelFormat16bppCbCr = 'ff95ba6e-11e0-4263-bb45-01721f3460a4'
GUID_WICPixelFormat16bppYQuantizedDctCoefficients = 'a355f433-48e8-4a42-84d8-e2aa26ca80a4'
GUID_WICPixelFormat16bppCbQuantizedDctCoefficients = 'd2c4ff61-56a5-49c2-8b5c-4c1925964837'
GUID_WICPixelFormat16bppCrQuantizedDctCoefficients = '2fe354f0-1680-42d8-9231-e73c0565bfc1'
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
GUID_MetadataFormatUnknown = 'a45e592f-9078-4a7c-adb5-4edc4fd61b1f'
GUID_MetadataFormatIfd = '537396c6-2d8a-4bb6-9bf8-2f0a8e2a3adf'
GUID_MetadataFormatSubIfd = '58a2e128-2db9-4e57-bb14-5177891ed331'
GUID_MetadataFormatExif = '1c3c4f9d-b84a-467d-9493-36cfbd59ea57'
GUID_MetadataFormatGps = '7134ab8a-9351-44ad-af62-448db6b502ec'
GUID_MetadataFormatInterop = 'ed686f8e-681f-4c8b-bd41-a8addbf6b3fc'
GUID_MetadataFormatApp0 = '79007028-268d-45d6-a3c2-354e6a504bc9'
GUID_MetadataFormatApp1 = '8fd3dfc3-f951-492b-817f-69c2e6d9a5b0'
GUID_MetadataFormatApp13 = '326556a2-f502-4354-9cc0-8e3f48eaf6b5'
GUID_MetadataFormatIPTC = '4fab0914-e129-4087-a1d1-bc812d45a7b5'
GUID_MetadataFormatIRB = '16100d66-8570-4bb9-b92d-fda4b23ece67'
GUID_MetadataFormat8BIMIPTC = '0010568c-0852-4e6a-b191-5c33ac5b0430'
GUID_MetadataFormat8BIMResolutionInfo = '739f305d-81db-43cb-ac5e-55013ef9f003'
GUID_MetadataFormat8BIMIPTCDigest = '1ca32285-9ccd-4786-8bd8-79539db6a006'
GUID_MetadataFormatXMP = 'bb5acc38-f216-4cec-a6c5-5f6e739763a9'
GUID_MetadataFormatThumbnail = '243dcee9-8703-40ee-8ef0-22a600b8058c'
GUID_MetadataFormatChunktEXt = '568d8936-c0a9-4923-905d-df2b38238fbc'
GUID_MetadataFormatXMPStruct = '22383cf1-ed17-4e2e-af17-d85b8f6b30d0'
GUID_MetadataFormatXMPBag = '833cca5f-dcb7-4516-806f-6596ab26dce4'
GUID_MetadataFormatXMPSeq = '63e8df02-eb6c-456c-a224-b25e794fd648'
GUID_MetadataFormatXMPAlt = '7b08a675-91aa-481b-a798-4da94908613b'
GUID_MetadataFormatLSD = 'e256031e-6299-4929-b98d-5ac884afba92'
GUID_MetadataFormatIMD = 'bd2bb086-4d52-48dd-9677-db483e85ae8f'
GUID_MetadataFormatGCE = '2a25cad8-deeb-4c69-a788-0ec2266dcafd'
GUID_MetadataFormatAPE = '2e043dc2-c967-4e05-875e-618bf67e85c3'
GUID_MetadataFormatJpegChrominance = 'f73d0dcf-cec6-4f85-9b0e-1c3956b1bef7'
GUID_MetadataFormatJpegLuminance = '86908007-edfc-4860-8d4b-4ee6e83e6058'
GUID_MetadataFormatJpegComment = '220e5f33-afd3-474e-9d31-7d4fe730f557'
GUID_MetadataFormatGifComment = 'c4b6e0e0-cfb4-4ad3-ab33-9aad2355a34a'
GUID_MetadataFormatChunkgAMA = 'f00935a5-1d5d-4cd1-81b2-9324d7eca781'
GUID_MetadataFormatChunkbKGD = 'e14d3571-6b47-4dea-b60a-87ce0a78dfb7'
GUID_MetadataFormatChunkiTXt = 'c2bec729-0b68-4b77-aa0e-6295a6ac1814'
GUID_MetadataFormatChunkcHRM = '9db3655b-2842-44b3-8067-12e9b375556a'
GUID_MetadataFormatChunkhIST = 'c59a82da-db74-48a4-bd6a-b69c4931ef95'
GUID_MetadataFormatChunkiCCP = 'eb4349ab-b685-450f-91b5-e802e892536c'
GUID_MetadataFormatChunksRGB = 'c115fd36-cc6f-4e3f-8363-524b87c6b0d9'
GUID_MetadataFormatChunktIME = '6b00ae2d-e24b-460a-98b6-878bd03072fd'
GUID_MetadataFormatDds = '4a064603-8c33-4e60-9c29-136231702d08'
GUID_MetadataFormatHeif = '817ef3e1-1288-45f4-a852-260d9e7cce83'
GUID_MetadataFormatHeifHDR = '568b8d8a-1e65-438c-8968-d60e1012beb9'
GUID_MetadataFormatWebpANIM = '6dc4fda6-78e6-4102-ae35-bcfa1edcc78b'
GUID_MetadataFormatWebpANMF = '43c105ee-b93b-4abb-b003-a08c0d870471'
CLSID_WICUnknownMetadataReader = '699745c2-5066-4b82-a8e3-d40478dbec8c'
CLSID_WICUnknownMetadataWriter = 'a09cca86-27ba-4f39-9053-121fa4dc08fc'
CLSID_WICApp0MetadataWriter = 'f3c633a2-46c8-498e-8fbb-cc6f721bbcde'
CLSID_WICApp0MetadataReader = '43324b33-a78f-480f-9111-9638aaccc832'
CLSID_WICApp1MetadataWriter = 'ee366069-1832-420f-b381-0479ad066f19'
CLSID_WICApp1MetadataReader = 'dde33513-774e-4bcd-ae79-02f4adfe62fc'
CLSID_WICApp13MetadataWriter = '7b19a919-a9d6-49e5-bd45-02c34e4e4cd5'
CLSID_WICApp13MetadataReader = 'aa7e3c50-864c-4604-bc04-8b0b76e637f6'
CLSID_WICIfdMetadataReader = '8f914656-9d0a-4eb2-9019-0bf96d8a9ee6'
CLSID_WICIfdMetadataWriter = 'b1ebfc28-c9bd-47a2-8d33-b948769777a7'
CLSID_WICSubIfdMetadataReader = '50d42f09-ecd1-4b41-b65d-da1fdaa75663'
CLSID_WICSubIfdMetadataWriter = '8ade5386-8e9b-4f4c-acf2-f0008706b238'
CLSID_WICExifMetadataReader = 'd9403860-297f-4a49-bf9b-77898150a442'
CLSID_WICExifMetadataWriter = 'c9a14cda-c339-460b-9078-d4debcfabe91'
CLSID_WICGpsMetadataReader = '3697790b-223b-484e-9925-c4869218f17a'
CLSID_WICGpsMetadataWriter = 'cb8c13e4-62b5-4c96-a48b-6ba6ace39c76'
CLSID_WICInteropMetadataReader = 'b5c8b898-0074-459f-b700-860d4651ea14'
CLSID_WICInteropMetadataWriter = '122ec645-cd7e-44d8-b186-2c8c20c3b50f'
CLSID_WICThumbnailMetadataReader = 'fb012959-f4f6-44d7-9d09-daa087a9db57'
CLSID_WICThumbnailMetadataWriter = 'd049b20c-5dd0-44fe-b0b3-8f92c8e6d080'
CLSID_WICIPTCMetadataReader = '03012959-f4f6-44d7-9d09-daa087a9db57'
CLSID_WICIPTCMetadataWriter = '1249b20c-5dd0-44fe-b0b3-8f92c8e6d080'
CLSID_WICIRBMetadataReader = 'd4dcd3d7-b4c2-47d9-a6bf-b89ba396a4a3'
CLSID_WICIRBMetadataWriter = '5c5c1935-0235-4434-80bc-251bc1ec39c6'
CLSID_WIC8BIMIPTCMetadataReader = '0010668c-0801-4da6-a4a4-826522b6d28f'
CLSID_WIC8BIMIPTCMetadataWriter = '00108226-ee41-44a2-9e9c-4be4d5b1d2cd'
CLSID_WIC8BIMResolutionInfoMetadataReader = '5805137a-e348-4f7c-b3cc-6db9965a0599'
CLSID_WIC8BIMResolutionInfoMetadataWriter = '4ff2fe0e-e74a-4b71-98c4-ab7dc16707ba'
CLSID_WIC8BIMIPTCDigestMetadataReader = '02805f1e-d5aa-415b-82c5-61c033a988a6'
CLSID_WIC8BIMIPTCDigestMetadataWriter = '2db5e62b-0d67-495f-8f9d-c2f0188647ac'
CLSID_WICPngTextMetadataReader = '4b59afcc-b8c3-408a-b670-89e5fab6fda7'
CLSID_WICPngTextMetadataWriter = 'b5ebafb9-253e-4a72-a744-0762d2685683'
CLSID_WICXMPMetadataReader = '72b624df-ae11-4948-a65c-351eb0829419'
CLSID_WICXMPMetadataWriter = '1765e14e-1bd4-462e-b6b1-590bf1262ac6'
CLSID_WICXMPStructMetadataReader = '01b90d9a-8209-47f7-9c52-e1244bf50ced'
CLSID_WICXMPStructMetadataWriter = '22c21f93-7ddb-411c-9b17-c5b7bd064abc'
CLSID_WICXMPBagMetadataReader = 'e7e79a30-4f2c-4fab-8d00-394f2d6bbebe'
CLSID_WICXMPBagMetadataWriter = 'ed822c8c-d6be-4301-a631-0e1416bad28f'
CLSID_WICXMPSeqMetadataReader = '7f12e753-fc71-43d7-a51d-92f35977abb5'
CLSID_WICXMPSeqMetadataWriter = '6d68d1de-d432-4b0f-923a-091183a9bda7'
CLSID_WICXMPAltMetadataReader = 'aa94dcc2-b8b0-4898-b835-000aabd74393'
CLSID_WICXMPAltMetadataWriter = '076c2a6c-f78f-4c46-a723-3583e70876ea'
CLSID_WICLSDMetadataReader = '41070793-59e4-479a-a1f7-954adc2ef5fc'
CLSID_WICLSDMetadataWriter = '73c037e7-e5d9-4954-876a-6da81d6e5768'
CLSID_WICGCEMetadataReader = 'b92e345d-f52d-41f3-b562-081bc772e3b9'
CLSID_WICGCEMetadataWriter = 'af95dc76-16b2-47f4-b3ea-3c31796693e7'
CLSID_WICIMDMetadataReader = '7447a267-0015-42c8-a8f1-fb3b94c68361'
CLSID_WICIMDMetadataWriter = '8c89071f-452e-4e95-9682-9d1024627172'
CLSID_WICAPEMetadataReader = '1767b93a-b021-44ea-920f-863c11f4f768'
CLSID_WICAPEMetadataWriter = 'bd6edfca-2890-482f-b233-8d7339a1cf8d'
CLSID_WICJpegChrominanceMetadataReader = '50b1904b-f28f-4574-93f4-0bade82c69e9'
CLSID_WICJpegChrominanceMetadataWriter = '3ff566f0-6e6b-49d4-96e6-b78886692c62'
CLSID_WICJpegLuminanceMetadataReader = '356f2f88-05a6-4728-b9a4-1bfbce04d838'
CLSID_WICJpegLuminanceMetadataWriter = '1d583abc-8a0e-4657-9982-a380ca58fb4b'
CLSID_WICJpegCommentMetadataReader = '9f66347c-60c4-4c4d-ab58-d2358685f607'
CLSID_WICJpegCommentMetadataWriter = 'e573236f-55b1-4eda-81ea-9f65db0290d3'
CLSID_WICGifCommentMetadataReader = '32557d3b-69dc-4f95-836e-f5972b2f6159'
CLSID_WICGifCommentMetadataWriter = 'a02797fc-c4ae-418c-af95-e637c7ead2a1'
CLSID_WICPngGamaMetadataReader = '3692ca39-e082-4350-9e1f-3704cb083cd5'
CLSID_WICPngGamaMetadataWriter = 'ff036d13-5d4b-46dd-b10f-106693d9fe4f'
CLSID_WICPngBkgdMetadataReader = '0ce7a4a6-03e8-4a60-9d15-282ef32ee7da'
CLSID_WICPngBkgdMetadataWriter = '68e3f2fd-31ae-4441-bb6a-fd7047525f90'
CLSID_WICPngItxtMetadataReader = 'aabfb2fa-3e1e-4a8f-8977-5556fb94ea23'
CLSID_WICPngItxtMetadataWriter = '31879719-e751-4df8-981d-68dff67704ed'
CLSID_WICPngChrmMetadataReader = 'f90b5f36-367b-402a-9dd1-bc0fd59d8f62'
CLSID_WICPngChrmMetadataWriter = 'e23ce3eb-5608-4e83-bcef-27b1987e51d7'
CLSID_WICPngHistMetadataReader = '877a0bb7-a313-4491-87b5-2e6d0594f520'
CLSID_WICPngHistMetadataWriter = '8a03e749-672e-446e-bf1f-2c11d233b6ff'
CLSID_WICPngIccpMetadataReader = 'f5d3e63b-cb0f-4628-a478-6d8244be36b1'
CLSID_WICPngIccpMetadataWriter = '16671e5f-0ce6-4cc4-9768-e89fe5018ade'
CLSID_WICPngSrgbMetadataReader = 'fb40360c-547e-4956-a3b9-d4418859ba66'
CLSID_WICPngSrgbMetadataWriter = 'a6ee35c6-87ec-47df-9f22-1d5aad840c82'
CLSID_WICPngTimeMetadataReader = 'd94edf02-efe5-4f0d-85c8-f5a68b3000b1'
CLSID_WICPngTimeMetadataWriter = '1ab78400-b5a3-4d91-8ace-33fcd1499be6'
CLSID_WICDdsMetadataReader = '276c88ca-7533-4a86-b676-66b36080d484'
CLSID_WICDdsMetadataWriter = 'fd688bbd-31ed-4db7-a723-934927d38367'
CLSID_WICHeifMetadataReader = 'acddfc3f-85ec-41bc-bdef-1bc262e4db05'
CLSID_WICHeifMetadataWriter = '3ae45e79-40bc-4401-ace5-dd3cb16e6afe'
CLSID_WICHeifHDRMetadataReader = '2438de3d-94d9-4be8-84a8-4de95a575e75'
CLSID_WICWebpAnimMetadataReader = '076f9911-a348-465c-a807-a252f3f2d3de'
CLSID_WICWebpAnmfMetadataReader = '85a10b03-c9f6-439f-be5e-c0fbef67807c'
def _define_WICRect_head():
    class WICRect(Structure):
        pass
    return WICRect
def _define_WICRect():
    WICRect = win32more.Graphics.Imaging.WICRect_head
    WICRect._fields_ = [
        ("X", Int32),
        ("Y", Int32),
        ("Width", Int32),
        ("Height", Int32),
    ]
    return WICRect
WICColorContextType = Int32
WICColorContextType_WICColorContextUninitialized = 0
WICColorContextType_WICColorContextProfile = 1
WICColorContextType_WICColorContextExifColorSpace = 2
WICBitmapCreateCacheOption = Int32
WICBitmapCreateCacheOption_WICBitmapNoCache = 0
WICBitmapCreateCacheOption_WICBitmapCacheOnDemand = 1
WICBitmapCreateCacheOption_WICBitmapCacheOnLoad = 2
WICBitmapCreateCacheOption_WICBITMAPCREATECACHEOPTION_FORCE_DWORD = 2147483647
WICDecodeOptions = Int32
WICDecodeOptions_WICDecodeMetadataCacheOnDemand = 0
WICDecodeOptions_WICDecodeMetadataCacheOnLoad = 1
WICDecodeOptions_WICMETADATACACHEOPTION_FORCE_DWORD = 2147483647
WICBitmapEncoderCacheOption = Int32
WICBitmapEncoderCacheOption_WICBitmapEncoderCacheInMemory = 0
WICBitmapEncoderCacheOption_WICBitmapEncoderCacheTempFile = 1
WICBitmapEncoderCacheOption_WICBitmapEncoderNoCache = 2
WICBitmapEncoderCacheOption_WICBITMAPENCODERCACHEOPTION_FORCE_DWORD = 2147483647
WICComponentType = Int32
WICComponentType_WICDecoder = 1
WICComponentType_WICEncoder = 2
WICComponentType_WICPixelFormatConverter = 4
WICComponentType_WICMetadataReader = 8
WICComponentType_WICMetadataWriter = 16
WICComponentType_WICPixelFormat = 32
WICComponentType_WICAllComponents = 63
WICComponentType_WICCOMPONENTTYPE_FORCE_DWORD = 2147483647
WICComponentEnumerateOptions = Int32
WICComponentEnumerateOptions_WICComponentEnumerateDefault = 0
WICComponentEnumerateOptions_WICComponentEnumerateRefresh = 1
WICComponentEnumerateOptions_WICComponentEnumerateDisabled = -2147483648
WICComponentEnumerateOptions_WICComponentEnumerateUnsigned = 1073741824
WICComponentEnumerateOptions_WICComponentEnumerateBuiltInOnly = 536870912
WICComponentEnumerateOptions_WICCOMPONENTENUMERATEOPTIONS_FORCE_DWORD = 2147483647
def _define_WICBitmapPattern_head():
    class WICBitmapPattern(Structure):
        pass
    return WICBitmapPattern
def _define_WICBitmapPattern():
    WICBitmapPattern = win32more.Graphics.Imaging.WICBitmapPattern_head
    WICBitmapPattern._fields_ = [
        ("Position", win32more.Foundation.ULARGE_INTEGER),
        ("Length", UInt32),
        ("Pattern", c_char_p_no),
        ("Mask", c_char_p_no),
        ("EndOfStream", win32more.Foundation.BOOL),
    ]
    return WICBitmapPattern
WICBitmapInterpolationMode = Int32
WICBitmapInterpolationMode_WICBitmapInterpolationModeNearestNeighbor = 0
WICBitmapInterpolationMode_WICBitmapInterpolationModeLinear = 1
WICBitmapInterpolationMode_WICBitmapInterpolationModeCubic = 2
WICBitmapInterpolationMode_WICBitmapInterpolationModeFant = 3
WICBitmapInterpolationMode_WICBitmapInterpolationModeHighQualityCubic = 4
WICBitmapInterpolationMode_WICBITMAPINTERPOLATIONMODE_FORCE_DWORD = 2147483647
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
WICBitmapAlphaChannelOption = Int32
WICBitmapAlphaChannelOption_WICBitmapUseAlpha = 0
WICBitmapAlphaChannelOption_WICBitmapUsePremultipliedAlpha = 1
WICBitmapAlphaChannelOption_WICBitmapIgnoreAlpha = 2
WICBitmapAlphaChannelOption_WICBITMAPALPHACHANNELOPTIONS_FORCE_DWORD = 2147483647
WICBitmapTransformOptions = Int32
WICBitmapTransformOptions_WICBitmapTransformRotate0 = 0
WICBitmapTransformOptions_WICBitmapTransformRotate90 = 1
WICBitmapTransformOptions_WICBitmapTransformRotate180 = 2
WICBitmapTransformOptions_WICBitmapTransformRotate270 = 3
WICBitmapTransformOptions_WICBitmapTransformFlipHorizontal = 8
WICBitmapTransformOptions_WICBitmapTransformFlipVertical = 16
WICBitmapTransformOptions_WICBITMAPTRANSFORMOPTIONS_FORCE_DWORD = 2147483647
WICBitmapLockFlags = Int32
WICBitmapLockFlags_WICBitmapLockRead = 1
WICBitmapLockFlags_WICBitmapLockWrite = 2
WICBitmapLockFlags_WICBITMAPLOCKFLAGS_FORCE_DWORD = 2147483647
WICBitmapDecoderCapabilities = Int32
WICBitmapDecoderCapabilities_WICBitmapDecoderCapabilitySameEncoder = 1
WICBitmapDecoderCapabilities_WICBitmapDecoderCapabilityCanDecodeAllImages = 2
WICBitmapDecoderCapabilities_WICBitmapDecoderCapabilityCanDecodeSomeImages = 4
WICBitmapDecoderCapabilities_WICBitmapDecoderCapabilityCanEnumerateMetadata = 8
WICBitmapDecoderCapabilities_WICBitmapDecoderCapabilityCanDecodeThumbnail = 16
WICBitmapDecoderCapabilities_WICBITMAPDECODERCAPABILITIES_FORCE_DWORD = 2147483647
WICProgressOperation = Int32
WICProgressOperation_WICProgressOperationCopyPixels = 1
WICProgressOperation_WICProgressOperationWritePixels = 2
WICProgressOperation_WICProgressOperationAll = 65535
WICProgressOperation_WICPROGRESSOPERATION_FORCE_DWORD = 2147483647
WICProgressNotification = Int32
WICProgressNotification_WICProgressNotificationBegin = 65536
WICProgressNotification_WICProgressNotificationEnd = 131072
WICProgressNotification_WICProgressNotificationFrequent = 262144
WICProgressNotification_WICProgressNotificationAll = -65536
WICProgressNotification_WICPROGRESSNOTIFICATION_FORCE_DWORD = 2147483647
WICComponentSigning = Int32
WICComponentSigning_WICComponentSigned = 1
WICComponentSigning_WICComponentUnsigned = 2
WICComponentSigning_WICComponentSafe = 4
WICComponentSigning_WICComponentDisabled = -2147483648
WICComponentSigning_WICCOMPONENTSIGNING_FORCE_DWORD = 2147483647
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
WICGifGraphicControlExtensionProperties = UInt32
WICGifGraphicControlExtensionProperties_WICGifGraphicControlExtensionDisposal = 1
WICGifGraphicControlExtensionProperties_WICGifGraphicControlExtensionUserInputFlag = 2
WICGifGraphicControlExtensionProperties_WICGifGraphicControlExtensionTransparencyFlag = 3
WICGifGraphicControlExtensionProperties_WICGifGraphicControlExtensionDelay = 4
WICGifGraphicControlExtensionProperties_WICGifGraphicControlExtensionTransparentColorIndex = 5
WICGifGraphicControlExtensionProperties_WICGifGraphicControlExtensionProperties_FORCE_DWORD = 2147483647
WICGifApplicationExtensionProperties = UInt32
WICGifApplicationExtensionProperties_WICGifApplicationExtensionApplication = 1
WICGifApplicationExtensionProperties_WICGifApplicationExtensionData = 2
WICGifApplicationExtensionProperties_WICGifApplicationExtensionProperties_FORCE_DWORD = 2147483647
WICGifCommentExtensionProperties = UInt32
WICGifCommentExtensionProperties_WICGifCommentExtensionText = 1
WICGifCommentExtensionProperties_WICGifCommentExtensionProperties_FORCE_DWORD = 2147483647
WICJpegCommentProperties = UInt32
WICJpegCommentProperties_WICJpegCommentText = 1
WICJpegCommentProperties_WICJpegCommentProperties_FORCE_DWORD = 2147483647
WICJpegLuminanceProperties = UInt32
WICJpegLuminanceProperties_WICJpegLuminanceTable = 1
WICJpegLuminanceProperties_WICJpegLuminanceProperties_FORCE_DWORD = 2147483647
WICJpegChrominanceProperties = UInt32
WICJpegChrominanceProperties_WICJpegChrominanceTable = 1
WICJpegChrominanceProperties_WICJpegChrominanceProperties_FORCE_DWORD = 2147483647
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
WIC8BIMIptcDigestProperties = UInt32
WIC8BIMIptcDigestProperties_WIC8BIMIptcDigestPString = 1
WIC8BIMIptcDigestProperties_WIC8BIMIptcDigestIptcDigest = 2
WIC8BIMIptcDigestProperties_WIC8BIMIptcDigestProperties_FORCE_DWORD = 2147483647
WICPngGamaProperties = UInt32
WICPngGamaProperties_WICPngGamaGamma = 1
WICPngGamaProperties_WICPngGamaProperties_FORCE_DWORD = 2147483647
WICPngBkgdProperties = UInt32
WICPngBkgdProperties_WICPngBkgdBackgroundColor = 1
WICPngBkgdProperties_WICPngBkgdProperties_FORCE_DWORD = 2147483647
WICPngItxtProperties = UInt32
WICPngItxtProperties_WICPngItxtKeyword = 1
WICPngItxtProperties_WICPngItxtCompressionFlag = 2
WICPngItxtProperties_WICPngItxtLanguageTag = 3
WICPngItxtProperties_WICPngItxtTranslatedKeyword = 4
WICPngItxtProperties_WICPngItxtText = 5
WICPngItxtProperties_WICPngItxtProperties_FORCE_DWORD = 2147483647
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
WICPngHistProperties = UInt32
WICPngHistProperties_WICPngHistFrequencies = 1
WICPngHistProperties_WICPngHistProperties_FORCE_DWORD = 2147483647
WICPngIccpProperties = UInt32
WICPngIccpProperties_WICPngIccpProfileName = 1
WICPngIccpProperties_WICPngIccpProfileData = 2
WICPngIccpProperties_WICPngIccpProperties_FORCE_DWORD = 2147483647
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
WICHeifProperties = UInt32
WICHeifProperties_WICHeifOrientation = 1
WICHeifProperties_WICHeifProperties_FORCE_DWORD = 2147483647
WICHeifHdrProperties = UInt32
WICHeifHdrProperties_WICHeifHdrMaximumLuminanceLevel = 1
WICHeifHdrProperties_WICHeifHdrMaximumFrameAverageLuminanceLevel = 2
WICHeifHdrProperties_WICHeifHdrMinimumMasteringDisplayLuminanceLevel = 3
WICHeifHdrProperties_WICHeifHdrMaximumMasteringDisplayLuminanceLevel = 4
WICHeifHdrProperties_WICHeifHdrCustomVideoPrimaries = 5
WICHeifHdrProperties_WICHeifHdrProperties_FORCE_DWORD = 2147483647
WICWebpAnimProperties = UInt32
WICWebpAnimProperties_WICWebpAnimLoopCount = 1
WICWebpAnimProperties_WICWebpAnimProperties_FORCE_DWORD = 2147483647
WICWebpAnmfProperties = UInt32
WICWebpAnmfProperties_WICWebpAnmfFrameDuration = 1
WICWebpAnmfProperties_WICWebpAnmfProperties_FORCE_DWORD = 2147483647
WICSectionAccessLevel = UInt32
WICSectionAccessLevel_WICSectionAccessLevelRead = 1
WICSectionAccessLevel_WICSectionAccessLevelReadWrite = 3
WICSectionAccessLevel_WICSectionAccessLevel_FORCE_DWORD = 2147483647
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
WICJpegIndexingOptions = UInt32
WICJpegIndexingOptions_WICJpegIndexingOptionsGenerateOnDemand = 0
WICJpegIndexingOptions_WICJpegIndexingOptionsGenerateOnLoad = 1
WICJpegIndexingOptions_WICJpegIndexingOptions_FORCE_DWORD = 2147483647
WICJpegTransferMatrix = UInt32
WICJpegTransferMatrix_WICJpegTransferMatrixIdentity = 0
WICJpegTransferMatrix_WICJpegTransferMatrixBT601 = 1
WICJpegTransferMatrix_WICJpegTransferMatrix_FORCE_DWORD = 2147483647
WICJpegScanType = UInt32
WICJpegScanType_WICJpegScanTypeInterleaved = 0
WICJpegScanType_WICJpegScanTypePlanarComponents = 1
WICJpegScanType_WICJpegScanTypeProgressive = 2
WICJpegScanType_WICJpegScanType_FORCE_DWORD = 2147483647
def _define_WICImageParameters_head():
    class WICImageParameters(Structure):
        pass
    return WICImageParameters
def _define_WICImageParameters():
    WICImageParameters = win32more.Graphics.Imaging.WICImageParameters_head
    WICImageParameters._fields_ = [
        ("PixelFormat", win32more.Graphics.Direct2D.Common.D2D1_PIXEL_FORMAT),
        ("DpiX", Single),
        ("DpiY", Single),
        ("Top", Single),
        ("Left", Single),
        ("PixelWidth", UInt32),
        ("PixelHeight", UInt32),
    ]
    return WICImageParameters
def _define_WICBitmapPlaneDescription_head():
    class WICBitmapPlaneDescription(Structure):
        pass
    return WICBitmapPlaneDescription
def _define_WICBitmapPlaneDescription():
    WICBitmapPlaneDescription = win32more.Graphics.Imaging.WICBitmapPlaneDescription_head
    WICBitmapPlaneDescription._fields_ = [
        ("Format", Guid),
        ("Width", UInt32),
        ("Height", UInt32),
    ]
    return WICBitmapPlaneDescription
def _define_WICBitmapPlane_head():
    class WICBitmapPlane(Structure):
        pass
    return WICBitmapPlane
def _define_WICBitmapPlane():
    WICBitmapPlane = win32more.Graphics.Imaging.WICBitmapPlane_head
    WICBitmapPlane._fields_ = [
        ("Format", Guid),
        ("pbBuffer", c_char_p_no),
        ("cbStride", UInt32),
        ("cbBufferSize", UInt32),
    ]
    return WICBitmapPlane
def _define_WICJpegFrameHeader_head():
    class WICJpegFrameHeader(Structure):
        pass
    return WICJpegFrameHeader
def _define_WICJpegFrameHeader():
    WICJpegFrameHeader = win32more.Graphics.Imaging.WICJpegFrameHeader_head
    WICJpegFrameHeader._fields_ = [
        ("Width", UInt32),
        ("Height", UInt32),
        ("TransferMatrix", win32more.Graphics.Imaging.WICJpegTransferMatrix),
        ("ScanType", win32more.Graphics.Imaging.WICJpegScanType),
        ("cComponents", UInt32),
        ("ComponentIdentifiers", UInt32),
        ("SampleFactors", UInt32),
        ("QuantizationTableIndices", UInt32),
    ]
    return WICJpegFrameHeader
def _define_WICJpegScanHeader_head():
    class WICJpegScanHeader(Structure):
        pass
    return WICJpegScanHeader
def _define_WICJpegScanHeader():
    WICJpegScanHeader = win32more.Graphics.Imaging.WICJpegScanHeader_head
    WICJpegScanHeader._fields_ = [
        ("cComponents", UInt32),
        ("RestartInterval", UInt32),
        ("ComponentSelectors", UInt32),
        ("HuffmanTableIndices", UInt32),
        ("StartSpectralSelection", Byte),
        ("EndSpectralSelection", Byte),
        ("SuccessiveApproximationHigh", Byte),
        ("SuccessiveApproximationLow", Byte),
    ]
    return WICJpegScanHeader
def _define_IWICPalette_head():
    class IWICPalette(win32more.System.Com.IUnknown_head):
        Guid = Guid('00000040-a8f2-4877-ba0a-fd2b6645fb94')
    return IWICPalette
def _define_IWICPalette():
    IWICPalette = win32more.Graphics.Imaging.IWICPalette_head
    IWICPalette.InitializePredefined = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Imaging.WICBitmapPaletteType,win32more.Foundation.BOOL, use_last_error=False)(3, 'InitializePredefined', ((1, 'ePaletteType'),(1, 'fAddTransparentColor'),)))
    IWICPalette.InitializeCustom = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32),UInt32, use_last_error=False)(4, 'InitializeCustom', ((1, 'pColors'),(1, 'cCount'),)))
    IWICPalette.InitializeFromBitmap = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Imaging.IWICBitmapSource_head,UInt32,win32more.Foundation.BOOL, use_last_error=False)(5, 'InitializeFromBitmap', ((1, 'pISurface'),(1, 'cCount'),(1, 'fAddTransparentColor'),)))
    IWICPalette.InitializeFromPalette = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Imaging.IWICPalette_head, use_last_error=False)(6, 'InitializeFromPalette', ((1, 'pIPalette'),)))
    IWICPalette.GetType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Imaging.WICBitmapPaletteType), use_last_error=False)(7, 'GetType', ((1, 'pePaletteType'),)))
    IWICPalette.GetColorCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(8, 'GetColorCount', ((1, 'pcCount'),)))
    IWICPalette.GetColors = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(UInt32),POINTER(UInt32), use_last_error=False)(9, 'GetColors', ((1, 'cCount'),(1, 'pColors'),(1, 'pcActualColors'),)))
    IWICPalette.IsBlackWhite = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(10, 'IsBlackWhite', ((1, 'pfIsBlackWhite'),)))
    IWICPalette.IsGrayscale = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(11, 'IsGrayscale', ((1, 'pfIsGrayscale'),)))
    IWICPalette.HasAlpha = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(12, 'HasAlpha', ((1, 'pfHasAlpha'),)))
    win32more.System.Com.IUnknown
    return IWICPalette
def _define_IWICBitmapSource_head():
    class IWICBitmapSource(win32more.System.Com.IUnknown_head):
        Guid = Guid('00000120-a8f2-4877-ba0a-fd2b6645fb94')
    return IWICBitmapSource
def _define_IWICBitmapSource():
    IWICBitmapSource = win32more.Graphics.Imaging.IWICBitmapSource_head
    IWICBitmapSource.GetSize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32),POINTER(UInt32), use_last_error=False)(3, 'GetSize', ((1, 'puiWidth'),(1, 'puiHeight'),)))
    IWICBitmapSource.GetPixelFormat = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid), use_last_error=False)(4, 'GetPixelFormat', ((1, 'pPixelFormat'),)))
    IWICBitmapSource.GetResolution = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double),POINTER(Double), use_last_error=False)(5, 'GetResolution', ((1, 'pDpiX'),(1, 'pDpiY'),)))
    IWICBitmapSource.CopyPalette = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Imaging.IWICPalette_head, use_last_error=False)(6, 'CopyPalette', ((1, 'pIPalette'),)))
    IWICBitmapSource.CopyPixels = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Imaging.WICRect_head),UInt32,UInt32,POINTER(Byte), use_last_error=False)(7, 'CopyPixels', ((1, 'prc'),(1, 'cbStride'),(1, 'cbBufferSize'),(1, 'pbBuffer'),)))
    win32more.System.Com.IUnknown
    return IWICBitmapSource
def _define_IWICFormatConverter_head():
    class IWICFormatConverter(win32more.Graphics.Imaging.IWICBitmapSource_head):
        Guid = Guid('00000301-a8f2-4877-ba0a-fd2b6645fb94')
    return IWICFormatConverter
def _define_IWICFormatConverter():
    IWICFormatConverter = win32more.Graphics.Imaging.IWICFormatConverter_head
    IWICFormatConverter.Initialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Imaging.IWICBitmapSource_head,POINTER(Guid),win32more.Graphics.Imaging.WICBitmapDitherType,win32more.Graphics.Imaging.IWICPalette_head,Double,win32more.Graphics.Imaging.WICBitmapPaletteType, use_last_error=False)(8, 'Initialize', ((1, 'pISource'),(1, 'dstFormat'),(1, 'dither'),(1, 'pIPalette'),(1, 'alphaThresholdPercent'),(1, 'paletteTranslate'),)))
    IWICFormatConverter.CanConvert = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(Guid),POINTER(win32more.Foundation.BOOL), use_last_error=False)(9, 'CanConvert', ((1, 'srcPixelFormat'),(1, 'dstPixelFormat'),(1, 'pfCanConvert'),)))
    win32more.Graphics.Imaging.IWICBitmapSource
    return IWICFormatConverter
def _define_IWICPlanarFormatConverter_head():
    class IWICPlanarFormatConverter(win32more.Graphics.Imaging.IWICBitmapSource_head):
        Guid = Guid('bebee9cb-83b0-4dcc-8132-b0aaa55eac96')
    return IWICPlanarFormatConverter
def _define_IWICPlanarFormatConverter():
    IWICPlanarFormatConverter = win32more.Graphics.Imaging.IWICPlanarFormatConverter_head
    IWICPlanarFormatConverter.Initialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Imaging.IWICBitmapSource_head),UInt32,POINTER(Guid),win32more.Graphics.Imaging.WICBitmapDitherType,win32more.Graphics.Imaging.IWICPalette_head,Double,win32more.Graphics.Imaging.WICBitmapPaletteType, use_last_error=False)(8, 'Initialize', ((1, 'ppPlanes'),(1, 'cPlanes'),(1, 'dstFormat'),(1, 'dither'),(1, 'pIPalette'),(1, 'alphaThresholdPercent'),(1, 'paletteTranslate'),)))
    IWICPlanarFormatConverter.CanConvert = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),UInt32,POINTER(Guid),POINTER(win32more.Foundation.BOOL), use_last_error=False)(9, 'CanConvert', ((1, 'pSrcPixelFormats'),(1, 'cSrcPlanes'),(1, 'dstPixelFormat'),(1, 'pfCanConvert'),)))
    win32more.Graphics.Imaging.IWICBitmapSource
    return IWICPlanarFormatConverter
def _define_IWICBitmapScaler_head():
    class IWICBitmapScaler(win32more.Graphics.Imaging.IWICBitmapSource_head):
        Guid = Guid('00000302-a8f2-4877-ba0a-fd2b6645fb94')
    return IWICBitmapScaler
def _define_IWICBitmapScaler():
    IWICBitmapScaler = win32more.Graphics.Imaging.IWICBitmapScaler_head
    IWICBitmapScaler.Initialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Imaging.IWICBitmapSource_head,UInt32,UInt32,win32more.Graphics.Imaging.WICBitmapInterpolationMode, use_last_error=False)(8, 'Initialize', ((1, 'pISource'),(1, 'uiWidth'),(1, 'uiHeight'),(1, 'mode'),)))
    win32more.Graphics.Imaging.IWICBitmapSource
    return IWICBitmapScaler
def _define_IWICBitmapClipper_head():
    class IWICBitmapClipper(win32more.Graphics.Imaging.IWICBitmapSource_head):
        Guid = Guid('e4fbcf03-223d-4e81-9333-d635556dd1b5')
    return IWICBitmapClipper
def _define_IWICBitmapClipper():
    IWICBitmapClipper = win32more.Graphics.Imaging.IWICBitmapClipper_head
    IWICBitmapClipper.Initialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Imaging.IWICBitmapSource_head,POINTER(win32more.Graphics.Imaging.WICRect_head), use_last_error=False)(8, 'Initialize', ((1, 'pISource'),(1, 'prc'),)))
    win32more.Graphics.Imaging.IWICBitmapSource
    return IWICBitmapClipper
def _define_IWICBitmapFlipRotator_head():
    class IWICBitmapFlipRotator(win32more.Graphics.Imaging.IWICBitmapSource_head):
        Guid = Guid('5009834f-2d6a-41ce-9e1b-17c5aff7a782')
    return IWICBitmapFlipRotator
def _define_IWICBitmapFlipRotator():
    IWICBitmapFlipRotator = win32more.Graphics.Imaging.IWICBitmapFlipRotator_head
    IWICBitmapFlipRotator.Initialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Imaging.IWICBitmapSource_head,win32more.Graphics.Imaging.WICBitmapTransformOptions, use_last_error=False)(8, 'Initialize', ((1, 'pISource'),(1, 'options'),)))
    win32more.Graphics.Imaging.IWICBitmapSource
    return IWICBitmapFlipRotator
def _define_IWICBitmapLock_head():
    class IWICBitmapLock(win32more.System.Com.IUnknown_head):
        Guid = Guid('00000123-a8f2-4877-ba0a-fd2b6645fb94')
    return IWICBitmapLock
def _define_IWICBitmapLock():
    IWICBitmapLock = win32more.Graphics.Imaging.IWICBitmapLock_head
    IWICBitmapLock.GetSize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32),POINTER(UInt32), use_last_error=False)(3, 'GetSize', ((1, 'puiWidth'),(1, 'puiHeight'),)))
    IWICBitmapLock.GetStride = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(4, 'GetStride', ((1, 'pcbStride'),)))
    IWICBitmapLock.GetDataPointer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32),POINTER(c_char_p_no), use_last_error=False)(5, 'GetDataPointer', ((1, 'pcbBufferSize'),(1, 'ppbData'),)))
    IWICBitmapLock.GetPixelFormat = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid), use_last_error=False)(6, 'GetPixelFormat', ((1, 'pPixelFormat'),)))
    win32more.System.Com.IUnknown
    return IWICBitmapLock
def _define_IWICBitmap_head():
    class IWICBitmap(win32more.Graphics.Imaging.IWICBitmapSource_head):
        Guid = Guid('00000121-a8f2-4877-ba0a-fd2b6645fb94')
    return IWICBitmap
def _define_IWICBitmap():
    IWICBitmap = win32more.Graphics.Imaging.IWICBitmap_head
    IWICBitmap.Lock = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Imaging.WICRect_head),UInt32,POINTER(win32more.Graphics.Imaging.IWICBitmapLock_head), use_last_error=False)(8, 'Lock', ((1, 'prcLock'),(1, 'flags'),(1, 'ppILock'),)))
    IWICBitmap.SetPalette = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Imaging.IWICPalette_head, use_last_error=False)(9, 'SetPalette', ((1, 'pIPalette'),)))
    IWICBitmap.SetResolution = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Double,Double, use_last_error=False)(10, 'SetResolution', ((1, 'dpiX'),(1, 'dpiY'),)))
    win32more.Graphics.Imaging.IWICBitmapSource
    return IWICBitmap
def _define_IWICColorContext_head():
    class IWICColorContext(win32more.System.Com.IUnknown_head):
        Guid = Guid('3c613a02-34b2-44ea-9a7c-45aea9c6fd6d')
    return IWICColorContext
def _define_IWICColorContext():
    IWICColorContext = win32more.Graphics.Imaging.IWICColorContext_head
    IWICColorContext.InitializeFromFilename = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(3, 'InitializeFromFilename', ((1, 'wzFilename'),)))
    IWICColorContext.InitializeFromMemory = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Byte),UInt32, use_last_error=False)(4, 'InitializeFromMemory', ((1, 'pbBuffer'),(1, 'cbBufferSize'),)))
    IWICColorContext.InitializeFromExifColorSpace = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(5, 'InitializeFromExifColorSpace', ((1, 'value'),)))
    IWICColorContext.GetType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Imaging.WICColorContextType), use_last_error=False)(6, 'GetType', ((1, 'pType'),)))
    IWICColorContext.GetProfileBytes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(Byte),POINTER(UInt32), use_last_error=False)(7, 'GetProfileBytes', ((1, 'cbBuffer'),(1, 'pbBuffer'),(1, 'pcbActual'),)))
    IWICColorContext.GetExifColorSpace = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(8, 'GetExifColorSpace', ((1, 'pValue'),)))
    win32more.System.Com.IUnknown
    return IWICColorContext
def _define_IWICColorTransform_head():
    class IWICColorTransform(win32more.Graphics.Imaging.IWICBitmapSource_head):
        Guid = Guid('b66f034f-d0e2-40ab-b436-6de39e321a94')
    return IWICColorTransform
def _define_IWICColorTransform():
    IWICColorTransform = win32more.Graphics.Imaging.IWICColorTransform_head
    IWICColorTransform.Initialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Imaging.IWICBitmapSource_head,win32more.Graphics.Imaging.IWICColorContext_head,win32more.Graphics.Imaging.IWICColorContext_head,POINTER(Guid), use_last_error=False)(8, 'Initialize', ((1, 'pIBitmapSource'),(1, 'pIContextSource'),(1, 'pIContextDest'),(1, 'pixelFmtDest'),)))
    win32more.Graphics.Imaging.IWICBitmapSource
    return IWICColorTransform
def _define_IWICFastMetadataEncoder_head():
    class IWICFastMetadataEncoder(win32more.System.Com.IUnknown_head):
        Guid = Guid('b84e2c09-78c9-4ac4-8bd3-524ae1663a2f')
    return IWICFastMetadataEncoder
def _define_IWICFastMetadataEncoder():
    IWICFastMetadataEncoder = win32more.Graphics.Imaging.IWICFastMetadataEncoder_head
    IWICFastMetadataEncoder.Commit = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(3, 'Commit', ()))
    IWICFastMetadataEncoder.GetMetadataQueryWriter = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Imaging.IWICMetadataQueryWriter_head), use_last_error=False)(4, 'GetMetadataQueryWriter', ((1, 'ppIMetadataQueryWriter'),)))
    win32more.System.Com.IUnknown
    return IWICFastMetadataEncoder
def _define_IWICStream_head():
    class IWICStream(win32more.System.Com.IStream_head):
        Guid = Guid('135ff860-22b7-4ddf-b0f6-218f4f299a43')
    return IWICStream
def _define_IWICStream():
    IWICStream = win32more.Graphics.Imaging.IWICStream_head
    IWICStream.InitializeFromIStream = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IStream_head, use_last_error=False)(14, 'InitializeFromIStream', ((1, 'pIStream'),)))
    IWICStream.InitializeFromFilename = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32, use_last_error=False)(15, 'InitializeFromFilename', ((1, 'wzFileName'),(1, 'dwDesiredAccess'),)))
    IWICStream.InitializeFromMemory = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Byte),UInt32, use_last_error=False)(16, 'InitializeFromMemory', ((1, 'pbBuffer'),(1, 'cbBufferSize'),)))
    IWICStream.InitializeFromIStreamRegion = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IStream_head,win32more.Foundation.ULARGE_INTEGER,win32more.Foundation.ULARGE_INTEGER, use_last_error=False)(17, 'InitializeFromIStreamRegion', ((1, 'pIStream'),(1, 'ulOffset'),(1, 'ulMaxSize'),)))
    win32more.System.Com.IStream
    return IWICStream
def _define_IWICEnumMetadataItem_head():
    class IWICEnumMetadataItem(win32more.System.Com.IUnknown_head):
        Guid = Guid('dc2bb46d-3f07-481e-8625-220c4aedbb33')
    return IWICEnumMetadataItem
def _define_IWICEnumMetadataItem():
    IWICEnumMetadataItem = win32more.Graphics.Imaging.IWICEnumMetadataItem_head
    IWICEnumMetadataItem.Next = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT),POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT),POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT),POINTER(UInt32), use_last_error=False)(3, 'Next', ((1, 'celt'),(1, 'rgeltSchema'),(1, 'rgeltId'),(1, 'rgeltValue'),(1, 'pceltFetched'),)))
    IWICEnumMetadataItem.Skip = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(4, 'Skip', ((1, 'celt'),)))
    IWICEnumMetadataItem.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(5, 'Reset', ()))
    IWICEnumMetadataItem.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Imaging.IWICEnumMetadataItem_head), use_last_error=False)(6, 'Clone', ((1, 'ppIEnumMetadataItem'),)))
    win32more.System.Com.IUnknown
    return IWICEnumMetadataItem
def _define_IWICMetadataQueryReader_head():
    class IWICMetadataQueryReader(win32more.System.Com.IUnknown_head):
        Guid = Guid('30989668-e1c9-4597-b395-458eedb808df')
    return IWICMetadataQueryReader
def _define_IWICMetadataQueryReader():
    IWICMetadataQueryReader = win32more.Graphics.Imaging.IWICMetadataQueryReader_head
    IWICMetadataQueryReader.GetContainerFormat = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid), use_last_error=False)(3, 'GetContainerFormat', ((1, 'pguidContainerFormat'),)))
    IWICMetadataQueryReader.GetLocation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(Char),POINTER(UInt32), use_last_error=False)(4, 'GetLocation', ((1, 'cchMaxLength'),(1, 'wzNamespace'),(1, 'pcchActualLength'),)))
    IWICMetadataQueryReader.GetMetadataByName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), use_last_error=False)(5, 'GetMetadataByName', ((1, 'wzName'),(1, 'pvarValue'),)))
    IWICMetadataQueryReader.GetEnumerator = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IEnumString_head), use_last_error=False)(6, 'GetEnumerator', ((1, 'ppIEnumString'),)))
    win32more.System.Com.IUnknown
    return IWICMetadataQueryReader
def _define_IWICMetadataQueryWriter_head():
    class IWICMetadataQueryWriter(win32more.Graphics.Imaging.IWICMetadataQueryReader_head):
        Guid = Guid('a721791a-0def-4d06-bd91-2118bf1db10b')
    return IWICMetadataQueryWriter
def _define_IWICMetadataQueryWriter():
    IWICMetadataQueryWriter = win32more.Graphics.Imaging.IWICMetadataQueryWriter_head
    IWICMetadataQueryWriter.SetMetadataByName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), use_last_error=False)(7, 'SetMetadataByName', ((1, 'wzName'),(1, 'pvarValue'),)))
    IWICMetadataQueryWriter.RemoveMetadataByName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(8, 'RemoveMetadataByName', ((1, 'wzName'),)))
    win32more.Graphics.Imaging.IWICMetadataQueryReader
    return IWICMetadataQueryWriter
def _define_IWICBitmapEncoder_head():
    class IWICBitmapEncoder(win32more.System.Com.IUnknown_head):
        Guid = Guid('00000103-a8f2-4877-ba0a-fd2b6645fb94')
    return IWICBitmapEncoder
def _define_IWICBitmapEncoder():
    IWICBitmapEncoder = win32more.Graphics.Imaging.IWICBitmapEncoder_head
    IWICBitmapEncoder.Initialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IStream_head,win32more.Graphics.Imaging.WICBitmapEncoderCacheOption, use_last_error=False)(3, 'Initialize', ((1, 'pIStream'),(1, 'cacheOption'),)))
    IWICBitmapEncoder.GetContainerFormat = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid), use_last_error=False)(4, 'GetContainerFormat', ((1, 'pguidContainerFormat'),)))
    IWICBitmapEncoder.GetEncoderInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Imaging.IWICBitmapEncoderInfo_head), use_last_error=False)(5, 'GetEncoderInfo', ((1, 'ppIEncoderInfo'),)))
    IWICBitmapEncoder.SetColorContexts = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Graphics.Imaging.IWICColorContext_head), use_last_error=False)(6, 'SetColorContexts', ((1, 'cCount'),(1, 'ppIColorContext'),)))
    IWICBitmapEncoder.SetPalette = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Imaging.IWICPalette_head, use_last_error=False)(7, 'SetPalette', ((1, 'pIPalette'),)))
    IWICBitmapEncoder.SetThumbnail = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Imaging.IWICBitmapSource_head, use_last_error=False)(8, 'SetThumbnail', ((1, 'pIThumbnail'),)))
    IWICBitmapEncoder.SetPreview = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Imaging.IWICBitmapSource_head, use_last_error=False)(9, 'SetPreview', ((1, 'pIPreview'),)))
    IWICBitmapEncoder.CreateNewFrame = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Imaging.IWICBitmapFrameEncode_head),POINTER(win32more.System.Com.StructuredStorage.IPropertyBag2_head), use_last_error=False)(10, 'CreateNewFrame', ((1, 'ppIFrameEncode'),(1, 'ppIEncoderOptions'),)))
    IWICBitmapEncoder.Commit = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(11, 'Commit', ()))
    IWICBitmapEncoder.GetMetadataQueryWriter = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Imaging.IWICMetadataQueryWriter_head), use_last_error=False)(12, 'GetMetadataQueryWriter', ((1, 'ppIMetadataQueryWriter'),)))
    win32more.System.Com.IUnknown
    return IWICBitmapEncoder
def _define_IWICBitmapFrameEncode_head():
    class IWICBitmapFrameEncode(win32more.System.Com.IUnknown_head):
        Guid = Guid('00000105-a8f2-4877-ba0a-fd2b6645fb94')
    return IWICBitmapFrameEncode
def _define_IWICBitmapFrameEncode():
    IWICBitmapFrameEncode = win32more.Graphics.Imaging.IWICBitmapFrameEncode_head
    IWICBitmapFrameEncode.Initialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.StructuredStorage.IPropertyBag2_head, use_last_error=False)(3, 'Initialize', ((1, 'pIEncoderOptions'),)))
    IWICBitmapFrameEncode.SetSize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32, use_last_error=False)(4, 'SetSize', ((1, 'uiWidth'),(1, 'uiHeight'),)))
    IWICBitmapFrameEncode.SetResolution = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Double,Double, use_last_error=False)(5, 'SetResolution', ((1, 'dpiX'),(1, 'dpiY'),)))
    IWICBitmapFrameEncode.SetPixelFormat = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid), use_last_error=False)(6, 'SetPixelFormat', ((1, 'pPixelFormat'),)))
    IWICBitmapFrameEncode.SetColorContexts = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Graphics.Imaging.IWICColorContext_head), use_last_error=False)(7, 'SetColorContexts', ((1, 'cCount'),(1, 'ppIColorContext'),)))
    IWICBitmapFrameEncode.SetPalette = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Imaging.IWICPalette_head, use_last_error=False)(8, 'SetPalette', ((1, 'pIPalette'),)))
    IWICBitmapFrameEncode.SetThumbnail = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Imaging.IWICBitmapSource_head, use_last_error=False)(9, 'SetThumbnail', ((1, 'pIThumbnail'),)))
    IWICBitmapFrameEncode.WritePixels = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,UInt32,POINTER(Byte), use_last_error=False)(10, 'WritePixels', ((1, 'lineCount'),(1, 'cbStride'),(1, 'cbBufferSize'),(1, 'pbPixels'),)))
    IWICBitmapFrameEncode.WriteSource = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Imaging.IWICBitmapSource_head,POINTER(win32more.Graphics.Imaging.WICRect_head), use_last_error=False)(11, 'WriteSource', ((1, 'pIBitmapSource'),(1, 'prc'),)))
    IWICBitmapFrameEncode.Commit = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(12, 'Commit', ()))
    IWICBitmapFrameEncode.GetMetadataQueryWriter = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Imaging.IWICMetadataQueryWriter_head), use_last_error=False)(13, 'GetMetadataQueryWriter', ((1, 'ppIMetadataQueryWriter'),)))
    win32more.System.Com.IUnknown
    return IWICBitmapFrameEncode
def _define_IWICPlanarBitmapFrameEncode_head():
    class IWICPlanarBitmapFrameEncode(win32more.System.Com.IUnknown_head):
        Guid = Guid('f928b7b8-2221-40c1-b72e-7e82f1974d1a')
    return IWICPlanarBitmapFrameEncode
def _define_IWICPlanarBitmapFrameEncode():
    IWICPlanarBitmapFrameEncode = win32more.Graphics.Imaging.IWICPlanarBitmapFrameEncode_head
    IWICPlanarBitmapFrameEncode.WritePixels = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Graphics.Imaging.WICBitmapPlane),UInt32, use_last_error=False)(3, 'WritePixels', ((1, 'lineCount'),(1, 'pPlanes'),(1, 'cPlanes'),)))
    IWICPlanarBitmapFrameEncode.WriteSource = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Imaging.IWICBitmapSource_head),UInt32,POINTER(win32more.Graphics.Imaging.WICRect_head), use_last_error=False)(4, 'WriteSource', ((1, 'ppPlanes'),(1, 'cPlanes'),(1, 'prcSource'),)))
    win32more.System.Com.IUnknown
    return IWICPlanarBitmapFrameEncode
def _define_IWICBitmapDecoder_head():
    class IWICBitmapDecoder(win32more.System.Com.IUnknown_head):
        Guid = Guid('9edde9e7-8dee-47ea-99df-e6faf2ed44bf')
    return IWICBitmapDecoder
def _define_IWICBitmapDecoder():
    IWICBitmapDecoder = win32more.Graphics.Imaging.IWICBitmapDecoder_head
    IWICBitmapDecoder.QueryCapability = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IStream_head,POINTER(UInt32), use_last_error=False)(3, 'QueryCapability', ((1, 'pIStream'),(1, 'pdwCapability'),)))
    IWICBitmapDecoder.Initialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IStream_head,win32more.Graphics.Imaging.WICDecodeOptions, use_last_error=False)(4, 'Initialize', ((1, 'pIStream'),(1, 'cacheOptions'),)))
    IWICBitmapDecoder.GetContainerFormat = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid), use_last_error=False)(5, 'GetContainerFormat', ((1, 'pguidContainerFormat'),)))
    IWICBitmapDecoder.GetDecoderInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Imaging.IWICBitmapDecoderInfo_head), use_last_error=False)(6, 'GetDecoderInfo', ((1, 'ppIDecoderInfo'),)))
    IWICBitmapDecoder.CopyPalette = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Imaging.IWICPalette_head, use_last_error=False)(7, 'CopyPalette', ((1, 'pIPalette'),)))
    IWICBitmapDecoder.GetMetadataQueryReader = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Imaging.IWICMetadataQueryReader_head), use_last_error=False)(8, 'GetMetadataQueryReader', ((1, 'ppIMetadataQueryReader'),)))
    IWICBitmapDecoder.GetPreview = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Imaging.IWICBitmapSource_head), use_last_error=False)(9, 'GetPreview', ((1, 'ppIBitmapSource'),)))
    IWICBitmapDecoder.GetColorContexts = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Graphics.Imaging.IWICColorContext_head),POINTER(UInt32), use_last_error=False)(10, 'GetColorContexts', ((1, 'cCount'),(1, 'ppIColorContexts'),(1, 'pcActualCount'),)))
    IWICBitmapDecoder.GetThumbnail = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Imaging.IWICBitmapSource_head), use_last_error=False)(11, 'GetThumbnail', ((1, 'ppIThumbnail'),)))
    IWICBitmapDecoder.GetFrameCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(12, 'GetFrameCount', ((1, 'pCount'),)))
    IWICBitmapDecoder.GetFrame = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Graphics.Imaging.IWICBitmapFrameDecode_head), use_last_error=False)(13, 'GetFrame', ((1, 'index'),(1, 'ppIBitmapFrame'),)))
    win32more.System.Com.IUnknown
    return IWICBitmapDecoder
def _define_IWICBitmapSourceTransform_head():
    class IWICBitmapSourceTransform(win32more.System.Com.IUnknown_head):
        Guid = Guid('3b16811b-6a43-4ec9-b713-3d5a0c13b940')
    return IWICBitmapSourceTransform
def _define_IWICBitmapSourceTransform():
    IWICBitmapSourceTransform = win32more.Graphics.Imaging.IWICBitmapSourceTransform_head
    IWICBitmapSourceTransform.CopyPixels = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Imaging.WICRect_head),UInt32,UInt32,POINTER(Guid),win32more.Graphics.Imaging.WICBitmapTransformOptions,UInt32,UInt32,POINTER(Byte), use_last_error=False)(3, 'CopyPixels', ((1, 'prc'),(1, 'uiWidth'),(1, 'uiHeight'),(1, 'pguidDstFormat'),(1, 'dstTransform'),(1, 'nStride'),(1, 'cbBufferSize'),(1, 'pbBuffer'),)))
    IWICBitmapSourceTransform.GetClosestSize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32),POINTER(UInt32), use_last_error=False)(4, 'GetClosestSize', ((1, 'puiWidth'),(1, 'puiHeight'),)))
    IWICBitmapSourceTransform.GetClosestPixelFormat = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid), use_last_error=False)(5, 'GetClosestPixelFormat', ((1, 'pguidDstFormat'),)))
    IWICBitmapSourceTransform.DoesSupportTransform = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Imaging.WICBitmapTransformOptions,POINTER(win32more.Foundation.BOOL), use_last_error=False)(6, 'DoesSupportTransform', ((1, 'dstTransform'),(1, 'pfIsSupported'),)))
    win32more.System.Com.IUnknown
    return IWICBitmapSourceTransform
def _define_IWICPlanarBitmapSourceTransform_head():
    class IWICPlanarBitmapSourceTransform(win32more.System.Com.IUnknown_head):
        Guid = Guid('3aff9cce-be95-4303-b927-e7d16ff4a613')
    return IWICPlanarBitmapSourceTransform
def _define_IWICPlanarBitmapSourceTransform():
    IWICPlanarBitmapSourceTransform = win32more.Graphics.Imaging.IWICPlanarBitmapSourceTransform_head
    IWICPlanarBitmapSourceTransform.DoesSupportTransform = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32),POINTER(UInt32),win32more.Graphics.Imaging.WICBitmapTransformOptions,win32more.Graphics.Imaging.WICPlanarOptions,POINTER(Guid),POINTER(win32more.Graphics.Imaging.WICBitmapPlaneDescription),UInt32,POINTER(win32more.Foundation.BOOL), use_last_error=False)(3, 'DoesSupportTransform', ((1, 'puiWidth'),(1, 'puiHeight'),(1, 'dstTransform'),(1, 'dstPlanarOptions'),(1, 'pguidDstFormats'),(1, 'pPlaneDescriptions'),(1, 'cPlanes'),(1, 'pfIsSupported'),)))
    IWICPlanarBitmapSourceTransform.CopyPixels = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Imaging.WICRect_head),UInt32,UInt32,win32more.Graphics.Imaging.WICBitmapTransformOptions,win32more.Graphics.Imaging.WICPlanarOptions,POINTER(win32more.Graphics.Imaging.WICBitmapPlane),UInt32, use_last_error=False)(4, 'CopyPixels', ((1, 'prcSource'),(1, 'uiWidth'),(1, 'uiHeight'),(1, 'dstTransform'),(1, 'dstPlanarOptions'),(1, 'pDstPlanes'),(1, 'cPlanes'),)))
    win32more.System.Com.IUnknown
    return IWICPlanarBitmapSourceTransform
def _define_IWICBitmapFrameDecode_head():
    class IWICBitmapFrameDecode(win32more.Graphics.Imaging.IWICBitmapSource_head):
        Guid = Guid('3b16811b-6a43-4ec9-a813-3d930c13b940')
    return IWICBitmapFrameDecode
def _define_IWICBitmapFrameDecode():
    IWICBitmapFrameDecode = win32more.Graphics.Imaging.IWICBitmapFrameDecode_head
    IWICBitmapFrameDecode.GetMetadataQueryReader = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Imaging.IWICMetadataQueryReader_head), use_last_error=False)(8, 'GetMetadataQueryReader', ((1, 'ppIMetadataQueryReader'),)))
    IWICBitmapFrameDecode.GetColorContexts = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Graphics.Imaging.IWICColorContext_head),POINTER(UInt32), use_last_error=False)(9, 'GetColorContexts', ((1, 'cCount'),(1, 'ppIColorContexts'),(1, 'pcActualCount'),)))
    IWICBitmapFrameDecode.GetThumbnail = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Imaging.IWICBitmapSource_head), use_last_error=False)(10, 'GetThumbnail', ((1, 'ppIThumbnail'),)))
    win32more.Graphics.Imaging.IWICBitmapSource
    return IWICBitmapFrameDecode
def _define_IWICProgressiveLevelControl_head():
    class IWICProgressiveLevelControl(win32more.System.Com.IUnknown_head):
        Guid = Guid('daac296f-7aa5-4dbf-8d15-225c5976f891')
    return IWICProgressiveLevelControl
def _define_IWICProgressiveLevelControl():
    IWICProgressiveLevelControl = win32more.Graphics.Imaging.IWICProgressiveLevelControl_head
    IWICProgressiveLevelControl.GetLevelCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(3, 'GetLevelCount', ((1, 'pcLevels'),)))
    IWICProgressiveLevelControl.GetCurrentLevel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(4, 'GetCurrentLevel', ((1, 'pnLevel'),)))
    IWICProgressiveLevelControl.SetCurrentLevel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(5, 'SetCurrentLevel', ((1, 'nLevel'),)))
    win32more.System.Com.IUnknown
    return IWICProgressiveLevelControl
def _define_IWICProgressCallback_head():
    class IWICProgressCallback(win32more.System.Com.IUnknown_head):
        Guid = Guid('4776f9cd-9517-45fa-bf24-e89c5ec5c60c')
    return IWICProgressCallback
def _define_IWICProgressCallback():
    IWICProgressCallback = win32more.Graphics.Imaging.IWICProgressCallback_head
    IWICProgressCallback.Notify = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Graphics.Imaging.WICProgressOperation,Double, use_last_error=False)(3, 'Notify', ((1, 'uFrameNum'),(1, 'operation'),(1, 'dblProgress'),)))
    win32more.System.Com.IUnknown
    return IWICProgressCallback
def _define_PFNProgressNotification():
    return CFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,UInt32,win32more.Graphics.Imaging.WICProgressOperation,Double, use_last_error=False)
def _define_IWICBitmapCodecProgressNotification_head():
    class IWICBitmapCodecProgressNotification(win32more.System.Com.IUnknown_head):
        Guid = Guid('64c1024e-c3cf-4462-8078-88c2b11c46d9')
    return IWICBitmapCodecProgressNotification
def _define_IWICBitmapCodecProgressNotification():
    IWICBitmapCodecProgressNotification = win32more.Graphics.Imaging.IWICBitmapCodecProgressNotification_head
    IWICBitmapCodecProgressNotification.RegisterProgressNotification = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Imaging.PFNProgressNotification,c_void_p,UInt32, use_last_error=False)(3, 'RegisterProgressNotification', ((1, 'pfnProgressNotification'),(1, 'pvData'),(1, 'dwProgressFlags'),)))
    win32more.System.Com.IUnknown
    return IWICBitmapCodecProgressNotification
def _define_IWICComponentInfo_head():
    class IWICComponentInfo(win32more.System.Com.IUnknown_head):
        Guid = Guid('23bc3f0a-698b-4357-886b-f24d50671334')
    return IWICComponentInfo
def _define_IWICComponentInfo():
    IWICComponentInfo = win32more.Graphics.Imaging.IWICComponentInfo_head
    IWICComponentInfo.GetComponentType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Imaging.WICComponentType), use_last_error=False)(3, 'GetComponentType', ((1, 'pType'),)))
    IWICComponentInfo.GetCLSID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid), use_last_error=False)(4, 'GetCLSID', ((1, 'pclsid'),)))
    IWICComponentInfo.GetSigningStatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(5, 'GetSigningStatus', ((1, 'pStatus'),)))
    IWICComponentInfo.GetAuthor = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(Char),POINTER(UInt32), use_last_error=False)(6, 'GetAuthor', ((1, 'cchAuthor'),(1, 'wzAuthor'),(1, 'pcchActual'),)))
    IWICComponentInfo.GetVendorGUID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid), use_last_error=False)(7, 'GetVendorGUID', ((1, 'pguidVendor'),)))
    IWICComponentInfo.GetVersion = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(Char),POINTER(UInt32), use_last_error=False)(8, 'GetVersion', ((1, 'cchVersion'),(1, 'wzVersion'),(1, 'pcchActual'),)))
    IWICComponentInfo.GetSpecVersion = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(Char),POINTER(UInt32), use_last_error=False)(9, 'GetSpecVersion', ((1, 'cchSpecVersion'),(1, 'wzSpecVersion'),(1, 'pcchActual'),)))
    IWICComponentInfo.GetFriendlyName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(Char),POINTER(UInt32), use_last_error=False)(10, 'GetFriendlyName', ((1, 'cchFriendlyName'),(1, 'wzFriendlyName'),(1, 'pcchActual'),)))
    win32more.System.Com.IUnknown
    return IWICComponentInfo
def _define_IWICFormatConverterInfo_head():
    class IWICFormatConverterInfo(win32more.Graphics.Imaging.IWICComponentInfo_head):
        Guid = Guid('9f34fb65-13f4-4f15-bc57-3726b5e53d9f')
    return IWICFormatConverterInfo
def _define_IWICFormatConverterInfo():
    IWICFormatConverterInfo = win32more.Graphics.Imaging.IWICFormatConverterInfo_head
    IWICFormatConverterInfo.GetPixelFormats = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(Guid),POINTER(UInt32), use_last_error=False)(11, 'GetPixelFormats', ((1, 'cFormats'),(1, 'pPixelFormatGUIDs'),(1, 'pcActual'),)))
    IWICFormatConverterInfo.CreateInstance = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Imaging.IWICFormatConverter_head), use_last_error=False)(12, 'CreateInstance', ((1, 'ppIConverter'),)))
    win32more.Graphics.Imaging.IWICComponentInfo
    return IWICFormatConverterInfo
def _define_IWICBitmapCodecInfo_head():
    class IWICBitmapCodecInfo(win32more.Graphics.Imaging.IWICComponentInfo_head):
        Guid = Guid('e87a44c4-b76e-4c47-8b09-298eb12a2714')
    return IWICBitmapCodecInfo
def _define_IWICBitmapCodecInfo():
    IWICBitmapCodecInfo = win32more.Graphics.Imaging.IWICBitmapCodecInfo_head
    IWICBitmapCodecInfo.GetContainerFormat = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid), use_last_error=False)(11, 'GetContainerFormat', ((1, 'pguidContainerFormat'),)))
    IWICBitmapCodecInfo.GetPixelFormats = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(Guid),POINTER(UInt32), use_last_error=False)(12, 'GetPixelFormats', ((1, 'cFormats'),(1, 'pguidPixelFormats'),(1, 'pcActual'),)))
    IWICBitmapCodecInfo.GetColorManagementVersion = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(Char),POINTER(UInt32), use_last_error=False)(13, 'GetColorManagementVersion', ((1, 'cchColorManagementVersion'),(1, 'wzColorManagementVersion'),(1, 'pcchActual'),)))
    IWICBitmapCodecInfo.GetDeviceManufacturer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(Char),POINTER(UInt32), use_last_error=False)(14, 'GetDeviceManufacturer', ((1, 'cchDeviceManufacturer'),(1, 'wzDeviceManufacturer'),(1, 'pcchActual'),)))
    IWICBitmapCodecInfo.GetDeviceModels = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(Char),POINTER(UInt32), use_last_error=False)(15, 'GetDeviceModels', ((1, 'cchDeviceModels'),(1, 'wzDeviceModels'),(1, 'pcchActual'),)))
    IWICBitmapCodecInfo.GetMimeTypes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(Char),POINTER(UInt32), use_last_error=False)(16, 'GetMimeTypes', ((1, 'cchMimeTypes'),(1, 'wzMimeTypes'),(1, 'pcchActual'),)))
    IWICBitmapCodecInfo.GetFileExtensions = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(Char),POINTER(UInt32), use_last_error=False)(17, 'GetFileExtensions', ((1, 'cchFileExtensions'),(1, 'wzFileExtensions'),(1, 'pcchActual'),)))
    IWICBitmapCodecInfo.DoesSupportAnimation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(18, 'DoesSupportAnimation', ((1, 'pfSupportAnimation'),)))
    IWICBitmapCodecInfo.DoesSupportChromakey = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(19, 'DoesSupportChromakey', ((1, 'pfSupportChromakey'),)))
    IWICBitmapCodecInfo.DoesSupportLossless = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(20, 'DoesSupportLossless', ((1, 'pfSupportLossless'),)))
    IWICBitmapCodecInfo.DoesSupportMultiframe = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(21, 'DoesSupportMultiframe', ((1, 'pfSupportMultiframe'),)))
    IWICBitmapCodecInfo.MatchesMimeType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.BOOL), use_last_error=False)(22, 'MatchesMimeType', ((1, 'wzMimeType'),(1, 'pfMatches'),)))
    win32more.Graphics.Imaging.IWICComponentInfo
    return IWICBitmapCodecInfo
def _define_IWICBitmapEncoderInfo_head():
    class IWICBitmapEncoderInfo(win32more.Graphics.Imaging.IWICBitmapCodecInfo_head):
        Guid = Guid('94c9b4ee-a09f-4f92-8a1e-4a9bce7e76fb')
    return IWICBitmapEncoderInfo
def _define_IWICBitmapEncoderInfo():
    IWICBitmapEncoderInfo = win32more.Graphics.Imaging.IWICBitmapEncoderInfo_head
    IWICBitmapEncoderInfo.CreateInstance = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Imaging.IWICBitmapEncoder_head), use_last_error=False)(23, 'CreateInstance', ((1, 'ppIBitmapEncoder'),)))
    win32more.Graphics.Imaging.IWICBitmapCodecInfo
    return IWICBitmapEncoderInfo
def _define_IWICBitmapDecoderInfo_head():
    class IWICBitmapDecoderInfo(win32more.Graphics.Imaging.IWICBitmapCodecInfo_head):
        Guid = Guid('d8cd007f-d08f-4191-9bfc-236ea7f0e4b5')
    return IWICBitmapDecoderInfo
def _define_IWICBitmapDecoderInfo():
    IWICBitmapDecoderInfo = win32more.Graphics.Imaging.IWICBitmapDecoderInfo_head
    IWICBitmapDecoderInfo.GetPatterns = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Graphics.Imaging.WICBitmapPattern_head),POINTER(UInt32),POINTER(UInt32), use_last_error=False)(23, 'GetPatterns', ((1, 'cbSizePatterns'),(1, 'pPatterns'),(1, 'pcPatterns'),(1, 'pcbPatternsActual'),)))
    IWICBitmapDecoderInfo.MatchesPattern = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IStream_head,POINTER(win32more.Foundation.BOOL), use_last_error=False)(24, 'MatchesPattern', ((1, 'pIStream'),(1, 'pfMatches'),)))
    IWICBitmapDecoderInfo.CreateInstance = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Imaging.IWICBitmapDecoder_head), use_last_error=False)(25, 'CreateInstance', ((1, 'ppIBitmapDecoder'),)))
    win32more.Graphics.Imaging.IWICBitmapCodecInfo
    return IWICBitmapDecoderInfo
def _define_IWICPixelFormatInfo_head():
    class IWICPixelFormatInfo(win32more.Graphics.Imaging.IWICComponentInfo_head):
        Guid = Guid('e8eda601-3d48-431a-ab44-69059be88bbe')
    return IWICPixelFormatInfo
def _define_IWICPixelFormatInfo():
    IWICPixelFormatInfo = win32more.Graphics.Imaging.IWICPixelFormatInfo_head
    IWICPixelFormatInfo.GetFormatGUID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid), use_last_error=False)(11, 'GetFormatGUID', ((1, 'pFormat'),)))
    IWICPixelFormatInfo.GetColorContext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Imaging.IWICColorContext_head), use_last_error=False)(12, 'GetColorContext', ((1, 'ppIColorContext'),)))
    IWICPixelFormatInfo.GetBitsPerPixel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(13, 'GetBitsPerPixel', ((1, 'puiBitsPerPixel'),)))
    IWICPixelFormatInfo.GetChannelCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(14, 'GetChannelCount', ((1, 'puiChannelCount'),)))
    IWICPixelFormatInfo.GetChannelMask = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,POINTER(Byte),POINTER(UInt32), use_last_error=False)(15, 'GetChannelMask', ((1, 'uiChannelIndex'),(1, 'cbMaskBuffer'),(1, 'pbMaskBuffer'),(1, 'pcbActual'),)))
    win32more.Graphics.Imaging.IWICComponentInfo
    return IWICPixelFormatInfo
def _define_IWICPixelFormatInfo2_head():
    class IWICPixelFormatInfo2(win32more.Graphics.Imaging.IWICPixelFormatInfo_head):
        Guid = Guid('a9db33a2-af5f-43c7-b679-74f5984b5aa4')
    return IWICPixelFormatInfo2
def _define_IWICPixelFormatInfo2():
    IWICPixelFormatInfo2 = win32more.Graphics.Imaging.IWICPixelFormatInfo2_head
    IWICPixelFormatInfo2.SupportsTransparency = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(16, 'SupportsTransparency', ((1, 'pfSupportsTransparency'),)))
    IWICPixelFormatInfo2.GetNumericRepresentation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Imaging.WICPixelFormatNumericRepresentation), use_last_error=False)(17, 'GetNumericRepresentation', ((1, 'pNumericRepresentation'),)))
    win32more.Graphics.Imaging.IWICPixelFormatInfo
    return IWICPixelFormatInfo2
def _define_IWICImagingFactory_head():
    class IWICImagingFactory(win32more.System.Com.IUnknown_head):
        Guid = Guid('ec5ec8a9-c395-4314-9c77-54d7a935ff70')
    return IWICImagingFactory
def _define_IWICImagingFactory():
    IWICImagingFactory = win32more.Graphics.Imaging.IWICImagingFactory_head
    IWICImagingFactory.CreateDecoderFromFilename = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(Guid),UInt32,win32more.Graphics.Imaging.WICDecodeOptions,POINTER(win32more.Graphics.Imaging.IWICBitmapDecoder_head), use_last_error=False)(3, 'CreateDecoderFromFilename', ((1, 'wzFilename'),(1, 'pguidVendor'),(1, 'dwDesiredAccess'),(1, 'metadataOptions'),(1, 'ppIDecoder'),)))
    IWICImagingFactory.CreateDecoderFromStream = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IStream_head,POINTER(Guid),win32more.Graphics.Imaging.WICDecodeOptions,POINTER(win32more.Graphics.Imaging.IWICBitmapDecoder_head), use_last_error=False)(4, 'CreateDecoderFromStream', ((1, 'pIStream'),(1, 'pguidVendor'),(1, 'metadataOptions'),(1, 'ppIDecoder'),)))
    IWICImagingFactory.CreateDecoderFromFileHandle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UIntPtr,POINTER(Guid),win32more.Graphics.Imaging.WICDecodeOptions,POINTER(win32more.Graphics.Imaging.IWICBitmapDecoder_head), use_last_error=False)(5, 'CreateDecoderFromFileHandle', ((1, 'hFile'),(1, 'pguidVendor'),(1, 'metadataOptions'),(1, 'ppIDecoder'),)))
    IWICImagingFactory.CreateComponentInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(win32more.Graphics.Imaging.IWICComponentInfo_head), use_last_error=False)(6, 'CreateComponentInfo', ((1, 'clsidComponent'),(1, 'ppIInfo'),)))
    IWICImagingFactory.CreateDecoder = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(Guid),POINTER(win32more.Graphics.Imaging.IWICBitmapDecoder_head), use_last_error=False)(7, 'CreateDecoder', ((1, 'guidContainerFormat'),(1, 'pguidVendor'),(1, 'ppIDecoder'),)))
    IWICImagingFactory.CreateEncoder = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(Guid),POINTER(win32more.Graphics.Imaging.IWICBitmapEncoder_head), use_last_error=False)(8, 'CreateEncoder', ((1, 'guidContainerFormat'),(1, 'pguidVendor'),(1, 'ppIEncoder'),)))
    IWICImagingFactory.CreatePalette = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Imaging.IWICPalette_head), use_last_error=False)(9, 'CreatePalette', ((1, 'ppIPalette'),)))
    IWICImagingFactory.CreateFormatConverter = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Imaging.IWICFormatConverter_head), use_last_error=False)(10, 'CreateFormatConverter', ((1, 'ppIFormatConverter'),)))
    IWICImagingFactory.CreateBitmapScaler = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Imaging.IWICBitmapScaler_head), use_last_error=False)(11, 'CreateBitmapScaler', ((1, 'ppIBitmapScaler'),)))
    IWICImagingFactory.CreateBitmapClipper = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Imaging.IWICBitmapClipper_head), use_last_error=False)(12, 'CreateBitmapClipper', ((1, 'ppIBitmapClipper'),)))
    IWICImagingFactory.CreateBitmapFlipRotator = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Imaging.IWICBitmapFlipRotator_head), use_last_error=False)(13, 'CreateBitmapFlipRotator', ((1, 'ppIBitmapFlipRotator'),)))
    IWICImagingFactory.CreateStream = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Imaging.IWICStream_head), use_last_error=False)(14, 'CreateStream', ((1, 'ppIWICStream'),)))
    IWICImagingFactory.CreateColorContext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Imaging.IWICColorContext_head), use_last_error=False)(15, 'CreateColorContext', ((1, 'ppIWICColorContext'),)))
    IWICImagingFactory.CreateColorTransformer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Imaging.IWICColorTransform_head), use_last_error=False)(16, 'CreateColorTransformer', ((1, 'ppIWICColorTransform'),)))
    IWICImagingFactory.CreateBitmap = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,POINTER(Guid),win32more.Graphics.Imaging.WICBitmapCreateCacheOption,POINTER(win32more.Graphics.Imaging.IWICBitmap_head), use_last_error=False)(17, 'CreateBitmap', ((1, 'uiWidth'),(1, 'uiHeight'),(1, 'pixelFormat'),(1, 'option'),(1, 'ppIBitmap'),)))
    IWICImagingFactory.CreateBitmapFromSource = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Imaging.IWICBitmapSource_head,win32more.Graphics.Imaging.WICBitmapCreateCacheOption,POINTER(win32more.Graphics.Imaging.IWICBitmap_head), use_last_error=False)(18, 'CreateBitmapFromSource', ((1, 'pIBitmapSource'),(1, 'option'),(1, 'ppIBitmap'),)))
    IWICImagingFactory.CreateBitmapFromSourceRect = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Imaging.IWICBitmapSource_head,UInt32,UInt32,UInt32,UInt32,POINTER(win32more.Graphics.Imaging.IWICBitmap_head), use_last_error=False)(19, 'CreateBitmapFromSourceRect', ((1, 'pIBitmapSource'),(1, 'x'),(1, 'y'),(1, 'width'),(1, 'height'),(1, 'ppIBitmap'),)))
    IWICImagingFactory.CreateBitmapFromMemory = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,POINTER(Guid),UInt32,UInt32,POINTER(Byte),POINTER(win32more.Graphics.Imaging.IWICBitmap_head), use_last_error=False)(20, 'CreateBitmapFromMemory', ((1, 'uiWidth'),(1, 'uiHeight'),(1, 'pixelFormat'),(1, 'cbStride'),(1, 'cbBufferSize'),(1, 'pbBuffer'),(1, 'ppIBitmap'),)))
    IWICImagingFactory.CreateBitmapFromHBITMAP = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Gdi.HBITMAP,win32more.Graphics.Gdi.HPALETTE,win32more.Graphics.Imaging.WICBitmapAlphaChannelOption,POINTER(win32more.Graphics.Imaging.IWICBitmap_head), use_last_error=False)(21, 'CreateBitmapFromHBITMAP', ((1, 'hBitmap'),(1, 'hPalette'),(1, 'options'),(1, 'ppIBitmap'),)))
    IWICImagingFactory.CreateBitmapFromHICON = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.WindowsAndMessaging.HICON,POINTER(win32more.Graphics.Imaging.IWICBitmap_head), use_last_error=False)(22, 'CreateBitmapFromHICON', ((1, 'hIcon'),(1, 'ppIBitmap'),)))
    IWICImagingFactory.CreateComponentEnumerator = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,POINTER(win32more.System.Com.IEnumUnknown_head), use_last_error=False)(23, 'CreateComponentEnumerator', ((1, 'componentTypes'),(1, 'options'),(1, 'ppIEnumUnknown'),)))
    IWICImagingFactory.CreateFastMetadataEncoderFromDecoder = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Imaging.IWICBitmapDecoder_head,POINTER(win32more.Graphics.Imaging.IWICFastMetadataEncoder_head), use_last_error=False)(24, 'CreateFastMetadataEncoderFromDecoder', ((1, 'pIDecoder'),(1, 'ppIFastEncoder'),)))
    IWICImagingFactory.CreateFastMetadataEncoderFromFrameDecode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Imaging.IWICBitmapFrameDecode_head,POINTER(win32more.Graphics.Imaging.IWICFastMetadataEncoder_head), use_last_error=False)(25, 'CreateFastMetadataEncoderFromFrameDecode', ((1, 'pIFrameDecoder'),(1, 'ppIFastEncoder'),)))
    IWICImagingFactory.CreateQueryWriter = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(Guid),POINTER(win32more.Graphics.Imaging.IWICMetadataQueryWriter_head), use_last_error=False)(26, 'CreateQueryWriter', ((1, 'guidMetadataFormat'),(1, 'pguidVendor'),(1, 'ppIQueryWriter'),)))
    IWICImagingFactory.CreateQueryWriterFromReader = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Imaging.IWICMetadataQueryReader_head,POINTER(Guid),POINTER(win32more.Graphics.Imaging.IWICMetadataQueryWriter_head), use_last_error=False)(27, 'CreateQueryWriterFromReader', ((1, 'pIQueryReader'),(1, 'pguidVendor'),(1, 'ppIQueryWriter'),)))
    win32more.System.Com.IUnknown
    return IWICImagingFactory
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
WICJpegYCrCbSubsamplingOption = Int32
WICJpegYCrCbSubsamplingOption_WICJpegYCrCbSubsamplingDefault = 0
WICJpegYCrCbSubsamplingOption_WICJpegYCrCbSubsampling420 = 1
WICJpegYCrCbSubsamplingOption_WICJpegYCrCbSubsampling422 = 2
WICJpegYCrCbSubsamplingOption_WICJpegYCrCbSubsampling444 = 3
WICJpegYCrCbSubsamplingOption_WICJpegYCrCbSubsampling440 = 4
WICJpegYCrCbSubsamplingOption_WICJPEGYCRCBSUBSAMPLING_FORCE_DWORD = 2147483647
WICPngFilterOption = Int32
WICPngFilterOption_WICPngFilterUnspecified = 0
WICPngFilterOption_WICPngFilterNone = 1
WICPngFilterOption_WICPngFilterSub = 2
WICPngFilterOption_WICPngFilterUp = 3
WICPngFilterOption_WICPngFilterAverage = 4
WICPngFilterOption_WICPngFilterPaeth = 5
WICPngFilterOption_WICPngFilterAdaptive = 6
WICPngFilterOption_WICPNGFILTEROPTION_FORCE_DWORD = 2147483647
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
WICRawCapabilities = Int32
WICRawCapabilities_WICRawCapabilityNotSupported = 0
WICRawCapabilities_WICRawCapabilityGetSupported = 1
WICRawCapabilities_WICRawCapabilityFullySupported = 2
WICRawCapabilities_WICRAWCAPABILITIES_FORCE_DWORD = 2147483647
WICRawRotationCapabilities = Int32
WICRawRotationCapabilities_WICRawRotationCapabilityNotSupported = 0
WICRawRotationCapabilities_WICRawRotationCapabilityGetSupported = 1
WICRawRotationCapabilities_WICRawRotationCapabilityNinetyDegreesSupported = 2
WICRawRotationCapabilities_WICRawRotationCapabilityFullySupported = 3
WICRawRotationCapabilities_WICRAWROTATIONCAPABILITIES_FORCE_DWORD = 2147483647
def _define_WICRawCapabilitiesInfo_head():
    class WICRawCapabilitiesInfo(Structure):
        pass
    return WICRawCapabilitiesInfo
def _define_WICRawCapabilitiesInfo():
    WICRawCapabilitiesInfo = win32more.Graphics.Imaging.WICRawCapabilitiesInfo_head
    WICRawCapabilitiesInfo._fields_ = [
        ("cbSize", UInt32),
        ("CodecMajorVersion", UInt32),
        ("CodecMinorVersion", UInt32),
        ("ExposureCompensationSupport", win32more.Graphics.Imaging.WICRawCapabilities),
        ("ContrastSupport", win32more.Graphics.Imaging.WICRawCapabilities),
        ("RGBWhitePointSupport", win32more.Graphics.Imaging.WICRawCapabilities),
        ("NamedWhitePointSupport", win32more.Graphics.Imaging.WICRawCapabilities),
        ("NamedWhitePointSupportMask", UInt32),
        ("KelvinWhitePointSupport", win32more.Graphics.Imaging.WICRawCapabilities),
        ("GammaSupport", win32more.Graphics.Imaging.WICRawCapabilities),
        ("TintSupport", win32more.Graphics.Imaging.WICRawCapabilities),
        ("SaturationSupport", win32more.Graphics.Imaging.WICRawCapabilities),
        ("SharpnessSupport", win32more.Graphics.Imaging.WICRawCapabilities),
        ("NoiseReductionSupport", win32more.Graphics.Imaging.WICRawCapabilities),
        ("DestinationColorProfileSupport", win32more.Graphics.Imaging.WICRawCapabilities),
        ("ToneCurveSupport", win32more.Graphics.Imaging.WICRawCapabilities),
        ("RotationSupport", win32more.Graphics.Imaging.WICRawRotationCapabilities),
        ("RenderModeSupport", win32more.Graphics.Imaging.WICRawCapabilities),
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
def _define_WICRawToneCurvePoint_head():
    class WICRawToneCurvePoint(Structure):
        pass
    return WICRawToneCurvePoint
def _define_WICRawToneCurvePoint():
    WICRawToneCurvePoint = win32more.Graphics.Imaging.WICRawToneCurvePoint_head
    WICRawToneCurvePoint._fields_ = [
        ("Input", Double),
        ("Output", Double),
    ]
    return WICRawToneCurvePoint
def _define_WICRawToneCurve_head():
    class WICRawToneCurve(Structure):
        pass
    return WICRawToneCurve
def _define_WICRawToneCurve():
    WICRawToneCurve = win32more.Graphics.Imaging.WICRawToneCurve_head
    WICRawToneCurve._fields_ = [
        ("cPoints", UInt32),
        ("aPoints", win32more.Graphics.Imaging.WICRawToneCurvePoint * 0),
    ]
    return WICRawToneCurve
def _define_IWICDevelopRawNotificationCallback_head():
    class IWICDevelopRawNotificationCallback(win32more.System.Com.IUnknown_head):
        Guid = Guid('95c75a6e-3e8c-4ec2-85a8-aebcc551e59b')
    return IWICDevelopRawNotificationCallback
def _define_IWICDevelopRawNotificationCallback():
    IWICDevelopRawNotificationCallback = win32more.Graphics.Imaging.IWICDevelopRawNotificationCallback_head
    IWICDevelopRawNotificationCallback.Notify = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(3, 'Notify', ((1, 'NotificationMask'),)))
    win32more.System.Com.IUnknown
    return IWICDevelopRawNotificationCallback
def _define_IWICDevelopRaw_head():
    class IWICDevelopRaw(win32more.Graphics.Imaging.IWICBitmapFrameDecode_head):
        Guid = Guid('fbec5e44-f7be-4b65-b7f8-c0c81fef026d')
    return IWICDevelopRaw
def _define_IWICDevelopRaw():
    IWICDevelopRaw = win32more.Graphics.Imaging.IWICDevelopRaw_head
    IWICDevelopRaw.QueryRawCapabilitiesInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Imaging.WICRawCapabilitiesInfo_head), use_last_error=False)(11, 'QueryRawCapabilitiesInfo', ((1, 'pInfo'),)))
    IWICDevelopRaw.LoadParameterSet = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Imaging.WICRawParameterSet, use_last_error=False)(12, 'LoadParameterSet', ((1, 'ParameterSet'),)))
    IWICDevelopRaw.GetCurrentParameterSet = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.StructuredStorage.IPropertyBag2_head), use_last_error=False)(13, 'GetCurrentParameterSet', ((1, 'ppCurrentParameterSet'),)))
    IWICDevelopRaw.SetExposureCompensation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Double, use_last_error=False)(14, 'SetExposureCompensation', ((1, 'ev'),)))
    IWICDevelopRaw.GetExposureCompensation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double), use_last_error=False)(15, 'GetExposureCompensation', ((1, 'pEV'),)))
    IWICDevelopRaw.SetWhitePointRGB = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,UInt32, use_last_error=False)(16, 'SetWhitePointRGB', ((1, 'Red'),(1, 'Green'),(1, 'Blue'),)))
    IWICDevelopRaw.GetWhitePointRGB = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32),POINTER(UInt32),POINTER(UInt32), use_last_error=False)(17, 'GetWhitePointRGB', ((1, 'pRed'),(1, 'pGreen'),(1, 'pBlue'),)))
    IWICDevelopRaw.SetNamedWhitePoint = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Imaging.WICNamedWhitePoint, use_last_error=False)(18, 'SetNamedWhitePoint', ((1, 'WhitePoint'),)))
    IWICDevelopRaw.GetNamedWhitePoint = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Imaging.WICNamedWhitePoint), use_last_error=False)(19, 'GetNamedWhitePoint', ((1, 'pWhitePoint'),)))
    IWICDevelopRaw.SetWhitePointKelvin = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(20, 'SetWhitePointKelvin', ((1, 'WhitePointKelvin'),)))
    IWICDevelopRaw.GetWhitePointKelvin = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(21, 'GetWhitePointKelvin', ((1, 'pWhitePointKelvin'),)))
    IWICDevelopRaw.GetKelvinRangeInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32),POINTER(UInt32),POINTER(UInt32), use_last_error=False)(22, 'GetKelvinRangeInfo', ((1, 'pMinKelvinTemp'),(1, 'pMaxKelvinTemp'),(1, 'pKelvinTempStepValue'),)))
    IWICDevelopRaw.SetContrast = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Double, use_last_error=False)(23, 'SetContrast', ((1, 'Contrast'),)))
    IWICDevelopRaw.GetContrast = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double), use_last_error=False)(24, 'GetContrast', ((1, 'pContrast'),)))
    IWICDevelopRaw.SetGamma = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Double, use_last_error=False)(25, 'SetGamma', ((1, 'Gamma'),)))
    IWICDevelopRaw.GetGamma = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double), use_last_error=False)(26, 'GetGamma', ((1, 'pGamma'),)))
    IWICDevelopRaw.SetSharpness = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Double, use_last_error=False)(27, 'SetSharpness', ((1, 'Sharpness'),)))
    IWICDevelopRaw.GetSharpness = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double), use_last_error=False)(28, 'GetSharpness', ((1, 'pSharpness'),)))
    IWICDevelopRaw.SetSaturation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Double, use_last_error=False)(29, 'SetSaturation', ((1, 'Saturation'),)))
    IWICDevelopRaw.GetSaturation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double), use_last_error=False)(30, 'GetSaturation', ((1, 'pSaturation'),)))
    IWICDevelopRaw.SetTint = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Double, use_last_error=False)(31, 'SetTint', ((1, 'Tint'),)))
    IWICDevelopRaw.GetTint = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double), use_last_error=False)(32, 'GetTint', ((1, 'pTint'),)))
    IWICDevelopRaw.SetNoiseReduction = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Double, use_last_error=False)(33, 'SetNoiseReduction', ((1, 'NoiseReduction'),)))
    IWICDevelopRaw.GetNoiseReduction = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double), use_last_error=False)(34, 'GetNoiseReduction', ((1, 'pNoiseReduction'),)))
    IWICDevelopRaw.SetDestinationColorContext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Imaging.IWICColorContext_head, use_last_error=False)(35, 'SetDestinationColorContext', ((1, 'pColorContext'),)))
    IWICDevelopRaw.SetToneCurve = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Graphics.Imaging.WICRawToneCurve_head), use_last_error=False)(36, 'SetToneCurve', ((1, 'cbToneCurveSize'),(1, 'pToneCurve'),)))
    IWICDevelopRaw.GetToneCurve = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Graphics.Imaging.WICRawToneCurve_head),POINTER(UInt32), use_last_error=False)(37, 'GetToneCurve', ((1, 'cbToneCurveBufferSize'),(1, 'pToneCurve'),(1, 'pcbActualToneCurveBufferSize'),)))
    IWICDevelopRaw.SetRotation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Double, use_last_error=False)(38, 'SetRotation', ((1, 'Rotation'),)))
    IWICDevelopRaw.GetRotation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double), use_last_error=False)(39, 'GetRotation', ((1, 'pRotation'),)))
    IWICDevelopRaw.SetRenderMode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Imaging.WICRawRenderMode, use_last_error=False)(40, 'SetRenderMode', ((1, 'RenderMode'),)))
    IWICDevelopRaw.GetRenderMode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Imaging.WICRawRenderMode), use_last_error=False)(41, 'GetRenderMode', ((1, 'pRenderMode'),)))
    IWICDevelopRaw.SetNotificationCallback = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Imaging.IWICDevelopRawNotificationCallback_head, use_last_error=False)(42, 'SetNotificationCallback', ((1, 'pCallback'),)))
    win32more.Graphics.Imaging.IWICBitmapFrameDecode
    return IWICDevelopRaw
WICDdsDimension = Int32
WICDdsDimension_WICDdsTexture1D = 0
WICDdsDimension_WICDdsTexture2D = 1
WICDdsDimension_WICDdsTexture3D = 2
WICDdsDimension_WICDdsTextureCube = 3
WICDdsDimension_WICDDSTEXTURE_FORCE_DWORD = 2147483647
WICDdsAlphaMode = Int32
WICDdsAlphaMode_WICDdsAlphaModeUnknown = 0
WICDdsAlphaMode_WICDdsAlphaModeStraight = 1
WICDdsAlphaMode_WICDdsAlphaModePremultiplied = 2
WICDdsAlphaMode_WICDdsAlphaModeOpaque = 3
WICDdsAlphaMode_WICDdsAlphaModeCustom = 4
WICDdsAlphaMode_WICDDSALPHAMODE_FORCE_DWORD = 2147483647
def _define_WICDdsParameters_head():
    class WICDdsParameters(Structure):
        pass
    return WICDdsParameters
def _define_WICDdsParameters():
    WICDdsParameters = win32more.Graphics.Imaging.WICDdsParameters_head
    WICDdsParameters._fields_ = [
        ("Width", UInt32),
        ("Height", UInt32),
        ("Depth", UInt32),
        ("MipLevels", UInt32),
        ("ArraySize", UInt32),
        ("DxgiFormat", win32more.Graphics.Dxgi.Common.DXGI_FORMAT),
        ("Dimension", win32more.Graphics.Imaging.WICDdsDimension),
        ("AlphaMode", win32more.Graphics.Imaging.WICDdsAlphaMode),
    ]
    return WICDdsParameters
def _define_IWICDdsDecoder_head():
    class IWICDdsDecoder(win32more.System.Com.IUnknown_head):
        Guid = Guid('409cd537-8532-40cb-9774-e2feb2df4e9c')
    return IWICDdsDecoder
def _define_IWICDdsDecoder():
    IWICDdsDecoder = win32more.Graphics.Imaging.IWICDdsDecoder_head
    IWICDdsDecoder.GetParameters = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Imaging.WICDdsParameters_head), use_last_error=False)(3, 'GetParameters', ((1, 'pParameters'),)))
    IWICDdsDecoder.GetFrame = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,UInt32,POINTER(win32more.Graphics.Imaging.IWICBitmapFrameDecode_head), use_last_error=False)(4, 'GetFrame', ((1, 'arrayIndex'),(1, 'mipLevel'),(1, 'sliceIndex'),(1, 'ppIBitmapFrame'),)))
    win32more.System.Com.IUnknown
    return IWICDdsDecoder
def _define_IWICDdsEncoder_head():
    class IWICDdsEncoder(win32more.System.Com.IUnknown_head):
        Guid = Guid('5cacdb4c-407e-41b3-b936-d0f010cd6732')
    return IWICDdsEncoder
def _define_IWICDdsEncoder():
    IWICDdsEncoder = win32more.Graphics.Imaging.IWICDdsEncoder_head
    IWICDdsEncoder.SetParameters = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Imaging.WICDdsParameters_head), use_last_error=False)(3, 'SetParameters', ((1, 'pParameters'),)))
    IWICDdsEncoder.GetParameters = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Imaging.WICDdsParameters_head), use_last_error=False)(4, 'GetParameters', ((1, 'pParameters'),)))
    IWICDdsEncoder.CreateNewFrame = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Imaging.IWICBitmapFrameEncode_head),POINTER(UInt32),POINTER(UInt32),POINTER(UInt32), use_last_error=False)(5, 'CreateNewFrame', ((1, 'ppIFrameEncode'),(1, 'pArrayIndex'),(1, 'pMipLevel'),(1, 'pSliceIndex'),)))
    win32more.System.Com.IUnknown
    return IWICDdsEncoder
def _define_WICDdsFormatInfo_head():
    class WICDdsFormatInfo(Structure):
        pass
    return WICDdsFormatInfo
def _define_WICDdsFormatInfo():
    WICDdsFormatInfo = win32more.Graphics.Imaging.WICDdsFormatInfo_head
    WICDdsFormatInfo._fields_ = [
        ("DxgiFormat", win32more.Graphics.Dxgi.Common.DXGI_FORMAT),
        ("BytesPerBlock", UInt32),
        ("BlockWidth", UInt32),
        ("BlockHeight", UInt32),
    ]
    return WICDdsFormatInfo
def _define_IWICDdsFrameDecode_head():
    class IWICDdsFrameDecode(win32more.System.Com.IUnknown_head):
        Guid = Guid('3d4c0c61-18a4-41e4-bd80-481a4fc9f464')
    return IWICDdsFrameDecode
def _define_IWICDdsFrameDecode():
    IWICDdsFrameDecode = win32more.Graphics.Imaging.IWICDdsFrameDecode_head
    IWICDdsFrameDecode.GetSizeInBlocks = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32),POINTER(UInt32), use_last_error=False)(3, 'GetSizeInBlocks', ((1, 'pWidthInBlocks'),(1, 'pHeightInBlocks'),)))
    IWICDdsFrameDecode.GetFormatInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Imaging.WICDdsFormatInfo_head), use_last_error=False)(4, 'GetFormatInfo', ((1, 'pFormatInfo'),)))
    IWICDdsFrameDecode.CopyBlocks = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Imaging.WICRect_head),UInt32,UInt32,POINTER(Byte), use_last_error=False)(5, 'CopyBlocks', ((1, 'prcBoundsInBlocks'),(1, 'cbStride'),(1, 'cbBufferSize'),(1, 'pbBuffer'),)))
    win32more.System.Com.IUnknown
    return IWICDdsFrameDecode
def _define_IWICJpegFrameDecode_head():
    class IWICJpegFrameDecode(win32more.System.Com.IUnknown_head):
        Guid = Guid('8939f66e-c46a-4c21-a9d1-98b327ce1679')
    return IWICJpegFrameDecode
def _define_IWICJpegFrameDecode():
    IWICJpegFrameDecode = win32more.Graphics.Imaging.IWICJpegFrameDecode_head
    IWICJpegFrameDecode.DoesSupportIndexing = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(3, 'DoesSupportIndexing', ((1, 'pfIndexingSupported'),)))
    IWICJpegFrameDecode.SetIndexing = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Imaging.WICJpegIndexingOptions,UInt32, use_last_error=False)(4, 'SetIndexing', ((1, 'options'),(1, 'horizontalIntervalSize'),)))
    IWICJpegFrameDecode.ClearIndexing = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(5, 'ClearIndexing', ()))
    IWICJpegFrameDecode.GetAcHuffmanTable = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,POINTER(win32more.Graphics.Dxgi.Common.DXGI_JPEG_AC_HUFFMAN_TABLE_head), use_last_error=False)(6, 'GetAcHuffmanTable', ((1, 'scanIndex'),(1, 'tableIndex'),(1, 'pAcHuffmanTable'),)))
    IWICJpegFrameDecode.GetDcHuffmanTable = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,POINTER(win32more.Graphics.Dxgi.Common.DXGI_JPEG_DC_HUFFMAN_TABLE_head), use_last_error=False)(7, 'GetDcHuffmanTable', ((1, 'scanIndex'),(1, 'tableIndex'),(1, 'pDcHuffmanTable'),)))
    IWICJpegFrameDecode.GetQuantizationTable = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,POINTER(win32more.Graphics.Dxgi.Common.DXGI_JPEG_QUANTIZATION_TABLE_head), use_last_error=False)(8, 'GetQuantizationTable', ((1, 'scanIndex'),(1, 'tableIndex'),(1, 'pQuantizationTable'),)))
    IWICJpegFrameDecode.GetFrameHeader = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Imaging.WICJpegFrameHeader_head), use_last_error=False)(9, 'GetFrameHeader', ((1, 'pFrameHeader'),)))
    IWICJpegFrameDecode.GetScanHeader = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Graphics.Imaging.WICJpegScanHeader_head), use_last_error=False)(10, 'GetScanHeader', ((1, 'scanIndex'),(1, 'pScanHeader'),)))
    IWICJpegFrameDecode.CopyScan = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,UInt32,POINTER(Byte),POINTER(UInt32), use_last_error=False)(11, 'CopyScan', ((1, 'scanIndex'),(1, 'scanOffset'),(1, 'cbScanData'),(1, 'pbScanData'),(1, 'pcbScanDataActual'),)))
    IWICJpegFrameDecode.CopyMinimalStream = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,POINTER(Byte),POINTER(UInt32), use_last_error=False)(12, 'CopyMinimalStream', ((1, 'streamOffset'),(1, 'cbStreamData'),(1, 'pbStreamData'),(1, 'pcbStreamDataActual'),)))
    win32more.System.Com.IUnknown
    return IWICJpegFrameDecode
def _define_IWICJpegFrameEncode_head():
    class IWICJpegFrameEncode(win32more.System.Com.IUnknown_head):
        Guid = Guid('2f0c601f-d2c6-468c-abfa-49495d983ed1')
    return IWICJpegFrameEncode
def _define_IWICJpegFrameEncode():
    IWICJpegFrameEncode = win32more.Graphics.Imaging.IWICJpegFrameEncode_head
    IWICJpegFrameEncode.GetAcHuffmanTable = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,POINTER(win32more.Graphics.Dxgi.Common.DXGI_JPEG_AC_HUFFMAN_TABLE_head), use_last_error=False)(3, 'GetAcHuffmanTable', ((1, 'scanIndex'),(1, 'tableIndex'),(1, 'pAcHuffmanTable'),)))
    IWICJpegFrameEncode.GetDcHuffmanTable = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,POINTER(win32more.Graphics.Dxgi.Common.DXGI_JPEG_DC_HUFFMAN_TABLE_head), use_last_error=False)(4, 'GetDcHuffmanTable', ((1, 'scanIndex'),(1, 'tableIndex'),(1, 'pDcHuffmanTable'),)))
    IWICJpegFrameEncode.GetQuantizationTable = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,POINTER(win32more.Graphics.Dxgi.Common.DXGI_JPEG_QUANTIZATION_TABLE_head), use_last_error=False)(5, 'GetQuantizationTable', ((1, 'scanIndex'),(1, 'tableIndex'),(1, 'pQuantizationTable'),)))
    IWICJpegFrameEncode.WriteScan = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(Byte), use_last_error=False)(6, 'WriteScan', ((1, 'cbScanData'),(1, 'pbScanData'),)))
    win32more.System.Com.IUnknown
    return IWICJpegFrameEncode
WICMetadataCreationOptions = Int32
WICMetadataCreationOptions_WICMetadataCreationDefault = 0
WICMetadataCreationOptions_WICMetadataCreationAllowUnknown = 0
WICMetadataCreationOptions_WICMetadataCreationFailUnknown = 65536
WICMetadataCreationOptions_WICMetadataCreationMask = -65536
WICPersistOptions = Int32
WICPersistOptions_WICPersistOptionDefault = 0
WICPersistOptions_WICPersistOptionLittleEndian = 0
WICPersistOptions_WICPersistOptionBigEndian = 1
WICPersistOptions_WICPersistOptionStrictFormat = 2
WICPersistOptions_WICPersistOptionNoCacheStream = 4
WICPersistOptions_WICPersistOptionPreferUTF8 = 8
WICPersistOptions_WICPersistOptionMask = 65535
def _define_IWICMetadataBlockReader_head():
    class IWICMetadataBlockReader(win32more.System.Com.IUnknown_head):
        Guid = Guid('feaa2a8d-b3f3-43e4-b25c-d1de990a1ae1')
    return IWICMetadataBlockReader
def _define_IWICMetadataBlockReader():
    IWICMetadataBlockReader = win32more.Graphics.Imaging.IWICMetadataBlockReader_head
    IWICMetadataBlockReader.GetContainerFormat = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid), use_last_error=False)(3, 'GetContainerFormat', ((1, 'pguidContainerFormat'),)))
    IWICMetadataBlockReader.GetCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(4, 'GetCount', ((1, 'pcCount'),)))
    IWICMetadataBlockReader.GetReaderByIndex = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Graphics.Imaging.IWICMetadataReader_head), use_last_error=False)(5, 'GetReaderByIndex', ((1, 'nIndex'),(1, 'ppIMetadataReader'),)))
    IWICMetadataBlockReader.GetEnumerator = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IEnumUnknown_head), use_last_error=False)(6, 'GetEnumerator', ((1, 'ppIEnumMetadata'),)))
    win32more.System.Com.IUnknown
    return IWICMetadataBlockReader
def _define_IWICMetadataBlockWriter_head():
    class IWICMetadataBlockWriter(win32more.Graphics.Imaging.IWICMetadataBlockReader_head):
        Guid = Guid('08fb9676-b444-41e8-8dbe-6a53a542bff1')
    return IWICMetadataBlockWriter
def _define_IWICMetadataBlockWriter():
    IWICMetadataBlockWriter = win32more.Graphics.Imaging.IWICMetadataBlockWriter_head
    IWICMetadataBlockWriter.InitializeFromBlockReader = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Imaging.IWICMetadataBlockReader_head, use_last_error=False)(7, 'InitializeFromBlockReader', ((1, 'pIMDBlockReader'),)))
    IWICMetadataBlockWriter.GetWriterByIndex = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Graphics.Imaging.IWICMetadataWriter_head), use_last_error=False)(8, 'GetWriterByIndex', ((1, 'nIndex'),(1, 'ppIMetadataWriter'),)))
    IWICMetadataBlockWriter.AddWriter = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Imaging.IWICMetadataWriter_head, use_last_error=False)(9, 'AddWriter', ((1, 'pIMetadataWriter'),)))
    IWICMetadataBlockWriter.SetWriterByIndex = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Graphics.Imaging.IWICMetadataWriter_head, use_last_error=False)(10, 'SetWriterByIndex', ((1, 'nIndex'),(1, 'pIMetadataWriter'),)))
    IWICMetadataBlockWriter.RemoveWriterByIndex = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(11, 'RemoveWriterByIndex', ((1, 'nIndex'),)))
    win32more.Graphics.Imaging.IWICMetadataBlockReader
    return IWICMetadataBlockWriter
def _define_IWICMetadataReader_head():
    class IWICMetadataReader(win32more.System.Com.IUnknown_head):
        Guid = Guid('9204fe99-d8fc-4fd5-a001-9536b067a899')
    return IWICMetadataReader
def _define_IWICMetadataReader():
    IWICMetadataReader = win32more.Graphics.Imaging.IWICMetadataReader_head
    IWICMetadataReader.GetMetadataFormat = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid), use_last_error=False)(3, 'GetMetadataFormat', ((1, 'pguidMetadataFormat'),)))
    IWICMetadataReader.GetMetadataHandlerInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Imaging.IWICMetadataHandlerInfo_head), use_last_error=False)(4, 'GetMetadataHandlerInfo', ((1, 'ppIHandler'),)))
    IWICMetadataReader.GetCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(5, 'GetCount', ((1, 'pcCount'),)))
    IWICMetadataReader.GetValueByIndex = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), use_last_error=False)(6, 'GetValueByIndex', ((1, 'nIndex'),(1, 'pvarSchema'),(1, 'pvarId'),(1, 'pvarValue'),)))
    IWICMetadataReader.GetValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), use_last_error=False)(7, 'GetValue', ((1, 'pvarSchema'),(1, 'pvarId'),(1, 'pvarValue'),)))
    IWICMetadataReader.GetEnumerator = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Imaging.IWICEnumMetadataItem_head), use_last_error=False)(8, 'GetEnumerator', ((1, 'ppIEnumMetadata'),)))
    win32more.System.Com.IUnknown
    return IWICMetadataReader
def _define_IWICMetadataWriter_head():
    class IWICMetadataWriter(win32more.Graphics.Imaging.IWICMetadataReader_head):
        Guid = Guid('f7836e16-3be0-470b-86bb-160d0aecd7de')
    return IWICMetadataWriter
def _define_IWICMetadataWriter():
    IWICMetadataWriter = win32more.Graphics.Imaging.IWICMetadataWriter_head
    IWICMetadataWriter.SetValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), use_last_error=False)(9, 'SetValue', ((1, 'pvarSchema'),(1, 'pvarId'),(1, 'pvarValue'),)))
    IWICMetadataWriter.SetValueByIndex = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), use_last_error=False)(10, 'SetValueByIndex', ((1, 'nIndex'),(1, 'pvarSchema'),(1, 'pvarId'),(1, 'pvarValue'),)))
    IWICMetadataWriter.RemoveValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), use_last_error=False)(11, 'RemoveValue', ((1, 'pvarSchema'),(1, 'pvarId'),)))
    IWICMetadataWriter.RemoveValueByIndex = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(12, 'RemoveValueByIndex', ((1, 'nIndex'),)))
    win32more.Graphics.Imaging.IWICMetadataReader
    return IWICMetadataWriter
def _define_IWICStreamProvider_head():
    class IWICStreamProvider(win32more.System.Com.IUnknown_head):
        Guid = Guid('449494bc-b468-4927-96d7-ba90d31ab505')
    return IWICStreamProvider
def _define_IWICStreamProvider():
    IWICStreamProvider = win32more.Graphics.Imaging.IWICStreamProvider_head
    IWICStreamProvider.GetStream = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IStream_head), use_last_error=False)(3, 'GetStream', ((1, 'ppIStream'),)))
    IWICStreamProvider.GetPersistOptions = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(4, 'GetPersistOptions', ((1, 'pdwPersistOptions'),)))
    IWICStreamProvider.GetPreferredVendorGUID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid), use_last_error=False)(5, 'GetPreferredVendorGUID', ((1, 'pguidPreferredVendor'),)))
    IWICStreamProvider.RefreshStream = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(6, 'RefreshStream', ()))
    win32more.System.Com.IUnknown
    return IWICStreamProvider
def _define_IWICPersistStream_head():
    class IWICPersistStream(win32more.System.Com.IPersistStream_head):
        Guid = Guid('00675040-6908-45f8-86a3-49c7dfd6d9ad')
    return IWICPersistStream
def _define_IWICPersistStream():
    IWICPersistStream = win32more.Graphics.Imaging.IWICPersistStream_head
    IWICPersistStream.LoadEx = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IStream_head,POINTER(Guid),UInt32, use_last_error=False)(8, 'LoadEx', ((1, 'pIStream'),(1, 'pguidPreferredVendor'),(1, 'dwPersistOptions'),)))
    IWICPersistStream.SaveEx = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IStream_head,UInt32,win32more.Foundation.BOOL, use_last_error=False)(9, 'SaveEx', ((1, 'pIStream'),(1, 'dwPersistOptions'),(1, 'fClearDirty'),)))
    win32more.System.Com.IPersistStream
    return IWICPersistStream
def _define_IWICMetadataHandlerInfo_head():
    class IWICMetadataHandlerInfo(win32more.Graphics.Imaging.IWICComponentInfo_head):
        Guid = Guid('aba958bf-c672-44d1-8d61-ce6df2e682c2')
    return IWICMetadataHandlerInfo
def _define_IWICMetadataHandlerInfo():
    IWICMetadataHandlerInfo = win32more.Graphics.Imaging.IWICMetadataHandlerInfo_head
    IWICMetadataHandlerInfo.GetMetadataFormat = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid), use_last_error=False)(11, 'GetMetadataFormat', ((1, 'pguidMetadataFormat'),)))
    IWICMetadataHandlerInfo.GetContainerFormats = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(Guid),POINTER(UInt32), use_last_error=False)(12, 'GetContainerFormats', ((1, 'cContainerFormats'),(1, 'pguidContainerFormats'),(1, 'pcchActual'),)))
    IWICMetadataHandlerInfo.GetDeviceManufacturer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(Char),POINTER(UInt32), use_last_error=False)(13, 'GetDeviceManufacturer', ((1, 'cchDeviceManufacturer'),(1, 'wzDeviceManufacturer'),(1, 'pcchActual'),)))
    IWICMetadataHandlerInfo.GetDeviceModels = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(Char),POINTER(UInt32), use_last_error=False)(14, 'GetDeviceModels', ((1, 'cchDeviceModels'),(1, 'wzDeviceModels'),(1, 'pcchActual'),)))
    IWICMetadataHandlerInfo.DoesRequireFullStream = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(15, 'DoesRequireFullStream', ((1, 'pfRequiresFullStream'),)))
    IWICMetadataHandlerInfo.DoesSupportPadding = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(16, 'DoesSupportPadding', ((1, 'pfSupportsPadding'),)))
    IWICMetadataHandlerInfo.DoesRequireFixedSize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(17, 'DoesRequireFixedSize', ((1, 'pfFixedSize'),)))
    win32more.Graphics.Imaging.IWICComponentInfo
    return IWICMetadataHandlerInfo
def _define_WICMetadataPattern_head():
    class WICMetadataPattern(Structure):
        pass
    return WICMetadataPattern
def _define_WICMetadataPattern():
    WICMetadataPattern = win32more.Graphics.Imaging.WICMetadataPattern_head
    WICMetadataPattern._fields_ = [
        ("Position", win32more.Foundation.ULARGE_INTEGER),
        ("Length", UInt32),
        ("Pattern", c_char_p_no),
        ("Mask", c_char_p_no),
        ("DataOffset", win32more.Foundation.ULARGE_INTEGER),
    ]
    return WICMetadataPattern
def _define_IWICMetadataReaderInfo_head():
    class IWICMetadataReaderInfo(win32more.Graphics.Imaging.IWICMetadataHandlerInfo_head):
        Guid = Guid('eebf1f5b-07c1-4447-a3ab-22acaf78a804')
    return IWICMetadataReaderInfo
def _define_IWICMetadataReaderInfo():
    IWICMetadataReaderInfo = win32more.Graphics.Imaging.IWICMetadataReaderInfo_head
    IWICMetadataReaderInfo.GetPatterns = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),UInt32,POINTER(win32more.Graphics.Imaging.WICMetadataPattern_head),POINTER(UInt32),POINTER(UInt32), use_last_error=False)(18, 'GetPatterns', ((1, 'guidContainerFormat'),(1, 'cbSize'),(1, 'pPattern'),(1, 'pcCount'),(1, 'pcbActual'),)))
    IWICMetadataReaderInfo.MatchesPattern = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),win32more.System.Com.IStream_head,POINTER(win32more.Foundation.BOOL), use_last_error=False)(19, 'MatchesPattern', ((1, 'guidContainerFormat'),(1, 'pIStream'),(1, 'pfMatches'),)))
    IWICMetadataReaderInfo.CreateInstance = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Imaging.IWICMetadataReader_head), use_last_error=False)(20, 'CreateInstance', ((1, 'ppIReader'),)))
    win32more.Graphics.Imaging.IWICMetadataHandlerInfo
    return IWICMetadataReaderInfo
def _define_WICMetadataHeader_head():
    class WICMetadataHeader(Structure):
        pass
    return WICMetadataHeader
def _define_WICMetadataHeader():
    WICMetadataHeader = win32more.Graphics.Imaging.WICMetadataHeader_head
    WICMetadataHeader._fields_ = [
        ("Position", win32more.Foundation.ULARGE_INTEGER),
        ("Length", UInt32),
        ("Header", c_char_p_no),
        ("DataOffset", win32more.Foundation.ULARGE_INTEGER),
    ]
    return WICMetadataHeader
def _define_IWICMetadataWriterInfo_head():
    class IWICMetadataWriterInfo(win32more.Graphics.Imaging.IWICMetadataHandlerInfo_head):
        Guid = Guid('b22e3fba-3925-4323-b5c1-9ebfc430f236')
    return IWICMetadataWriterInfo
def _define_IWICMetadataWriterInfo():
    IWICMetadataWriterInfo = win32more.Graphics.Imaging.IWICMetadataWriterInfo_head
    IWICMetadataWriterInfo.GetHeader = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),UInt32,POINTER(win32more.Graphics.Imaging.WICMetadataHeader_head),POINTER(UInt32), use_last_error=False)(18, 'GetHeader', ((1, 'guidContainerFormat'),(1, 'cbSize'),(1, 'pHeader'),(1, 'pcbActual'),)))
    IWICMetadataWriterInfo.CreateInstance = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Imaging.IWICMetadataWriter_head), use_last_error=False)(19, 'CreateInstance', ((1, 'ppIWriter'),)))
    win32more.Graphics.Imaging.IWICMetadataHandlerInfo
    return IWICMetadataWriterInfo
def _define_IWICComponentFactory_head():
    class IWICComponentFactory(win32more.Graphics.Imaging.IWICImagingFactory_head):
        Guid = Guid('412d0c3a-9650-44fa-af5b-dd2a06c8e8fb')
    return IWICComponentFactory
def _define_IWICComponentFactory():
    IWICComponentFactory = win32more.Graphics.Imaging.IWICComponentFactory_head
    IWICComponentFactory.CreateMetadataReader = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(Guid),UInt32,win32more.System.Com.IStream_head,POINTER(win32more.Graphics.Imaging.IWICMetadataReader_head), use_last_error=False)(28, 'CreateMetadataReader', ((1, 'guidMetadataFormat'),(1, 'pguidVendor'),(1, 'dwOptions'),(1, 'pIStream'),(1, 'ppIReader'),)))
    IWICComponentFactory.CreateMetadataReaderFromContainer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(Guid),UInt32,win32more.System.Com.IStream_head,POINTER(win32more.Graphics.Imaging.IWICMetadataReader_head), use_last_error=False)(29, 'CreateMetadataReaderFromContainer', ((1, 'guidContainerFormat'),(1, 'pguidVendor'),(1, 'dwOptions'),(1, 'pIStream'),(1, 'ppIReader'),)))
    IWICComponentFactory.CreateMetadataWriter = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(Guid),UInt32,POINTER(win32more.Graphics.Imaging.IWICMetadataWriter_head), use_last_error=False)(30, 'CreateMetadataWriter', ((1, 'guidMetadataFormat'),(1, 'pguidVendor'),(1, 'dwMetadataOptions'),(1, 'ppIWriter'),)))
    IWICComponentFactory.CreateMetadataWriterFromReader = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Imaging.IWICMetadataReader_head,POINTER(Guid),POINTER(win32more.Graphics.Imaging.IWICMetadataWriter_head), use_last_error=False)(31, 'CreateMetadataWriterFromReader', ((1, 'pIReader'),(1, 'pguidVendor'),(1, 'ppIWriter'),)))
    IWICComponentFactory.CreateQueryReaderFromBlockReader = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Imaging.IWICMetadataBlockReader_head,POINTER(win32more.Graphics.Imaging.IWICMetadataQueryReader_head), use_last_error=False)(32, 'CreateQueryReaderFromBlockReader', ((1, 'pIBlockReader'),(1, 'ppIQueryReader'),)))
    IWICComponentFactory.CreateQueryWriterFromBlockWriter = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Imaging.IWICMetadataBlockWriter_head,POINTER(win32more.Graphics.Imaging.IWICMetadataQueryWriter_head), use_last_error=False)(33, 'CreateQueryWriterFromBlockWriter', ((1, 'pIBlockWriter'),(1, 'ppIQueryWriter'),)))
    IWICComponentFactory.CreateEncoderPropertyBag = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.StructuredStorage.PROPBAG2),UInt32,POINTER(win32more.System.Com.StructuredStorage.IPropertyBag2_head), use_last_error=False)(34, 'CreateEncoderPropertyBag', ((1, 'ppropOptions'),(1, 'cCount'),(1, 'ppIPropertyBag'),)))
    win32more.Graphics.Imaging.IWICImagingFactory
    return IWICComponentFactory
def _define_WICConvertBitmapSource():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),win32more.Graphics.Imaging.IWICBitmapSource_head,POINTER(win32more.Graphics.Imaging.IWICBitmapSource_head), use_last_error=False)(("WICConvertBitmapSource", windll["WindowsCodecs"]), ((1, 'dstFormat'),(1, 'pISrc'),(1, 'ppIDst'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WICCreateBitmapFromSection():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,POINTER(Guid),win32more.Foundation.HANDLE,UInt32,UInt32,POINTER(win32more.Graphics.Imaging.IWICBitmap_head), use_last_error=False)(("WICCreateBitmapFromSection", windll["WindowsCodecs"]), ((1, 'width'),(1, 'height'),(1, 'pixelFormat'),(1, 'hSection'),(1, 'stride'),(1, 'offset'),(1, 'ppIBitmap'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WICCreateBitmapFromSectionEx():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,POINTER(Guid),win32more.Foundation.HANDLE,UInt32,UInt32,win32more.Graphics.Imaging.WICSectionAccessLevel,POINTER(win32more.Graphics.Imaging.IWICBitmap_head), use_last_error=False)(("WICCreateBitmapFromSectionEx", windll["WindowsCodecs"]), ((1, 'width'),(1, 'height'),(1, 'pixelFormat'),(1, 'hSection'),(1, 'stride'),(1, 'offset'),(1, 'desiredAccessLevel'),(1, 'ppIBitmap'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WICMapGuidToShortName():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),UInt32,POINTER(Char),POINTER(UInt32), use_last_error=False)(("WICMapGuidToShortName", windll["WindowsCodecs"]), ((1, 'guid'),(1, 'cchName'),(1, 'wzName'),(1, 'pcchActual'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WICMapShortNameToGuid():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(Guid), use_last_error=False)(("WICMapShortNameToGuid", windll["WindowsCodecs"]), ((1, 'wzName'),(1, 'pguid'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WICMapSchemaToName():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),win32more.Foundation.PWSTR,UInt32,POINTER(Char),POINTER(UInt32), use_last_error=False)(("WICMapSchemaToName", windll["WindowsCodecs"]), ((1, 'guidMetadataFormat'),(1, 'pwzSchema'),(1, 'cchName'),(1, 'wzName'),(1, 'pcchActual'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WICMatchMetadataContent():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(Guid),win32more.System.Com.IStream_head,POINTER(Guid), use_last_error=False)(("WICMatchMetadataContent", windll["WindowsCodecs"]), ((1, 'guidContainerFormat'),(1, 'pguidVendor'),(1, 'pIStream'),(1, 'pguidMetadataFormat'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WICSerializeMetadataContent():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),win32more.Graphics.Imaging.IWICMetadataWriter_head,UInt32,win32more.System.Com.IStream_head, use_last_error=False)(("WICSerializeMetadataContent", windll["WindowsCodecs"]), ((1, 'guidContainerFormat'),(1, 'pIWriter'),(1, 'dwPersistOptions'),(1, 'pIStream'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WICGetMetadataContentSize():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),win32more.Graphics.Imaging.IWICMetadataWriter_head,POINTER(win32more.Foundation.ULARGE_INTEGER_head), use_last_error=False)(("WICGetMetadataContentSize", windll["WindowsCodecs"]), ((1, 'guidContainerFormat'),(1, 'pIWriter'),(1, 'pcbSize'),))
    except (FileNotFoundError, AttributeError):
        return None
__all__ = [
    "WINCODEC_SDK_VERSION1",
    "WINCODEC_SDK_VERSION2",
    "CLSID_WICImagingFactory",
    "CLSID_WICImagingFactory1",
    "CLSID_WICImagingFactory2",
    "WINCODEC_SDK_VERSION",
    "GUID_VendorMicrosoft",
    "GUID_VendorMicrosoftBuiltIn",
    "CLSID_WICPngDecoder",
    "CLSID_WICPngDecoder1",
    "CLSID_WICPngDecoder2",
    "CLSID_WICBmpDecoder",
    "CLSID_WICIcoDecoder",
    "CLSID_WICJpegDecoder",
    "CLSID_WICGifDecoder",
    "CLSID_WICTiffDecoder",
    "CLSID_WICWmpDecoder",
    "CLSID_WICDdsDecoder",
    "CLSID_WICBmpEncoder",
    "CLSID_WICPngEncoder",
    "CLSID_WICJpegEncoder",
    "CLSID_WICGifEncoder",
    "CLSID_WICTiffEncoder",
    "CLSID_WICWmpEncoder",
    "CLSID_WICDdsEncoder",
    "CLSID_WICAdngDecoder",
    "CLSID_WICJpegQualcommPhoneEncoder",
    "CLSID_WICHeifDecoder",
    "CLSID_WICHeifEncoder",
    "CLSID_WICWebpDecoder",
    "CLSID_WICRAWDecoder",
    "GUID_ContainerFormatBmp",
    "GUID_ContainerFormatPng",
    "GUID_ContainerFormatIco",
    "GUID_ContainerFormatJpeg",
    "GUID_ContainerFormatTiff",
    "GUID_ContainerFormatGif",
    "GUID_ContainerFormatWmp",
    "GUID_ContainerFormatDds",
    "GUID_ContainerFormatAdng",
    "GUID_ContainerFormatHeif",
    "GUID_ContainerFormatWebp",
    "GUID_ContainerFormatRaw",
    "CLSID_WICImagingCategories",
    "CATID_WICBitmapDecoders",
    "CATID_WICBitmapEncoders",
    "CATID_WICPixelFormats",
    "CATID_WICFormatConverters",
    "CATID_WICMetadataReader",
    "CATID_WICMetadataWriter",
    "CLSID_WICDefaultFormatConverter",
    "CLSID_WICFormatConverterHighColor",
    "CLSID_WICFormatConverterNChannel",
    "CLSID_WICFormatConverterWMPhoto",
    "CLSID_WICPlanarFormatConverter",
    "WIC_JPEG_MAX_COMPONENT_COUNT",
    "WIC_JPEG_MAX_TABLE_INDEX",
    "WIC_JPEG_SAMPLE_FACTORS_ONE",
    "WIC_JPEG_SAMPLE_FACTORS_THREE_420",
    "WIC_JPEG_SAMPLE_FACTORS_THREE_422",
    "WIC_JPEG_SAMPLE_FACTORS_THREE_440",
    "WIC_JPEG_SAMPLE_FACTORS_THREE_444",
    "WIC_JPEG_QUANTIZATION_BASELINE_ONE",
    "WIC_JPEG_QUANTIZATION_BASELINE_THREE",
    "WIC_JPEG_HUFFMAN_BASELINE_ONE",
    "WIC_JPEG_HUFFMAN_BASELINE_THREE",
    "GUID_WICPixelFormatDontCare",
    "GUID_WICPixelFormat1bppIndexed",
    "GUID_WICPixelFormat2bppIndexed",
    "GUID_WICPixelFormat4bppIndexed",
    "GUID_WICPixelFormat8bppIndexed",
    "GUID_WICPixelFormatBlackWhite",
    "GUID_WICPixelFormat2bppGray",
    "GUID_WICPixelFormat4bppGray",
    "GUID_WICPixelFormat8bppGray",
    "GUID_WICPixelFormat8bppAlpha",
    "GUID_WICPixelFormat16bppBGR555",
    "GUID_WICPixelFormat16bppBGR565",
    "GUID_WICPixelFormat16bppBGRA5551",
    "GUID_WICPixelFormat16bppGray",
    "GUID_WICPixelFormat24bppBGR",
    "GUID_WICPixelFormat24bppRGB",
    "GUID_WICPixelFormat32bppBGR",
    "GUID_WICPixelFormat32bppBGRA",
    "GUID_WICPixelFormat32bppPBGRA",
    "GUID_WICPixelFormat32bppGrayFloat",
    "GUID_WICPixelFormat32bppRGB",
    "GUID_WICPixelFormat32bppRGBA",
    "GUID_WICPixelFormat32bppPRGBA",
    "GUID_WICPixelFormat48bppRGB",
    "GUID_WICPixelFormat48bppBGR",
    "GUID_WICPixelFormat64bppRGB",
    "GUID_WICPixelFormat64bppRGBA",
    "GUID_WICPixelFormat64bppBGRA",
    "GUID_WICPixelFormat64bppPRGBA",
    "GUID_WICPixelFormat64bppPBGRA",
    "GUID_WICPixelFormat16bppGrayFixedPoint",
    "GUID_WICPixelFormat32bppBGR101010",
    "GUID_WICPixelFormat48bppRGBFixedPoint",
    "GUID_WICPixelFormat48bppBGRFixedPoint",
    "GUID_WICPixelFormat96bppRGBFixedPoint",
    "GUID_WICPixelFormat96bppRGBFloat",
    "GUID_WICPixelFormat128bppRGBAFloat",
    "GUID_WICPixelFormat128bppPRGBAFloat",
    "GUID_WICPixelFormat128bppRGBFloat",
    "GUID_WICPixelFormat32bppCMYK",
    "GUID_WICPixelFormat64bppRGBAFixedPoint",
    "GUID_WICPixelFormat64bppBGRAFixedPoint",
    "GUID_WICPixelFormat64bppRGBFixedPoint",
    "GUID_WICPixelFormat128bppRGBAFixedPoint",
    "GUID_WICPixelFormat128bppRGBFixedPoint",
    "GUID_WICPixelFormat64bppRGBAHalf",
    "GUID_WICPixelFormat64bppPRGBAHalf",
    "GUID_WICPixelFormat64bppRGBHalf",
    "GUID_WICPixelFormat48bppRGBHalf",
    "GUID_WICPixelFormat32bppRGBE",
    "GUID_WICPixelFormat16bppGrayHalf",
    "GUID_WICPixelFormat32bppGrayFixedPoint",
    "GUID_WICPixelFormat32bppRGBA1010102",
    "GUID_WICPixelFormat32bppRGBA1010102XR",
    "GUID_WICPixelFormat32bppR10G10B10A2",
    "GUID_WICPixelFormat32bppR10G10B10A2HDR10",
    "GUID_WICPixelFormat64bppCMYK",
    "GUID_WICPixelFormat24bpp3Channels",
    "GUID_WICPixelFormat32bpp4Channels",
    "GUID_WICPixelFormat40bpp5Channels",
    "GUID_WICPixelFormat48bpp6Channels",
    "GUID_WICPixelFormat56bpp7Channels",
    "GUID_WICPixelFormat64bpp8Channels",
    "GUID_WICPixelFormat48bpp3Channels",
    "GUID_WICPixelFormat64bpp4Channels",
    "GUID_WICPixelFormat80bpp5Channels",
    "GUID_WICPixelFormat96bpp6Channels",
    "GUID_WICPixelFormat112bpp7Channels",
    "GUID_WICPixelFormat128bpp8Channels",
    "GUID_WICPixelFormat40bppCMYKAlpha",
    "GUID_WICPixelFormat80bppCMYKAlpha",
    "GUID_WICPixelFormat32bpp3ChannelsAlpha",
    "GUID_WICPixelFormat40bpp4ChannelsAlpha",
    "GUID_WICPixelFormat48bpp5ChannelsAlpha",
    "GUID_WICPixelFormat56bpp6ChannelsAlpha",
    "GUID_WICPixelFormat64bpp7ChannelsAlpha",
    "GUID_WICPixelFormat72bpp8ChannelsAlpha",
    "GUID_WICPixelFormat64bpp3ChannelsAlpha",
    "GUID_WICPixelFormat80bpp4ChannelsAlpha",
    "GUID_WICPixelFormat96bpp5ChannelsAlpha",
    "GUID_WICPixelFormat112bpp6ChannelsAlpha",
    "GUID_WICPixelFormat128bpp7ChannelsAlpha",
    "GUID_WICPixelFormat144bpp8ChannelsAlpha",
    "GUID_WICPixelFormat8bppY",
    "GUID_WICPixelFormat8bppCb",
    "GUID_WICPixelFormat8bppCr",
    "GUID_WICPixelFormat16bppCbCr",
    "GUID_WICPixelFormat16bppYQuantizedDctCoefficients",
    "GUID_WICPixelFormat16bppCbQuantizedDctCoefficients",
    "GUID_WICPixelFormat16bppCrQuantizedDctCoefficients",
    "FACILITY_WINCODEC_ERR",
    "WINCODEC_ERR_BASE",
    "WINCODEC_ERR_GENERIC_ERROR",
    "WINCODEC_ERR_INVALIDPARAMETER",
    "WINCODEC_ERR_OUTOFMEMORY",
    "WINCODEC_ERR_NOTIMPLEMENTED",
    "WINCODEC_ERR_ABORTED",
    "WINCODEC_ERR_ACCESSDENIED",
    "WICRawChangeNotification_ExposureCompensation",
    "WICRawChangeNotification_NamedWhitePoint",
    "WICRawChangeNotification_KelvinWhitePoint",
    "WICRawChangeNotification_RGBWhitePoint",
    "WICRawChangeNotification_Contrast",
    "WICRawChangeNotification_Gamma",
    "WICRawChangeNotification_Sharpness",
    "WICRawChangeNotification_Saturation",
    "WICRawChangeNotification_Tint",
    "WICRawChangeNotification_NoiseReduction",
    "WICRawChangeNotification_DestinationColorContext",
    "WICRawChangeNotification_ToneCurve",
    "WICRawChangeNotification_Rotation",
    "WICRawChangeNotification_RenderMode",
    "GUID_MetadataFormatUnknown",
    "GUID_MetadataFormatIfd",
    "GUID_MetadataFormatSubIfd",
    "GUID_MetadataFormatExif",
    "GUID_MetadataFormatGps",
    "GUID_MetadataFormatInterop",
    "GUID_MetadataFormatApp0",
    "GUID_MetadataFormatApp1",
    "GUID_MetadataFormatApp13",
    "GUID_MetadataFormatIPTC",
    "GUID_MetadataFormatIRB",
    "GUID_MetadataFormat8BIMIPTC",
    "GUID_MetadataFormat8BIMResolutionInfo",
    "GUID_MetadataFormat8BIMIPTCDigest",
    "GUID_MetadataFormatXMP",
    "GUID_MetadataFormatThumbnail",
    "GUID_MetadataFormatChunktEXt",
    "GUID_MetadataFormatXMPStruct",
    "GUID_MetadataFormatXMPBag",
    "GUID_MetadataFormatXMPSeq",
    "GUID_MetadataFormatXMPAlt",
    "GUID_MetadataFormatLSD",
    "GUID_MetadataFormatIMD",
    "GUID_MetadataFormatGCE",
    "GUID_MetadataFormatAPE",
    "GUID_MetadataFormatJpegChrominance",
    "GUID_MetadataFormatJpegLuminance",
    "GUID_MetadataFormatJpegComment",
    "GUID_MetadataFormatGifComment",
    "GUID_MetadataFormatChunkgAMA",
    "GUID_MetadataFormatChunkbKGD",
    "GUID_MetadataFormatChunkiTXt",
    "GUID_MetadataFormatChunkcHRM",
    "GUID_MetadataFormatChunkhIST",
    "GUID_MetadataFormatChunkiCCP",
    "GUID_MetadataFormatChunksRGB",
    "GUID_MetadataFormatChunktIME",
    "GUID_MetadataFormatDds",
    "GUID_MetadataFormatHeif",
    "GUID_MetadataFormatHeifHDR",
    "GUID_MetadataFormatWebpANIM",
    "GUID_MetadataFormatWebpANMF",
    "CLSID_WICUnknownMetadataReader",
    "CLSID_WICUnknownMetadataWriter",
    "CLSID_WICApp0MetadataWriter",
    "CLSID_WICApp0MetadataReader",
    "CLSID_WICApp1MetadataWriter",
    "CLSID_WICApp1MetadataReader",
    "CLSID_WICApp13MetadataWriter",
    "CLSID_WICApp13MetadataReader",
    "CLSID_WICIfdMetadataReader",
    "CLSID_WICIfdMetadataWriter",
    "CLSID_WICSubIfdMetadataReader",
    "CLSID_WICSubIfdMetadataWriter",
    "CLSID_WICExifMetadataReader",
    "CLSID_WICExifMetadataWriter",
    "CLSID_WICGpsMetadataReader",
    "CLSID_WICGpsMetadataWriter",
    "CLSID_WICInteropMetadataReader",
    "CLSID_WICInteropMetadataWriter",
    "CLSID_WICThumbnailMetadataReader",
    "CLSID_WICThumbnailMetadataWriter",
    "CLSID_WICIPTCMetadataReader",
    "CLSID_WICIPTCMetadataWriter",
    "CLSID_WICIRBMetadataReader",
    "CLSID_WICIRBMetadataWriter",
    "CLSID_WIC8BIMIPTCMetadataReader",
    "CLSID_WIC8BIMIPTCMetadataWriter",
    "CLSID_WIC8BIMResolutionInfoMetadataReader",
    "CLSID_WIC8BIMResolutionInfoMetadataWriter",
    "CLSID_WIC8BIMIPTCDigestMetadataReader",
    "CLSID_WIC8BIMIPTCDigestMetadataWriter",
    "CLSID_WICPngTextMetadataReader",
    "CLSID_WICPngTextMetadataWriter",
    "CLSID_WICXMPMetadataReader",
    "CLSID_WICXMPMetadataWriter",
    "CLSID_WICXMPStructMetadataReader",
    "CLSID_WICXMPStructMetadataWriter",
    "CLSID_WICXMPBagMetadataReader",
    "CLSID_WICXMPBagMetadataWriter",
    "CLSID_WICXMPSeqMetadataReader",
    "CLSID_WICXMPSeqMetadataWriter",
    "CLSID_WICXMPAltMetadataReader",
    "CLSID_WICXMPAltMetadataWriter",
    "CLSID_WICLSDMetadataReader",
    "CLSID_WICLSDMetadataWriter",
    "CLSID_WICGCEMetadataReader",
    "CLSID_WICGCEMetadataWriter",
    "CLSID_WICIMDMetadataReader",
    "CLSID_WICIMDMetadataWriter",
    "CLSID_WICAPEMetadataReader",
    "CLSID_WICAPEMetadataWriter",
    "CLSID_WICJpegChrominanceMetadataReader",
    "CLSID_WICJpegChrominanceMetadataWriter",
    "CLSID_WICJpegLuminanceMetadataReader",
    "CLSID_WICJpegLuminanceMetadataWriter",
    "CLSID_WICJpegCommentMetadataReader",
    "CLSID_WICJpegCommentMetadataWriter",
    "CLSID_WICGifCommentMetadataReader",
    "CLSID_WICGifCommentMetadataWriter",
    "CLSID_WICPngGamaMetadataReader",
    "CLSID_WICPngGamaMetadataWriter",
    "CLSID_WICPngBkgdMetadataReader",
    "CLSID_WICPngBkgdMetadataWriter",
    "CLSID_WICPngItxtMetadataReader",
    "CLSID_WICPngItxtMetadataWriter",
    "CLSID_WICPngChrmMetadataReader",
    "CLSID_WICPngChrmMetadataWriter",
    "CLSID_WICPngHistMetadataReader",
    "CLSID_WICPngHistMetadataWriter",
    "CLSID_WICPngIccpMetadataReader",
    "CLSID_WICPngIccpMetadataWriter",
    "CLSID_WICPngSrgbMetadataReader",
    "CLSID_WICPngSrgbMetadataWriter",
    "CLSID_WICPngTimeMetadataReader",
    "CLSID_WICPngTimeMetadataWriter",
    "CLSID_WICDdsMetadataReader",
    "CLSID_WICDdsMetadataWriter",
    "CLSID_WICHeifMetadataReader",
    "CLSID_WICHeifMetadataWriter",
    "CLSID_WICHeifHDRMetadataReader",
    "CLSID_WICWebpAnimMetadataReader",
    "CLSID_WICWebpAnmfMetadataReader",
    "WICRect",
    "WICColorContextType",
    "WICColorContextType_WICColorContextUninitialized",
    "WICColorContextType_WICColorContextProfile",
    "WICColorContextType_WICColorContextExifColorSpace",
    "WICBitmapCreateCacheOption",
    "WICBitmapCreateCacheOption_WICBitmapNoCache",
    "WICBitmapCreateCacheOption_WICBitmapCacheOnDemand",
    "WICBitmapCreateCacheOption_WICBitmapCacheOnLoad",
    "WICBitmapCreateCacheOption_WICBITMAPCREATECACHEOPTION_FORCE_DWORD",
    "WICDecodeOptions",
    "WICDecodeOptions_WICDecodeMetadataCacheOnDemand",
    "WICDecodeOptions_WICDecodeMetadataCacheOnLoad",
    "WICDecodeOptions_WICMETADATACACHEOPTION_FORCE_DWORD",
    "WICBitmapEncoderCacheOption",
    "WICBitmapEncoderCacheOption_WICBitmapEncoderCacheInMemory",
    "WICBitmapEncoderCacheOption_WICBitmapEncoderCacheTempFile",
    "WICBitmapEncoderCacheOption_WICBitmapEncoderNoCache",
    "WICBitmapEncoderCacheOption_WICBITMAPENCODERCACHEOPTION_FORCE_DWORD",
    "WICComponentType",
    "WICComponentType_WICDecoder",
    "WICComponentType_WICEncoder",
    "WICComponentType_WICPixelFormatConverter",
    "WICComponentType_WICMetadataReader",
    "WICComponentType_WICMetadataWriter",
    "WICComponentType_WICPixelFormat",
    "WICComponentType_WICAllComponents",
    "WICComponentType_WICCOMPONENTTYPE_FORCE_DWORD",
    "WICComponentEnumerateOptions",
    "WICComponentEnumerateOptions_WICComponentEnumerateDefault",
    "WICComponentEnumerateOptions_WICComponentEnumerateRefresh",
    "WICComponentEnumerateOptions_WICComponentEnumerateDisabled",
    "WICComponentEnumerateOptions_WICComponentEnumerateUnsigned",
    "WICComponentEnumerateOptions_WICComponentEnumerateBuiltInOnly",
    "WICComponentEnumerateOptions_WICCOMPONENTENUMERATEOPTIONS_FORCE_DWORD",
    "WICBitmapPattern",
    "WICBitmapInterpolationMode",
    "WICBitmapInterpolationMode_WICBitmapInterpolationModeNearestNeighbor",
    "WICBitmapInterpolationMode_WICBitmapInterpolationModeLinear",
    "WICBitmapInterpolationMode_WICBitmapInterpolationModeCubic",
    "WICBitmapInterpolationMode_WICBitmapInterpolationModeFant",
    "WICBitmapInterpolationMode_WICBitmapInterpolationModeHighQualityCubic",
    "WICBitmapInterpolationMode_WICBITMAPINTERPOLATIONMODE_FORCE_DWORD",
    "WICBitmapPaletteType",
    "WICBitmapPaletteType_WICBitmapPaletteTypeCustom",
    "WICBitmapPaletteType_WICBitmapPaletteTypeMedianCut",
    "WICBitmapPaletteType_WICBitmapPaletteTypeFixedBW",
    "WICBitmapPaletteType_WICBitmapPaletteTypeFixedHalftone8",
    "WICBitmapPaletteType_WICBitmapPaletteTypeFixedHalftone27",
    "WICBitmapPaletteType_WICBitmapPaletteTypeFixedHalftone64",
    "WICBitmapPaletteType_WICBitmapPaletteTypeFixedHalftone125",
    "WICBitmapPaletteType_WICBitmapPaletteTypeFixedHalftone216",
    "WICBitmapPaletteType_WICBitmapPaletteTypeFixedWebPalette",
    "WICBitmapPaletteType_WICBitmapPaletteTypeFixedHalftone252",
    "WICBitmapPaletteType_WICBitmapPaletteTypeFixedHalftone256",
    "WICBitmapPaletteType_WICBitmapPaletteTypeFixedGray4",
    "WICBitmapPaletteType_WICBitmapPaletteTypeFixedGray16",
    "WICBitmapPaletteType_WICBitmapPaletteTypeFixedGray256",
    "WICBitmapPaletteType_WICBITMAPPALETTETYPE_FORCE_DWORD",
    "WICBitmapDitherType",
    "WICBitmapDitherType_WICBitmapDitherTypeNone",
    "WICBitmapDitherType_WICBitmapDitherTypeSolid",
    "WICBitmapDitherType_WICBitmapDitherTypeOrdered4x4",
    "WICBitmapDitherType_WICBitmapDitherTypeOrdered8x8",
    "WICBitmapDitherType_WICBitmapDitherTypeOrdered16x16",
    "WICBitmapDitherType_WICBitmapDitherTypeSpiral4x4",
    "WICBitmapDitherType_WICBitmapDitherTypeSpiral8x8",
    "WICBitmapDitherType_WICBitmapDitherTypeDualSpiral4x4",
    "WICBitmapDitherType_WICBitmapDitherTypeDualSpiral8x8",
    "WICBitmapDitherType_WICBitmapDitherTypeErrorDiffusion",
    "WICBitmapDitherType_WICBITMAPDITHERTYPE_FORCE_DWORD",
    "WICBitmapAlphaChannelOption",
    "WICBitmapAlphaChannelOption_WICBitmapUseAlpha",
    "WICBitmapAlphaChannelOption_WICBitmapUsePremultipliedAlpha",
    "WICBitmapAlphaChannelOption_WICBitmapIgnoreAlpha",
    "WICBitmapAlphaChannelOption_WICBITMAPALPHACHANNELOPTIONS_FORCE_DWORD",
    "WICBitmapTransformOptions",
    "WICBitmapTransformOptions_WICBitmapTransformRotate0",
    "WICBitmapTransformOptions_WICBitmapTransformRotate90",
    "WICBitmapTransformOptions_WICBitmapTransformRotate180",
    "WICBitmapTransformOptions_WICBitmapTransformRotate270",
    "WICBitmapTransformOptions_WICBitmapTransformFlipHorizontal",
    "WICBitmapTransformOptions_WICBitmapTransformFlipVertical",
    "WICBitmapTransformOptions_WICBITMAPTRANSFORMOPTIONS_FORCE_DWORD",
    "WICBitmapLockFlags",
    "WICBitmapLockFlags_WICBitmapLockRead",
    "WICBitmapLockFlags_WICBitmapLockWrite",
    "WICBitmapLockFlags_WICBITMAPLOCKFLAGS_FORCE_DWORD",
    "WICBitmapDecoderCapabilities",
    "WICBitmapDecoderCapabilities_WICBitmapDecoderCapabilitySameEncoder",
    "WICBitmapDecoderCapabilities_WICBitmapDecoderCapabilityCanDecodeAllImages",
    "WICBitmapDecoderCapabilities_WICBitmapDecoderCapabilityCanDecodeSomeImages",
    "WICBitmapDecoderCapabilities_WICBitmapDecoderCapabilityCanEnumerateMetadata",
    "WICBitmapDecoderCapabilities_WICBitmapDecoderCapabilityCanDecodeThumbnail",
    "WICBitmapDecoderCapabilities_WICBITMAPDECODERCAPABILITIES_FORCE_DWORD",
    "WICProgressOperation",
    "WICProgressOperation_WICProgressOperationCopyPixels",
    "WICProgressOperation_WICProgressOperationWritePixels",
    "WICProgressOperation_WICProgressOperationAll",
    "WICProgressOperation_WICPROGRESSOPERATION_FORCE_DWORD",
    "WICProgressNotification",
    "WICProgressNotification_WICProgressNotificationBegin",
    "WICProgressNotification_WICProgressNotificationEnd",
    "WICProgressNotification_WICProgressNotificationFrequent",
    "WICProgressNotification_WICProgressNotificationAll",
    "WICProgressNotification_WICPROGRESSNOTIFICATION_FORCE_DWORD",
    "WICComponentSigning",
    "WICComponentSigning_WICComponentSigned",
    "WICComponentSigning_WICComponentUnsigned",
    "WICComponentSigning_WICComponentSafe",
    "WICComponentSigning_WICComponentDisabled",
    "WICComponentSigning_WICCOMPONENTSIGNING_FORCE_DWORD",
    "WICGifLogicalScreenDescriptorProperties",
    "WICGifLogicalScreenDescriptorProperties_WICGifLogicalScreenSignature",
    "WICGifLogicalScreenDescriptorProperties_WICGifLogicalScreenDescriptorWidth",
    "WICGifLogicalScreenDescriptorProperties_WICGifLogicalScreenDescriptorHeight",
    "WICGifLogicalScreenDescriptorProperties_WICGifLogicalScreenDescriptorGlobalColorTableFlag",
    "WICGifLogicalScreenDescriptorProperties_WICGifLogicalScreenDescriptorColorResolution",
    "WICGifLogicalScreenDescriptorProperties_WICGifLogicalScreenDescriptorSortFlag",
    "WICGifLogicalScreenDescriptorProperties_WICGifLogicalScreenDescriptorGlobalColorTableSize",
    "WICGifLogicalScreenDescriptorProperties_WICGifLogicalScreenDescriptorBackgroundColorIndex",
    "WICGifLogicalScreenDescriptorProperties_WICGifLogicalScreenDescriptorPixelAspectRatio",
    "WICGifLogicalScreenDescriptorProperties_WICGifLogicalScreenDescriptorProperties_FORCE_DWORD",
    "WICGifImageDescriptorProperties",
    "WICGifImageDescriptorProperties_WICGifImageDescriptorLeft",
    "WICGifImageDescriptorProperties_WICGifImageDescriptorTop",
    "WICGifImageDescriptorProperties_WICGifImageDescriptorWidth",
    "WICGifImageDescriptorProperties_WICGifImageDescriptorHeight",
    "WICGifImageDescriptorProperties_WICGifImageDescriptorLocalColorTableFlag",
    "WICGifImageDescriptorProperties_WICGifImageDescriptorInterlaceFlag",
    "WICGifImageDescriptorProperties_WICGifImageDescriptorSortFlag",
    "WICGifImageDescriptorProperties_WICGifImageDescriptorLocalColorTableSize",
    "WICGifImageDescriptorProperties_WICGifImageDescriptorProperties_FORCE_DWORD",
    "WICGifGraphicControlExtensionProperties",
    "WICGifGraphicControlExtensionProperties_WICGifGraphicControlExtensionDisposal",
    "WICGifGraphicControlExtensionProperties_WICGifGraphicControlExtensionUserInputFlag",
    "WICGifGraphicControlExtensionProperties_WICGifGraphicControlExtensionTransparencyFlag",
    "WICGifGraphicControlExtensionProperties_WICGifGraphicControlExtensionDelay",
    "WICGifGraphicControlExtensionProperties_WICGifGraphicControlExtensionTransparentColorIndex",
    "WICGifGraphicControlExtensionProperties_WICGifGraphicControlExtensionProperties_FORCE_DWORD",
    "WICGifApplicationExtensionProperties",
    "WICGifApplicationExtensionProperties_WICGifApplicationExtensionApplication",
    "WICGifApplicationExtensionProperties_WICGifApplicationExtensionData",
    "WICGifApplicationExtensionProperties_WICGifApplicationExtensionProperties_FORCE_DWORD",
    "WICGifCommentExtensionProperties",
    "WICGifCommentExtensionProperties_WICGifCommentExtensionText",
    "WICGifCommentExtensionProperties_WICGifCommentExtensionProperties_FORCE_DWORD",
    "WICJpegCommentProperties",
    "WICJpegCommentProperties_WICJpegCommentText",
    "WICJpegCommentProperties_WICJpegCommentProperties_FORCE_DWORD",
    "WICJpegLuminanceProperties",
    "WICJpegLuminanceProperties_WICJpegLuminanceTable",
    "WICJpegLuminanceProperties_WICJpegLuminanceProperties_FORCE_DWORD",
    "WICJpegChrominanceProperties",
    "WICJpegChrominanceProperties_WICJpegChrominanceTable",
    "WICJpegChrominanceProperties_WICJpegChrominanceProperties_FORCE_DWORD",
    "WIC8BIMIptcProperties",
    "WIC8BIMIptcProperties_WIC8BIMIptcPString",
    "WIC8BIMIptcProperties_WIC8BIMIptcEmbeddedIPTC",
    "WIC8BIMIptcProperties_WIC8BIMIptcProperties_FORCE_DWORD",
    "WIC8BIMResolutionInfoProperties",
    "WIC8BIMResolutionInfoProperties_WIC8BIMResolutionInfoPString",
    "WIC8BIMResolutionInfoProperties_WIC8BIMResolutionInfoHResolution",
    "WIC8BIMResolutionInfoProperties_WIC8BIMResolutionInfoHResolutionUnit",
    "WIC8BIMResolutionInfoProperties_WIC8BIMResolutionInfoWidthUnit",
    "WIC8BIMResolutionInfoProperties_WIC8BIMResolutionInfoVResolution",
    "WIC8BIMResolutionInfoProperties_WIC8BIMResolutionInfoVResolutionUnit",
    "WIC8BIMResolutionInfoProperties_WIC8BIMResolutionInfoHeightUnit",
    "WIC8BIMResolutionInfoProperties_WIC8BIMResolutionInfoProperties_FORCE_DWORD",
    "WIC8BIMIptcDigestProperties",
    "WIC8BIMIptcDigestProperties_WIC8BIMIptcDigestPString",
    "WIC8BIMIptcDigestProperties_WIC8BIMIptcDigestIptcDigest",
    "WIC8BIMIptcDigestProperties_WIC8BIMIptcDigestProperties_FORCE_DWORD",
    "WICPngGamaProperties",
    "WICPngGamaProperties_WICPngGamaGamma",
    "WICPngGamaProperties_WICPngGamaProperties_FORCE_DWORD",
    "WICPngBkgdProperties",
    "WICPngBkgdProperties_WICPngBkgdBackgroundColor",
    "WICPngBkgdProperties_WICPngBkgdProperties_FORCE_DWORD",
    "WICPngItxtProperties",
    "WICPngItxtProperties_WICPngItxtKeyword",
    "WICPngItxtProperties_WICPngItxtCompressionFlag",
    "WICPngItxtProperties_WICPngItxtLanguageTag",
    "WICPngItxtProperties_WICPngItxtTranslatedKeyword",
    "WICPngItxtProperties_WICPngItxtText",
    "WICPngItxtProperties_WICPngItxtProperties_FORCE_DWORD",
    "WICPngChrmProperties",
    "WICPngChrmProperties_WICPngChrmWhitePointX",
    "WICPngChrmProperties_WICPngChrmWhitePointY",
    "WICPngChrmProperties_WICPngChrmRedX",
    "WICPngChrmProperties_WICPngChrmRedY",
    "WICPngChrmProperties_WICPngChrmGreenX",
    "WICPngChrmProperties_WICPngChrmGreenY",
    "WICPngChrmProperties_WICPngChrmBlueX",
    "WICPngChrmProperties_WICPngChrmBlueY",
    "WICPngChrmProperties_WICPngChrmProperties_FORCE_DWORD",
    "WICPngHistProperties",
    "WICPngHistProperties_WICPngHistFrequencies",
    "WICPngHistProperties_WICPngHistProperties_FORCE_DWORD",
    "WICPngIccpProperties",
    "WICPngIccpProperties_WICPngIccpProfileName",
    "WICPngIccpProperties_WICPngIccpProfileData",
    "WICPngIccpProperties_WICPngIccpProperties_FORCE_DWORD",
    "WICPngSrgbProperties",
    "WICPngSrgbProperties_WICPngSrgbRenderingIntent",
    "WICPngSrgbProperties_WICPngSrgbProperties_FORCE_DWORD",
    "WICPngTimeProperties",
    "WICPngTimeProperties_WICPngTimeYear",
    "WICPngTimeProperties_WICPngTimeMonth",
    "WICPngTimeProperties_WICPngTimeDay",
    "WICPngTimeProperties_WICPngTimeHour",
    "WICPngTimeProperties_WICPngTimeMinute",
    "WICPngTimeProperties_WICPngTimeSecond",
    "WICPngTimeProperties_WICPngTimeProperties_FORCE_DWORD",
    "WICHeifProperties",
    "WICHeifProperties_WICHeifOrientation",
    "WICHeifProperties_WICHeifProperties_FORCE_DWORD",
    "WICHeifHdrProperties",
    "WICHeifHdrProperties_WICHeifHdrMaximumLuminanceLevel",
    "WICHeifHdrProperties_WICHeifHdrMaximumFrameAverageLuminanceLevel",
    "WICHeifHdrProperties_WICHeifHdrMinimumMasteringDisplayLuminanceLevel",
    "WICHeifHdrProperties_WICHeifHdrMaximumMasteringDisplayLuminanceLevel",
    "WICHeifHdrProperties_WICHeifHdrCustomVideoPrimaries",
    "WICHeifHdrProperties_WICHeifHdrProperties_FORCE_DWORD",
    "WICWebpAnimProperties",
    "WICWebpAnimProperties_WICWebpAnimLoopCount",
    "WICWebpAnimProperties_WICWebpAnimProperties_FORCE_DWORD",
    "WICWebpAnmfProperties",
    "WICWebpAnmfProperties_WICWebpAnmfFrameDuration",
    "WICWebpAnmfProperties_WICWebpAnmfProperties_FORCE_DWORD",
    "WICSectionAccessLevel",
    "WICSectionAccessLevel_WICSectionAccessLevelRead",
    "WICSectionAccessLevel_WICSectionAccessLevelReadWrite",
    "WICSectionAccessLevel_WICSectionAccessLevel_FORCE_DWORD",
    "WICPixelFormatNumericRepresentation",
    "WICPixelFormatNumericRepresentation_WICPixelFormatNumericRepresentationUnspecified",
    "WICPixelFormatNumericRepresentation_WICPixelFormatNumericRepresentationIndexed",
    "WICPixelFormatNumericRepresentation_WICPixelFormatNumericRepresentationUnsignedInteger",
    "WICPixelFormatNumericRepresentation_WICPixelFormatNumericRepresentationSignedInteger",
    "WICPixelFormatNumericRepresentation_WICPixelFormatNumericRepresentationFixed",
    "WICPixelFormatNumericRepresentation_WICPixelFormatNumericRepresentationFloat",
    "WICPixelFormatNumericRepresentation_WICPixelFormatNumericRepresentation_FORCE_DWORD",
    "WICPlanarOptions",
    "WICPlanarOptions_WICPlanarOptionsDefault",
    "WICPlanarOptions_WICPlanarOptionsPreserveSubsampling",
    "WICPlanarOptions_WICPLANAROPTIONS_FORCE_DWORD",
    "WICJpegIndexingOptions",
    "WICJpegIndexingOptions_WICJpegIndexingOptionsGenerateOnDemand",
    "WICJpegIndexingOptions_WICJpegIndexingOptionsGenerateOnLoad",
    "WICJpegIndexingOptions_WICJpegIndexingOptions_FORCE_DWORD",
    "WICJpegTransferMatrix",
    "WICJpegTransferMatrix_WICJpegTransferMatrixIdentity",
    "WICJpegTransferMatrix_WICJpegTransferMatrixBT601",
    "WICJpegTransferMatrix_WICJpegTransferMatrix_FORCE_DWORD",
    "WICJpegScanType",
    "WICJpegScanType_WICJpegScanTypeInterleaved",
    "WICJpegScanType_WICJpegScanTypePlanarComponents",
    "WICJpegScanType_WICJpegScanTypeProgressive",
    "WICJpegScanType_WICJpegScanType_FORCE_DWORD",
    "WICImageParameters",
    "WICBitmapPlaneDescription",
    "WICBitmapPlane",
    "WICJpegFrameHeader",
    "WICJpegScanHeader",
    "IWICPalette",
    "IWICBitmapSource",
    "IWICFormatConverter",
    "IWICPlanarFormatConverter",
    "IWICBitmapScaler",
    "IWICBitmapClipper",
    "IWICBitmapFlipRotator",
    "IWICBitmapLock",
    "IWICBitmap",
    "IWICColorContext",
    "IWICColorTransform",
    "IWICFastMetadataEncoder",
    "IWICStream",
    "IWICEnumMetadataItem",
    "IWICMetadataQueryReader",
    "IWICMetadataQueryWriter",
    "IWICBitmapEncoder",
    "IWICBitmapFrameEncode",
    "IWICPlanarBitmapFrameEncode",
    "IWICBitmapDecoder",
    "IWICBitmapSourceTransform",
    "IWICPlanarBitmapSourceTransform",
    "IWICBitmapFrameDecode",
    "IWICProgressiveLevelControl",
    "IWICProgressCallback",
    "PFNProgressNotification",
    "IWICBitmapCodecProgressNotification",
    "IWICComponentInfo",
    "IWICFormatConverterInfo",
    "IWICBitmapCodecInfo",
    "IWICBitmapEncoderInfo",
    "IWICBitmapDecoderInfo",
    "IWICPixelFormatInfo",
    "IWICPixelFormatInfo2",
    "IWICImagingFactory",
    "WICTiffCompressionOption",
    "WICTiffCompressionOption_WICTiffCompressionDontCare",
    "WICTiffCompressionOption_WICTiffCompressionNone",
    "WICTiffCompressionOption_WICTiffCompressionCCITT3",
    "WICTiffCompressionOption_WICTiffCompressionCCITT4",
    "WICTiffCompressionOption_WICTiffCompressionLZW",
    "WICTiffCompressionOption_WICTiffCompressionRLE",
    "WICTiffCompressionOption_WICTiffCompressionZIP",
    "WICTiffCompressionOption_WICTiffCompressionLZWHDifferencing",
    "WICTiffCompressionOption_WICTIFFCOMPRESSIONOPTION_FORCE_DWORD",
    "WICJpegYCrCbSubsamplingOption",
    "WICJpegYCrCbSubsamplingOption_WICJpegYCrCbSubsamplingDefault",
    "WICJpegYCrCbSubsamplingOption_WICJpegYCrCbSubsampling420",
    "WICJpegYCrCbSubsamplingOption_WICJpegYCrCbSubsampling422",
    "WICJpegYCrCbSubsamplingOption_WICJpegYCrCbSubsampling444",
    "WICJpegYCrCbSubsamplingOption_WICJpegYCrCbSubsampling440",
    "WICJpegYCrCbSubsamplingOption_WICJPEGYCRCBSUBSAMPLING_FORCE_DWORD",
    "WICPngFilterOption",
    "WICPngFilterOption_WICPngFilterUnspecified",
    "WICPngFilterOption_WICPngFilterNone",
    "WICPngFilterOption_WICPngFilterSub",
    "WICPngFilterOption_WICPngFilterUp",
    "WICPngFilterOption_WICPngFilterAverage",
    "WICPngFilterOption_WICPngFilterPaeth",
    "WICPngFilterOption_WICPngFilterAdaptive",
    "WICPngFilterOption_WICPNGFILTEROPTION_FORCE_DWORD",
    "WICNamedWhitePoint",
    "WICNamedWhitePoint_WICWhitePointDefault",
    "WICNamedWhitePoint_WICWhitePointDaylight",
    "WICNamedWhitePoint_WICWhitePointCloudy",
    "WICNamedWhitePoint_WICWhitePointShade",
    "WICNamedWhitePoint_WICWhitePointTungsten",
    "WICNamedWhitePoint_WICWhitePointFluorescent",
    "WICNamedWhitePoint_WICWhitePointFlash",
    "WICNamedWhitePoint_WICWhitePointUnderwater",
    "WICNamedWhitePoint_WICWhitePointCustom",
    "WICNamedWhitePoint_WICWhitePointAutoWhiteBalance",
    "WICNamedWhitePoint_WICWhitePointAsShot",
    "WICNamedWhitePoint_WICNAMEDWHITEPOINT_FORCE_DWORD",
    "WICRawCapabilities",
    "WICRawCapabilities_WICRawCapabilityNotSupported",
    "WICRawCapabilities_WICRawCapabilityGetSupported",
    "WICRawCapabilities_WICRawCapabilityFullySupported",
    "WICRawCapabilities_WICRAWCAPABILITIES_FORCE_DWORD",
    "WICRawRotationCapabilities",
    "WICRawRotationCapabilities_WICRawRotationCapabilityNotSupported",
    "WICRawRotationCapabilities_WICRawRotationCapabilityGetSupported",
    "WICRawRotationCapabilities_WICRawRotationCapabilityNinetyDegreesSupported",
    "WICRawRotationCapabilities_WICRawRotationCapabilityFullySupported",
    "WICRawRotationCapabilities_WICRAWROTATIONCAPABILITIES_FORCE_DWORD",
    "WICRawCapabilitiesInfo",
    "WICRawParameterSet",
    "WICRawParameterSet_WICAsShotParameterSet",
    "WICRawParameterSet_WICUserAdjustedParameterSet",
    "WICRawParameterSet_WICAutoAdjustedParameterSet",
    "WICRawParameterSet_WICRAWPARAMETERSET_FORCE_DWORD",
    "WICRawRenderMode",
    "WICRawRenderMode_WICRawRenderModeDraft",
    "WICRawRenderMode_WICRawRenderModeNormal",
    "WICRawRenderMode_WICRawRenderModeBestQuality",
    "WICRawRenderMode_WICRAWRENDERMODE_FORCE_DWORD",
    "WICRawToneCurvePoint",
    "WICRawToneCurve",
    "IWICDevelopRawNotificationCallback",
    "IWICDevelopRaw",
    "WICDdsDimension",
    "WICDdsDimension_WICDdsTexture1D",
    "WICDdsDimension_WICDdsTexture2D",
    "WICDdsDimension_WICDdsTexture3D",
    "WICDdsDimension_WICDdsTextureCube",
    "WICDdsDimension_WICDDSTEXTURE_FORCE_DWORD",
    "WICDdsAlphaMode",
    "WICDdsAlphaMode_WICDdsAlphaModeUnknown",
    "WICDdsAlphaMode_WICDdsAlphaModeStraight",
    "WICDdsAlphaMode_WICDdsAlphaModePremultiplied",
    "WICDdsAlphaMode_WICDdsAlphaModeOpaque",
    "WICDdsAlphaMode_WICDdsAlphaModeCustom",
    "WICDdsAlphaMode_WICDDSALPHAMODE_FORCE_DWORD",
    "WICDdsParameters",
    "IWICDdsDecoder",
    "IWICDdsEncoder",
    "WICDdsFormatInfo",
    "IWICDdsFrameDecode",
    "IWICJpegFrameDecode",
    "IWICJpegFrameEncode",
    "WICMetadataCreationOptions",
    "WICMetadataCreationOptions_WICMetadataCreationDefault",
    "WICMetadataCreationOptions_WICMetadataCreationAllowUnknown",
    "WICMetadataCreationOptions_WICMetadataCreationFailUnknown",
    "WICMetadataCreationOptions_WICMetadataCreationMask",
    "WICPersistOptions",
    "WICPersistOptions_WICPersistOptionDefault",
    "WICPersistOptions_WICPersistOptionLittleEndian",
    "WICPersistOptions_WICPersistOptionBigEndian",
    "WICPersistOptions_WICPersistOptionStrictFormat",
    "WICPersistOptions_WICPersistOptionNoCacheStream",
    "WICPersistOptions_WICPersistOptionPreferUTF8",
    "WICPersistOptions_WICPersistOptionMask",
    "IWICMetadataBlockReader",
    "IWICMetadataBlockWriter",
    "IWICMetadataReader",
    "IWICMetadataWriter",
    "IWICStreamProvider",
    "IWICPersistStream",
    "IWICMetadataHandlerInfo",
    "WICMetadataPattern",
    "IWICMetadataReaderInfo",
    "WICMetadataHeader",
    "IWICMetadataWriterInfo",
    "IWICComponentFactory",
    "WICConvertBitmapSource",
    "WICCreateBitmapFromSection",
    "WICCreateBitmapFromSectionEx",
    "WICMapGuidToShortName",
    "WICMapShortNameToGuid",
    "WICMapSchemaToName",
    "WICMatchMetadataContent",
    "WICSerializeMetadataContent",
    "WICGetMetadataContentSize",
]
