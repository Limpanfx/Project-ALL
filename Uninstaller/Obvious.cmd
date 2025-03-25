@echo off
echo Uninstalling League of Legends...

taskkill /F /IM LeagueClient.exe >nul 2>&1
echo ✅ terminated the LeagueClient.exe process 
taskkill /F /IM RiotClientServices.exe >nul 2>&1
echo ✅ killed the RiotClientServices.exe process
wmic product where "name like 'League of Legends%'" call uninstall /nointeractive
echo ✅ WMIC uninstallation of League of Legends program

rd /s /q "C:\Riot Games\League of Legends"
echo ✅ deleted League of Legends directory
rd /s /q "%ProgramData%\Riot Games"
echo ✅ deleted game settings and updates in riot games directory
rd /s /q "%LOCALAPPDATA%\Riot Games"
echo ✅ deleted Riot Games-related files from the Local AppData
rd /s /q "%LOCALAPPDATA%\Riot Games"
echo ✅ deleted Riot Games-related files from the Roaming AppData
rd /s /q "%APPDATA%\Riot Games"

echo ✅ League of Legends has succesfully been removed ✅
pause
