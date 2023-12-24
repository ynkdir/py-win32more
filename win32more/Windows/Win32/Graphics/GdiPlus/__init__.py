from __future__ import annotations
from win32more import ARCH, Boolean, Byte, Bytes, Char, ComPtr, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, MissingType, POINTER, SByte, SUCCEEDED, Single, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer, ConstantLazyLoader
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.Graphics.DirectDraw
import win32more.Windows.Win32.Graphics.Gdi
import win32more.Windows.Win32.Graphics.GdiPlus
import win32more.Windows.Win32.System.Com
import win32more.Windows.Win32.UI.WindowsAndMessaging
GDIP_EMFPLUS_RECORD_BASE: UInt32 = 16384
GDIP_WMF_RECORD_BASE: UInt32 = 65536
ImageFormatUndefined: Guid = Guid('{b96b3ca9-0728-11d3-9d7b-0000f81ef32e}')
ImageFormatMemoryBMP: Guid = Guid('{b96b3caa-0728-11d3-9d7b-0000f81ef32e}')
ImageFormatBMP: Guid = Guid('{b96b3cab-0728-11d3-9d7b-0000f81ef32e}')
ImageFormatEMF: Guid = Guid('{b96b3cac-0728-11d3-9d7b-0000f81ef32e}')
ImageFormatWMF: Guid = Guid('{b96b3cad-0728-11d3-9d7b-0000f81ef32e}')
ImageFormatJPEG: Guid = Guid('{b96b3cae-0728-11d3-9d7b-0000f81ef32e}')
ImageFormatPNG: Guid = Guid('{b96b3caf-0728-11d3-9d7b-0000f81ef32e}')
ImageFormatGIF: Guid = Guid('{b96b3cb0-0728-11d3-9d7b-0000f81ef32e}')
ImageFormatTIFF: Guid = Guid('{b96b3cb1-0728-11d3-9d7b-0000f81ef32e}')
ImageFormatEXIF: Guid = Guid('{b96b3cb2-0728-11d3-9d7b-0000f81ef32e}')
ImageFormatIcon: Guid = Guid('{b96b3cb5-0728-11d3-9d7b-0000f81ef32e}')
ImageFormatHEIF: Guid = Guid('{b96b3cb6-0728-11d3-9d7b-0000f81ef32e}')
ImageFormatWEBP: Guid = Guid('{b96b3cb7-0728-11d3-9d7b-0000f81ef32e}')
FrameDimensionTime: Guid = Guid('{6aedbd6d-3fb5-418a-83a6-7f45229dc872}')
FrameDimensionResolution: Guid = Guid('{84236f7b-3bd3-428f-8dab-4ea1439ca315}')
FrameDimensionPage: Guid = Guid('{7462dc86-6180-4c7e-8e3f-ee7333a7a483}')
FormatIDImageInformation: Guid = Guid('{e5836cbe-5eef-4f1d-acde-ae4c43b608ce}')
FormatIDJpegAppHeaders: Guid = Guid('{1c4afdcd-6177-43cf-abc7-5f51af39ee85}')
EncoderCompression: Guid = Guid('{e09d739d-ccd4-44ee-8eba-3fbf8be4fc58}')
EncoderColorDepth: Guid = Guid('{66087055-ad66-4c7c-9a18-38a2310b8337}')
EncoderScanMethod: Guid = Guid('{3a4e2661-3109-4e56-8536-42c156e7dcfa}')
EncoderVersion: Guid = Guid('{24d18c76-814a-41a4-bf53-1c219cccf797}')
EncoderRenderMethod: Guid = Guid('{6d42c53a-229a-4825-8bb7-5c99e2b9a8b8}')
EncoderQuality: Guid = Guid('{1d5be4b5-fa4a-452d-9cdd-5db35105e7eb}')
EncoderTransformation: Guid = Guid('{8d0eb2d1-a58e-4ea8-aa14-108074b7b6f9}')
EncoderLuminanceTable: Guid = Guid('{edb33bce-0266-4a77-b904-27216099e717}')
EncoderChrominanceTable: Guid = Guid('{f2e455dc-09b3-4316-8260-676ada32481c}')
EncoderSaveFlag: Guid = Guid('{292266fc-ac40-47bf-8cfc-a85b89a655de}')
EncoderColorSpace: Guid = Guid('{ae7a62a0-ee2c-49d8-9d07-1ba8a927596e}')
EncoderImageItems: Guid = Guid('{63875e13-1f1d-45ab-9195-a29b6066a650}')
EncoderSaveAsCMYK: Guid = Guid('{a219bbc9-0a9d-4005-a3ee-3a421b8bb06c}')
CodecIImageBytes: Guid = Guid('{025d1823-6c7d-447b-bbdb-a3cbc3dfa2fc}')
PropertyTagTypeByte: UInt32 = 1
PropertyTagTypeASCII: UInt32 = 2
PropertyTagTypeShort: UInt32 = 3
PropertyTagTypeLong: UInt32 = 4
PropertyTagTypeRational: UInt32 = 5
PropertyTagTypeUndefined: UInt32 = 7
PropertyTagTypeSLONG: UInt32 = 9
PropertyTagTypeSRational: UInt32 = 10
PropertyTagExifIFD: UInt32 = 34665
PropertyTagGpsIFD: UInt32 = 34853
PropertyTagNewSubfileType: UInt32 = 254
PropertyTagSubfileType: UInt32 = 255
PropertyTagImageWidth: UInt32 = 256
PropertyTagImageHeight: UInt32 = 257
PropertyTagBitsPerSample: UInt32 = 258
PropertyTagCompression: UInt32 = 259
PropertyTagPhotometricInterp: UInt32 = 262
PropertyTagThreshHolding: UInt32 = 263
PropertyTagCellWidth: UInt32 = 264
PropertyTagCellHeight: UInt32 = 265
PropertyTagFillOrder: UInt32 = 266
PropertyTagDocumentName: UInt32 = 269
PropertyTagImageDescription: UInt32 = 270
PropertyTagEquipMake: UInt32 = 271
PropertyTagEquipModel: UInt32 = 272
PropertyTagStripOffsets: UInt32 = 273
PropertyTagOrientation: UInt32 = 274
PropertyTagSamplesPerPixel: UInt32 = 277
PropertyTagRowsPerStrip: UInt32 = 278
PropertyTagStripBytesCount: UInt32 = 279
PropertyTagMinSampleValue: UInt32 = 280
PropertyTagMaxSampleValue: UInt32 = 281
PropertyTagXResolution: UInt32 = 282
PropertyTagYResolution: UInt32 = 283
PropertyTagPlanarConfig: UInt32 = 284
PropertyTagPageName: UInt32 = 285
PropertyTagXPosition: UInt32 = 286
PropertyTagYPosition: UInt32 = 287
PropertyTagFreeOffset: UInt32 = 288
PropertyTagFreeByteCounts: UInt32 = 289
PropertyTagGrayResponseUnit: UInt32 = 290
PropertyTagGrayResponseCurve: UInt32 = 291
PropertyTagT4Option: UInt32 = 292
PropertyTagT6Option: UInt32 = 293
PropertyTagResolutionUnit: UInt32 = 296
PropertyTagPageNumber: UInt32 = 297
PropertyTagTransferFuncition: UInt32 = 301
PropertyTagSoftwareUsed: UInt32 = 305
PropertyTagDateTime: UInt32 = 306
PropertyTagArtist: UInt32 = 315
PropertyTagHostComputer: UInt32 = 316
PropertyTagPredictor: UInt32 = 317
PropertyTagWhitePoint: UInt32 = 318
PropertyTagPrimaryChromaticities: UInt32 = 319
PropertyTagColorMap: UInt32 = 320
PropertyTagHalftoneHints: UInt32 = 321
PropertyTagTileWidth: UInt32 = 322
PropertyTagTileLength: UInt32 = 323
PropertyTagTileOffset: UInt32 = 324
PropertyTagTileByteCounts: UInt32 = 325
PropertyTagInkSet: UInt32 = 332
PropertyTagInkNames: UInt32 = 333
PropertyTagNumberOfInks: UInt32 = 334
PropertyTagDotRange: UInt32 = 336
PropertyTagTargetPrinter: UInt32 = 337
PropertyTagExtraSamples: UInt32 = 338
PropertyTagSampleFormat: UInt32 = 339
PropertyTagSMinSampleValue: UInt32 = 340
PropertyTagSMaxSampleValue: UInt32 = 341
PropertyTagTransferRange: UInt32 = 342
PropertyTagJPEGProc: UInt32 = 512
PropertyTagJPEGInterFormat: UInt32 = 513
PropertyTagJPEGInterLength: UInt32 = 514
PropertyTagJPEGRestartInterval: UInt32 = 515
PropertyTagJPEGLosslessPredictors: UInt32 = 517
PropertyTagJPEGPointTransforms: UInt32 = 518
PropertyTagJPEGQTables: UInt32 = 519
PropertyTagJPEGDCTables: UInt32 = 520
PropertyTagJPEGACTables: UInt32 = 521
PropertyTagYCbCrCoefficients: UInt32 = 529
PropertyTagYCbCrSubsampling: UInt32 = 530
PropertyTagYCbCrPositioning: UInt32 = 531
PropertyTagREFBlackWhite: UInt32 = 532
PropertyTagICCProfile: UInt32 = 34675
PropertyTagGamma: UInt32 = 769
PropertyTagICCProfileDescriptor: UInt32 = 770
PropertyTagSRGBRenderingIntent: UInt32 = 771
PropertyTagImageTitle: UInt32 = 800
PropertyTagCopyright: UInt32 = 33432
PropertyTagResolutionXUnit: UInt32 = 20481
PropertyTagResolutionYUnit: UInt32 = 20482
PropertyTagResolutionXLengthUnit: UInt32 = 20483
PropertyTagResolutionYLengthUnit: UInt32 = 20484
PropertyTagPrintFlags: UInt32 = 20485
PropertyTagPrintFlagsVersion: UInt32 = 20486
PropertyTagPrintFlagsCrop: UInt32 = 20487
PropertyTagPrintFlagsBleedWidth: UInt32 = 20488
PropertyTagPrintFlagsBleedWidthScale: UInt32 = 20489
PropertyTagHalftoneLPI: UInt32 = 20490
PropertyTagHalftoneLPIUnit: UInt32 = 20491
PropertyTagHalftoneDegree: UInt32 = 20492
PropertyTagHalftoneShape: UInt32 = 20493
PropertyTagHalftoneMisc: UInt32 = 20494
PropertyTagHalftoneScreen: UInt32 = 20495
PropertyTagJPEGQuality: UInt32 = 20496
PropertyTagGridSize: UInt32 = 20497
PropertyTagThumbnailFormat: UInt32 = 20498
PropertyTagThumbnailWidth: UInt32 = 20499
PropertyTagThumbnailHeight: UInt32 = 20500
PropertyTagThumbnailColorDepth: UInt32 = 20501
PropertyTagThumbnailPlanes: UInt32 = 20502
PropertyTagThumbnailRawBytes: UInt32 = 20503
PropertyTagThumbnailSize: UInt32 = 20504
PropertyTagThumbnailCompressedSize: UInt32 = 20505
PropertyTagColorTransferFunction: UInt32 = 20506
PropertyTagThumbnailData: UInt32 = 20507
PropertyTagThumbnailImageWidth: UInt32 = 20512
PropertyTagThumbnailImageHeight: UInt32 = 20513
PropertyTagThumbnailBitsPerSample: UInt32 = 20514
PropertyTagThumbnailCompression: UInt32 = 20515
PropertyTagThumbnailPhotometricInterp: UInt32 = 20516
PropertyTagThumbnailImageDescription: UInt32 = 20517
PropertyTagThumbnailEquipMake: UInt32 = 20518
PropertyTagThumbnailEquipModel: UInt32 = 20519
PropertyTagThumbnailStripOffsets: UInt32 = 20520
PropertyTagThumbnailOrientation: UInt32 = 20521
PropertyTagThumbnailSamplesPerPixel: UInt32 = 20522
PropertyTagThumbnailRowsPerStrip: UInt32 = 20523
PropertyTagThumbnailStripBytesCount: UInt32 = 20524
PropertyTagThumbnailResolutionX: UInt32 = 20525
PropertyTagThumbnailResolutionY: UInt32 = 20526
PropertyTagThumbnailPlanarConfig: UInt32 = 20527
PropertyTagThumbnailResolutionUnit: UInt32 = 20528
PropertyTagThumbnailTransferFunction: UInt32 = 20529
PropertyTagThumbnailSoftwareUsed: UInt32 = 20530
PropertyTagThumbnailDateTime: UInt32 = 20531
PropertyTagThumbnailArtist: UInt32 = 20532
PropertyTagThumbnailWhitePoint: UInt32 = 20533
PropertyTagThumbnailPrimaryChromaticities: UInt32 = 20534
PropertyTagThumbnailYCbCrCoefficients: UInt32 = 20535
PropertyTagThumbnailYCbCrSubsampling: UInt32 = 20536
PropertyTagThumbnailYCbCrPositioning: UInt32 = 20537
PropertyTagThumbnailRefBlackWhite: UInt32 = 20538
PropertyTagThumbnailCopyRight: UInt32 = 20539
PropertyTagLuminanceTable: UInt32 = 20624
PropertyTagChrominanceTable: UInt32 = 20625
PropertyTagFrameDelay: UInt32 = 20736
PropertyTagLoopCount: UInt32 = 20737
PropertyTagGlobalPalette: UInt32 = 20738
PropertyTagIndexBackground: UInt32 = 20739
PropertyTagIndexTransparent: UInt32 = 20740
PropertyTagPixelUnit: UInt32 = 20752
PropertyTagPixelPerUnitX: UInt32 = 20753
PropertyTagPixelPerUnitY: UInt32 = 20754
PropertyTagPaletteHistogram: UInt32 = 20755
PropertyTagExifExposureTime: UInt32 = 33434
PropertyTagExifFNumber: UInt32 = 33437
PropertyTagExifExposureProg: UInt32 = 34850
PropertyTagExifSpectralSense: UInt32 = 34852
PropertyTagExifISOSpeed: UInt32 = 34855
PropertyTagExifOECF: UInt32 = 34856
PropertyTagExifVer: UInt32 = 36864
PropertyTagExifDTOrig: UInt32 = 36867
PropertyTagExifDTDigitized: UInt32 = 36868
PropertyTagExifCompConfig: UInt32 = 37121
PropertyTagExifCompBPP: UInt32 = 37122
PropertyTagExifShutterSpeed: UInt32 = 37377
PropertyTagExifAperture: UInt32 = 37378
PropertyTagExifBrightness: UInt32 = 37379
PropertyTagExifExposureBias: UInt32 = 37380
PropertyTagExifMaxAperture: UInt32 = 37381
PropertyTagExifSubjectDist: UInt32 = 37382
PropertyTagExifMeteringMode: UInt32 = 37383
PropertyTagExifLightSource: UInt32 = 37384
PropertyTagExifFlash: UInt32 = 37385
PropertyTagExifFocalLength: UInt32 = 37386
PropertyTagExifSubjectArea: UInt32 = 37396
PropertyTagExifMakerNote: UInt32 = 37500
PropertyTagExifUserComment: UInt32 = 37510
PropertyTagExifDTSubsec: UInt32 = 37520
PropertyTagExifDTOrigSS: UInt32 = 37521
PropertyTagExifDTDigSS: UInt32 = 37522
PropertyTagExifFPXVer: UInt32 = 40960
PropertyTagExifColorSpace: UInt32 = 40961
PropertyTagExifPixXDim: UInt32 = 40962
PropertyTagExifPixYDim: UInt32 = 40963
PropertyTagExifRelatedWav: UInt32 = 40964
PropertyTagExifInterop: UInt32 = 40965
PropertyTagExifFlashEnergy: UInt32 = 41483
PropertyTagExifSpatialFR: UInt32 = 41484
PropertyTagExifFocalXRes: UInt32 = 41486
PropertyTagExifFocalYRes: UInt32 = 41487
PropertyTagExifFocalResUnit: UInt32 = 41488
PropertyTagExifSubjectLoc: UInt32 = 41492
PropertyTagExifExposureIndex: UInt32 = 41493
PropertyTagExifSensingMethod: UInt32 = 41495
PropertyTagExifFileSource: UInt32 = 41728
PropertyTagExifSceneType: UInt32 = 41729
PropertyTagExifCfaPattern: UInt32 = 41730
PropertyTagExifCustomRendered: UInt32 = 41985
PropertyTagExifExposureMode: UInt32 = 41986
PropertyTagExifWhiteBalance: UInt32 = 41987
PropertyTagExifDigitalZoomRatio: UInt32 = 41988
PropertyTagExifFocalLengthIn35mmFilm: UInt32 = 41989
PropertyTagExifSceneCaptureType: UInt32 = 41990
PropertyTagExifGainControl: UInt32 = 41991
PropertyTagExifContrast: UInt32 = 41992
PropertyTagExifSaturation: UInt32 = 41993
PropertyTagExifSharpness: UInt32 = 41994
PropertyTagExifDeviceSettingDesc: UInt32 = 41995
PropertyTagExifSubjectDistanceRange: UInt32 = 41996
PropertyTagExifUniqueImageID: UInt32 = 42016
PropertyTagGpsVer: UInt32 = 0
PropertyTagGpsLatitudeRef: UInt32 = 1
PropertyTagGpsLatitude: UInt32 = 2
PropertyTagGpsLongitudeRef: UInt32 = 3
PropertyTagGpsLongitude: UInt32 = 4
PropertyTagGpsAltitudeRef: UInt32 = 5
PropertyTagGpsAltitude: UInt32 = 6
PropertyTagGpsGpsTime: UInt32 = 7
PropertyTagGpsGpsSatellites: UInt32 = 8
PropertyTagGpsGpsStatus: UInt32 = 9
PropertyTagGpsGpsMeasureMode: UInt32 = 10
PropertyTagGpsGpsDop: UInt32 = 11
PropertyTagGpsSpeedRef: UInt32 = 12
PropertyTagGpsSpeed: UInt32 = 13
PropertyTagGpsTrackRef: UInt32 = 14
PropertyTagGpsTrack: UInt32 = 15
PropertyTagGpsImgDirRef: UInt32 = 16
PropertyTagGpsImgDir: UInt32 = 17
PropertyTagGpsMapDatum: UInt32 = 18
PropertyTagGpsDestLatRef: UInt32 = 19
PropertyTagGpsDestLat: UInt32 = 20
PropertyTagGpsDestLongRef: UInt32 = 21
PropertyTagGpsDestLong: UInt32 = 22
PropertyTagGpsDestBearRef: UInt32 = 23
PropertyTagGpsDestBear: UInt32 = 24
PropertyTagGpsDestDistRef: UInt32 = 25
PropertyTagGpsDestDist: UInt32 = 26
PropertyTagGpsProcessingMethod: UInt32 = 27
PropertyTagGpsAreaInformation: UInt32 = 28
PropertyTagGpsDate: UInt32 = 29
PropertyTagGpsDifferential: UInt32 = 30
GDIP_EMFPLUSFLAGS_DISPLAY: UInt32 = 1
ALPHA_SHIFT: UInt32 = 24
RED_SHIFT: UInt32 = 16
GREEN_SHIFT: UInt32 = 8
BLUE_SHIFT: UInt32 = 0
PixelFormatIndexed: UInt32 = 65536
PixelFormatGDI: UInt32 = 131072
PixelFormatAlpha: UInt32 = 262144
PixelFormatPAlpha: UInt32 = 524288
PixelFormatExtended: UInt32 = 1048576
PixelFormatCanonical: UInt32 = 2097152
PixelFormatUndefined: UInt32 = 0
PixelFormatDontCare: UInt32 = 0
PixelFormatMax: UInt32 = 16
FlatnessDefault: Single = 0.25
BlurEffectGuid: Guid = Guid('{633c80a4-1843-482b-9ef2-be2834c5fdd4}')
SharpenEffectGuid: Guid = Guid('{63cbf3ee-c526-402c-8f71-62c540bf5142}')
ColorMatrixEffectGuid: Guid = Guid('{718f2615-7933-40e3-a511-5f68fe14dd74}')
ColorLUTEffectGuid: Guid = Guid('{a7ce72a9-0f7f-40d7-b3cc-d0c02d5c3212}')
BrightnessContrastEffectGuid: Guid = Guid('{d3a1dbe1-8ec4-4c17-9f4c-ea97ad1c343d}')
HueSaturationLightnessEffectGuid: Guid = Guid('{8b2dd6c3-eb07-4d87-a5f0-7108e26a9c5f}')
LevelsEffectGuid: Guid = Guid('{99c354ec-2a31-4f3a-8c34-17a803b33a25}')
TintEffectGuid: Guid = Guid('{1077af00-2848-4441-9489-44ad4c2d7a2c}')
ColorBalanceEffectGuid: Guid = Guid('{537e597d-251e-48da-9664-29ca496b70f8}')
RedEyeCorrectionEffectGuid: Guid = Guid('{74d29d05-69a4-4266-9549-3cc52836b632}')
ColorCurveEffectGuid: Guid = Guid('{dd6a0022-58e4-4a67-9d9b-d48eb881a53d}')
@winfunctype('gdiplus.dll')
def GdipAlloc(size: UIntPtr) -> VoidPtr: ...
@winfunctype('gdiplus.dll')
def GdipFree(ptr: VoidPtr) -> Void: ...
@winfunctype('gdiplus.dll')
def GdiplusStartup(token: POINTER(UIntPtr), input: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GdiplusStartupInput), output: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GdiplusStartupOutput)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdiplusShutdown(token: UIntPtr) -> Void: ...
@winfunctype('gdiplus.dll')
def GdipCreateEffect(guid: Guid, effect: POINTER(POINTER(win32more.Windows.Win32.Graphics.GdiPlus.CGpEffect))) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipDeleteEffect(effect: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.CGpEffect)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipGetEffectParameterSize(effect: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.CGpEffect), size: POINTER(UInt32)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipSetEffectParameters(effect: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.CGpEffect), params: VoidPtr, size: UInt32) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipGetEffectParameters(effect: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.CGpEffect), size: POINTER(UInt32), params: VoidPtr) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipCreatePath(brushMode: win32more.Windows.Win32.Graphics.GdiPlus.FillMode, path: POINTER(POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPath))) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipCreatePath2(param0: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.PointF), param1: POINTER(Byte), param2: Int32, param3: win32more.Windows.Win32.Graphics.GdiPlus.FillMode, path: POINTER(POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPath))) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipCreatePath2I(param0: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.Point), param1: POINTER(Byte), param2: Int32, param3: win32more.Windows.Win32.Graphics.GdiPlus.FillMode, path: POINTER(POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPath))) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipClonePath(path: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPath), clonePath: POINTER(POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPath))) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipDeletePath(path: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPath)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipResetPath(path: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPath)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipGetPointCount(path: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPath), count: POINTER(Int32)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipGetPathTypes(path: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPath), types: POINTER(Byte), count: Int32) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipGetPathPoints(param0: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPath), points: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.PointF), count: Int32) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipGetPathPointsI(param0: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPath), points: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.Point), count: Int32) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipGetPathFillMode(path: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPath), fillmode: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.FillMode)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipSetPathFillMode(path: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPath), fillmode: win32more.Windows.Win32.Graphics.GdiPlus.FillMode) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipGetPathData(path: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPath), pathData: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.PathData)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipStartPathFigure(path: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPath)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipClosePathFigure(path: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPath)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipClosePathFigures(path: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPath)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipSetPathMarker(path: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPath)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipClearPathMarkers(path: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPath)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipReversePath(path: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPath)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipGetPathLastPoint(path: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPath), lastPoint: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.PointF)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipAddPathLine(path: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPath), x1: Single, y1: Single, x2: Single, y2: Single) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipAddPathLine2(path: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPath), points: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.PointF), count: Int32) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipAddPathArc(path: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPath), x: Single, y: Single, width: Single, height: Single, startAngle: Single, sweepAngle: Single) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipAddPathBezier(path: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPath), x1: Single, y1: Single, x2: Single, y2: Single, x3: Single, y3: Single, x4: Single, y4: Single) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipAddPathBeziers(path: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPath), points: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.PointF), count: Int32) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipAddPathCurve(path: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPath), points: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.PointF), count: Int32) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipAddPathCurve2(path: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPath), points: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.PointF), count: Int32, tension: Single) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipAddPathCurve3(path: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPath), points: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.PointF), count: Int32, offset: Int32, numberOfSegments: Int32, tension: Single) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipAddPathClosedCurve(path: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPath), points: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.PointF), count: Int32) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipAddPathClosedCurve2(path: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPath), points: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.PointF), count: Int32, tension: Single) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipAddPathRectangle(path: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPath), x: Single, y: Single, width: Single, height: Single) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipAddPathRectangles(path: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPath), rects: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.RectF), count: Int32) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipAddPathEllipse(path: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPath), x: Single, y: Single, width: Single, height: Single) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipAddPathPie(path: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPath), x: Single, y: Single, width: Single, height: Single, startAngle: Single, sweepAngle: Single) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipAddPathPolygon(path: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPath), points: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.PointF), count: Int32) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipAddPathPath(path: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPath), addingPath: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPath), connect: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipAddPathString(path: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPath), string: win32more.Windows.Win32.Foundation.PWSTR, length: Int32, family: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpFontFamily), style: Int32, emSize: Single, layoutRect: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.RectF), format: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpStringFormat)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipAddPathStringI(path: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPath), string: win32more.Windows.Win32.Foundation.PWSTR, length: Int32, family: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpFontFamily), style: Int32, emSize: Single, layoutRect: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.Rect), format: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpStringFormat)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipAddPathLineI(path: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPath), x1: Int32, y1: Int32, x2: Int32, y2: Int32) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipAddPathLine2I(path: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPath), points: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.Point), count: Int32) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipAddPathArcI(path: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPath), x: Int32, y: Int32, width: Int32, height: Int32, startAngle: Single, sweepAngle: Single) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipAddPathBezierI(path: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPath), x1: Int32, y1: Int32, x2: Int32, y2: Int32, x3: Int32, y3: Int32, x4: Int32, y4: Int32) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipAddPathBeziersI(path: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPath), points: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.Point), count: Int32) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipAddPathCurveI(path: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPath), points: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.Point), count: Int32) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipAddPathCurve2I(path: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPath), points: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.Point), count: Int32, tension: Single) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipAddPathCurve3I(path: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPath), points: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.Point), count: Int32, offset: Int32, numberOfSegments: Int32, tension: Single) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipAddPathClosedCurveI(path: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPath), points: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.Point), count: Int32) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipAddPathClosedCurve2I(path: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPath), points: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.Point), count: Int32, tension: Single) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipAddPathRectangleI(path: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPath), x: Int32, y: Int32, width: Int32, height: Int32) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipAddPathRectanglesI(path: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPath), rects: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.Rect), count: Int32) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipAddPathEllipseI(path: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPath), x: Int32, y: Int32, width: Int32, height: Int32) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipAddPathPieI(path: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPath), x: Int32, y: Int32, width: Int32, height: Int32, startAngle: Single, sweepAngle: Single) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipAddPathPolygonI(path: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPath), points: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.Point), count: Int32) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipFlattenPath(path: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPath), matrix: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.Matrix), flatness: Single) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipWindingModeOutline(path: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPath), matrix: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.Matrix), flatness: Single) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipWidenPath(nativePath: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPath), pen: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPen), matrix: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.Matrix), flatness: Single) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipWarpPath(path: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPath), matrix: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.Matrix), points: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.PointF), count: Int32, srcx: Single, srcy: Single, srcwidth: Single, srcheight: Single, warpMode: win32more.Windows.Win32.Graphics.GdiPlus.WarpMode, flatness: Single) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipTransformPath(path: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPath), matrix: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.Matrix)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipGetPathWorldBounds(path: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPath), bounds: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.RectF), matrix: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.Matrix), pen: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPen)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipGetPathWorldBoundsI(path: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPath), bounds: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.Rect), matrix: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.Matrix), pen: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPen)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipIsVisiblePathPoint(path: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPath), x: Single, y: Single, graphics: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics), result: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipIsVisiblePathPointI(path: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPath), x: Int32, y: Int32, graphics: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics), result: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipIsOutlineVisiblePathPoint(path: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPath), x: Single, y: Single, pen: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPen), graphics: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics), result: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipIsOutlineVisiblePathPointI(path: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPath), x: Int32, y: Int32, pen: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPen), graphics: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics), result: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipCreatePathIter(iterator: POINTER(POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPathIterator)), path: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPath)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipDeletePathIter(iterator: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPathIterator)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipPathIterNextSubpath(iterator: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPathIterator), resultCount: POINTER(Int32), startIndex: POINTER(Int32), endIndex: POINTER(Int32), isClosed: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipPathIterNextSubpathPath(iterator: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPathIterator), resultCount: POINTER(Int32), path: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPath), isClosed: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipPathIterNextPathType(iterator: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPathIterator), resultCount: POINTER(Int32), pathType: POINTER(Byte), startIndex: POINTER(Int32), endIndex: POINTER(Int32)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipPathIterNextMarker(iterator: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPathIterator), resultCount: POINTER(Int32), startIndex: POINTER(Int32), endIndex: POINTER(Int32)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipPathIterNextMarkerPath(iterator: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPathIterator), resultCount: POINTER(Int32), path: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPath)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipPathIterGetCount(iterator: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPathIterator), count: POINTER(Int32)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipPathIterGetSubpathCount(iterator: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPathIterator), count: POINTER(Int32)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipPathIterIsValid(iterator: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPathIterator), valid: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipPathIterHasCurve(iterator: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPathIterator), hasCurve: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipPathIterRewind(iterator: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPathIterator)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipPathIterEnumerate(iterator: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPathIterator), resultCount: POINTER(Int32), points: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.PointF), types: POINTER(Byte), count: Int32) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipPathIterCopyData(iterator: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPathIterator), resultCount: POINTER(Int32), points: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.PointF), types: POINTER(Byte), startIndex: Int32, endIndex: Int32) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipCreateMatrix(matrix: POINTER(POINTER(win32more.Windows.Win32.Graphics.GdiPlus.Matrix))) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipCreateMatrix2(m11: Single, m12: Single, m21: Single, m22: Single, dx: Single, dy: Single, matrix: POINTER(POINTER(win32more.Windows.Win32.Graphics.GdiPlus.Matrix))) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipCreateMatrix3(rect: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.RectF), dstplg: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.PointF), matrix: POINTER(POINTER(win32more.Windows.Win32.Graphics.GdiPlus.Matrix))) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipCreateMatrix3I(rect: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.Rect), dstplg: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.Point), matrix: POINTER(POINTER(win32more.Windows.Win32.Graphics.GdiPlus.Matrix))) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipCloneMatrix(matrix: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.Matrix), cloneMatrix: POINTER(POINTER(win32more.Windows.Win32.Graphics.GdiPlus.Matrix))) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipDeleteMatrix(matrix: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.Matrix)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipSetMatrixElements(matrix: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.Matrix), m11: Single, m12: Single, m21: Single, m22: Single, dx: Single, dy: Single) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipMultiplyMatrix(matrix: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.Matrix), matrix2: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.Matrix), order: win32more.Windows.Win32.Graphics.GdiPlus.MatrixOrder) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipTranslateMatrix(matrix: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.Matrix), offsetX: Single, offsetY: Single, order: win32more.Windows.Win32.Graphics.GdiPlus.MatrixOrder) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipScaleMatrix(matrix: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.Matrix), scaleX: Single, scaleY: Single, order: win32more.Windows.Win32.Graphics.GdiPlus.MatrixOrder) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipRotateMatrix(matrix: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.Matrix), angle: Single, order: win32more.Windows.Win32.Graphics.GdiPlus.MatrixOrder) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipShearMatrix(matrix: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.Matrix), shearX: Single, shearY: Single, order: win32more.Windows.Win32.Graphics.GdiPlus.MatrixOrder) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipInvertMatrix(matrix: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.Matrix)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipTransformMatrixPoints(matrix: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.Matrix), pts: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.PointF), count: Int32) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipTransformMatrixPointsI(matrix: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.Matrix), pts: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.Point), count: Int32) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipVectorTransformMatrixPoints(matrix: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.Matrix), pts: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.PointF), count: Int32) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipVectorTransformMatrixPointsI(matrix: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.Matrix), pts: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.Point), count: Int32) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipGetMatrixElements(matrix: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.Matrix), matrixOut: POINTER(Single)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipIsMatrixInvertible(matrix: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.Matrix), result: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipIsMatrixIdentity(matrix: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.Matrix), result: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipIsMatrixEqual(matrix: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.Matrix), matrix2: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.Matrix), result: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipCreateRegion(region: POINTER(POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpRegion))) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipCreateRegionRect(rect: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.RectF), region: POINTER(POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpRegion))) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipCreateRegionRectI(rect: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.Rect), region: POINTER(POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpRegion))) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipCreateRegionPath(path: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPath), region: POINTER(POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpRegion))) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipCreateRegionRgnData(regionData: POINTER(Byte), size: Int32, region: POINTER(POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpRegion))) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipCreateRegionHrgn(hRgn: win32more.Windows.Win32.Graphics.Gdi.HRGN, region: POINTER(POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpRegion))) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipCloneRegion(region: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpRegion), cloneRegion: POINTER(POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpRegion))) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipDeleteRegion(region: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpRegion)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipSetInfinite(region: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpRegion)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipSetEmpty(region: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpRegion)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipCombineRegionRect(region: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpRegion), rect: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.RectF), combineMode: win32more.Windows.Win32.Graphics.GdiPlus.CombineMode) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipCombineRegionRectI(region: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpRegion), rect: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.Rect), combineMode: win32more.Windows.Win32.Graphics.GdiPlus.CombineMode) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipCombineRegionPath(region: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpRegion), path: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPath), combineMode: win32more.Windows.Win32.Graphics.GdiPlus.CombineMode) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipCombineRegionRegion(region: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpRegion), region2: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpRegion), combineMode: win32more.Windows.Win32.Graphics.GdiPlus.CombineMode) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipTranslateRegion(region: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpRegion), dx: Single, dy: Single) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipTranslateRegionI(region: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpRegion), dx: Int32, dy: Int32) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipTransformRegion(region: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpRegion), matrix: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.Matrix)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipGetRegionBounds(region: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpRegion), graphics: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics), rect: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.RectF)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipGetRegionBoundsI(region: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpRegion), graphics: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics), rect: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.Rect)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipGetRegionHRgn(region: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpRegion), graphics: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics), hRgn: POINTER(win32more.Windows.Win32.Graphics.Gdi.HRGN)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipIsEmptyRegion(region: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpRegion), graphics: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics), result: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipIsInfiniteRegion(region: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpRegion), graphics: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics), result: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipIsEqualRegion(region: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpRegion), region2: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpRegion), graphics: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics), result: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipGetRegionDataSize(region: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpRegion), bufferSize: POINTER(UInt32)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipGetRegionData(region: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpRegion), buffer: POINTER(Byte), bufferSize: UInt32, sizeFilled: POINTER(UInt32)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipIsVisibleRegionPoint(region: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpRegion), x: Single, y: Single, graphics: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics), result: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipIsVisibleRegionPointI(region: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpRegion), x: Int32, y: Int32, graphics: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics), result: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipIsVisibleRegionRect(region: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpRegion), x: Single, y: Single, width: Single, height: Single, graphics: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics), result: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipIsVisibleRegionRectI(region: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpRegion), x: Int32, y: Int32, width: Int32, height: Int32, graphics: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics), result: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipGetRegionScansCount(region: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpRegion), count: POINTER(UInt32), matrix: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.Matrix)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipGetRegionScans(region: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpRegion), rects: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.RectF), count: POINTER(Int32), matrix: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.Matrix)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipGetRegionScansI(region: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpRegion), rects: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.Rect), count: POINTER(Int32), matrix: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.Matrix)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipCloneBrush(brush: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpBrush), cloneBrush: POINTER(POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpBrush))) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipDeleteBrush(brush: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpBrush)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipGetBrushType(brush: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpBrush), type: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.BrushType)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipCreateHatchBrush(hatchstyle: win32more.Windows.Win32.Graphics.GdiPlus.HatchStyle, forecol: UInt32, backcol: UInt32, brush: POINTER(POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpHatch))) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipGetHatchStyle(brush: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpHatch), hatchstyle: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.HatchStyle)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipGetHatchForegroundColor(brush: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpHatch), forecol: POINTER(UInt32)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipGetHatchBackgroundColor(brush: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpHatch), backcol: POINTER(UInt32)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipCreateTexture(image: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpImage), wrapmode: win32more.Windows.Win32.Graphics.GdiPlus.WrapMode, texture: POINTER(POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpTexture))) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipCreateTexture2(image: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpImage), wrapmode: win32more.Windows.Win32.Graphics.GdiPlus.WrapMode, x: Single, y: Single, width: Single, height: Single, texture: POINTER(POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpTexture))) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipCreateTextureIA(image: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpImage), imageAttributes: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpImageAttributes), x: Single, y: Single, width: Single, height: Single, texture: POINTER(POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpTexture))) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipCreateTexture2I(image: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpImage), wrapmode: win32more.Windows.Win32.Graphics.GdiPlus.WrapMode, x: Int32, y: Int32, width: Int32, height: Int32, texture: POINTER(POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpTexture))) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipCreateTextureIAI(image: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpImage), imageAttributes: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpImageAttributes), x: Int32, y: Int32, width: Int32, height: Int32, texture: POINTER(POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpTexture))) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipGetTextureTransform(brush: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpTexture), matrix: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.Matrix)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipSetTextureTransform(brush: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpTexture), matrix: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.Matrix)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipResetTextureTransform(brush: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpTexture)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipMultiplyTextureTransform(brush: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpTexture), matrix: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.Matrix), order: win32more.Windows.Win32.Graphics.GdiPlus.MatrixOrder) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipTranslateTextureTransform(brush: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpTexture), dx: Single, dy: Single, order: win32more.Windows.Win32.Graphics.GdiPlus.MatrixOrder) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipScaleTextureTransform(brush: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpTexture), sx: Single, sy: Single, order: win32more.Windows.Win32.Graphics.GdiPlus.MatrixOrder) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipRotateTextureTransform(brush: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpTexture), angle: Single, order: win32more.Windows.Win32.Graphics.GdiPlus.MatrixOrder) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipSetTextureWrapMode(brush: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpTexture), wrapmode: win32more.Windows.Win32.Graphics.GdiPlus.WrapMode) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipGetTextureWrapMode(brush: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpTexture), wrapmode: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.WrapMode)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipGetTextureImage(brush: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpTexture), image: POINTER(POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpImage))) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipCreateSolidFill(color: UInt32, brush: POINTER(POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpSolidFill))) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipSetSolidFillColor(brush: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpSolidFill), color: UInt32) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipGetSolidFillColor(brush: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpSolidFill), color: POINTER(UInt32)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipCreateLineBrush(point1: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.PointF), point2: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.PointF), color1: UInt32, color2: UInt32, wrapMode: win32more.Windows.Win32.Graphics.GdiPlus.WrapMode, lineGradient: POINTER(POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpLineGradient))) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipCreateLineBrushI(point1: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.Point), point2: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.Point), color1: UInt32, color2: UInt32, wrapMode: win32more.Windows.Win32.Graphics.GdiPlus.WrapMode, lineGradient: POINTER(POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpLineGradient))) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipCreateLineBrushFromRect(rect: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.RectF), color1: UInt32, color2: UInt32, mode: win32more.Windows.Win32.Graphics.GdiPlus.LinearGradientMode, wrapMode: win32more.Windows.Win32.Graphics.GdiPlus.WrapMode, lineGradient: POINTER(POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpLineGradient))) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipCreateLineBrushFromRectI(rect: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.Rect), color1: UInt32, color2: UInt32, mode: win32more.Windows.Win32.Graphics.GdiPlus.LinearGradientMode, wrapMode: win32more.Windows.Win32.Graphics.GdiPlus.WrapMode, lineGradient: POINTER(POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpLineGradient))) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipCreateLineBrushFromRectWithAngle(rect: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.RectF), color1: UInt32, color2: UInt32, angle: Single, isAngleScalable: win32more.Windows.Win32.Foundation.BOOL, wrapMode: win32more.Windows.Win32.Graphics.GdiPlus.WrapMode, lineGradient: POINTER(POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpLineGradient))) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipCreateLineBrushFromRectWithAngleI(rect: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.Rect), color1: UInt32, color2: UInt32, angle: Single, isAngleScalable: win32more.Windows.Win32.Foundation.BOOL, wrapMode: win32more.Windows.Win32.Graphics.GdiPlus.WrapMode, lineGradient: POINTER(POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpLineGradient))) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipSetLineColors(brush: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpLineGradient), color1: UInt32, color2: UInt32) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipGetLineColors(brush: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpLineGradient), colors: POINTER(UInt32)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipGetLineRect(brush: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpLineGradient), rect: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.RectF)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipGetLineRectI(brush: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpLineGradient), rect: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.Rect)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipSetLineGammaCorrection(brush: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpLineGradient), useGammaCorrection: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipGetLineGammaCorrection(brush: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpLineGradient), useGammaCorrection: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipGetLineBlendCount(brush: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpLineGradient), count: POINTER(Int32)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipGetLineBlend(brush: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpLineGradient), blend: POINTER(Single), positions: POINTER(Single), count: Int32) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipSetLineBlend(brush: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpLineGradient), blend: POINTER(Single), positions: POINTER(Single), count: Int32) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipGetLinePresetBlendCount(brush: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpLineGradient), count: POINTER(Int32)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipGetLinePresetBlend(brush: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpLineGradient), blend: POINTER(UInt32), positions: POINTER(Single), count: Int32) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipSetLinePresetBlend(brush: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpLineGradient), blend: POINTER(UInt32), positions: POINTER(Single), count: Int32) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipSetLineSigmaBlend(brush: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpLineGradient), focus: Single, scale: Single) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipSetLineLinearBlend(brush: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpLineGradient), focus: Single, scale: Single) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipSetLineWrapMode(brush: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpLineGradient), wrapmode: win32more.Windows.Win32.Graphics.GdiPlus.WrapMode) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipGetLineWrapMode(brush: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpLineGradient), wrapmode: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.WrapMode)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipGetLineTransform(brush: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpLineGradient), matrix: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.Matrix)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipSetLineTransform(brush: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpLineGradient), matrix: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.Matrix)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipResetLineTransform(brush: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpLineGradient)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipMultiplyLineTransform(brush: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpLineGradient), matrix: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.Matrix), order: win32more.Windows.Win32.Graphics.GdiPlus.MatrixOrder) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipTranslateLineTransform(brush: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpLineGradient), dx: Single, dy: Single, order: win32more.Windows.Win32.Graphics.GdiPlus.MatrixOrder) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipScaleLineTransform(brush: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpLineGradient), sx: Single, sy: Single, order: win32more.Windows.Win32.Graphics.GdiPlus.MatrixOrder) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipRotateLineTransform(brush: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpLineGradient), angle: Single, order: win32more.Windows.Win32.Graphics.GdiPlus.MatrixOrder) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipCreatePathGradient(points: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.PointF), count: Int32, wrapMode: win32more.Windows.Win32.Graphics.GdiPlus.WrapMode, polyGradient: POINTER(POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPathGradient))) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipCreatePathGradientI(points: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.Point), count: Int32, wrapMode: win32more.Windows.Win32.Graphics.GdiPlus.WrapMode, polyGradient: POINTER(POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPathGradient))) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipCreatePathGradientFromPath(path: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPath), polyGradient: POINTER(POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPathGradient))) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipGetPathGradientCenterColor(brush: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPathGradient), colors: POINTER(UInt32)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipSetPathGradientCenterColor(brush: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPathGradient), colors: UInt32) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipGetPathGradientSurroundColorsWithCount(brush: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPathGradient), color: POINTER(UInt32), count: POINTER(Int32)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipSetPathGradientSurroundColorsWithCount(brush: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPathGradient), color: POINTER(UInt32), count: POINTER(Int32)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipGetPathGradientPath(brush: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPathGradient), path: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPath)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipSetPathGradientPath(brush: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPathGradient), path: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPath)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipGetPathGradientCenterPoint(brush: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPathGradient), points: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.PointF)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipGetPathGradientCenterPointI(brush: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPathGradient), points: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.Point)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipSetPathGradientCenterPoint(brush: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPathGradient), points: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.PointF)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipSetPathGradientCenterPointI(brush: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPathGradient), points: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.Point)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipGetPathGradientRect(brush: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPathGradient), rect: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.RectF)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipGetPathGradientRectI(brush: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPathGradient), rect: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.Rect)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipGetPathGradientPointCount(brush: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPathGradient), count: POINTER(Int32)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipGetPathGradientSurroundColorCount(brush: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPathGradient), count: POINTER(Int32)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipSetPathGradientGammaCorrection(brush: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPathGradient), useGammaCorrection: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipGetPathGradientGammaCorrection(brush: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPathGradient), useGammaCorrection: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipGetPathGradientBlendCount(brush: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPathGradient), count: POINTER(Int32)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipGetPathGradientBlend(brush: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPathGradient), blend: POINTER(Single), positions: POINTER(Single), count: Int32) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipSetPathGradientBlend(brush: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPathGradient), blend: POINTER(Single), positions: POINTER(Single), count: Int32) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipGetPathGradientPresetBlendCount(brush: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPathGradient), count: POINTER(Int32)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipGetPathGradientPresetBlend(brush: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPathGradient), blend: POINTER(UInt32), positions: POINTER(Single), count: Int32) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipSetPathGradientPresetBlend(brush: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPathGradient), blend: POINTER(UInt32), positions: POINTER(Single), count: Int32) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipSetPathGradientSigmaBlend(brush: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPathGradient), focus: Single, scale: Single) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipSetPathGradientLinearBlend(brush: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPathGradient), focus: Single, scale: Single) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipGetPathGradientWrapMode(brush: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPathGradient), wrapmode: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.WrapMode)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipSetPathGradientWrapMode(brush: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPathGradient), wrapmode: win32more.Windows.Win32.Graphics.GdiPlus.WrapMode) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipGetPathGradientTransform(brush: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPathGradient), matrix: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.Matrix)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipSetPathGradientTransform(brush: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPathGradient), matrix: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.Matrix)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipResetPathGradientTransform(brush: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPathGradient)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipMultiplyPathGradientTransform(brush: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPathGradient), matrix: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.Matrix), order: win32more.Windows.Win32.Graphics.GdiPlus.MatrixOrder) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipTranslatePathGradientTransform(brush: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPathGradient), dx: Single, dy: Single, order: win32more.Windows.Win32.Graphics.GdiPlus.MatrixOrder) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipScalePathGradientTransform(brush: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPathGradient), sx: Single, sy: Single, order: win32more.Windows.Win32.Graphics.GdiPlus.MatrixOrder) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipRotatePathGradientTransform(brush: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPathGradient), angle: Single, order: win32more.Windows.Win32.Graphics.GdiPlus.MatrixOrder) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipGetPathGradientFocusScales(brush: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPathGradient), xScale: POINTER(Single), yScale: POINTER(Single)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipSetPathGradientFocusScales(brush: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPathGradient), xScale: Single, yScale: Single) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipCreatePen1(color: UInt32, width: Single, unit: win32more.Windows.Win32.Graphics.GdiPlus.Unit, pen: POINTER(POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPen))) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipCreatePen2(brush: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpBrush), width: Single, unit: win32more.Windows.Win32.Graphics.GdiPlus.Unit, pen: POINTER(POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPen))) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipClonePen(pen: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPen), clonepen: POINTER(POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPen))) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipDeletePen(pen: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPen)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipSetPenWidth(pen: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPen), width: Single) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipGetPenWidth(pen: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPen), width: POINTER(Single)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipSetPenUnit(pen: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPen), unit: win32more.Windows.Win32.Graphics.GdiPlus.Unit) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipGetPenUnit(pen: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPen), unit: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.Unit)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipSetPenLineCap197819(pen: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPen), startCap: win32more.Windows.Win32.Graphics.GdiPlus.LineCap, endCap: win32more.Windows.Win32.Graphics.GdiPlus.LineCap, dashCap: win32more.Windows.Win32.Graphics.GdiPlus.DashCap) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipSetPenStartCap(pen: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPen), startCap: win32more.Windows.Win32.Graphics.GdiPlus.LineCap) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipSetPenEndCap(pen: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPen), endCap: win32more.Windows.Win32.Graphics.GdiPlus.LineCap) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipSetPenDashCap197819(pen: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPen), dashCap: win32more.Windows.Win32.Graphics.GdiPlus.DashCap) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipGetPenStartCap(pen: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPen), startCap: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.LineCap)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipGetPenEndCap(pen: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPen), endCap: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.LineCap)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipGetPenDashCap197819(pen: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPen), dashCap: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.DashCap)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipSetPenLineJoin(pen: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPen), lineJoin: win32more.Windows.Win32.Graphics.GdiPlus.LineJoin) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipGetPenLineJoin(pen: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPen), lineJoin: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.LineJoin)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipSetPenCustomStartCap(pen: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPen), customCap: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpCustomLineCap)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipGetPenCustomStartCap(pen: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPen), customCap: POINTER(POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpCustomLineCap))) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipSetPenCustomEndCap(pen: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPen), customCap: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpCustomLineCap)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipGetPenCustomEndCap(pen: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPen), customCap: POINTER(POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpCustomLineCap))) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipSetPenMiterLimit(pen: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPen), miterLimit: Single) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipGetPenMiterLimit(pen: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPen), miterLimit: POINTER(Single)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipSetPenMode(pen: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPen), penMode: win32more.Windows.Win32.Graphics.GdiPlus.PenAlignment) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipGetPenMode(pen: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPen), penMode: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.PenAlignment)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipSetPenTransform(pen: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPen), matrix: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.Matrix)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipGetPenTransform(pen: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPen), matrix: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.Matrix)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipResetPenTransform(pen: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPen)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipMultiplyPenTransform(pen: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPen), matrix: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.Matrix), order: win32more.Windows.Win32.Graphics.GdiPlus.MatrixOrder) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipTranslatePenTransform(pen: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPen), dx: Single, dy: Single, order: win32more.Windows.Win32.Graphics.GdiPlus.MatrixOrder) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipScalePenTransform(pen: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPen), sx: Single, sy: Single, order: win32more.Windows.Win32.Graphics.GdiPlus.MatrixOrder) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipRotatePenTransform(pen: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPen), angle: Single, order: win32more.Windows.Win32.Graphics.GdiPlus.MatrixOrder) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipSetPenColor(pen: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPen), argb: UInt32) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipGetPenColor(pen: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPen), argb: POINTER(UInt32)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipSetPenBrushFill(pen: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPen), brush: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpBrush)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipGetPenBrushFill(pen: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPen), brush: POINTER(POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpBrush))) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipGetPenFillType(pen: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPen), type: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.PenType)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipGetPenDashStyle(pen: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPen), dashstyle: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.DashStyle)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipSetPenDashStyle(pen: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPen), dashstyle: win32more.Windows.Win32.Graphics.GdiPlus.DashStyle) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipGetPenDashOffset(pen: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPen), offset: POINTER(Single)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipSetPenDashOffset(pen: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPen), offset: Single) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipGetPenDashCount(pen: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPen), count: POINTER(Int32)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipSetPenDashArray(pen: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPen), dash: POINTER(Single), count: Int32) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipGetPenDashArray(pen: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPen), dash: POINTER(Single), count: Int32) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipGetPenCompoundCount(pen: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPen), count: POINTER(Int32)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipSetPenCompoundArray(pen: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPen), dash: POINTER(Single), count: Int32) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipGetPenCompoundArray(pen: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPen), dash: POINTER(Single), count: Int32) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipCreateCustomLineCap(fillPath: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPath), strokePath: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPath), baseCap: win32more.Windows.Win32.Graphics.GdiPlus.LineCap, baseInset: Single, customCap: POINTER(POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpCustomLineCap))) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipDeleteCustomLineCap(customCap: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpCustomLineCap)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipCloneCustomLineCap(customCap: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpCustomLineCap), clonedCap: POINTER(POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpCustomLineCap))) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipGetCustomLineCapType(customCap: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpCustomLineCap), capType: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.CustomLineCapType)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipSetCustomLineCapStrokeCaps(customCap: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpCustomLineCap), startCap: win32more.Windows.Win32.Graphics.GdiPlus.LineCap, endCap: win32more.Windows.Win32.Graphics.GdiPlus.LineCap) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipGetCustomLineCapStrokeCaps(customCap: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpCustomLineCap), startCap: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.LineCap), endCap: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.LineCap)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipSetCustomLineCapStrokeJoin(customCap: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpCustomLineCap), lineJoin: win32more.Windows.Win32.Graphics.GdiPlus.LineJoin) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipGetCustomLineCapStrokeJoin(customCap: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpCustomLineCap), lineJoin: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.LineJoin)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipSetCustomLineCapBaseCap(customCap: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpCustomLineCap), baseCap: win32more.Windows.Win32.Graphics.GdiPlus.LineCap) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipGetCustomLineCapBaseCap(customCap: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpCustomLineCap), baseCap: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.LineCap)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipSetCustomLineCapBaseInset(customCap: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpCustomLineCap), inset: Single) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipGetCustomLineCapBaseInset(customCap: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpCustomLineCap), inset: POINTER(Single)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipSetCustomLineCapWidthScale(customCap: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpCustomLineCap), widthScale: Single) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipGetCustomLineCapWidthScale(customCap: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpCustomLineCap), widthScale: POINTER(Single)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipCreateAdjustableArrowCap(height: Single, width: Single, isFilled: win32more.Windows.Win32.Foundation.BOOL, cap: POINTER(POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpAdjustableArrowCap))) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipSetAdjustableArrowCapHeight(cap: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpAdjustableArrowCap), height: Single) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipGetAdjustableArrowCapHeight(cap: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpAdjustableArrowCap), height: POINTER(Single)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipSetAdjustableArrowCapWidth(cap: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpAdjustableArrowCap), width: Single) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipGetAdjustableArrowCapWidth(cap: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpAdjustableArrowCap), width: POINTER(Single)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipSetAdjustableArrowCapMiddleInset(cap: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpAdjustableArrowCap), middleInset: Single) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipGetAdjustableArrowCapMiddleInset(cap: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpAdjustableArrowCap), middleInset: POINTER(Single)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipSetAdjustableArrowCapFillState(cap: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpAdjustableArrowCap), fillState: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipGetAdjustableArrowCapFillState(cap: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpAdjustableArrowCap), fillState: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipLoadImageFromStream(stream: win32more.Windows.Win32.System.Com.IStream, image: POINTER(POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpImage))) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipLoadImageFromFile(filename: win32more.Windows.Win32.Foundation.PWSTR, image: POINTER(POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpImage))) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipLoadImageFromStreamICM(stream: win32more.Windows.Win32.System.Com.IStream, image: POINTER(POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpImage))) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipLoadImageFromFileICM(filename: win32more.Windows.Win32.Foundation.PWSTR, image: POINTER(POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpImage))) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipCloneImage(image: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpImage), cloneImage: POINTER(POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpImage))) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipDisposeImage(image: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpImage)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipSaveImageToFile(image: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpImage), filename: win32more.Windows.Win32.Foundation.PWSTR, clsidEncoder: POINTER(Guid), encoderParams: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.EncoderParameters)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipSaveImageToStream(image: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpImage), stream: win32more.Windows.Win32.System.Com.IStream, clsidEncoder: POINTER(Guid), encoderParams: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.EncoderParameters)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipSaveAdd(image: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpImage), encoderParams: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.EncoderParameters)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipSaveAddImage(image: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpImage), newImage: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpImage), encoderParams: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.EncoderParameters)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipGetImageGraphicsContext(image: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpImage), graphics: POINTER(POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics))) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipGetImageBounds(image: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpImage), srcRect: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.RectF), srcUnit: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.Unit)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipGetImageDimension(image: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpImage), width: POINTER(Single), height: POINTER(Single)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipGetImageType(image: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpImage), type: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.ImageType)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipGetImageWidth(image: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpImage), width: POINTER(UInt32)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipGetImageHeight(image: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpImage), height: POINTER(UInt32)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipGetImageHorizontalResolution(image: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpImage), resolution: POINTER(Single)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipGetImageVerticalResolution(image: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpImage), resolution: POINTER(Single)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipGetImageFlags(image: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpImage), flags: POINTER(UInt32)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipGetImageRawFormat(image: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpImage), format: POINTER(Guid)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipGetImagePixelFormat(image: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpImage), format: POINTER(Int32)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipGetImageThumbnail(image: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpImage), thumbWidth: UInt32, thumbHeight: UInt32, thumbImage: POINTER(POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpImage)), callback: IntPtr, callbackData: VoidPtr) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipGetEncoderParameterListSize(image: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpImage), clsidEncoder: POINTER(Guid), size: POINTER(UInt32)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipGetEncoderParameterList(image: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpImage), clsidEncoder: POINTER(Guid), size: UInt32, buffer: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.EncoderParameters)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipImageGetFrameDimensionsCount(image: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpImage), count: POINTER(UInt32)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipImageGetFrameDimensionsList(image: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpImage), dimensionIDs: POINTER(Guid), count: UInt32) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipImageGetFrameCount(image: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpImage), dimensionID: POINTER(Guid), count: POINTER(UInt32)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipImageSelectActiveFrame(image: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpImage), dimensionID: POINTER(Guid), frameIndex: UInt32) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipImageRotateFlip(image: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpImage), rfType: win32more.Windows.Win32.Graphics.GdiPlus.RotateFlipType) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipGetImagePalette(image: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpImage), palette: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.ColorPalette), size: Int32) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipSetImagePalette(image: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpImage), palette: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.ColorPalette)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipGetImagePaletteSize(image: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpImage), size: POINTER(Int32)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipGetPropertyCount(image: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpImage), numOfProperty: POINTER(UInt32)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipGetPropertyIdList(image: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpImage), numOfProperty: UInt32, list: POINTER(UInt32)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipGetPropertyItemSize(image: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpImage), propId: UInt32, size: POINTER(UInt32)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipGetPropertyItem(image: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpImage), propId: UInt32, propSize: UInt32, buffer: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.PropertyItem)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipGetPropertySize(image: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpImage), totalBufferSize: POINTER(UInt32), numProperties: POINTER(UInt32)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipGetAllPropertyItems(image: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpImage), totalBufferSize: UInt32, numProperties: UInt32, allItems: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.PropertyItem)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipRemovePropertyItem(image: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpImage), propId: UInt32) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipSetPropertyItem(image: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpImage), item: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.PropertyItem)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipFindFirstImageItem(image: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpImage), item: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.ImageItemData)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipFindNextImageItem(image: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpImage), item: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.ImageItemData)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipGetImageItemData(image: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpImage), item: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.ImageItemData)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipImageForceValidation(image: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpImage)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipCreateBitmapFromStream(stream: win32more.Windows.Win32.System.Com.IStream, bitmap: POINTER(POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpBitmap))) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipCreateBitmapFromFile(filename: win32more.Windows.Win32.Foundation.PWSTR, bitmap: POINTER(POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpBitmap))) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipCreateBitmapFromStreamICM(stream: win32more.Windows.Win32.System.Com.IStream, bitmap: POINTER(POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpBitmap))) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipCreateBitmapFromFileICM(filename: win32more.Windows.Win32.Foundation.PWSTR, bitmap: POINTER(POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpBitmap))) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipCreateBitmapFromScan0(width: Int32, height: Int32, stride: Int32, format: Int32, scan0: POINTER(Byte), bitmap: POINTER(POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpBitmap))) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipCreateBitmapFromGraphics(width: Int32, height: Int32, target: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics), bitmap: POINTER(POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpBitmap))) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipCreateBitmapFromDirectDrawSurface(surface: win32more.Windows.Win32.Graphics.DirectDraw.IDirectDrawSurface7, bitmap: POINTER(POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpBitmap))) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipCreateBitmapFromGdiDib(gdiBitmapInfo: POINTER(win32more.Windows.Win32.Graphics.Gdi.BITMAPINFO), gdiBitmapData: VoidPtr, bitmap: POINTER(POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpBitmap))) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipCreateBitmapFromHBITMAP(hbm: win32more.Windows.Win32.Graphics.Gdi.HBITMAP, hpal: win32more.Windows.Win32.Graphics.Gdi.HPALETTE, bitmap: POINTER(POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpBitmap))) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipCreateHBITMAPFromBitmap(bitmap: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpBitmap), hbmReturn: POINTER(win32more.Windows.Win32.Graphics.Gdi.HBITMAP), background: UInt32) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipCreateBitmapFromHICON(hicon: win32more.Windows.Win32.UI.WindowsAndMessaging.HICON, bitmap: POINTER(POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpBitmap))) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipCreateHICONFromBitmap(bitmap: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpBitmap), hbmReturn: POINTER(win32more.Windows.Win32.UI.WindowsAndMessaging.HICON)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipCreateBitmapFromResource(hInstance: win32more.Windows.Win32.Foundation.HINSTANCE, lpBitmapName: win32more.Windows.Win32.Foundation.PWSTR, bitmap: POINTER(POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpBitmap))) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipCloneBitmapArea(x: Single, y: Single, width: Single, height: Single, format: Int32, srcBitmap: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpBitmap), dstBitmap: POINTER(POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpBitmap))) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipCloneBitmapAreaI(x: Int32, y: Int32, width: Int32, height: Int32, format: Int32, srcBitmap: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpBitmap), dstBitmap: POINTER(POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpBitmap))) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipBitmapLockBits(bitmap: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpBitmap), rect: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.Rect), flags: UInt32, format: Int32, lockedBitmapData: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.BitmapData)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipBitmapUnlockBits(bitmap: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpBitmap), lockedBitmapData: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.BitmapData)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipBitmapGetPixel(bitmap: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpBitmap), x: Int32, y: Int32, color: POINTER(UInt32)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipBitmapSetPixel(bitmap: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpBitmap), x: Int32, y: Int32, color: UInt32) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipImageSetAbort(pImage: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpImage), pIAbort: win32more.Windows.Win32.Graphics.GdiPlus.GdiplusAbort) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipGraphicsSetAbort(pGraphics: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics), pIAbort: win32more.Windows.Win32.Graphics.GdiPlus.GdiplusAbort) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipBitmapConvertFormat(pInputBitmap: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpBitmap), format: Int32, dithertype: win32more.Windows.Win32.Graphics.GdiPlus.DitherType, palettetype: win32more.Windows.Win32.Graphics.GdiPlus.PaletteType, palette: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.ColorPalette), alphaThresholdPercent: Single) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipInitializePalette(palette: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.ColorPalette), palettetype: win32more.Windows.Win32.Graphics.GdiPlus.PaletteType, optimalColors: Int32, useTransparentColor: win32more.Windows.Win32.Foundation.BOOL, bitmap: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpBitmap)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipBitmapApplyEffect(bitmap: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpBitmap), effect: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.CGpEffect), roi: POINTER(win32more.Windows.Win32.Foundation.RECT), useAuxData: win32more.Windows.Win32.Foundation.BOOL, auxData: POINTER(VoidPtr), auxDataSize: POINTER(Int32)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipBitmapCreateApplyEffect(inputBitmaps: POINTER(POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpBitmap)), numInputs: Int32, effect: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.CGpEffect), roi: POINTER(win32more.Windows.Win32.Foundation.RECT), outputRect: POINTER(win32more.Windows.Win32.Foundation.RECT), outputBitmap: POINTER(POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpBitmap)), useAuxData: win32more.Windows.Win32.Foundation.BOOL, auxData: POINTER(VoidPtr), auxDataSize: POINTER(Int32)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipBitmapGetHistogram(bitmap: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpBitmap), format: win32more.Windows.Win32.Graphics.GdiPlus.HistogramFormat, NumberOfEntries: UInt32, channel0: POINTER(UInt32), channel1: POINTER(UInt32), channel2: POINTER(UInt32), channel3: POINTER(UInt32)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipBitmapGetHistogramSize(format: win32more.Windows.Win32.Graphics.GdiPlus.HistogramFormat, NumberOfEntries: POINTER(UInt32)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipBitmapSetResolution(bitmap: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpBitmap), xdpi: Single, ydpi: Single) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipCreateImageAttributes(imageattr: POINTER(POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpImageAttributes))) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipCloneImageAttributes(imageattr: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpImageAttributes), cloneImageattr: POINTER(POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpImageAttributes))) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipDisposeImageAttributes(imageattr: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpImageAttributes)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipSetImageAttributesToIdentity(imageattr: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpImageAttributes), type: win32more.Windows.Win32.Graphics.GdiPlus.ColorAdjustType) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipResetImageAttributes(imageattr: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpImageAttributes), type: win32more.Windows.Win32.Graphics.GdiPlus.ColorAdjustType) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipSetImageAttributesColorMatrix(imageattr: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpImageAttributes), type: win32more.Windows.Win32.Graphics.GdiPlus.ColorAdjustType, enableFlag: win32more.Windows.Win32.Foundation.BOOL, colorMatrix: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.ColorMatrix), grayMatrix: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.ColorMatrix), flags: win32more.Windows.Win32.Graphics.GdiPlus.ColorMatrixFlags) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipSetImageAttributesThreshold(imageattr: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpImageAttributes), type: win32more.Windows.Win32.Graphics.GdiPlus.ColorAdjustType, enableFlag: win32more.Windows.Win32.Foundation.BOOL, threshold: Single) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipSetImageAttributesGamma(imageattr: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpImageAttributes), type: win32more.Windows.Win32.Graphics.GdiPlus.ColorAdjustType, enableFlag: win32more.Windows.Win32.Foundation.BOOL, gamma: Single) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipSetImageAttributesNoOp(imageattr: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpImageAttributes), type: win32more.Windows.Win32.Graphics.GdiPlus.ColorAdjustType, enableFlag: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipSetImageAttributesColorKeys(imageattr: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpImageAttributes), type: win32more.Windows.Win32.Graphics.GdiPlus.ColorAdjustType, enableFlag: win32more.Windows.Win32.Foundation.BOOL, colorLow: UInt32, colorHigh: UInt32) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipSetImageAttributesOutputChannel(imageattr: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpImageAttributes), type: win32more.Windows.Win32.Graphics.GdiPlus.ColorAdjustType, enableFlag: win32more.Windows.Win32.Foundation.BOOL, channelFlags: win32more.Windows.Win32.Graphics.GdiPlus.ColorChannelFlags) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipSetImageAttributesOutputChannelColorProfile(imageattr: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpImageAttributes), type: win32more.Windows.Win32.Graphics.GdiPlus.ColorAdjustType, enableFlag: win32more.Windows.Win32.Foundation.BOOL, colorProfileFilename: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipSetImageAttributesRemapTable(imageattr: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpImageAttributes), type: win32more.Windows.Win32.Graphics.GdiPlus.ColorAdjustType, enableFlag: win32more.Windows.Win32.Foundation.BOOL, mapSize: UInt32, map: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.ColorMap)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipSetImageAttributesWrapMode(imageAttr: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpImageAttributes), wrap: win32more.Windows.Win32.Graphics.GdiPlus.WrapMode, argb: UInt32, clamp: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipGetImageAttributesAdjustedPalette(imageAttr: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpImageAttributes), colorPalette: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.ColorPalette), colorAdjustType: win32more.Windows.Win32.Graphics.GdiPlus.ColorAdjustType) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipFlush(graphics: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics), intention: win32more.Windows.Win32.Graphics.GdiPlus.FlushIntention) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipCreateFromHDC(hdc: win32more.Windows.Win32.Graphics.Gdi.HDC, graphics: POINTER(POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics))) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipCreateFromHDC2(hdc: win32more.Windows.Win32.Graphics.Gdi.HDC, hDevice: win32more.Windows.Win32.Foundation.HANDLE, graphics: POINTER(POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics))) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipCreateFromHWND(hwnd: win32more.Windows.Win32.Foundation.HWND, graphics: POINTER(POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics))) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipCreateFromHWNDICM(hwnd: win32more.Windows.Win32.Foundation.HWND, graphics: POINTER(POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics))) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipDeleteGraphics(graphics: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipGetDC(graphics: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics), hdc: POINTER(win32more.Windows.Win32.Graphics.Gdi.HDC)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipReleaseDC(graphics: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics), hdc: win32more.Windows.Win32.Graphics.Gdi.HDC) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipSetCompositingMode(graphics: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics), compositingMode: win32more.Windows.Win32.Graphics.GdiPlus.CompositingMode) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipGetCompositingMode(graphics: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics), compositingMode: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.CompositingMode)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipSetRenderingOrigin(graphics: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics), x: Int32, y: Int32) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipGetRenderingOrigin(graphics: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics), x: POINTER(Int32), y: POINTER(Int32)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipSetCompositingQuality(graphics: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics), compositingQuality: win32more.Windows.Win32.Graphics.GdiPlus.CompositingQuality) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipGetCompositingQuality(graphics: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics), compositingQuality: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.CompositingQuality)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipSetSmoothingMode(graphics: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics), smoothingMode: win32more.Windows.Win32.Graphics.GdiPlus.SmoothingMode) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipGetSmoothingMode(graphics: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics), smoothingMode: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.SmoothingMode)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipSetPixelOffsetMode(graphics: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics), pixelOffsetMode: win32more.Windows.Win32.Graphics.GdiPlus.PixelOffsetMode) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipGetPixelOffsetMode(graphics: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics), pixelOffsetMode: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.PixelOffsetMode)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipSetTextRenderingHint(graphics: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics), mode: win32more.Windows.Win32.Graphics.GdiPlus.TextRenderingHint) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipGetTextRenderingHint(graphics: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics), mode: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.TextRenderingHint)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipSetTextContrast(graphics: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics), contrast: UInt32) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipGetTextContrast(graphics: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics), contrast: POINTER(UInt32)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipSetInterpolationMode(graphics: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics), interpolationMode: win32more.Windows.Win32.Graphics.GdiPlus.InterpolationMode) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipGetInterpolationMode(graphics: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics), interpolationMode: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.InterpolationMode)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipSetWorldTransform(graphics: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics), matrix: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.Matrix)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipResetWorldTransform(graphics: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipMultiplyWorldTransform(graphics: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics), matrix: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.Matrix), order: win32more.Windows.Win32.Graphics.GdiPlus.MatrixOrder) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipTranslateWorldTransform(graphics: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics), dx: Single, dy: Single, order: win32more.Windows.Win32.Graphics.GdiPlus.MatrixOrder) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipScaleWorldTransform(graphics: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics), sx: Single, sy: Single, order: win32more.Windows.Win32.Graphics.GdiPlus.MatrixOrder) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipRotateWorldTransform(graphics: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics), angle: Single, order: win32more.Windows.Win32.Graphics.GdiPlus.MatrixOrder) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipGetWorldTransform(graphics: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics), matrix: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.Matrix)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipResetPageTransform(graphics: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipGetPageUnit(graphics: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics), unit: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.Unit)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipGetPageScale(graphics: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics), scale: POINTER(Single)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipSetPageUnit(graphics: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics), unit: win32more.Windows.Win32.Graphics.GdiPlus.Unit) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipSetPageScale(graphics: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics), scale: Single) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipGetDpiX(graphics: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics), dpi: POINTER(Single)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipGetDpiY(graphics: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics), dpi: POINTER(Single)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipTransformPoints(graphics: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics), destSpace: win32more.Windows.Win32.Graphics.GdiPlus.CoordinateSpace, srcSpace: win32more.Windows.Win32.Graphics.GdiPlus.CoordinateSpace, points: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.PointF), count: Int32) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipTransformPointsI(graphics: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics), destSpace: win32more.Windows.Win32.Graphics.GdiPlus.CoordinateSpace, srcSpace: win32more.Windows.Win32.Graphics.GdiPlus.CoordinateSpace, points: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.Point), count: Int32) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipGetNearestColor(graphics: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics), argb: POINTER(UInt32)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipCreateHalftonePalette() -> win32more.Windows.Win32.Graphics.Gdi.HPALETTE: ...
@winfunctype('gdiplus.dll')
def GdipDrawLine(graphics: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics), pen: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPen), x1: Single, y1: Single, x2: Single, y2: Single) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipDrawLineI(graphics: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics), pen: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPen), x1: Int32, y1: Int32, x2: Int32, y2: Int32) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipDrawLines(graphics: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics), pen: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPen), points: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.PointF), count: Int32) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipDrawLinesI(graphics: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics), pen: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPen), points: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.Point), count: Int32) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipDrawArc(graphics: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics), pen: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPen), x: Single, y: Single, width: Single, height: Single, startAngle: Single, sweepAngle: Single) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipDrawArcI(graphics: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics), pen: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPen), x: Int32, y: Int32, width: Int32, height: Int32, startAngle: Single, sweepAngle: Single) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipDrawBezier(graphics: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics), pen: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPen), x1: Single, y1: Single, x2: Single, y2: Single, x3: Single, y3: Single, x4: Single, y4: Single) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipDrawBezierI(graphics: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics), pen: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPen), x1: Int32, y1: Int32, x2: Int32, y2: Int32, x3: Int32, y3: Int32, x4: Int32, y4: Int32) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipDrawBeziers(graphics: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics), pen: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPen), points: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.PointF), count: Int32) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipDrawBeziersI(graphics: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics), pen: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPen), points: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.Point), count: Int32) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipDrawRectangle(graphics: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics), pen: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPen), x: Single, y: Single, width: Single, height: Single) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipDrawRectangleI(graphics: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics), pen: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPen), x: Int32, y: Int32, width: Int32, height: Int32) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipDrawRectangles(graphics: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics), pen: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPen), rects: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.RectF), count: Int32) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipDrawRectanglesI(graphics: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics), pen: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPen), rects: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.Rect), count: Int32) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipDrawEllipse(graphics: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics), pen: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPen), x: Single, y: Single, width: Single, height: Single) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipDrawEllipseI(graphics: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics), pen: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPen), x: Int32, y: Int32, width: Int32, height: Int32) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipDrawPie(graphics: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics), pen: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPen), x: Single, y: Single, width: Single, height: Single, startAngle: Single, sweepAngle: Single) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipDrawPieI(graphics: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics), pen: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPen), x: Int32, y: Int32, width: Int32, height: Int32, startAngle: Single, sweepAngle: Single) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipDrawPolygon(graphics: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics), pen: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPen), points: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.PointF), count: Int32) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipDrawPolygonI(graphics: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics), pen: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPen), points: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.Point), count: Int32) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipDrawPath(graphics: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics), pen: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPen), path: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPath)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipDrawCurve(graphics: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics), pen: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPen), points: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.PointF), count: Int32) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipDrawCurveI(graphics: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics), pen: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPen), points: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.Point), count: Int32) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipDrawCurve2(graphics: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics), pen: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPen), points: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.PointF), count: Int32, tension: Single) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipDrawCurve2I(graphics: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics), pen: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPen), points: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.Point), count: Int32, tension: Single) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipDrawCurve3(graphics: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics), pen: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPen), points: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.PointF), count: Int32, offset: Int32, numberOfSegments: Int32, tension: Single) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipDrawCurve3I(graphics: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics), pen: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPen), points: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.Point), count: Int32, offset: Int32, numberOfSegments: Int32, tension: Single) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipDrawClosedCurve(graphics: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics), pen: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPen), points: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.PointF), count: Int32) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipDrawClosedCurveI(graphics: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics), pen: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPen), points: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.Point), count: Int32) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipDrawClosedCurve2(graphics: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics), pen: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPen), points: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.PointF), count: Int32, tension: Single) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipDrawClosedCurve2I(graphics: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics), pen: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPen), points: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.Point), count: Int32, tension: Single) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipGraphicsClear(graphics: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics), color: UInt32) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipFillRectangle(graphics: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics), brush: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpBrush), x: Single, y: Single, width: Single, height: Single) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipFillRectangleI(graphics: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics), brush: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpBrush), x: Int32, y: Int32, width: Int32, height: Int32) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipFillRectangles(graphics: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics), brush: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpBrush), rects: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.RectF), count: Int32) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipFillRectanglesI(graphics: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics), brush: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpBrush), rects: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.Rect), count: Int32) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipFillPolygon(graphics: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics), brush: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpBrush), points: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.PointF), count: Int32, fillMode: win32more.Windows.Win32.Graphics.GdiPlus.FillMode) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipFillPolygonI(graphics: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics), brush: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpBrush), points: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.Point), count: Int32, fillMode: win32more.Windows.Win32.Graphics.GdiPlus.FillMode) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipFillPolygon2(graphics: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics), brush: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpBrush), points: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.PointF), count: Int32) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipFillPolygon2I(graphics: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics), brush: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpBrush), points: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.Point), count: Int32) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipFillEllipse(graphics: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics), brush: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpBrush), x: Single, y: Single, width: Single, height: Single) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipFillEllipseI(graphics: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics), brush: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpBrush), x: Int32, y: Int32, width: Int32, height: Int32) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipFillPie(graphics: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics), brush: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpBrush), x: Single, y: Single, width: Single, height: Single, startAngle: Single, sweepAngle: Single) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipFillPieI(graphics: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics), brush: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpBrush), x: Int32, y: Int32, width: Int32, height: Int32, startAngle: Single, sweepAngle: Single) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipFillPath(graphics: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics), brush: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpBrush), path: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPath)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipFillClosedCurve(graphics: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics), brush: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpBrush), points: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.PointF), count: Int32) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipFillClosedCurveI(graphics: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics), brush: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpBrush), points: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.Point), count: Int32) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipFillClosedCurve2(graphics: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics), brush: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpBrush), points: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.PointF), count: Int32, tension: Single, fillMode: win32more.Windows.Win32.Graphics.GdiPlus.FillMode) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipFillClosedCurve2I(graphics: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics), brush: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpBrush), points: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.Point), count: Int32, tension: Single, fillMode: win32more.Windows.Win32.Graphics.GdiPlus.FillMode) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipFillRegion(graphics: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics), brush: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpBrush), region: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpRegion)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipDrawImageFX(graphics: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics), image: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpImage), source: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.RectF), xForm: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.Matrix), effect: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.CGpEffect), imageAttributes: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpImageAttributes), srcUnit: win32more.Windows.Win32.Graphics.GdiPlus.Unit) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipDrawImage(graphics: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics), image: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpImage), x: Single, y: Single) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipDrawImageI(graphics: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics), image: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpImage), x: Int32, y: Int32) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipDrawImageRect(graphics: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics), image: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpImage), x: Single, y: Single, width: Single, height: Single) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipDrawImageRectI(graphics: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics), image: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpImage), x: Int32, y: Int32, width: Int32, height: Int32) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipDrawImagePoints(graphics: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics), image: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpImage), dstpoints: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.PointF), count: Int32) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipDrawImagePointsI(graphics: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics), image: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpImage), dstpoints: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.Point), count: Int32) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipDrawImagePointRect(graphics: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics), image: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpImage), x: Single, y: Single, srcx: Single, srcy: Single, srcwidth: Single, srcheight: Single, srcUnit: win32more.Windows.Win32.Graphics.GdiPlus.Unit) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipDrawImagePointRectI(graphics: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics), image: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpImage), x: Int32, y: Int32, srcx: Int32, srcy: Int32, srcwidth: Int32, srcheight: Int32, srcUnit: win32more.Windows.Win32.Graphics.GdiPlus.Unit) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipDrawImageRectRect(graphics: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics), image: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpImage), dstx: Single, dsty: Single, dstwidth: Single, dstheight: Single, srcx: Single, srcy: Single, srcwidth: Single, srcheight: Single, srcUnit: win32more.Windows.Win32.Graphics.GdiPlus.Unit, imageAttributes: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpImageAttributes), callback: IntPtr, callbackData: VoidPtr) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipDrawImageRectRectI(graphics: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics), image: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpImage), dstx: Int32, dsty: Int32, dstwidth: Int32, dstheight: Int32, srcx: Int32, srcy: Int32, srcwidth: Int32, srcheight: Int32, srcUnit: win32more.Windows.Win32.Graphics.GdiPlus.Unit, imageAttributes: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpImageAttributes), callback: IntPtr, callbackData: VoidPtr) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipDrawImagePointsRect(graphics: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics), image: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpImage), points: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.PointF), count: Int32, srcx: Single, srcy: Single, srcwidth: Single, srcheight: Single, srcUnit: win32more.Windows.Win32.Graphics.GdiPlus.Unit, imageAttributes: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpImageAttributes), callback: IntPtr, callbackData: VoidPtr) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipDrawImagePointsRectI(graphics: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics), image: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpImage), points: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.Point), count: Int32, srcx: Int32, srcy: Int32, srcwidth: Int32, srcheight: Int32, srcUnit: win32more.Windows.Win32.Graphics.GdiPlus.Unit, imageAttributes: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpImageAttributes), callback: IntPtr, callbackData: VoidPtr) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipEnumerateMetafileDestPoint(graphics: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics), metafile: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpMetafile), destPoint: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.PointF), callback: IntPtr, callbackData: VoidPtr, imageAttributes: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpImageAttributes)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipEnumerateMetafileDestPointI(graphics: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics), metafile: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpMetafile), destPoint: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.Point), callback: IntPtr, callbackData: VoidPtr, imageAttributes: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpImageAttributes)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipEnumerateMetafileDestRect(graphics: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics), metafile: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpMetafile), destRect: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.RectF), callback: IntPtr, callbackData: VoidPtr, imageAttributes: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpImageAttributes)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipEnumerateMetafileDestRectI(graphics: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics), metafile: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpMetafile), destRect: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.Rect), callback: IntPtr, callbackData: VoidPtr, imageAttributes: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpImageAttributes)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipEnumerateMetafileDestPoints(graphics: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics), metafile: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpMetafile), destPoints: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.PointF), count: Int32, callback: IntPtr, callbackData: VoidPtr, imageAttributes: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpImageAttributes)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipEnumerateMetafileDestPointsI(graphics: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics), metafile: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpMetafile), destPoints: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.Point), count: Int32, callback: IntPtr, callbackData: VoidPtr, imageAttributes: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpImageAttributes)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipEnumerateMetafileSrcRectDestPoint(graphics: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics), metafile: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpMetafile), destPoint: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.PointF), srcRect: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.RectF), srcUnit: win32more.Windows.Win32.Graphics.GdiPlus.Unit, callback: IntPtr, callbackData: VoidPtr, imageAttributes: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpImageAttributes)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipEnumerateMetafileSrcRectDestPointI(graphics: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics), metafile: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpMetafile), destPoint: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.Point), srcRect: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.Rect), srcUnit: win32more.Windows.Win32.Graphics.GdiPlus.Unit, callback: IntPtr, callbackData: VoidPtr, imageAttributes: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpImageAttributes)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipEnumerateMetafileSrcRectDestRect(graphics: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics), metafile: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpMetafile), destRect: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.RectF), srcRect: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.RectF), srcUnit: win32more.Windows.Win32.Graphics.GdiPlus.Unit, callback: IntPtr, callbackData: VoidPtr, imageAttributes: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpImageAttributes)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipEnumerateMetafileSrcRectDestRectI(graphics: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics), metafile: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpMetafile), destRect: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.Rect), srcRect: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.Rect), srcUnit: win32more.Windows.Win32.Graphics.GdiPlus.Unit, callback: IntPtr, callbackData: VoidPtr, imageAttributes: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpImageAttributes)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipEnumerateMetafileSrcRectDestPoints(graphics: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics), metafile: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpMetafile), destPoints: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.PointF), count: Int32, srcRect: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.RectF), srcUnit: win32more.Windows.Win32.Graphics.GdiPlus.Unit, callback: IntPtr, callbackData: VoidPtr, imageAttributes: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpImageAttributes)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipEnumerateMetafileSrcRectDestPointsI(graphics: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics), metafile: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpMetafile), destPoints: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.Point), count: Int32, srcRect: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.Rect), srcUnit: win32more.Windows.Win32.Graphics.GdiPlus.Unit, callback: IntPtr, callbackData: VoidPtr, imageAttributes: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpImageAttributes)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipPlayMetafileRecord(metafile: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpMetafile), recordType: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType, flags: UInt32, dataSize: UInt32, data: POINTER(Byte)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipSetClipGraphics(graphics: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics), srcgraphics: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics), combineMode: win32more.Windows.Win32.Graphics.GdiPlus.CombineMode) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipSetClipRect(graphics: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics), x: Single, y: Single, width: Single, height: Single, combineMode: win32more.Windows.Win32.Graphics.GdiPlus.CombineMode) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipSetClipRectI(graphics: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics), x: Int32, y: Int32, width: Int32, height: Int32, combineMode: win32more.Windows.Win32.Graphics.GdiPlus.CombineMode) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipSetClipPath(graphics: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics), path: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpPath), combineMode: win32more.Windows.Win32.Graphics.GdiPlus.CombineMode) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipSetClipRegion(graphics: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics), region: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpRegion), combineMode: win32more.Windows.Win32.Graphics.GdiPlus.CombineMode) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipSetClipHrgn(graphics: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics), hRgn: win32more.Windows.Win32.Graphics.Gdi.HRGN, combineMode: win32more.Windows.Win32.Graphics.GdiPlus.CombineMode) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipResetClip(graphics: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipTranslateClip(graphics: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics), dx: Single, dy: Single) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipTranslateClipI(graphics: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics), dx: Int32, dy: Int32) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipGetClip(graphics: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics), region: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpRegion)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipGetClipBounds(graphics: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics), rect: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.RectF)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipGetClipBoundsI(graphics: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics), rect: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.Rect)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipIsClipEmpty(graphics: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics), result: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipGetVisibleClipBounds(graphics: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics), rect: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.RectF)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipGetVisibleClipBoundsI(graphics: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics), rect: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.Rect)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipIsVisibleClipEmpty(graphics: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics), result: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipIsVisiblePoint(graphics: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics), x: Single, y: Single, result: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipIsVisiblePointI(graphics: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics), x: Int32, y: Int32, result: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipIsVisibleRect(graphics: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics), x: Single, y: Single, width: Single, height: Single, result: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipIsVisibleRectI(graphics: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics), x: Int32, y: Int32, width: Int32, height: Int32, result: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipSaveGraphics(graphics: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics), state: POINTER(UInt32)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipRestoreGraphics(graphics: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics), state: UInt32) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipBeginContainer(graphics: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics), dstrect: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.RectF), srcrect: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.RectF), unit: win32more.Windows.Win32.Graphics.GdiPlus.Unit, state: POINTER(UInt32)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipBeginContainerI(graphics: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics), dstrect: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.Rect), srcrect: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.Rect), unit: win32more.Windows.Win32.Graphics.GdiPlus.Unit, state: POINTER(UInt32)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipBeginContainer2(graphics: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics), state: POINTER(UInt32)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipEndContainer(graphics: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics), state: UInt32) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipGetMetafileHeaderFromWmf(hWmf: win32more.Windows.Win32.Graphics.Gdi.HMETAFILE, wmfPlaceableFileHeader: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.WmfPlaceableFileHeader), header: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.MetafileHeader)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipGetMetafileHeaderFromEmf(hEmf: win32more.Windows.Win32.Graphics.Gdi.HENHMETAFILE, header: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.MetafileHeader)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipGetMetafileHeaderFromFile(filename: win32more.Windows.Win32.Foundation.PWSTR, header: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.MetafileHeader)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipGetMetafileHeaderFromStream(stream: win32more.Windows.Win32.System.Com.IStream, header: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.MetafileHeader)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipGetMetafileHeaderFromMetafile(metafile: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpMetafile), header: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.MetafileHeader)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipGetHemfFromMetafile(metafile: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpMetafile), hEmf: POINTER(win32more.Windows.Win32.Graphics.Gdi.HENHMETAFILE)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipCreateStreamOnFile(filename: win32more.Windows.Win32.Foundation.PWSTR, access: UInt32, stream: POINTER(win32more.Windows.Win32.System.Com.IStream)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipCreateMetafileFromWmf(hWmf: win32more.Windows.Win32.Graphics.Gdi.HMETAFILE, deleteWmf: win32more.Windows.Win32.Foundation.BOOL, wmfPlaceableFileHeader: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.WmfPlaceableFileHeader), metafile: POINTER(POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpMetafile))) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipCreateMetafileFromEmf(hEmf: win32more.Windows.Win32.Graphics.Gdi.HENHMETAFILE, deleteEmf: win32more.Windows.Win32.Foundation.BOOL, metafile: POINTER(POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpMetafile))) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipCreateMetafileFromFile(file: win32more.Windows.Win32.Foundation.PWSTR, metafile: POINTER(POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpMetafile))) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipCreateMetafileFromWmfFile(file: win32more.Windows.Win32.Foundation.PWSTR, wmfPlaceableFileHeader: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.WmfPlaceableFileHeader), metafile: POINTER(POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpMetafile))) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipCreateMetafileFromStream(stream: win32more.Windows.Win32.System.Com.IStream, metafile: POINTER(POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpMetafile))) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipRecordMetafile(referenceHdc: win32more.Windows.Win32.Graphics.Gdi.HDC, type: win32more.Windows.Win32.Graphics.GdiPlus.EmfType, frameRect: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.RectF), frameUnit: win32more.Windows.Win32.Graphics.GdiPlus.MetafileFrameUnit, description: win32more.Windows.Win32.Foundation.PWSTR, metafile: POINTER(POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpMetafile))) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipRecordMetafileI(referenceHdc: win32more.Windows.Win32.Graphics.Gdi.HDC, type: win32more.Windows.Win32.Graphics.GdiPlus.EmfType, frameRect: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.Rect), frameUnit: win32more.Windows.Win32.Graphics.GdiPlus.MetafileFrameUnit, description: win32more.Windows.Win32.Foundation.PWSTR, metafile: POINTER(POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpMetafile))) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipRecordMetafileFileName(fileName: win32more.Windows.Win32.Foundation.PWSTR, referenceHdc: win32more.Windows.Win32.Graphics.Gdi.HDC, type: win32more.Windows.Win32.Graphics.GdiPlus.EmfType, frameRect: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.RectF), frameUnit: win32more.Windows.Win32.Graphics.GdiPlus.MetafileFrameUnit, description: win32more.Windows.Win32.Foundation.PWSTR, metafile: POINTER(POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpMetafile))) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipRecordMetafileFileNameI(fileName: win32more.Windows.Win32.Foundation.PWSTR, referenceHdc: win32more.Windows.Win32.Graphics.Gdi.HDC, type: win32more.Windows.Win32.Graphics.GdiPlus.EmfType, frameRect: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.Rect), frameUnit: win32more.Windows.Win32.Graphics.GdiPlus.MetafileFrameUnit, description: win32more.Windows.Win32.Foundation.PWSTR, metafile: POINTER(POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpMetafile))) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipRecordMetafileStream(stream: win32more.Windows.Win32.System.Com.IStream, referenceHdc: win32more.Windows.Win32.Graphics.Gdi.HDC, type: win32more.Windows.Win32.Graphics.GdiPlus.EmfType, frameRect: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.RectF), frameUnit: win32more.Windows.Win32.Graphics.GdiPlus.MetafileFrameUnit, description: win32more.Windows.Win32.Foundation.PWSTR, metafile: POINTER(POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpMetafile))) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipRecordMetafileStreamI(stream: win32more.Windows.Win32.System.Com.IStream, referenceHdc: win32more.Windows.Win32.Graphics.Gdi.HDC, type: win32more.Windows.Win32.Graphics.GdiPlus.EmfType, frameRect: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.Rect), frameUnit: win32more.Windows.Win32.Graphics.GdiPlus.MetafileFrameUnit, description: win32more.Windows.Win32.Foundation.PWSTR, metafile: POINTER(POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpMetafile))) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipSetMetafileDownLevelRasterizationLimit(metafile: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpMetafile), metafileRasterizationLimitDpi: UInt32) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipGetMetafileDownLevelRasterizationLimit(metafile: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpMetafile), metafileRasterizationLimitDpi: POINTER(UInt32)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipGetImageDecodersSize(numDecoders: POINTER(UInt32), size: POINTER(UInt32)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipGetImageDecoders(numDecoders: UInt32, size: UInt32, decoders: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.ImageCodecInfo)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipGetImageEncodersSize(numEncoders: POINTER(UInt32), size: POINTER(UInt32)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipGetImageEncoders(numEncoders: UInt32, size: UInt32, encoders: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.ImageCodecInfo)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipComment(graphics: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics), sizeData: UInt32, data: POINTER(Byte)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipCreateFontFamilyFromName(name: win32more.Windows.Win32.Foundation.PWSTR, fontCollection: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpFontCollection), fontFamily: POINTER(POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpFontFamily))) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipDeleteFontFamily(fontFamily: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpFontFamily)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipCloneFontFamily(fontFamily: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpFontFamily), clonedFontFamily: POINTER(POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpFontFamily))) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipGetGenericFontFamilySansSerif(nativeFamily: POINTER(POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpFontFamily))) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipGetGenericFontFamilySerif(nativeFamily: POINTER(POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpFontFamily))) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipGetGenericFontFamilyMonospace(nativeFamily: POINTER(POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpFontFamily))) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipGetFamilyName(family: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpFontFamily), name: win32more.Windows.Win32.Foundation.PWSTR, language: UInt16) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipIsStyleAvailable(family: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpFontFamily), style: Int32, IsStyleAvailable: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipGetEmHeight(family: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpFontFamily), style: Int32, EmHeight: POINTER(UInt16)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipGetCellAscent(family: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpFontFamily), style: Int32, CellAscent: POINTER(UInt16)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipGetCellDescent(family: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpFontFamily), style: Int32, CellDescent: POINTER(UInt16)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipGetLineSpacing(family: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpFontFamily), style: Int32, LineSpacing: POINTER(UInt16)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipCreateFontFromDC(hdc: win32more.Windows.Win32.Graphics.Gdi.HDC, font: POINTER(POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpFont))) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipCreateFontFromLogfontA(hdc: win32more.Windows.Win32.Graphics.Gdi.HDC, logfont: POINTER(win32more.Windows.Win32.Graphics.Gdi.LOGFONTA), font: POINTER(POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpFont))) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipCreateFontFromLogfontW(hdc: win32more.Windows.Win32.Graphics.Gdi.HDC, logfont: POINTER(win32more.Windows.Win32.Graphics.Gdi.LOGFONTW), font: POINTER(POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpFont))) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipCreateFont(fontFamily: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpFontFamily), emSize: Single, style: Int32, unit: win32more.Windows.Win32.Graphics.GdiPlus.Unit, font: POINTER(POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpFont))) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipCloneFont(font: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpFont), cloneFont: POINTER(POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpFont))) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipDeleteFont(font: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpFont)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipGetFamily(font: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpFont), family: POINTER(POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpFontFamily))) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipGetFontStyle(font: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpFont), style: POINTER(Int32)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipGetFontSize(font: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpFont), size: POINTER(Single)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipGetFontUnit(font: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpFont), unit: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.Unit)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipGetFontHeight(font: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpFont), graphics: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics), height: POINTER(Single)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipGetFontHeightGivenDPI(font: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpFont), dpi: Single, height: POINTER(Single)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipGetLogFontA(font: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpFont), graphics: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics), logfontA: POINTER(win32more.Windows.Win32.Graphics.Gdi.LOGFONTA)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipGetLogFontW(font: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpFont), graphics: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics), logfontW: POINTER(win32more.Windows.Win32.Graphics.Gdi.LOGFONTW)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipNewInstalledFontCollection(fontCollection: POINTER(POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpFontCollection))) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipNewPrivateFontCollection(fontCollection: POINTER(POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpFontCollection))) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipDeletePrivateFontCollection(fontCollection: POINTER(POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpFontCollection))) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipGetFontCollectionFamilyCount(fontCollection: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpFontCollection), numFound: POINTER(Int32)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipGetFontCollectionFamilyList(fontCollection: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpFontCollection), numSought: Int32, gpfamilies: POINTER(POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpFontFamily)), numFound: POINTER(Int32)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipPrivateAddFontFile(fontCollection: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpFontCollection), filename: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipPrivateAddMemoryFont(fontCollection: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpFontCollection), memory: VoidPtr, length: Int32) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipDrawString(graphics: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics), string: win32more.Windows.Win32.Foundation.PWSTR, length: Int32, font: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpFont), layoutRect: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.RectF), stringFormat: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpStringFormat), brush: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpBrush)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipMeasureString(graphics: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics), string: win32more.Windows.Win32.Foundation.PWSTR, length: Int32, font: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpFont), layoutRect: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.RectF), stringFormat: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpStringFormat), boundingBox: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.RectF), codepointsFitted: POINTER(Int32), linesFilled: POINTER(Int32)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipMeasureCharacterRanges(graphics: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics), string: win32more.Windows.Win32.Foundation.PWSTR, length: Int32, font: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpFont), layoutRect: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.RectF), stringFormat: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpStringFormat), regionCount: Int32, regions: POINTER(POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpRegion))) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipDrawDriverString(graphics: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics), text: POINTER(UInt16), length: Int32, font: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpFont), brush: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpBrush), positions: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.PointF), flags: Int32, matrix: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.Matrix)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipMeasureDriverString(graphics: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics), text: POINTER(UInt16), length: Int32, font: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpFont), positions: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.PointF), flags: Int32, matrix: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.Matrix), boundingBox: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.RectF)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipCreateStringFormat(formatAttributes: Int32, language: UInt16, format: POINTER(POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpStringFormat))) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipStringFormatGetGenericDefault(format: POINTER(POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpStringFormat))) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipStringFormatGetGenericTypographic(format: POINTER(POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpStringFormat))) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipDeleteStringFormat(format: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpStringFormat)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipCloneStringFormat(format: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpStringFormat), newFormat: POINTER(POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpStringFormat))) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipSetStringFormatFlags(format: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpStringFormat), flags: Int32) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipGetStringFormatFlags(format: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpStringFormat), flags: POINTER(Int32)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipSetStringFormatAlign(format: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpStringFormat), align: win32more.Windows.Win32.Graphics.GdiPlus.StringAlignment) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipGetStringFormatAlign(format: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpStringFormat), align: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.StringAlignment)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipSetStringFormatLineAlign(format: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpStringFormat), align: win32more.Windows.Win32.Graphics.GdiPlus.StringAlignment) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipGetStringFormatLineAlign(format: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpStringFormat), align: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.StringAlignment)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipSetStringFormatTrimming(format: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpStringFormat), trimming: win32more.Windows.Win32.Graphics.GdiPlus.StringTrimming) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipGetStringFormatTrimming(format: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpStringFormat), trimming: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.StringTrimming)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipSetStringFormatHotkeyPrefix(format: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpStringFormat), hotkeyPrefix: Int32) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipGetStringFormatHotkeyPrefix(format: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpStringFormat), hotkeyPrefix: POINTER(Int32)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipSetStringFormatTabStops(format: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpStringFormat), firstTabOffset: Single, count: Int32, tabStops: POINTER(Single)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipGetStringFormatTabStops(format: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpStringFormat), count: Int32, firstTabOffset: POINTER(Single), tabStops: POINTER(Single)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipGetStringFormatTabStopCount(format: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpStringFormat), count: POINTER(Int32)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipSetStringFormatDigitSubstitution(format: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpStringFormat), language: UInt16, substitute: win32more.Windows.Win32.Graphics.GdiPlus.StringDigitSubstitute) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipGetStringFormatDigitSubstitution(format: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpStringFormat), language: POINTER(UInt16), substitute: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.StringDigitSubstitute)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipGetStringFormatMeasurableCharacterRangeCount(format: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpStringFormat), count: POINTER(Int32)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipSetStringFormatMeasurableCharacterRanges(format: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpStringFormat), rangeCount: Int32, ranges: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.CharacterRange)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipCreateCachedBitmap(bitmap: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpBitmap), graphics: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics), cachedBitmap: POINTER(POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpCachedBitmap))) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipDeleteCachedBitmap(cachedBitmap: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpCachedBitmap)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipDrawCachedBitmap(graphics: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics), cachedBitmap: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpCachedBitmap), x: Int32, y: Int32) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipEmfToWmfBits(hemf: win32more.Windows.Win32.Graphics.Gdi.HENHMETAFILE, cbData16: UInt32, pData16: POINTER(Byte), iMapMode: Int32, eFlags: Int32) -> UInt32: ...
@winfunctype('gdiplus.dll')
def GdipSetImageAttributesCachedBackground(imageattr: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpImageAttributes), enableFlag: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipTestControl(control: win32more.Windows.Win32.Graphics.GdiPlus.GpTestControlEnum, param1: VoidPtr) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdiplusNotificationHook(token: POINTER(UIntPtr)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdiplusNotificationUnhook(token: UIntPtr) -> Void: ...
@winfunctype('gdiplus.dll')
def GdipConvertToEmfPlus(refGraphics: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics), metafile: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpMetafile), conversionFailureFlag: POINTER(Int32), emfType: win32more.Windows.Win32.Graphics.GdiPlus.EmfType, description: win32more.Windows.Win32.Foundation.PWSTR, out_metafile: POINTER(POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpMetafile))) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipConvertToEmfPlusToFile(refGraphics: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics), metafile: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpMetafile), conversionFailureFlag: POINTER(Int32), filename: win32more.Windows.Win32.Foundation.PWSTR, emfType: win32more.Windows.Win32.Graphics.GdiPlus.EmfType, description: win32more.Windows.Win32.Foundation.PWSTR, out_metafile: POINTER(POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpMetafile))) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype('gdiplus.dll')
def GdipConvertToEmfPlusToStream(refGraphics: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpGraphics), metafile: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpMetafile), conversionFailureFlag: POINTER(Int32), stream: win32more.Windows.Win32.System.Com.IStream, emfType: win32more.Windows.Win32.Graphics.GdiPlus.EmfType, description: win32more.Windows.Win32.Foundation.PWSTR, out_metafile: POINTER(POINTER(win32more.Windows.Win32.Graphics.GdiPlus.GpMetafile))) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
Bitmap = IntPtr
class BitmapData(EasyCastStructure):
    Width: UInt32
    Height: UInt32
    Stride: Int32
    PixelFormat: Int32
    Scan0: VoidPtr
    Reserved: UIntPtr
