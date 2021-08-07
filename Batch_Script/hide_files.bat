@echo off

echo This batch files help you hide/unhide any files/directory.

:a
echo.
set /p type="Enter type of operation (hide/unhide): "
echo.
set /p file="Enter valid file name or folder directory: "

if %type%==hide (attrib +h +s +r %file%)
if %type%==unhide (attrib -h -s -r %file%)

goto a