@echo off

echo Ping measures the round-trip time for messages sent from the originating host to a destination computer that are echoed back to the source.

:a
echo.
set /p id="Enter domain to ping: "
echo.
ping %id%

goto a