class Blur(EasyCastStructure):
    Base: win32more.Windows.Win32.Graphics.GdiPlus.Effect
class BlurParams(EasyCastStructure):
    radius: Single
    expandEdge: win32more.Windows.Win32.Foundation.BOOL
class BrightnessContrast(EasyCastStructure):
    Base: win32more.Windows.Win32.Graphics.GdiPlus.Effect
class BrightnessContrastParams(EasyCastStructure):
    brightnessLevel: Int32
    contrastLevel: Int32
BrushType = Int32
BrushType_BrushTypeSolidColor: win32more.Windows.Win32.Graphics.GdiPlus.BrushType = 0
BrushType_BrushTypeHatchFill: win32more.Windows.Win32.Graphics.GdiPlus.BrushType = 1
BrushType_BrushTypeTextureFill: win32more.Windows.Win32.Graphics.GdiPlus.BrushType = 2
BrushType_BrushTypePathGradient: win32more.Windows.Win32.Graphics.GdiPlus.BrushType = 3
BrushType_BrushTypeLinearGradient: win32more.Windows.Win32.Graphics.GdiPlus.BrushType = 4
CGpEffect = IntPtr
CachedBitmap = IntPtr
class CharacterRange(EasyCastStructure):
    First: Int32
    Length: Int32
