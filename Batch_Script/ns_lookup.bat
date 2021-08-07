@echo off

echo NSLookup helps look up the IP Address for any domain.

:a
echo.
set /p id="Enter domain to lookup: "
echo.
nslookup %id%

goto a