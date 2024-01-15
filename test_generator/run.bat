set TESTDIR=test_generator
set WATCHDIR=%TESTDIR%\watch

if not exist %WATCHDIR% git init %WATCHDIR%

hatch run typing win32generator || exit
hatch run fmt win32generator || exit

rmdir /s /q %WATCHDIR%\win32more
py -m win32generator --loglevel=DEBUG --output-directory=%WATCHDIR% || exit

del %WATCHDIR%\win32all.py
py -m win32generator --loglevel=DEBUG --one=%WATCHDIR%\win32all.py win32generator\resources\metadata\Windows.Win32.json.xz || exit

del %WATCHDIR%\winrtall.py
py -m win32generator --loglevel=DEBUG --one=%WATCHDIR%\winrtall.py win32generator\resources\metadata\WindowsSDK.json.xz win32generator\resources\metadata\WindowsAppSDK.json.xz || exit

rmdir /s /q %WATCHDIR%\win32sel
py -m win32generator --loglevel=DEBUG --output-directory=%WATCHDIR% --package-name=win32sel --selector=%TESTDIR%\win32sel.txt || exit

rmdir /s /q %WATCHDIR%\winrtsel
py -m win32generator --loglevel=DEBUG --output-directory=%WATCHDIR% --package-name=winrtsel --selector=%TESTDIR%\winrtsel.txt || exit

py -m win32generator --loglevel=DEBUG --raw --one=%WATCHDIR%\raw_syntax.py --selector=%TESTDIR%\raw_syntax_selector.txt || exit
py %WATCHDIR%\raw_syntax.py || exit

py -m win32generator --loglevel=DEBUG --raw --one=%WATCHDIR%\raw_filedialog.py --selector=%TESTDIR%\raw_filedialog_selector.txt || exit
py %WATCHDIR%\raw_filedialog.py || exit

git -C %WATCHDIR% status