class Color(EasyCastStructure):
    AliceBlue = -984833
    AntiqueWhite = -332841
    Aqua = -16711681
    Aquamarine = -8388652
    Azure = -983041
    Beige = -657956
    Bisque = -6972
    Black = -16777216
    BlanchedAlmond = -5171
    Blue = -16776961
    BlueViolet = -7722014
    Brown = -5952982
    BurlyWood = -2180985
    CadetBlue = -10510688
    Chartreuse = -8388864
    Chocolate = -2987746
    Coral = -32944
    CornflowerBlue = -10185235
    Cornsilk = -1828
    Crimson = -2354116
    Cyan = -16711681
    DarkBlue = -16777077
    DarkCyan = -16741493
    DarkGoldenrod = -4684277
    DarkGray = -5658199
    DarkGreen = -16751616
    DarkKhaki = -4343957
    DarkMagenta = -7667573
    DarkOliveGreen = -11179217
    DarkOrange = -29696
    DarkOrchid = -6737204
    DarkRed = -7667712
    DarkSalmon = -1468806
    DarkSeaGreen = -7357301
    DarkSlateBlue = -12042869
    DarkSlateGray = -13676721
    DarkTurquoise = -16724271
    DarkViolet = -7077677
    DeepPink = -60269
    DeepSkyBlue = -16728065
    DimGray = -9868951
    DodgerBlue = -14774017
    Firebrick = -5103070
    FloralWhite = -1296
    ForestGreen = -14513374
    Fuchsia = -65281
    Gainsboro = -2302756
    GhostWhite = -460545
    Gold = -10496
    Goldenrod = -2448096
    Gray = -8355712
    Green = -16744448
    GreenYellow = -5374161
    Honeydew = -983056
    HotPink = -38476
    IndianRed = -3318692
    Indigo = -11861886
    Ivory = -16
    Khaki = -989556
    Lavender = -1644806
    LavenderBlush = -3851
    LawnGreen = -8586240
    LemonChiffon = -1331
    LightBlue = -5383962
    LightCoral = -1015680
    LightCyan = -2031617
    LightGoldenrodYellow = -329006
    LightGray = -2894893
    LightGreen = -7278960
    LightPink = -18751
    LightSalmon = -24454
    LightSeaGreen = -14634326
    LightSkyBlue = -7876870
    LightSlateGray = -8943463
    LightSteelBlue = -5192482
    LightYellow = -32
    Lime = -16711936
    LimeGreen = -13447886
    Linen = -331546
    Magenta = -65281
    Maroon = -8388608
    MediumAquamarine = -10039894
    MediumBlue = -16777011
    MediumOrchid = -4565549
    MediumPurple = -7114533
    MediumSeaGreen = -12799119
    MediumSlateBlue = -8689426
    MediumSpringGreen = -16713062
    MediumTurquoise = -12004916
    MediumVioletRed = -3730043
    MidnightBlue = -15132304
    MintCream = -655366
    MistyRose = -6943
    Moccasin = -6987
    NavajoWhite = -8531
    Navy = -16777088
    OldLace = -133658
    Olive = -8355840
    OliveDrab = -9728477
    Orange = -23296
    OrangeRed = -47872
    Orchid = -2461482
    PaleGoldenrod = -1120086
    PaleGreen = -6751336
    PaleTurquoise = -5247250
    PaleVioletRed = -2396013
    PapayaWhip = -4139
    PeachPuff = -9543
    Peru = -3308225
    Pink = -16181
    Plum = -2252579
    PowderBlue = -5185306
    Purple = -8388480
    Red = -65536
    RosyBrown = -4419697
    RoyalBlue = -12490271
    SaddleBrown = -7650029
    Salmon = -360334
    SandyBrown = -744352
    SeaGreen = -13726889
    SeaShell = -2578
    Sienna = -6270419
    Silver = -4144960
    SkyBlue = -7876885
    SlateBlue = -9807155
    SlateGray = -9404272
    Snow = -1286
    SpringGreen = -16711809
    SteelBlue = -12156236
    Tan = -2968436
    Teal = -16744320
    Thistle = -2572328
    Tomato = -40121
    Transparent = 16777215
    Turquoise = -12525360
    Violet = -1146130
    Wheat = -663885
    White = -1
    WhiteSmoke = -657931
    Yellow = -256
    YellowGreen = -6632142
    AlphaShift = 24
    RedShift = 16
    GreenShift = 8
    BlueShift = 0
    AlphaMask = -16777216
    RedMask = 16711680
    GreenMask = 65280
    BlueMask = 255
    Argb: UInt32
