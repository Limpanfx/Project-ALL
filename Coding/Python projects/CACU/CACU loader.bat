@echo off

set /p "pass=Personal ID: "

if "%pass%"=="P001" goto run
if "%pass%"=="P002" goto run

cls
echo Access Denied
pause
exit /b

:run
cls
echo Access Granted
python selector.py