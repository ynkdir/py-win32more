set TESTDIR=test_generator
set WATCHDIR=%TESTDIR%\watch

if not exist %WATCHDIR% git init %WATCHDIR%

hatch run typing win32generator || exit
hatch run fmt win32generator || exit

rmdir /s /q %WATCHDIR%\win32more
py -m win32generator --loglevel=DEBUG --package-directory=%WATCHDIR% json\Windows.Win32.json.xz json\WindowsSDK.json.xz json\WindowsAppSDK.json.xz || exit

del %WATCHDIR%\win32all.py
py -m win32generator --loglevel=DEBUG --one %WATCHDIR%\win32all.py json\Windows.Win32.json.xz || exit

del %WATCHDIR%\winrtall.py
py -m win32generator --loglevel=DEBUG --one %WATCHDIR%\winrtall.py json\WindowsSDK.json.xz json\WindowsAppSDK.json.xz || exit

rmdir /s /q %WATCHDIR%\win32sel
py -m win32generator --loglevel=DEBUG --package-directory=%WATCHDIR% --package-name=win32sel --selector=%TESTDIR%\win32sel.txt json\Windows.Win32.json.xz || exit

rmdir /s /q %WATCHDIR%\winrtsel
py -m win32generator --loglevel=DEBUG --package-directory=%WATCHDIR% --package-name=winrtsel --selector=%TESTDIR%\winrtsel.txt json\WindowsSDK.json.xz json\WindowsAppSDK.json.xz || exit

git -C %WATCHDIR% status