ColorAdjustType = Int32
ColorAdjustType_ColorAdjustTypeDefault: win32more.Windows.Win32.Graphics.GdiPlus.ColorAdjustType = 0
ColorAdjustType_ColorAdjustTypeBitmap: win32more.Windows.Win32.Graphics.GdiPlus.ColorAdjustType = 1
ColorAdjustType_ColorAdjustTypeBrush: win32more.Windows.Win32.Graphics.GdiPlus.ColorAdjustType = 2
ColorAdjustType_ColorAdjustTypePen: win32more.Windows.Win32.Graphics.GdiPlus.ColorAdjustType = 3
ColorAdjustType_ColorAdjustTypeText: win32more.Windows.Win32.Graphics.GdiPlus.ColorAdjustType = 4
ColorAdjustType_ColorAdjustTypeCount: win32more.Windows.Win32.Graphics.GdiPlus.ColorAdjustType = 5
ColorAdjustType_ColorAdjustTypeAny: win32more.Windows.Win32.Graphics.GdiPlus.ColorAdjustType = 6
class ColorBalance(EasyCastStructure):
    Base: win32more.Windows.Win32.Graphics.GdiPlus.Effect
class ColorBalanceParams(EasyCastStructure):
    cyanRed: Int32
    magentaGreen: Int32
    yellowBlue: Int32
