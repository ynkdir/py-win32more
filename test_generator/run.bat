set TESTDIR=test_generator
set WATCHDIR=%TESTDIR%\watch
set WIN32_METADATA=%TESTDIR%\Microsoft.Windows.SDK.Win32Metadata.64.0.22-preview.zip
set WINRT_METADATA=%TESTDIR%\Microsoft.Windows.SDK.Contracts.10.0.26100.6584.zip
set APPSDK_METADATA=%TESTDIR%\Microsoft.WindowsAppSDK.1.8.250916003.zip
set WEBVIEW2_METADATA=%TESTDIR%\Microsoft.Web.WebView2.1.0.3485.44.zip
set WIN2D_METADATA=%TESTDIR%\Microsoft.Graphics.Win2D.1.3.2.zip
set ALL_METADATA=%WIN32_METADATA% %WINRT_METADATA% %APPSDK_METADATA% %WEBVIEW2_METADATA% %WIN2D_METADATA%

if not exist %WIN32_METADATA% curl.exe -L -o %WIN32_METADATA% https://github.com/ynkdir/winmd-printer/releases/download/v1.0.0/Microsoft.Windows.SDK.Win32Metadata.64.0.22-preview.zip
if not exist %WINRT_METADATA% curl.exe -L -o %WINRT_METADATA% https://github.com/ynkdir/winmd-printer/releases/download/v1.0.0/Microsoft.Windows.SDK.Contracts.10.0.26100.6584.zip
if not exist %APPSDK_METADATA% curl.exe -L -o %APPSDK_METADATA% https://github.com/ynkdir/winmd-printer/releases/download/v1.0.0/Microsoft.WindowsAppSDK.1.8.250916003.zip
if not exist %WEBVIEW2_METADATA% curl.exe -L -o %WEBVIEW2_METADATA% https://github.com/ynkdir/winmd-printer/releases/download/v1.0.0/Microsoft.Web.WebView2.1.0.3485.44.zip
if not exist %WIN2D_METADATA% curl.exe -L -o %WIN2D_METADATA% https://github.com/ynkdir/winmd-printer/releases/download/v1.0.0/Microsoft.Graphics.Win2D.1.3.2.zip

if not exist %WATCHDIR% git init %WATCHDIR%

rmdir /s /q %WATCHDIR%\win32more
py -m win32generator --loglevel=DEBUG --output-directory=%WATCHDIR% %ALL_METADATA% || exit

del %WATCHDIR%\win32all.py
py -m win32generator --loglevel=DEBUG --one=%WATCHDIR%\win32all.py %WIN32_METADATA% || exit

del %WATCHDIR%\winrtall.py
py -m win32generator --loglevel=DEBUG --one=%WATCHDIR%\winrtall.py %WINRT_METADATA% %APPSDK_METADATA% || exit

rmdir /s /q %WATCHDIR%\win32sel
py -m win32generator --loglevel=DEBUG --output-directory=%WATCHDIR% --package-name=win32sel --selector=%TESTDIR%\win32sel.txt %ALL_METADATA% || exit

rmdir /s /q %WATCHDIR%\winrtsel
py -m win32generator --loglevel=DEBUG --output-directory=%WATCHDIR% --package-name=winrtsel --selector=%TESTDIR%\winrtsel.txt %ALL_METADATA% || exit

py -m win32generator --loglevel=DEBUG --raw --one=%WATCHDIR%\raw_syntax.py --selector=%TESTDIR%\raw_syntax_selector.txt %ALL_METADATA% || exit
py %WATCHDIR%\raw_syntax.py || exit

py -m win32generator --loglevel=DEBUG --raw --one=%WATCHDIR%\raw_filedialog.py --selector=%TESTDIR%\raw_filedialog_selector.txt %ALL_METADATA% || exit
py %WATCHDIR%\raw_filedialog.py || exit

py -m win32generator --loglevel=DEBUG --one=%WATCHDIR%\enum_explicit.py --selector=%TESTDIR%\enum_explicit_selector.txt %ALL_METADATA% || exit

git -C %WATCHDIR% status

