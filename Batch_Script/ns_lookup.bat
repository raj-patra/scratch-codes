@echo off

echo NSLookup helps look up the IP Address for any domain.

:a
echo.
set /p domain="Enter domain to lookup: "
echo.
nslookup %domain%

goto a