ColorChannelFlags = Int32
ColorChannelFlags_ColorChannelFlagsC: win32more.Windows.Win32.Graphics.GdiPlus.ColorChannelFlags = 0
ColorChannelFlags_ColorChannelFlagsM: win32more.Windows.Win32.Graphics.GdiPlus.ColorChannelFlags = 1
ColorChannelFlags_ColorChannelFlagsY: win32more.Windows.Win32.Graphics.GdiPlus.ColorChannelFlags = 2
ColorChannelFlags_ColorChannelFlagsK: win32more.Windows.Win32.Graphics.GdiPlus.ColorChannelFlags = 3
ColorChannelFlags_ColorChannelFlagsLast: win32more.Windows.Win32.Graphics.GdiPlus.ColorChannelFlags = 4
class ColorCurve(EasyCastStructure):
    Base: win32more.Windows.Win32.Graphics.GdiPlus.Effect
class ColorCurveParams(EasyCastStructure):
    adjustment: win32more.Windows.Win32.Graphics.GdiPlus.CurveAdjustments
    channel: win32more.Windows.Win32.Graphics.GdiPlus.CurveChannel
    adjustValue: Int32
class ColorLUT(EasyCastStructure):
    Base: win32more.Windows.Win32.Graphics.GdiPlus.Effect
class ColorLUTParams(EasyCastStructure):
    lutB: Byte * 256
    lutG: Byte * 256
    lutR: Byte * 256
    lutA: Byte * 256
class ColorMap(EasyCastStructure):
    oldColor: win32more.Windows.Win32.Graphics.GdiPlus.Color
    newColor: win32more.Windows.Win32.Graphics.GdiPlus.Color
class ColorMatrix(EasyCastStructure):
    m: Single * 25
class ColorMatrixEffect(EasyCastStructure):
    Base: win32more.Windows.Win32.Graphics.GdiPlus.Effect
ColorMatrixFlags = Int32
ColorMatrixFlags_ColorMatrixFlagsDefault: win32more.Windows.Win32.Graphics.GdiPlus.ColorMatrixFlags = 0
ColorMatrixFlags_ColorMatrixFlagsSkipGrays: win32more.Windows.Win32.Graphics.GdiPlus.ColorMatrixFlags = 1
ColorMatrixFlags_ColorMatrixFlagsAltGray: win32more.Windows.Win32.Graphics.GdiPlus.ColorMatrixFlags = 2
ColorMode = Int32
ColorMode_ColorModeARGB32: win32more.Windows.Win32.Graphics.GdiPlus.ColorMode = 0
ColorMode_ColorModeARGB64: win32more.Windows.Win32.Graphics.GdiPlus.ColorMode = 1
class ColorPalette(EasyCastStructure):
    Flags: UInt32
    Count: UInt32
    Entries: UInt32 * 1
CombineMode = Int32
CombineMode_CombineModeReplace: win32more.Windows.Win32.Graphics.GdiPlus.CombineMode = 0
CombineMode_CombineModeIntersect: win32more.Windows.Win32.Graphics.GdiPlus.CombineMode = 1
CombineMode_CombineModeUnion: win32more.Windows.Win32.Graphics.GdiPlus.CombineMode = 2
CombineMode_CombineModeXor: win32more.Windows.Win32.Graphics.GdiPlus.CombineMode = 3
CombineMode_CombineModeExclude: win32more.Windows.Win32.Graphics.GdiPlus.CombineMode = 4
CombineMode_CombineModeComplement: win32more.Windows.Win32.Graphics.GdiPlus.CombineMode = 5
CompositingMode = Int32
CompositingMode_CompositingModeSourceOver: win32more.Windows.Win32.Graphics.GdiPlus.CompositingMode = 0
CompositingMode_CompositingModeSourceCopy: win32more.Windows.Win32.Graphics.GdiPlus.CompositingMode = 1
CompositingQuality = Int32
CompositingQuality_CompositingQualityInvalid: win32more.Windows.Win32.Graphics.GdiPlus.CompositingQuality = -1
CompositingQuality_CompositingQualityDefault: win32more.Windows.Win32.Graphics.GdiPlus.CompositingQuality = 0
CompositingQuality_CompositingQualityHighSpeed: win32more.Windows.Win32.Graphics.GdiPlus.CompositingQuality = 1
CompositingQuality_CompositingQualityHighQuality: win32more.Windows.Win32.Graphics.GdiPlus.CompositingQuality = 2
CompositingQuality_CompositingQualityGammaCorrected: win32more.Windows.Win32.Graphics.GdiPlus.CompositingQuality = 3
CompositingQuality_CompositingQualityAssumeLinear: win32more.Windows.Win32.Graphics.GdiPlus.CompositingQuality = 4
ConvertToEmfPlusFlags = Int32
ConvertToEmfPlusFlags_ConvertToEmfPlusFlagsDefault: win32more.Windows.Win32.Graphics.GdiPlus.ConvertToEmfPlusFlags = 0
ConvertToEmfPlusFlags_ConvertToEmfPlusFlagsRopUsed: win32more.Windows.Win32.Graphics.GdiPlus.ConvertToEmfPlusFlags = 1
ConvertToEmfPlusFlags_ConvertToEmfPlusFlagsText: win32more.Windows.Win32.Graphics.GdiPlus.ConvertToEmfPlusFlags = 2
ConvertToEmfPlusFlags_ConvertToEmfPlusFlagsInvalidRecord: win32more.Windows.Win32.Graphics.GdiPlus.ConvertToEmfPlusFlags = 4
CoordinateSpace = Int32
CoordinateSpace_CoordinateSpaceWorld: win32more.Windows.Win32.Graphics.GdiPlus.CoordinateSpace = 0
CoordinateSpace_CoordinateSpacePage: win32more.Windows.Win32.Graphics.GdiPlus.CoordinateSpace = 1
CoordinateSpace_CoordinateSpaceDevice: win32more.Windows.Win32.Graphics.GdiPlus.CoordinateSpace = 2
CurveAdjustments = Int32
CurveAdjustments_AdjustExposure: win32more.Windows.Win32.Graphics.GdiPlus.CurveAdjustments = 0
CurveAdjustments_AdjustDensity: win32more.Windows.Win32.Graphics.GdiPlus.CurveAdjustments = 1
CurveAdjustments_AdjustContrast: win32more.Windows.Win32.Graphics.GdiPlus.CurveAdjustments = 2
CurveAdjustments_AdjustHighlight: win32more.Windows.Win32.Graphics.GdiPlus.CurveAdjustments = 3
CurveAdjustments_AdjustShadow: win32more.Windows.Win32.Graphics.GdiPlus.CurveAdjustments = 4
CurveAdjustments_AdjustMidtone: win32more.Windows.Win32.Graphics.GdiPlus.CurveAdjustments = 5
CurveAdjustments_AdjustWhiteSaturation: win32more.Windows.Win32.Graphics.GdiPlus.CurveAdjustments = 6
CurveAdjustments_AdjustBlackSaturation: win32more.Windows.Win32.Graphics.GdiPlus.CurveAdjustments = 7
CurveChannel = Int32
CurveChannel_CurveChannelAll: win32more.Windows.Win32.Graphics.GdiPlus.CurveChannel = 0
CurveChannel_CurveChannelRed: win32more.Windows.Win32.Graphics.GdiPlus.CurveChannel = 1
CurveChannel_CurveChannelGreen: win32more.Windows.Win32.Graphics.GdiPlus.CurveChannel = 2
CurveChannel_CurveChannelBlue: win32more.Windows.Win32.Graphics.GdiPlus.CurveChannel = 3
CustomLineCap = IntPtr
CustomLineCapType = Int32
CustomLineCapType_CustomLineCapTypeDefault: win32more.Windows.Win32.Graphics.GdiPlus.CustomLineCapType = 0
CustomLineCapType_CustomLineCapTypeAdjustableArrow: win32more.Windows.Win32.Graphics.GdiPlus.CustomLineCapType = 1
DashCap = Int32
DashCap_DashCapFlat: win32more.Windows.Win32.Graphics.GdiPlus.DashCap = 0
DashCap_DashCapRound: win32more.Windows.Win32.Graphics.GdiPlus.DashCap = 2
DashCap_DashCapTriangle: win32more.Windows.Win32.Graphics.GdiPlus.DashCap = 3
DashStyle = Int32
DashStyle_DashStyleSolid: win32more.Windows.Win32.Graphics.GdiPlus.DashStyle = 0
DashStyle_DashStyleDash: win32more.Windows.Win32.Graphics.GdiPlus.DashStyle = 1
DashStyle_DashStyleDot: win32more.Windows.Win32.Graphics.GdiPlus.DashStyle = 2
DashStyle_DashStyleDashDot: win32more.Windows.Win32.Graphics.GdiPlus.DashStyle = 3
DashStyle_DashStyleDashDotDot: win32more.Windows.Win32.Graphics.GdiPlus.DashStyle = 4
DashStyle_DashStyleCustom: win32more.Windows.Win32.Graphics.GdiPlus.DashStyle = 5
DebugEventLevel = Int32
DebugEventLevel_DebugEventLevelFatal: win32more.Windows.Win32.Graphics.GdiPlus.DebugEventLevel = 0
DebugEventLevel_DebugEventLevelWarning: win32more.Windows.Win32.Graphics.GdiPlus.DebugEventLevel = 1
@winfunctype_pointer
def DebugEventProc(level: win32more.Windows.Win32.Graphics.GdiPlus.DebugEventLevel, message: win32more.Windows.Win32.Foundation.PSTR) -> Void: ...
DitherType = Int32
DitherType_DitherTypeNone: win32more.Windows.Win32.Graphics.GdiPlus.DitherType = 0
DitherType_DitherTypeSolid: win32more.Windows.Win32.Graphics.GdiPlus.DitherType = 1
DitherType_DitherTypeOrdered4x4: win32more.Windows.Win32.Graphics.GdiPlus.DitherType = 2
DitherType_DitherTypeOrdered8x8: win32more.Windows.Win32.Graphics.GdiPlus.DitherType = 3
DitherType_DitherTypeOrdered16x16: win32more.Windows.Win32.Graphics.GdiPlus.DitherType = 4
DitherType_DitherTypeSpiral4x4: win32more.Windows.Win32.Graphics.GdiPlus.DitherType = 5
DitherType_DitherTypeSpiral8x8: win32more.Windows.Win32.Graphics.GdiPlus.DitherType = 6
DitherType_DitherTypeDualSpiral4x4: win32more.Windows.Win32.Graphics.GdiPlus.DitherType = 7
DitherType_DitherTypeDualSpiral8x8: win32more.Windows.Win32.Graphics.GdiPlus.DitherType = 8
DitherType_DitherTypeErrorDiffusion: win32more.Windows.Win32.Graphics.GdiPlus.DitherType = 9
DitherType_DitherTypeMax: win32more.Windows.Win32.Graphics.GdiPlus.DitherType = 10
@winfunctype_pointer
def DrawImageAbort() -> win32more.Windows.Win32.Foundation.BOOL: ...
DriverStringOptions = Int32
DriverStringOptions_DriverStringOptionsCmapLookup: win32more.Windows.Win32.Graphics.GdiPlus.DriverStringOptions = 1
DriverStringOptions_DriverStringOptionsVertical: win32more.Windows.Win32.Graphics.GdiPlus.DriverStringOptions = 2
DriverStringOptions_DriverStringOptionsRealizedAdvance: win32more.Windows.Win32.Graphics.GdiPlus.DriverStringOptions = 4
DriverStringOptions_DriverStringOptionsLimitSubpixel: win32more.Windows.Win32.Graphics.GdiPlus.DriverStringOptions = 8
class ENHMETAHEADER3(EasyCastStructure):
    iType: UInt32
    nSize: UInt32
    rclBounds: win32more.Windows.Win32.Foundation.RECTL
    rclFrame: win32more.Windows.Win32.Foundation.RECTL
    dSignature: UInt32
    nVersion: UInt32
    nBytes: UInt32
    nRecords: UInt32
    nHandles: UInt16
    sReserved: UInt16
    nDescription: UInt32
    offDescription: UInt32
    nPalEntries: UInt32
    szlDevice: win32more.Windows.Win32.Foundation.SIZE
    szlMillimeters: win32more.Windows.Win32.Foundation.SIZE
class Effect(EasyCastStructure):
    lpVtbl: POINTER(VoidPtr)
    nativeEffect: POINTER(win32more.Windows.Win32.Graphics.GdiPlus.CGpEffect)
    auxDataSize: Int32
    auxData: VoidPtr
    useAuxData: win32more.Windows.Win32.Foundation.BOOL
EmfPlusRecordType = Int32
EmfPlusRecordType_WmfRecordTypeSetBkColor: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 66049
EmfPlusRecordType_WmfRecordTypeSetBkMode: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 65794
EmfPlusRecordType_WmfRecordTypeSetMapMode: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 65795
EmfPlusRecordType_WmfRecordTypeSetROP2: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 65796
EmfPlusRecordType_WmfRecordTypeSetRelAbs: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 65797
EmfPlusRecordType_WmfRecordTypeSetPolyFillMode: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 65798
EmfPlusRecordType_WmfRecordTypeSetStretchBltMode: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 65799
EmfPlusRecordType_WmfRecordTypeSetTextCharExtra: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 65800
EmfPlusRecordType_WmfRecordTypeSetTextColor: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 66057
EmfPlusRecordType_WmfRecordTypeSetTextJustification: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 66058
EmfPlusRecordType_WmfRecordTypeSetWindowOrg: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 66059
EmfPlusRecordType_WmfRecordTypeSetWindowExt: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 66060
EmfPlusRecordType_WmfRecordTypeSetViewportOrg: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 66061
EmfPlusRecordType_WmfRecordTypeSetViewportExt: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 66062
EmfPlusRecordType_WmfRecordTypeOffsetWindowOrg: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 66063
EmfPlusRecordType_WmfRecordTypeScaleWindowExt: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 66576
EmfPlusRecordType_WmfRecordTypeOffsetViewportOrg: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 66065
EmfPlusRecordType_WmfRecordTypeScaleViewportExt: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 66578
EmfPlusRecordType_WmfRecordTypeLineTo: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 66067
EmfPlusRecordType_WmfRecordTypeMoveTo: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 66068
EmfPlusRecordType_WmfRecordTypeExcludeClipRect: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 66581
EmfPlusRecordType_WmfRecordTypeIntersectClipRect: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 66582
EmfPlusRecordType_WmfRecordTypeArc: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 67607
EmfPlusRecordType_WmfRecordTypeEllipse: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 66584
EmfPlusRecordType_WmfRecordTypeFloodFill: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 66585
EmfPlusRecordType_WmfRecordTypePie: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 67610
EmfPlusRecordType_WmfRecordTypeRectangle: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 66587
EmfPlusRecordType_WmfRecordTypeRoundRect: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 67100
EmfPlusRecordType_WmfRecordTypePatBlt: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 67101
EmfPlusRecordType_WmfRecordTypeSaveDC: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 65566
EmfPlusRecordType_WmfRecordTypeSetPixel: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 66591
EmfPlusRecordType_WmfRecordTypeOffsetClipRgn: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 66080
EmfPlusRecordType_WmfRecordTypeTextOut: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 66849
EmfPlusRecordType_WmfRecordTypeBitBlt: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 67874
EmfPlusRecordType_WmfRecordTypeStretchBlt: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 68387
EmfPlusRecordType_WmfRecordTypePolygon: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 66340
EmfPlusRecordType_WmfRecordTypePolyline: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 66341
EmfPlusRecordType_WmfRecordTypeEscape: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 67110
EmfPlusRecordType_WmfRecordTypeRestoreDC: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 65831
EmfPlusRecordType_WmfRecordTypeFillRegion: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 66088
EmfPlusRecordType_WmfRecordTypeFrameRegion: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 66601
EmfPlusRecordType_WmfRecordTypeInvertRegion: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 65834
EmfPlusRecordType_WmfRecordTypePaintRegion: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 65835
EmfPlusRecordType_WmfRecordTypeSelectClipRegion: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 65836
EmfPlusRecordType_WmfRecordTypeSelectObject: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 65837
EmfPlusRecordType_WmfRecordTypeSetTextAlign: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 65838
EmfPlusRecordType_WmfRecordTypeDrawText: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 67119
EmfPlusRecordType_WmfRecordTypeChord: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 67632
EmfPlusRecordType_WmfRecordTypeSetMapperFlags: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 66097
EmfPlusRecordType_WmfRecordTypeExtTextOut: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 68146
EmfPlusRecordType_WmfRecordTypeSetDIBToDev: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 68915
EmfPlusRecordType_WmfRecordTypeSelectPalette: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 66100
EmfPlusRecordType_WmfRecordTypeRealizePalette: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 65589
EmfPlusRecordType_WmfRecordTypeAnimatePalette: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 66614
EmfPlusRecordType_WmfRecordTypeSetPalEntries: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 65591
EmfPlusRecordType_WmfRecordTypePolyPolygon: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 66872
EmfPlusRecordType_WmfRecordTypeResizePalette: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 65849
EmfPlusRecordType_WmfRecordTypeDIBBitBlt: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 67904
EmfPlusRecordType_WmfRecordTypeDIBStretchBlt: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 68417
EmfPlusRecordType_WmfRecordTypeDIBCreatePatternBrush: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 65858
EmfPlusRecordType_WmfRecordTypeStretchDIB: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 69443
EmfPlusRecordType_WmfRecordTypeExtFloodFill: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 66888
EmfPlusRecordType_WmfRecordTypeSetLayout: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 65865
EmfPlusRecordType_WmfRecordTypeResetDC: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 65868
EmfPlusRecordType_WmfRecordTypeStartDoc: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 65869
EmfPlusRecordType_WmfRecordTypeStartPage: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 65615
EmfPlusRecordType_WmfRecordTypeEndPage: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 65616
EmfPlusRecordType_WmfRecordTypeAbortDoc: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 65618
EmfPlusRecordType_WmfRecordTypeEndDoc: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 65630
EmfPlusRecordType_WmfRecordTypeDeleteObject: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 66032
EmfPlusRecordType_WmfRecordTypeCreatePalette: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 65783
EmfPlusRecordType_WmfRecordTypeCreateBrush: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 65784
EmfPlusRecordType_WmfRecordTypeCreatePatternBrush: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 66041
EmfPlusRecordType_WmfRecordTypeCreatePenIndirect: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 66298
EmfPlusRecordType_WmfRecordTypeCreateFontIndirect: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 66299
EmfPlusRecordType_WmfRecordTypeCreateBrushIndirect: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 66300
EmfPlusRecordType_WmfRecordTypeCreateBitmapIndirect: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 66301
EmfPlusRecordType_WmfRecordTypeCreateBitmap: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 67326
EmfPlusRecordType_WmfRecordTypeCreateRegion: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 67327
EmfPlusRecordType_EmfRecordTypeHeader: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 1
EmfPlusRecordType_EmfRecordTypePolyBezier: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 2
EmfPlusRecordType_EmfRecordTypePolygon: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 3
EmfPlusRecordType_EmfRecordTypePolyline: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 4
EmfPlusRecordType_EmfRecordTypePolyBezierTo: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 5
EmfPlusRecordType_EmfRecordTypePolyLineTo: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 6
EmfPlusRecordType_EmfRecordTypePolyPolyline: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 7
EmfPlusRecordType_EmfRecordTypePolyPolygon: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 8
EmfPlusRecordType_EmfRecordTypeSetWindowExtEx: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 9
EmfPlusRecordType_EmfRecordTypeSetWindowOrgEx: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 10
EmfPlusRecordType_EmfRecordTypeSetViewportExtEx: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 11
EmfPlusRecordType_EmfRecordTypeSetViewportOrgEx: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 12
EmfPlusRecordType_EmfRecordTypeSetBrushOrgEx: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 13
EmfPlusRecordType_EmfRecordTypeEOF: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 14
EmfPlusRecordType_EmfRecordTypeSetPixelV: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 15
EmfPlusRecordType_EmfRecordTypeSetMapperFlags: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 16
EmfPlusRecordType_EmfRecordTypeSetMapMode: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 17
EmfPlusRecordType_EmfRecordTypeSetBkMode: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 18
EmfPlusRecordType_EmfRecordTypeSetPolyFillMode: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 19
EmfPlusRecordType_EmfRecordTypeSetROP2: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 20
EmfPlusRecordType_EmfRecordTypeSetStretchBltMode: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 21
EmfPlusRecordType_EmfRecordTypeSetTextAlign: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 22
EmfPlusRecordType_EmfRecordTypeSetColorAdjustment: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 23
EmfPlusRecordType_EmfRecordTypeSetTextColor: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 24
EmfPlusRecordType_EmfRecordTypeSetBkColor: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 25
EmfPlusRecordType_EmfRecordTypeOffsetClipRgn: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 26
EmfPlusRecordType_EmfRecordTypeMoveToEx: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 27
EmfPlusRecordType_EmfRecordTypeSetMetaRgn: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 28
EmfPlusRecordType_EmfRecordTypeExcludeClipRect: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 29
EmfPlusRecordType_EmfRecordTypeIntersectClipRect: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 30
EmfPlusRecordType_EmfRecordTypeScaleViewportExtEx: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 31
EmfPlusRecordType_EmfRecordTypeScaleWindowExtEx: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 32
EmfPlusRecordType_EmfRecordTypeSaveDC: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 33
EmfPlusRecordType_EmfRecordTypeRestoreDC: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 34
EmfPlusRecordType_EmfRecordTypeSetWorldTransform: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 35
EmfPlusRecordType_EmfRecordTypeModifyWorldTransform: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 36
EmfPlusRecordType_EmfRecordTypeSelectObject: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 37
EmfPlusRecordType_EmfRecordTypeCreatePen: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 38
EmfPlusRecordType_EmfRecordTypeCreateBrushIndirect: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 39
EmfPlusRecordType_EmfRecordTypeDeleteObject: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 40
EmfPlusRecordType_EmfRecordTypeAngleArc: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 41
EmfPlusRecordType_EmfRecordTypeEllipse: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 42
EmfPlusRecordType_EmfRecordTypeRectangle: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 43
EmfPlusRecordType_EmfRecordTypeRoundRect: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 44
EmfPlusRecordType_EmfRecordTypeArc: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 45
EmfPlusRecordType_EmfRecordTypeChord: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 46
EmfPlusRecordType_EmfRecordTypePie: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 47
EmfPlusRecordType_EmfRecordTypeSelectPalette: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 48
EmfPlusRecordType_EmfRecordTypeCreatePalette: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 49
EmfPlusRecordType_EmfRecordTypeSetPaletteEntries: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 50
EmfPlusRecordType_EmfRecordTypeResizePalette: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 51
EmfPlusRecordType_EmfRecordTypeRealizePalette: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 52
EmfPlusRecordType_EmfRecordTypeExtFloodFill: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 53
EmfPlusRecordType_EmfRecordTypeLineTo: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 54
EmfPlusRecordType_EmfRecordTypeArcTo: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 55
EmfPlusRecordType_EmfRecordTypePolyDraw: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 56
EmfPlusRecordType_EmfRecordTypeSetArcDirection: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 57
EmfPlusRecordType_EmfRecordTypeSetMiterLimit: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 58
EmfPlusRecordType_EmfRecordTypeBeginPath: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 59
EmfPlusRecordType_EmfRecordTypeEndPath: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 60
EmfPlusRecordType_EmfRecordTypeCloseFigure: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 61
EmfPlusRecordType_EmfRecordTypeFillPath: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 62
EmfPlusRecordType_EmfRecordTypeStrokeAndFillPath: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 63
EmfPlusRecordType_EmfRecordTypeStrokePath: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 64
EmfPlusRecordType_EmfRecordTypeFlattenPath: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 65
EmfPlusRecordType_EmfRecordTypeWidenPath: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 66
EmfPlusRecordType_EmfRecordTypeSelectClipPath: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 67
EmfPlusRecordType_EmfRecordTypeAbortPath: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 68
EmfPlusRecordType_EmfRecordTypeReserved_069: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 69
EmfPlusRecordType_EmfRecordTypeGdiComment: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 70
EmfPlusRecordType_EmfRecordTypeFillRgn: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 71
EmfPlusRecordType_EmfRecordTypeFrameRgn: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 72
EmfPlusRecordType_EmfRecordTypeInvertRgn: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 73
EmfPlusRecordType_EmfRecordTypePaintRgn: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 74
EmfPlusRecordType_EmfRecordTypeExtSelectClipRgn: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 75
EmfPlusRecordType_EmfRecordTypeBitBlt: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 76
EmfPlusRecordType_EmfRecordTypeStretchBlt: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 77
EmfPlusRecordType_EmfRecordTypeMaskBlt: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 78
EmfPlusRecordType_EmfRecordTypePlgBlt: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 79
EmfPlusRecordType_EmfRecordTypeSetDIBitsToDevice: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 80
EmfPlusRecordType_EmfRecordTypeStretchDIBits: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 81
EmfPlusRecordType_EmfRecordTypeExtCreateFontIndirect: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 82
EmfPlusRecordType_EmfRecordTypeExtTextOutA: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 83
EmfPlusRecordType_EmfRecordTypeExtTextOutW: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 84
EmfPlusRecordType_EmfRecordTypePolyBezier16: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 85
EmfPlusRecordType_EmfRecordTypePolygon16: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 86
EmfPlusRecordType_EmfRecordTypePolyline16: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 87
EmfPlusRecordType_EmfRecordTypePolyBezierTo16: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 88
EmfPlusRecordType_EmfRecordTypePolylineTo16: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 89
EmfPlusRecordType_EmfRecordTypePolyPolyline16: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 90
EmfPlusRecordType_EmfRecordTypePolyPolygon16: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 91
EmfPlusRecordType_EmfRecordTypePolyDraw16: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 92
EmfPlusRecordType_EmfRecordTypeCreateMonoBrush: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 93
EmfPlusRecordType_EmfRecordTypeCreateDIBPatternBrushPt: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 94
EmfPlusRecordType_EmfRecordTypeExtCreatePen: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 95
EmfPlusRecordType_EmfRecordTypePolyTextOutA: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 96
EmfPlusRecordType_EmfRecordTypePolyTextOutW: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 97
EmfPlusRecordType_EmfRecordTypeSetICMMode: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 98
EmfPlusRecordType_EmfRecordTypeCreateColorSpace: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 99
EmfPlusRecordType_EmfRecordTypeSetColorSpace: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 100
EmfPlusRecordType_EmfRecordTypeDeleteColorSpace: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 101
EmfPlusRecordType_EmfRecordTypeGLSRecord: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 102
EmfPlusRecordType_EmfRecordTypeGLSBoundedRecord: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 103
EmfPlusRecordType_EmfRecordTypePixelFormat: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 104
EmfPlusRecordType_EmfRecordTypeDrawEscape: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 105
EmfPlusRecordType_EmfRecordTypeExtEscape: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 106
EmfPlusRecordType_EmfRecordTypeStartDoc: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 107
EmfPlusRecordType_EmfRecordTypeSmallTextOut: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 108
EmfPlusRecordType_EmfRecordTypeForceUFIMapping: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 109
EmfPlusRecordType_EmfRecordTypeNamedEscape: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 110
EmfPlusRecordType_EmfRecordTypeColorCorrectPalette: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 111
EmfPlusRecordType_EmfRecordTypeSetICMProfileA: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 112
EmfPlusRecordType_EmfRecordTypeSetICMProfileW: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 113
EmfPlusRecordType_EmfRecordTypeAlphaBlend: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 114
EmfPlusRecordType_EmfRecordTypeSetLayout: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 115
EmfPlusRecordType_EmfRecordTypeTransparentBlt: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 116
EmfPlusRecordType_EmfRecordTypeReserved_117: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 117
EmfPlusRecordType_EmfRecordTypeGradientFill: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 118
EmfPlusRecordType_EmfRecordTypeSetLinkedUFIs: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 119
EmfPlusRecordType_EmfRecordTypeSetTextJustification: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 120
EmfPlusRecordType_EmfRecordTypeColorMatchToTargetW: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 121
EmfPlusRecordType_EmfRecordTypeCreateColorSpaceW: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 122
EmfPlusRecordType_EmfRecordTypeMax: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 122
EmfPlusRecordType_EmfRecordTypeMin: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 1
EmfPlusRecordType_EmfPlusRecordTypeInvalid: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 16384
EmfPlusRecordType_EmfPlusRecordTypeHeader: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 16385
EmfPlusRecordType_EmfPlusRecordTypeEndOfFile: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 16386
EmfPlusRecordType_EmfPlusRecordTypeComment: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 16387
EmfPlusRecordType_EmfPlusRecordTypeGetDC: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 16388
EmfPlusRecordType_EmfPlusRecordTypeMultiFormatStart: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 16389
EmfPlusRecordType_EmfPlusRecordTypeMultiFormatSection: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 16390
EmfPlusRecordType_EmfPlusRecordTypeMultiFormatEnd: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 16391
EmfPlusRecordType_EmfPlusRecordTypeObject: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 16392
EmfPlusRecordType_EmfPlusRecordTypeClear: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 16393
EmfPlusRecordType_EmfPlusRecordTypeFillRects: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 16394
EmfPlusRecordType_EmfPlusRecordTypeDrawRects: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 16395
EmfPlusRecordType_EmfPlusRecordTypeFillPolygon: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 16396
EmfPlusRecordType_EmfPlusRecordTypeDrawLines: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 16397
EmfPlusRecordType_EmfPlusRecordTypeFillEllipse: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 16398
EmfPlusRecordType_EmfPlusRecordTypeDrawEllipse: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 16399
EmfPlusRecordType_EmfPlusRecordTypeFillPie: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 16400
EmfPlusRecordType_EmfPlusRecordTypeDrawPie: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 16401
EmfPlusRecordType_EmfPlusRecordTypeDrawArc: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 16402
EmfPlusRecordType_EmfPlusRecordTypeFillRegion: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 16403
EmfPlusRecordType_EmfPlusRecordTypeFillPath: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 16404
EmfPlusRecordType_EmfPlusRecordTypeDrawPath: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 16405
EmfPlusRecordType_EmfPlusRecordTypeFillClosedCurve: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 16406
EmfPlusRecordType_EmfPlusRecordTypeDrawClosedCurve: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 16407
EmfPlusRecordType_EmfPlusRecordTypeDrawCurve: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 16408
EmfPlusRecordType_EmfPlusRecordTypeDrawBeziers: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 16409
EmfPlusRecordType_EmfPlusRecordTypeDrawImage: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 16410
EmfPlusRecordType_EmfPlusRecordTypeDrawImagePoints: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 16411
EmfPlusRecordType_EmfPlusRecordTypeDrawString: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 16412
EmfPlusRecordType_EmfPlusRecordTypeSetRenderingOrigin: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 16413
EmfPlusRecordType_EmfPlusRecordTypeSetAntiAliasMode: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 16414
EmfPlusRecordType_EmfPlusRecordTypeSetTextRenderingHint: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 16415
EmfPlusRecordType_EmfPlusRecordTypeSetTextContrast: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 16416
EmfPlusRecordType_EmfPlusRecordTypeSetInterpolationMode: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 16417
EmfPlusRecordType_EmfPlusRecordTypeSetPixelOffsetMode: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 16418
EmfPlusRecordType_EmfPlusRecordTypeSetCompositingMode: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 16419
EmfPlusRecordType_EmfPlusRecordTypeSetCompositingQuality: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 16420
EmfPlusRecordType_EmfPlusRecordTypeSave: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 16421
EmfPlusRecordType_EmfPlusRecordTypeRestore: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 16422
EmfPlusRecordType_EmfPlusRecordTypeBeginContainer: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 16423
EmfPlusRecordType_EmfPlusRecordTypeBeginContainerNoParams: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 16424
EmfPlusRecordType_EmfPlusRecordTypeEndContainer: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 16425
EmfPlusRecordType_EmfPlusRecordTypeSetWorldTransform: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 16426
EmfPlusRecordType_EmfPlusRecordTypeResetWorldTransform: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 16427
EmfPlusRecordType_EmfPlusRecordTypeMultiplyWorldTransform: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 16428
EmfPlusRecordType_EmfPlusRecordTypeTranslateWorldTransform: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 16429
EmfPlusRecordType_EmfPlusRecordTypeScaleWorldTransform: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 16430
EmfPlusRecordType_EmfPlusRecordTypeRotateWorldTransform: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 16431
EmfPlusRecordType_EmfPlusRecordTypeSetPageTransform: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 16432
EmfPlusRecordType_EmfPlusRecordTypeResetClip: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 16433
EmfPlusRecordType_EmfPlusRecordTypeSetClipRect: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 16434
EmfPlusRecordType_EmfPlusRecordTypeSetClipPath: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 16435
EmfPlusRecordType_EmfPlusRecordTypeSetClipRegion: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 16436
EmfPlusRecordType_EmfPlusRecordTypeOffsetClip: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 16437
EmfPlusRecordType_EmfPlusRecordTypeDrawDriverString: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 16438
EmfPlusRecordType_EmfPlusRecordTypeStrokeFillPath: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 16439
EmfPlusRecordType_EmfPlusRecordTypeSerializableObject: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 16440
EmfPlusRecordType_EmfPlusRecordTypeSetTSGraphics: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 16441
EmfPlusRecordType_EmfPlusRecordTypeSetTSClip: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 16442
EmfPlusRecordType_EmfPlusRecordTotal: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 16443
EmfPlusRecordType_EmfPlusRecordTypeMax: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 16442
EmfPlusRecordType_EmfPlusRecordTypeMin: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType = 16385
EmfToWmfBitsFlags = Int32
EmfToWmfBitsFlags_EmfToWmfBitsFlagsDefault: win32more.Windows.Win32.Graphics.GdiPlus.EmfToWmfBitsFlags = 0
EmfToWmfBitsFlags_EmfToWmfBitsFlagsEmbedEmf: win32more.Windows.Win32.Graphics.GdiPlus.EmfToWmfBitsFlags = 1
EmfToWmfBitsFlags_EmfToWmfBitsFlagsIncludePlaceable: win32more.Windows.Win32.Graphics.GdiPlus.EmfToWmfBitsFlags = 2
EmfToWmfBitsFlags_EmfToWmfBitsFlagsNoXORClip: win32more.Windows.Win32.Graphics.GdiPlus.EmfToWmfBitsFlags = 4
EmfType = Int32
EmfType_EmfTypeEmfOnly: win32more.Windows.Win32.Graphics.GdiPlus.EmfType = 3
EmfType_EmfTypeEmfPlusOnly: win32more.Windows.Win32.Graphics.GdiPlus.EmfType = 4
EmfType_EmfTypeEmfPlusDual: win32more.Windows.Win32.Graphics.GdiPlus.EmfType = 5
class EncoderParameter(EasyCastStructure):
    Guid: Guid
    NumberOfValues: UInt32
    Type: UInt32
    Value: VoidPtr
EncoderParameterValueType = Int32
EncoderParameterValueType_EncoderParameterValueTypeByte: win32more.Windows.Win32.Graphics.GdiPlus.EncoderParameterValueType = 1
EncoderParameterValueType_EncoderParameterValueTypeASCII: win32more.Windows.Win32.Graphics.GdiPlus.EncoderParameterValueType = 2
EncoderParameterValueType_EncoderParameterValueTypeShort: win32more.Windows.Win32.Graphics.GdiPlus.EncoderParameterValueType = 3
EncoderParameterValueType_EncoderParameterValueTypeLong: win32more.Windows.Win32.Graphics.GdiPlus.EncoderParameterValueType = 4
EncoderParameterValueType_EncoderParameterValueTypeRational: win32more.Windows.Win32.Graphics.GdiPlus.EncoderParameterValueType = 5
EncoderParameterValueType_EncoderParameterValueTypeLongRange: win32more.Windows.Win32.Graphics.GdiPlus.EncoderParameterValueType = 6
EncoderParameterValueType_EncoderParameterValueTypeUndefined: win32more.Windows.Win32.Graphics.GdiPlus.EncoderParameterValueType = 7
EncoderParameterValueType_EncoderParameterValueTypeRationalRange: win32more.Windows.Win32.Graphics.GdiPlus.EncoderParameterValueType = 8
EncoderParameterValueType_EncoderParameterValueTypePointer: win32more.Windows.Win32.Graphics.GdiPlus.EncoderParameterValueType = 9
class EncoderParameters(EasyCastStructure):
    Count: UInt32
    Parameter: win32more.Windows.Win32.Graphics.GdiPlus.EncoderParameter * 1
EncoderValue = Int32
EncoderValue_EncoderValueColorTypeCMYK: win32more.Windows.Win32.Graphics.GdiPlus.EncoderValue = 0
EncoderValue_EncoderValueColorTypeYCCK: win32more.Windows.Win32.Graphics.GdiPlus.EncoderValue = 1
EncoderValue_EncoderValueCompressionLZW: win32more.Windows.Win32.Graphics.GdiPlus.EncoderValue = 2
EncoderValue_EncoderValueCompressionCCITT3: win32more.Windows.Win32.Graphics.GdiPlus.EncoderValue = 3
EncoderValue_EncoderValueCompressionCCITT4: win32more.Windows.Win32.Graphics.GdiPlus.EncoderValue = 4
EncoderValue_EncoderValueCompressionRle: win32more.Windows.Win32.Graphics.GdiPlus.EncoderValue = 5
EncoderValue_EncoderValueCompressionNone: win32more.Windows.Win32.Graphics.GdiPlus.EncoderValue = 6
EncoderValue_EncoderValueScanMethodInterlaced: win32more.Windows.Win32.Graphics.GdiPlus.EncoderValue = 7
EncoderValue_EncoderValueScanMethodNonInterlaced: win32more.Windows.Win32.Graphics.GdiPlus.EncoderValue = 8
EncoderValue_EncoderValueVersionGif87: win32more.Windows.Win32.Graphics.GdiPlus.EncoderValue = 9
EncoderValue_EncoderValueVersionGif89: win32more.Windows.Win32.Graphics.GdiPlus.EncoderValue = 10
EncoderValue_EncoderValueRenderProgressive: win32more.Windows.Win32.Graphics.GdiPlus.EncoderValue = 11
EncoderValue_EncoderValueRenderNonProgressive: win32more.Windows.Win32.Graphics.GdiPlus.EncoderValue = 12
EncoderValue_EncoderValueTransformRotate90: win32more.Windows.Win32.Graphics.GdiPlus.EncoderValue = 13
EncoderValue_EncoderValueTransformRotate180: win32more.Windows.Win32.Graphics.GdiPlus.EncoderValue = 14
EncoderValue_EncoderValueTransformRotate270: win32more.Windows.Win32.Graphics.GdiPlus.EncoderValue = 15
EncoderValue_EncoderValueTransformFlipHorizontal: win32more.Windows.Win32.Graphics.GdiPlus.EncoderValue = 16
EncoderValue_EncoderValueTransformFlipVertical: win32more.Windows.Win32.Graphics.GdiPlus.EncoderValue = 17
EncoderValue_EncoderValueMultiFrame: win32more.Windows.Win32.Graphics.GdiPlus.EncoderValue = 18
EncoderValue_EncoderValueLastFrame: win32more.Windows.Win32.Graphics.GdiPlus.EncoderValue = 19
EncoderValue_EncoderValueFlush: win32more.Windows.Win32.Graphics.GdiPlus.EncoderValue = 20
EncoderValue_EncoderValueFrameDimensionTime: win32more.Windows.Win32.Graphics.GdiPlus.EncoderValue = 21
EncoderValue_EncoderValueFrameDimensionResolution: win32more.Windows.Win32.Graphics.GdiPlus.EncoderValue = 22
EncoderValue_EncoderValueFrameDimensionPage: win32more.Windows.Win32.Graphics.GdiPlus.EncoderValue = 23
EncoderValue_EncoderValueColorTypeGray: win32more.Windows.Win32.Graphics.GdiPlus.EncoderValue = 24
EncoderValue_EncoderValueColorTypeRGB: win32more.Windows.Win32.Graphics.GdiPlus.EncoderValue = 25
@winfunctype_pointer
def EnumerateMetafileProc(param0: win32more.Windows.Win32.Graphics.GdiPlus.EmfPlusRecordType, param1: UInt32, param2: UInt32, param3: POINTER(Byte), param4: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
FillMode = Int32
FillMode_FillModeAlternate: win32more.Windows.Win32.Graphics.GdiPlus.FillMode = 0
FillMode_FillModeWinding: win32more.Windows.Win32.Graphics.GdiPlus.FillMode = 1
FlushIntention = Int32
FlushIntention_FlushIntentionFlush: win32more.Windows.Win32.Graphics.GdiPlus.FlushIntention = 0
FlushIntention_FlushIntentionSync: win32more.Windows.Win32.Graphics.GdiPlus.FlushIntention = 1
Font = IntPtr
FontCollection = IntPtr
FontFamily = IntPtr
FontStyle = Int32
FontStyle_FontStyleRegular: win32more.Windows.Win32.Graphics.GdiPlus.FontStyle = 0
FontStyle_FontStyleBold: win32more.Windows.Win32.Graphics.GdiPlus.FontStyle = 1
FontStyle_FontStyleItalic: win32more.Windows.Win32.Graphics.GdiPlus.FontStyle = 2
FontStyle_FontStyleBoldItalic: win32more.Windows.Win32.Graphics.GdiPlus.FontStyle = 3
FontStyle_FontStyleUnderline: win32more.Windows.Win32.Graphics.GdiPlus.FontStyle = 4
FontStyle_FontStyleStrikeout: win32more.Windows.Win32.Graphics.GdiPlus.FontStyle = 8
class GdiplusAbort(ComPtr):
    extends: None
    @commethod(0)
    def Abort(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class GdiplusStartupInput(EasyCastStructure):
    GdiplusVersion: UInt32
    DebugEventCallback: IntPtr
    SuppressBackgroundThread: win32more.Windows.Win32.Foundation.BOOL
    SuppressExternalCodecs: win32more.Windows.Win32.Foundation.BOOL
class GdiplusStartupInputEx(EasyCastStructure):
    Base: win32more.Windows.Win32.Graphics.GdiPlus.GdiplusStartupInput
    StartupParameters: Int32
class GdiplusStartupOutput(EasyCastStructure):
    NotificationHook: IntPtr
    NotificationUnhook: IntPtr
GdiplusStartupParams = Int32
GdiplusStartupParams_GdiplusStartupDefault: win32more.Windows.Win32.Graphics.GdiPlus.GdiplusStartupParams = 0
GdiplusStartupParams_GdiplusStartupNoSetRound: win32more.Windows.Win32.Graphics.GdiPlus.GdiplusStartupParams = 1
GdiplusStartupParams_GdiplusStartupSetPSValue: win32more.Windows.Win32.Graphics.GdiPlus.GdiplusStartupParams = 2
GdiplusStartupParams_GdiplusStartupTransparencyMask: win32more.Windows.Win32.Graphics.GdiPlus.GdiplusStartupParams = -16777216
GenericFontFamily = Int32
GenericFontFamily_GenericFontFamilySerif: win32more.Windows.Win32.Graphics.GdiPlus.GenericFontFamily = 0
GenericFontFamily_GenericFontFamilySansSerif: win32more.Windows.Win32.Graphics.GdiPlus.GenericFontFamily = 1
GenericFontFamily_GenericFontFamilyMonospace: win32more.Windows.Win32.Graphics.GdiPlus.GenericFontFamily = 2
@winfunctype_pointer
def GetThumbnailImageAbort() -> win32more.Windows.Win32.Foundation.BOOL: ...
GpAdjustableArrowCap = IntPtr
GpBitmap = IntPtr
GpBrush = IntPtr
GpCachedBitmap = IntPtr
GpCustomLineCap = IntPtr
GpFont = IntPtr
GpFontCollection = IntPtr
GpFontFamily = IntPtr
GpGraphics = IntPtr
GpHatch = IntPtr
GpImage = IntPtr
GpImageAttributes = IntPtr
GpInstalledFontCollection = IntPtr
GpLineGradient = IntPtr
GpMetafile = IntPtr
GpPath = IntPtr
GpPathGradient = IntPtr
GpPathIterator = IntPtr
GpPen = IntPtr
GpPrivateFontCollection = IntPtr
GpRegion = IntPtr
GpSolidFill = IntPtr
GpStringFormat = IntPtr
GpTestControlEnum = Int32
GpTestControlEnum_TestControlForceBilinear: win32more.Windows.Win32.Graphics.GdiPlus.GpTestControlEnum = 0
GpTestControlEnum_TestControlNoICM: win32more.Windows.Win32.Graphics.GdiPlus.GpTestControlEnum = 1
GpTestControlEnum_TestControlGetBuildNumber: win32more.Windows.Win32.Graphics.GdiPlus.GpTestControlEnum = 2
GpTexture = IntPtr
HatchStyle = Int32
HatchStyle_HatchStyleHorizontal: win32more.Windows.Win32.Graphics.GdiPlus.HatchStyle = 0
HatchStyle_HatchStyleVertical: win32more.Windows.Win32.Graphics.GdiPlus.HatchStyle = 1
HatchStyle_HatchStyleForwardDiagonal: win32more.Windows.Win32.Graphics.GdiPlus.HatchStyle = 2
HatchStyle_HatchStyleBackwardDiagonal: win32more.Windows.Win32.Graphics.GdiPlus.HatchStyle = 3
HatchStyle_HatchStyleCross: win32more.Windows.Win32.Graphics.GdiPlus.HatchStyle = 4
HatchStyle_HatchStyleDiagonalCross: win32more.Windows.Win32.Graphics.GdiPlus.HatchStyle = 5
HatchStyle_HatchStyle05Percent: win32more.Windows.Win32.Graphics.GdiPlus.HatchStyle = 6
HatchStyle_HatchStyle10Percent: win32more.Windows.Win32.Graphics.GdiPlus.HatchStyle = 7
HatchStyle_HatchStyle20Percent: win32more.Windows.Win32.Graphics.GdiPlus.HatchStyle = 8
HatchStyle_HatchStyle25Percent: win32more.Windows.Win32.Graphics.GdiPlus.HatchStyle = 9
HatchStyle_HatchStyle30Percent: win32more.Windows.Win32.Graphics.GdiPlus.HatchStyle = 10
HatchStyle_HatchStyle40Percent: win32more.Windows.Win32.Graphics.GdiPlus.HatchStyle = 11
HatchStyle_HatchStyle50Percent: win32more.Windows.Win32.Graphics.GdiPlus.HatchStyle = 12
HatchStyle_HatchStyle60Percent: win32more.Windows.Win32.Graphics.GdiPlus.HatchStyle = 13
HatchStyle_HatchStyle70Percent: win32more.Windows.Win32.Graphics.GdiPlus.HatchStyle = 14
HatchStyle_HatchStyle75Percent: win32more.Windows.Win32.Graphics.GdiPlus.HatchStyle = 15
HatchStyle_HatchStyle80Percent: win32more.Windows.Win32.Graphics.GdiPlus.HatchStyle = 16
HatchStyle_HatchStyle90Percent: win32more.Windows.Win32.Graphics.GdiPlus.HatchStyle = 17
HatchStyle_HatchStyleLightDownwardDiagonal: win32more.Windows.Win32.Graphics.GdiPlus.HatchStyle = 18
HatchStyle_HatchStyleLightUpwardDiagonal: win32more.Windows.Win32.Graphics.GdiPlus.HatchStyle = 19
HatchStyle_HatchStyleDarkDownwardDiagonal: win32more.Windows.Win32.Graphics.GdiPlus.HatchStyle = 20
HatchStyle_HatchStyleDarkUpwardDiagonal: win32more.Windows.Win32.Graphics.GdiPlus.HatchStyle = 21
HatchStyle_HatchStyleWideDownwardDiagonal: win32more.Windows.Win32.Graphics.GdiPlus.HatchStyle = 22
HatchStyle_HatchStyleWideUpwardDiagonal: win32more.Windows.Win32.Graphics.GdiPlus.HatchStyle = 23
HatchStyle_HatchStyleLightVertical: win32more.Windows.Win32.Graphics.GdiPlus.HatchStyle = 24
HatchStyle_HatchStyleLightHorizontal: win32more.Windows.Win32.Graphics.GdiPlus.HatchStyle = 25
HatchStyle_HatchStyleNarrowVertical: win32more.Windows.Win32.Graphics.GdiPlus.HatchStyle = 26
HatchStyle_HatchStyleNarrowHorizontal: win32more.Windows.Win32.Graphics.GdiPlus.HatchStyle = 27
HatchStyle_HatchStyleDarkVertical: win32more.Windows.Win32.Graphics.GdiPlus.HatchStyle = 28
HatchStyle_HatchStyleDarkHorizontal: win32more.Windows.Win32.Graphics.GdiPlus.HatchStyle = 29
HatchStyle_HatchStyleDashedDownwardDiagonal: win32more.Windows.Win32.Graphics.GdiPlus.HatchStyle = 30
HatchStyle_HatchStyleDashedUpwardDiagonal: win32more.Windows.Win32.Graphics.GdiPlus.HatchStyle = 31
HatchStyle_HatchStyleDashedHorizontal: win32more.Windows.Win32.Graphics.GdiPlus.HatchStyle = 32
HatchStyle_HatchStyleDashedVertical: win32more.Windows.Win32.Graphics.GdiPlus.HatchStyle = 33
HatchStyle_HatchStyleSmallConfetti: win32more.Windows.Win32.Graphics.GdiPlus.HatchStyle = 34
HatchStyle_HatchStyleLargeConfetti: win32more.Windows.Win32.Graphics.GdiPlus.HatchStyle = 35
HatchStyle_HatchStyleZigZag: win32more.Windows.Win32.Graphics.GdiPlus.HatchStyle = 36
HatchStyle_HatchStyleWave: win32more.Windows.Win32.Graphics.GdiPlus.HatchStyle = 37
HatchStyle_HatchStyleDiagonalBrick: win32more.Windows.Win32.Graphics.GdiPlus.HatchStyle = 38
HatchStyle_HatchStyleHorizontalBrick: win32more.Windows.Win32.Graphics.GdiPlus.HatchStyle = 39
HatchStyle_HatchStyleWeave: win32more.Windows.Win32.Graphics.GdiPlus.HatchStyle = 40
HatchStyle_HatchStylePlaid: win32more.Windows.Win32.Graphics.GdiPlus.HatchStyle = 41
HatchStyle_HatchStyleDivot: win32more.Windows.Win32.Graphics.GdiPlus.HatchStyle = 42
HatchStyle_HatchStyleDottedGrid: win32more.Windows.Win32.Graphics.GdiPlus.HatchStyle = 43
HatchStyle_HatchStyleDottedDiamond: win32more.Windows.Win32.Graphics.GdiPlus.HatchStyle = 44
HatchStyle_HatchStyleShingle: win32more.Windows.Win32.Graphics.GdiPlus.HatchStyle = 45
HatchStyle_HatchStyleTrellis: win32more.Windows.Win32.Graphics.GdiPlus.HatchStyle = 46
HatchStyle_HatchStyleSphere: win32more.Windows.Win32.Graphics.GdiPlus.HatchStyle = 47
HatchStyle_HatchStyleSmallGrid: win32more.Windows.Win32.Graphics.GdiPlus.HatchStyle = 48
HatchStyle_HatchStyleSmallCheckerBoard: win32more.Windows.Win32.Graphics.GdiPlus.HatchStyle = 49
HatchStyle_HatchStyleLargeCheckerBoard: win32more.Windows.Win32.Graphics.GdiPlus.HatchStyle = 50
HatchStyle_HatchStyleOutlinedDiamond: win32more.Windows.Win32.Graphics.GdiPlus.HatchStyle = 51
HatchStyle_HatchStyleSolidDiamond: win32more.Windows.Win32.Graphics.GdiPlus.HatchStyle = 52
HatchStyle_HatchStyleTotal: win32more.Windows.Win32.Graphics.GdiPlus.HatchStyle = 53
HatchStyle_HatchStyleLargeGrid: win32more.Windows.Win32.Graphics.GdiPlus.HatchStyle = 4
HatchStyle_HatchStyleMin: win32more.Windows.Win32.Graphics.GdiPlus.HatchStyle = 0
HatchStyle_HatchStyleMax: win32more.Windows.Win32.Graphics.GdiPlus.HatchStyle = 52
HistogramFormat = Int32
HistogramFormat_HistogramFormatARGB: win32more.Windows.Win32.Graphics.GdiPlus.HistogramFormat = 0
HistogramFormat_HistogramFormatPARGB: win32more.Windows.Win32.Graphics.GdiPlus.HistogramFormat = 1
HistogramFormat_HistogramFormatRGB: win32more.Windows.Win32.Graphics.GdiPlus.HistogramFormat = 2
HistogramFormat_HistogramFormatGray: win32more.Windows.Win32.Graphics.GdiPlus.HistogramFormat = 3
HistogramFormat_HistogramFormatB: win32more.Windows.Win32.Graphics.GdiPlus.HistogramFormat = 4
HistogramFormat_HistogramFormatG: win32more.Windows.Win32.Graphics.GdiPlus.HistogramFormat = 5
HistogramFormat_HistogramFormatR: win32more.Windows.Win32.Graphics.GdiPlus.HistogramFormat = 6
HistogramFormat_HistogramFormatA: win32more.Windows.Win32.Graphics.GdiPlus.HistogramFormat = 7
HotkeyPrefix = Int32
HotkeyPrefix_HotkeyPrefixNone: win32more.Windows.Win32.Graphics.GdiPlus.HotkeyPrefix = 0
HotkeyPrefix_HotkeyPrefixShow: win32more.Windows.Win32.Graphics.GdiPlus.HotkeyPrefix = 1
HotkeyPrefix_HotkeyPrefixHide: win32more.Windows.Win32.Graphics.GdiPlus.HotkeyPrefix = 2
class HueSaturationLightness(EasyCastStructure):
    Base: win32more.Windows.Win32.Graphics.GdiPlus.Effect
class HueSaturationLightnessParams(EasyCastStructure):
    hueLevel: Int32
    saturationLevel: Int32
    lightnessLevel: Int32
class IImageBytes(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{025d1823-6c7d-447b-bbdb-a3cbc3dfa2fc}')
    @commethod(3)
    def CountBytes(self, pcb: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def LockBytes(self, cb: UInt32, ulOffset: UInt32, ppvBytes: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def UnlockBytes(self, pvBytes: VoidPtr, cb: UInt32, ulOffset: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
Image = IntPtr
@winfunctype_pointer
def ImageAbort(param0: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
ImageCodecFlags = Int32
ImageCodecFlags_ImageCodecFlagsEncoder: win32more.Windows.Win32.Graphics.GdiPlus.ImageCodecFlags = 1
ImageCodecFlags_ImageCodecFlagsDecoder: win32more.Windows.Win32.Graphics.GdiPlus.ImageCodecFlags = 2
ImageCodecFlags_ImageCodecFlagsSupportBitmap: win32more.Windows.Win32.Graphics.GdiPlus.ImageCodecFlags = 4
ImageCodecFlags_ImageCodecFlagsSupportVector: win32more.Windows.Win32.Graphics.GdiPlus.ImageCodecFlags = 8
ImageCodecFlags_ImageCodecFlagsSeekableEncode: win32more.Windows.Win32.Graphics.GdiPlus.ImageCodecFlags = 16
ImageCodecFlags_ImageCodecFlagsBlockingDecode: win32more.Windows.Win32.Graphics.GdiPlus.ImageCodecFlags = 32
ImageCodecFlags_ImageCodecFlagsBuiltin: win32more.Windows.Win32.Graphics.GdiPlus.ImageCodecFlags = 65536
ImageCodecFlags_ImageCodecFlagsSystem: win32more.Windows.Win32.Graphics.GdiPlus.ImageCodecFlags = 131072
ImageCodecFlags_ImageCodecFlagsUser: win32more.Windows.Win32.Graphics.GdiPlus.ImageCodecFlags = 262144
class ImageCodecInfo(EasyCastStructure):
    Clsid: Guid
    FormatID: Guid
    CodecName: win32more.Windows.Win32.Foundation.PWSTR
    DllName: win32more.Windows.Win32.Foundation.PWSTR
    FormatDescription: win32more.Windows.Win32.Foundation.PWSTR
    FilenameExtension: win32more.Windows.Win32.Foundation.PWSTR
    MimeType: win32more.Windows.Win32.Foundation.PWSTR
    Flags: UInt32
    Version: UInt32
    SigCount: UInt32
    SigSize: UInt32
    SigPattern: POINTER(Byte)
    SigMask: POINTER(Byte)
ImageFlags = Int32
ImageFlags_ImageFlagsNone: win32more.Windows.Win32.Graphics.GdiPlus.ImageFlags = 0
ImageFlags_ImageFlagsScalable: win32more.Windows.Win32.Graphics.GdiPlus.ImageFlags = 1
ImageFlags_ImageFlagsHasAlpha: win32more.Windows.Win32.Graphics.GdiPlus.ImageFlags = 2
ImageFlags_ImageFlagsHasTranslucent: win32more.Windows.Win32.Graphics.GdiPlus.ImageFlags = 4
ImageFlags_ImageFlagsPartiallyScalable: win32more.Windows.Win32.Graphics.GdiPlus.ImageFlags = 8
ImageFlags_ImageFlagsColorSpaceRGB: win32more.Windows.Win32.Graphics.GdiPlus.ImageFlags = 16
ImageFlags_ImageFlagsColorSpaceCMYK: win32more.Windows.Win32.Graphics.GdiPlus.ImageFlags = 32
ImageFlags_ImageFlagsColorSpaceGRAY: win32more.Windows.Win32.Graphics.GdiPlus.ImageFlags = 64
ImageFlags_ImageFlagsColorSpaceYCBCR: win32more.Windows.Win32.Graphics.GdiPlus.ImageFlags = 128
ImageFlags_ImageFlagsColorSpaceYCCK: win32more.Windows.Win32.Graphics.GdiPlus.ImageFlags = 256
ImageFlags_ImageFlagsHasRealDPI: win32more.Windows.Win32.Graphics.GdiPlus.ImageFlags = 4096
ImageFlags_ImageFlagsHasRealPixelSize: win32more.Windows.Win32.Graphics.GdiPlus.ImageFlags = 8192
ImageFlags_ImageFlagsReadOnly: win32more.Windows.Win32.Graphics.GdiPlus.ImageFlags = 65536
ImageFlags_ImageFlagsCaching: win32more.Windows.Win32.Graphics.GdiPlus.ImageFlags = 131072
class ImageItemData(EasyCastStructure):
    Size: UInt32
    Position: UInt32
    Desc: VoidPtr
    DescSize: UInt32
    Data: VoidPtr
    DataSize: UInt32
    Cookie: UInt32
ImageLockMode = Int32
ImageLockMode_ImageLockModeRead: win32more.Windows.Win32.Graphics.GdiPlus.ImageLockMode = 1
ImageLockMode_ImageLockModeWrite: win32more.Windows.Win32.Graphics.GdiPlus.ImageLockMode = 2
ImageLockMode_ImageLockModeUserInputBuf: win32more.Windows.Win32.Graphics.GdiPlus.ImageLockMode = 4
ImageType = Int32
ImageType_ImageTypeUnknown: win32more.Windows.Win32.Graphics.GdiPlus.ImageType = 0
ImageType_ImageTypeBitmap: win32more.Windows.Win32.Graphics.GdiPlus.ImageType = 1
ImageType_ImageTypeMetafile: win32more.Windows.Win32.Graphics.GdiPlus.ImageType = 2
InstalledFontCollection = IntPtr
InterpolationMode = Int32
InterpolationMode_InterpolationModeInvalid: win32more.Windows.Win32.Graphics.GdiPlus.InterpolationMode = -1
InterpolationMode_InterpolationModeDefault: win32more.Windows.Win32.Graphics.GdiPlus.InterpolationMode = 0
InterpolationMode_InterpolationModeLowQuality: win32more.Windows.Win32.Graphics.GdiPlus.InterpolationMode = 1
InterpolationMode_InterpolationModeHighQuality: win32more.Windows.Win32.Graphics.GdiPlus.InterpolationMode = 2
InterpolationMode_InterpolationModeBilinear: win32more.Windows.Win32.Graphics.GdiPlus.InterpolationMode = 3
InterpolationMode_InterpolationModeBicubic: win32more.Windows.Win32.Graphics.GdiPlus.InterpolationMode = 4
InterpolationMode_InterpolationModeNearestNeighbor: win32more.Windows.Win32.Graphics.GdiPlus.InterpolationMode = 5
InterpolationMode_InterpolationModeHighQualityBilinear: win32more.Windows.Win32.Graphics.GdiPlus.InterpolationMode = 6
InterpolationMode_InterpolationModeHighQualityBicubic: win32more.Windows.Win32.Graphics.GdiPlus.InterpolationMode = 7
ItemDataPosition = Int32
ItemDataPosition_ItemDataPositionAfterHeader: win32more.Windows.Win32.Graphics.GdiPlus.ItemDataPosition = 0
ItemDataPosition_ItemDataPositionAfterPalette: win32more.Windows.Win32.Graphics.GdiPlus.ItemDataPosition = 1
ItemDataPosition_ItemDataPositionAfterBits: win32more.Windows.Win32.Graphics.GdiPlus.ItemDataPosition = 2
class Levels(EasyCastStructure):
    Base: win32more.Windows.Win32.Graphics.GdiPlus.Effect
class LevelsParams(EasyCastStructure):
    highlight: Int32
    midtone: Int32
    shadow: Int32
LineCap = Int32
LineCap_LineCapFlat: win32more.Windows.Win32.Graphics.GdiPlus.LineCap = 0
LineCap_LineCapSquare: win32more.Windows.Win32.Graphics.GdiPlus.LineCap = 1
LineCap_LineCapRound: win32more.Windows.Win32.Graphics.GdiPlus.LineCap = 2
LineCap_LineCapTriangle: win32more.Windows.Win32.Graphics.GdiPlus.LineCap = 3
LineCap_LineCapNoAnchor: win32more.Windows.Win32.Graphics.GdiPlus.LineCap = 16
LineCap_LineCapSquareAnchor: win32more.Windows.Win32.Graphics.GdiPlus.LineCap = 17
LineCap_LineCapRoundAnchor: win32more.Windows.Win32.Graphics.GdiPlus.LineCap = 18
LineCap_LineCapDiamondAnchor: win32more.Windows.Win32.Graphics.GdiPlus.LineCap = 19
LineCap_LineCapArrowAnchor: win32more.Windows.Win32.Graphics.GdiPlus.LineCap = 20
LineCap_LineCapCustom: win32more.Windows.Win32.Graphics.GdiPlus.LineCap = 255
LineCap_LineCapAnchorMask: win32more.Windows.Win32.Graphics.GdiPlus.LineCap = 240
LineJoin = Int32
LineJoin_LineJoinMiter: win32more.Windows.Win32.Graphics.GdiPlus.LineJoin = 0
LineJoin_LineJoinBevel: win32more.Windows.Win32.Graphics.GdiPlus.LineJoin = 1
LineJoin_LineJoinRound: win32more.Windows.Win32.Graphics.GdiPlus.LineJoin = 2
LineJoin_LineJoinMiterClipped: win32more.Windows.Win32.Graphics.GdiPlus.LineJoin = 3
LinearGradientMode = Int32
LinearGradientMode_LinearGradientModeHorizontal: win32more.Windows.Win32.Graphics.GdiPlus.LinearGradientMode = 0
LinearGradientMode_LinearGradientModeVertical: win32more.Windows.Win32.Graphics.GdiPlus.LinearGradientMode = 1
LinearGradientMode_LinearGradientModeForwardDiagonal: win32more.Windows.Win32.Graphics.GdiPlus.LinearGradientMode = 2
LinearGradientMode_LinearGradientModeBackwardDiagonal: win32more.Windows.Win32.Graphics.GdiPlus.LinearGradientMode = 3
Matrix = IntPtr
MatrixOrder = Int32
MatrixOrder_MatrixOrderPrepend: win32more.Windows.Win32.Graphics.GdiPlus.MatrixOrder = 0
MatrixOrder_MatrixOrderAppend: win32more.Windows.Win32.Graphics.GdiPlus.MatrixOrder = 1
Metafile = IntPtr
MetafileFrameUnit = Int32
MetafileFrameUnit_MetafileFrameUnitPixel: win32more.Windows.Win32.Graphics.GdiPlus.MetafileFrameUnit = 2
MetafileFrameUnit_MetafileFrameUnitPoint: win32more.Windows.Win32.Graphics.GdiPlus.MetafileFrameUnit = 3
MetafileFrameUnit_MetafileFrameUnitInch: win32more.Windows.Win32.Graphics.GdiPlus.MetafileFrameUnit = 4
MetafileFrameUnit_MetafileFrameUnitDocument: win32more.Windows.Win32.Graphics.GdiPlus.MetafileFrameUnit = 5
MetafileFrameUnit_MetafileFrameUnitMillimeter: win32more.Windows.Win32.Graphics.GdiPlus.MetafileFrameUnit = 6
MetafileFrameUnit_MetafileFrameUnitGdi: win32more.Windows.Win32.Graphics.GdiPlus.MetafileFrameUnit = 7
class MetafileHeader(EasyCastStructure):
    Type: win32more.Windows.Win32.Graphics.GdiPlus.MetafileType
    Size: UInt32
    Version: UInt32
    EmfPlusFlags: UInt32
    DpiX: Single
    DpiY: Single
    X: Int32
    Y: Int32
    Width: Int32
    Height: Int32
    Anonymous: _Anonymous_e__Union
    EmfPlusHeaderSize: Int32
    LogicalDpiX: Int32
    LogicalDpiY: Int32
    class _Anonymous_e__Union(EasyCastUnion):
        WmfHeader: win32more.Windows.Win32.Graphics.Gdi.METAHEADER
        EmfHeader: win32more.Windows.Win32.Graphics.GdiPlus.ENHMETAHEADER3
MetafileType = Int32
MetafileType_MetafileTypeInvalid: win32more.Windows.Win32.Graphics.GdiPlus.MetafileType = 0
MetafileType_MetafileTypeWmf: win32more.Windows.Win32.Graphics.GdiPlus.MetafileType = 1
MetafileType_MetafileTypeWmfPlaceable: win32more.Windows.Win32.Graphics.GdiPlus.MetafileType = 2
MetafileType_MetafileTypeEmf: win32more.Windows.Win32.Graphics.GdiPlus.MetafileType = 3
MetafileType_MetafileTypeEmfPlusOnly: win32more.Windows.Win32.Graphics.GdiPlus.MetafileType = 4
MetafileType_MetafileTypeEmfPlusDual: win32more.Windows.Win32.Graphics.GdiPlus.MetafileType = 5
@winfunctype_pointer
def NotificationHookProc(token: POINTER(UIntPtr)) -> win32more.Windows.Win32.Graphics.GdiPlus.Status: ...
@winfunctype_pointer
def NotificationUnhookProc(token: UIntPtr) -> Void: ...
ObjectType = Int32
ObjectType_ObjectTypeInvalid: win32more.Windows.Win32.Graphics.GdiPlus.ObjectType = 0
ObjectType_ObjectTypeBrush: win32more.Windows.Win32.Graphics.GdiPlus.ObjectType = 1
ObjectType_ObjectTypePen: win32more.Windows.Win32.Graphics.GdiPlus.ObjectType = 2
ObjectType_ObjectTypePath: win32more.Windows.Win32.Graphics.GdiPlus.ObjectType = 3
ObjectType_ObjectTypeRegion: win32more.Windows.Win32.Graphics.GdiPlus.ObjectType = 4
ObjectType_ObjectTypeImage: win32more.Windows.Win32.Graphics.GdiPlus.ObjectType = 5
ObjectType_ObjectTypeFont: win32more.Windows.Win32.Graphics.GdiPlus.ObjectType = 6
ObjectType_ObjectTypeStringFormat: win32more.Windows.Win32.Graphics.GdiPlus.ObjectType = 7
ObjectType_ObjectTypeImageAttributes: win32more.Windows.Win32.Graphics.GdiPlus.ObjectType = 8
ObjectType_ObjectTypeCustomLineCap: win32more.Windows.Win32.Graphics.GdiPlus.ObjectType = 9
ObjectType_ObjectTypeGraphics: win32more.Windows.Win32.Graphics.GdiPlus.ObjectType = 10
ObjectType_ObjectTypeMax: win32more.Windows.Win32.Graphics.GdiPlus.ObjectType = 10
ObjectType_ObjectTypeMin: win32more.Windows.Win32.Graphics.GdiPlus.ObjectType = 1
class PWMFRect16(EasyCastStructure):
    Left: Int16
    Top: Int16
    Right: Int16
    Bottom: Int16
PaletteFlags = Int32
PaletteFlags_PaletteFlagsHasAlpha: win32more.Windows.Win32.Graphics.GdiPlus.PaletteFlags = 1
PaletteFlags_PaletteFlagsGrayScale: win32more.Windows.Win32.Graphics.GdiPlus.PaletteFlags = 2
PaletteFlags_PaletteFlagsHalftone: win32more.Windows.Win32.Graphics.GdiPlus.PaletteFlags = 4
PaletteType = Int32
PaletteType_PaletteTypeCustom: win32more.Windows.Win32.Graphics.GdiPlus.PaletteType = 0
PaletteType_PaletteTypeOptimal: win32more.Windows.Win32.Graphics.GdiPlus.PaletteType = 1
PaletteType_PaletteTypeFixedBW: win32more.Windows.Win32.Graphics.GdiPlus.PaletteType = 2
PaletteType_PaletteTypeFixedHalftone8: win32more.Windows.Win32.Graphics.GdiPlus.PaletteType = 3
PaletteType_PaletteTypeFixedHalftone27: win32more.Windows.Win32.Graphics.GdiPlus.PaletteType = 4
PaletteType_PaletteTypeFixedHalftone64: win32more.Windows.Win32.Graphics.GdiPlus.PaletteType = 5
PaletteType_PaletteTypeFixedHalftone125: win32more.Windows.Win32.Graphics.GdiPlus.PaletteType = 6
PaletteType_PaletteTypeFixedHalftone216: win32more.Windows.Win32.Graphics.GdiPlus.PaletteType = 7
PaletteType_PaletteTypeFixedHalftone252: win32more.Windows.Win32.Graphics.GdiPlus.PaletteType = 8
PaletteType_PaletteTypeFixedHalftone256: win32more.Windows.Win32.Graphics.GdiPlus.PaletteType = 9
PathData = IntPtr
PathPointType = Int32
PathPointType_PathPointTypeStart: win32more.Windows.Win32.Graphics.GdiPlus.PathPointType = 0
PathPointType_PathPointTypeLine: win32more.Windows.Win32.Graphics.GdiPlus.PathPointType = 1
PathPointType_PathPointTypeBezier: win32more.Windows.Win32.Graphics.GdiPlus.PathPointType = 3
PathPointType_PathPointTypePathTypeMask: win32more.Windows.Win32.Graphics.GdiPlus.PathPointType = 7
PathPointType_PathPointTypeDashMode: win32more.Windows.Win32.Graphics.GdiPlus.PathPointType = 16
PathPointType_PathPointTypePathMarker: win32more.Windows.Win32.Graphics.GdiPlus.PathPointType = 32
PathPointType_PathPointTypeCloseSubpath: win32more.Windows.Win32.Graphics.GdiPlus.PathPointType = 128
PathPointType_PathPointTypeBezier3: win32more.Windows.Win32.Graphics.GdiPlus.PathPointType = 3
PenAlignment = Int32
PenAlignment_PenAlignmentCenter: win32more.Windows.Win32.Graphics.GdiPlus.PenAlignment = 0
PenAlignment_PenAlignmentInset: win32more.Windows.Win32.Graphics.GdiPlus.PenAlignment = 1
PenType = Int32
PenType_PenTypeSolidColor: win32more.Windows.Win32.Graphics.GdiPlus.PenType = 0
PenType_PenTypeHatchFill: win32more.Windows.Win32.Graphics.GdiPlus.PenType = 1
PenType_PenTypeTextureFill: win32more.Windows.Win32.Graphics.GdiPlus.PenType = 2
PenType_PenTypePathGradient: win32more.Windows.Win32.Graphics.GdiPlus.PenType = 3
PenType_PenTypeLinearGradient: win32more.Windows.Win32.Graphics.GdiPlus.PenType = 4
PenType_PenTypeUnknown: win32more.Windows.Win32.Graphics.GdiPlus.PenType = -1
PixelOffsetMode = Int32
PixelOffsetMode_PixelOffsetModeInvalid: win32more.Windows.Win32.Graphics.GdiPlus.PixelOffsetMode = -1
PixelOffsetMode_PixelOffsetModeDefault: win32more.Windows.Win32.Graphics.GdiPlus.PixelOffsetMode = 0
PixelOffsetMode_PixelOffsetModeHighSpeed: win32more.Windows.Win32.Graphics.GdiPlus.PixelOffsetMode = 1
PixelOffsetMode_PixelOffsetModeHighQuality: win32more.Windows.Win32.Graphics.GdiPlus.PixelOffsetMode = 2
PixelOffsetMode_PixelOffsetModeNone: win32more.Windows.Win32.Graphics.GdiPlus.PixelOffsetMode = 3
PixelOffsetMode_PixelOffsetModeHalf: win32more.Windows.Win32.Graphics.GdiPlus.PixelOffsetMode = 4
class Point(EasyCastStructure):
    X: Int32
    Y: Int32
class PointF(EasyCastStructure):
    X: Single
    Y: Single
PrivateFontCollection = IntPtr
class PropertyItem(EasyCastStructure):
    id: UInt32
    length: UInt32
    type: UInt16
    value: VoidPtr
QualityMode = Int32
QualityMode_QualityModeInvalid: win32more.Windows.Win32.Graphics.GdiPlus.QualityMode = -1
QualityMode_QualityModeDefault: win32more.Windows.Win32.Graphics.GdiPlus.QualityMode = 0
QualityMode_QualityModeLow: win32more.Windows.Win32.Graphics.GdiPlus.QualityMode = 1
QualityMode_QualityModeHigh: win32more.Windows.Win32.Graphics.GdiPlus.QualityMode = 2
class Rect(EasyCastStructure):
    X: Int32
    Y: Int32
    Width: Int32
    Height: Int32
class RectF(EasyCastStructure):
    X: Single
    Y: Single
    Width: Single
    Height: Single
class RedEyeCorrection(EasyCastStructure):
    Base: win32more.Windows.Win32.Graphics.GdiPlus.Effect
class RedEyeCorrectionParams(EasyCastStructure):
    numberOfAreas: UInt32
    areas: POINTER(win32more.Windows.Win32.Foundation.RECT)
Region = IntPtr
RotateFlipType = Int32
RotateFlipType_RotateNoneFlipNone: win32more.Windows.Win32.Graphics.GdiPlus.RotateFlipType = 0
RotateFlipType_Rotate90FlipNone: win32more.Windows.Win32.Graphics.GdiPlus.RotateFlipType = 1
RotateFlipType_Rotate180FlipNone: win32more.Windows.Win32.Graphics.GdiPlus.RotateFlipType = 2
RotateFlipType_Rotate270FlipNone: win32more.Windows.Win32.Graphics.GdiPlus.RotateFlipType = 3
RotateFlipType_RotateNoneFlipX: win32more.Windows.Win32.Graphics.GdiPlus.RotateFlipType = 4
RotateFlipType_Rotate90FlipX: win32more.Windows.Win32.Graphics.GdiPlus.RotateFlipType = 5
RotateFlipType_Rotate180FlipX: win32more.Windows.Win32.Graphics.GdiPlus.RotateFlipType = 6
RotateFlipType_Rotate270FlipX: win32more.Windows.Win32.Graphics.GdiPlus.RotateFlipType = 7
RotateFlipType_RotateNoneFlipY: win32more.Windows.Win32.Graphics.GdiPlus.RotateFlipType = 6
RotateFlipType_Rotate90FlipY: win32more.Windows.Win32.Graphics.GdiPlus.RotateFlipType = 7
RotateFlipType_Rotate180FlipY: win32more.Windows.Win32.Graphics.GdiPlus.RotateFlipType = 4
RotateFlipType_Rotate270FlipY: win32more.Windows.Win32.Graphics.GdiPlus.RotateFlipType = 5
RotateFlipType_RotateNoneFlipXY: win32more.Windows.Win32.Graphics.GdiPlus.RotateFlipType = 2
RotateFlipType_Rotate90FlipXY: win32more.Windows.Win32.Graphics.GdiPlus.RotateFlipType = 3
RotateFlipType_Rotate180FlipXY: win32more.Windows.Win32.Graphics.GdiPlus.RotateFlipType = 0
RotateFlipType_Rotate270FlipXY: win32more.Windows.Win32.Graphics.GdiPlus.RotateFlipType = 1
class Sharpen(EasyCastStructure):
    Base: win32more.Windows.Win32.Graphics.GdiPlus.Effect
class SharpenParams(EasyCastStructure):
    radius: Single
    amount: Single
class Size(EasyCastStructure):
    Width: Int32
    Height: Int32
class SizeF(EasyCastStructure):
    Width: Single
    Height: Single
SmoothingMode = Int32
SmoothingMode_SmoothingModeInvalid: win32more.Windows.Win32.Graphics.GdiPlus.SmoothingMode = -1
SmoothingMode_SmoothingModeDefault: win32more.Windows.Win32.Graphics.GdiPlus.SmoothingMode = 0
SmoothingMode_SmoothingModeHighSpeed: win32more.Windows.Win32.Graphics.GdiPlus.SmoothingMode = 1
SmoothingMode_SmoothingModeHighQuality: win32more.Windows.Win32.Graphics.GdiPlus.SmoothingMode = 2
SmoothingMode_SmoothingModeNone: win32more.Windows.Win32.Graphics.GdiPlus.SmoothingMode = 3
SmoothingMode_SmoothingModeAntiAlias: win32more.Windows.Win32.Graphics.GdiPlus.SmoothingMode = 4
SmoothingMode_SmoothingModeAntiAlias8x4: win32more.Windows.Win32.Graphics.GdiPlus.SmoothingMode = 4
SmoothingMode_SmoothingModeAntiAlias8x8: win32more.Windows.Win32.Graphics.GdiPlus.SmoothingMode = 5
Status = Int32
Status_Ok: win32more.Windows.Win32.Graphics.GdiPlus.Status = 0
Status_GenericError: win32more.Windows.Win32.Graphics.GdiPlus.Status = 1
Status_InvalidParameter: win32more.Windows.Win32.Graphics.GdiPlus.Status = 2
Status_OutOfMemory: win32more.Windows.Win32.Graphics.GdiPlus.Status = 3
Status_ObjectBusy: win32more.Windows.Win32.Graphics.GdiPlus.Status = 4
Status_InsufficientBuffer: win32more.Windows.Win32.Graphics.GdiPlus.Status = 5
Status_NotImplemented: win32more.Windows.Win32.Graphics.GdiPlus.Status = 6
Status_Win32Error: win32more.Windows.Win32.Graphics.GdiPlus.Status = 7
Status_WrongState: win32more.Windows.Win32.Graphics.GdiPlus.Status = 8
Status_Aborted: win32more.Windows.Win32.Graphics.GdiPlus.Status = 9
Status_FileNotFound: win32more.Windows.Win32.Graphics.GdiPlus.Status = 10
Status_ValueOverflow: win32more.Windows.Win32.Graphics.GdiPlus.Status = 11
Status_AccessDenied: win32more.Windows.Win32.Graphics.GdiPlus.Status = 12
Status_UnknownImageFormat: win32more.Windows.Win32.Graphics.GdiPlus.Status = 13
Status_FontFamilyNotFound: win32more.Windows.Win32.Graphics.GdiPlus.Status = 14
Status_FontStyleNotFound: win32more.Windows.Win32.Graphics.GdiPlus.Status = 15
Status_NotTrueTypeFont: win32more.Windows.Win32.Graphics.GdiPlus.Status = 16
Status_UnsupportedGdiplusVersion: win32more.Windows.Win32.Graphics.GdiPlus.Status = 17
Status_GdiplusNotInitialized: win32more.Windows.Win32.Graphics.GdiPlus.Status = 18
Status_PropertyNotFound: win32more.Windows.Win32.Graphics.GdiPlus.Status = 19
Status_PropertyNotSupported: win32more.Windows.Win32.Graphics.GdiPlus.Status = 20
Status_ProfileNotFound: win32more.Windows.Win32.Graphics.GdiPlus.Status = 21
StringAlignment = Int32
StringAlignment_StringAlignmentNear: win32more.Windows.Win32.Graphics.GdiPlus.StringAlignment = 0
StringAlignment_StringAlignmentCenter: win32more.Windows.Win32.Graphics.GdiPlus.StringAlignment = 1
StringAlignment_StringAlignmentFar: win32more.Windows.Win32.Graphics.GdiPlus.StringAlignment = 2
StringDigitSubstitute = Int32
StringDigitSubstitute_StringDigitSubstituteUser: win32more.Windows.Win32.Graphics.GdiPlus.StringDigitSubstitute = 0
StringDigitSubstitute_StringDigitSubstituteNone: win32more.Windows.Win32.Graphics.GdiPlus.StringDigitSubstitute = 1
StringDigitSubstitute_StringDigitSubstituteNational: win32more.Windows.Win32.Graphics.GdiPlus.StringDigitSubstitute = 2
StringDigitSubstitute_StringDigitSubstituteTraditional: win32more.Windows.Win32.Graphics.GdiPlus.StringDigitSubstitute = 3
StringFormatFlags = Int32
StringFormatFlags_StringFormatFlagsDirectionRightToLeft: win32more.Windows.Win32.Graphics.GdiPlus.StringFormatFlags = 1
StringFormatFlags_StringFormatFlagsDirectionVertical: win32more.Windows.Win32.Graphics.GdiPlus.StringFormatFlags = 2
StringFormatFlags_StringFormatFlagsNoFitBlackBox: win32more.Windows.Win32.Graphics.GdiPlus.StringFormatFlags = 4
StringFormatFlags_StringFormatFlagsDisplayFormatControl: win32more.Windows.Win32.Graphics.GdiPlus.StringFormatFlags = 32
StringFormatFlags_StringFormatFlagsNoFontFallback: win32more.Windows.Win32.Graphics.GdiPlus.StringFormatFlags = 1024
StringFormatFlags_StringFormatFlagsMeasureTrailingSpaces: win32more.Windows.Win32.Graphics.GdiPlus.StringFormatFlags = 2048
StringFormatFlags_StringFormatFlagsNoWrap: win32more.Windows.Win32.Graphics.GdiPlus.StringFormatFlags = 4096
StringFormatFlags_StringFormatFlagsLineLimit: win32more.Windows.Win32.Graphics.GdiPlus.StringFormatFlags = 8192
StringFormatFlags_StringFormatFlagsNoClip: win32more.Windows.Win32.Graphics.GdiPlus.StringFormatFlags = 16384
StringFormatFlags_StringFormatFlagsBypassGDI: win32more.Windows.Win32.Graphics.GdiPlus.StringFormatFlags = -2147483648
StringTrimming = Int32
StringTrimming_StringTrimmingNone: win32more.Windows.Win32.Graphics.GdiPlus.StringTrimming = 0
StringTrimming_StringTrimmingCharacter: win32more.Windows.Win32.Graphics.GdiPlus.StringTrimming = 1
StringTrimming_StringTrimmingWord: win32more.Windows.Win32.Graphics.GdiPlus.StringTrimming = 2
StringTrimming_StringTrimmingEllipsisCharacter: win32more.Windows.Win32.Graphics.GdiPlus.StringTrimming = 3
StringTrimming_StringTrimmingEllipsisWord: win32more.Windows.Win32.Graphics.GdiPlus.StringTrimming = 4
StringTrimming_StringTrimmingEllipsisPath: win32more.Windows.Win32.Graphics.GdiPlus.StringTrimming = 5
TextRenderingHint = Int32
TextRenderingHint_TextRenderingHintSystemDefault: win32more.Windows.Win32.Graphics.GdiPlus.TextRenderingHint = 0
TextRenderingHint_TextRenderingHintSingleBitPerPixelGridFit: win32more.Windows.Win32.Graphics.GdiPlus.TextRenderingHint = 1
TextRenderingHint_TextRenderingHintSingleBitPerPixel: win32more.Windows.Win32.Graphics.GdiPlus.TextRenderingHint = 2
TextRenderingHint_TextRenderingHintAntiAliasGridFit: win32more.Windows.Win32.Graphics.GdiPlus.TextRenderingHint = 3
TextRenderingHint_TextRenderingHintAntiAlias: win32more.Windows.Win32.Graphics.GdiPlus.TextRenderingHint = 4
TextRenderingHint_TextRenderingHintClearTypeGridFit: win32more.Windows.Win32.Graphics.GdiPlus.TextRenderingHint = 5
class Tint(EasyCastStructure):
    Base: win32more.Windows.Win32.Graphics.GdiPlus.Effect
class TintParams(EasyCastStructure):
    hue: Int32
    amount: Int32
Unit = Int32
Unit_UnitWorld: win32more.Windows.Win32.Graphics.GdiPlus.Unit = 0
Unit_UnitDisplay: win32more.Windows.Win32.Graphics.GdiPlus.Unit = 1
Unit_UnitPixel: win32more.Windows.Win32.Graphics.GdiPlus.Unit = 2
Unit_UnitPoint: win32more.Windows.Win32.Graphics.GdiPlus.Unit = 3
Unit_UnitInch: win32more.Windows.Win32.Graphics.GdiPlus.Unit = 4
Unit_UnitDocument: win32more.Windows.Win32.Graphics.GdiPlus.Unit = 5
Unit_UnitMillimeter: win32more.Windows.Win32.Graphics.GdiPlus.Unit = 6
WarpMode = Int32
WarpMode_WarpModePerspective: win32more.Windows.Win32.Graphics.GdiPlus.WarpMode = 0
WarpMode_WarpModeBilinear: win32more.Windows.Win32.Graphics.GdiPlus.WarpMode = 1
class WmfPlaceableFileHeader(EasyCastStructure):
    Key: UInt32
    Hmf: Int16
    BoundingBox: win32more.Windows.Win32.Graphics.GdiPlus.PWMFRect16
    Inch: Int16
    Reserved: UInt32
    Checksum: Int16
    _pack_ = 2
WrapMode = Int32
WrapMode_WrapModeTile: win32more.Windows.Win32.Graphics.GdiPlus.WrapMode = 0
WrapMode_WrapModeTileFlipX: win32more.Windows.Win32.Graphics.GdiPlus.WrapMode = 1
WrapMode_WrapModeTileFlipY: win32more.Windows.Win32.Graphics.GdiPlus.WrapMode = 2
WrapMode_WrapModeTileFlipXY: win32more.Windows.Win32.Graphics.GdiPlus.WrapMode = 3
WrapMode_WrapModeClamp: win32more.Windows.Win32.Graphics.GdiPlus.WrapMode = 4


make_ready(__name__)
