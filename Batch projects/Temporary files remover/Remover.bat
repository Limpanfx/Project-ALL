@echo off
setlocal enabledelayedexpansion

echo ========================================================
echo             Windows Temporary Files Cleanup
echo ========================================================
echo.

:: Get admin privileges
NET FILE 1>NUL 2>NUL
if '%errorlevel%' == '0' (
    goto :run_as_admin
) else (
    echo Requesting administrative privileges...
    echo This is required to access and delete system temp files.
    echo.
    
    powershell -Command "Start-Process -FilePath '%0' -Verb RunAs"
    exit /b
)

:run_as_admin
echo Running with administrative privileges.
echo.

:: Define temp folder locations
set "SYSTEM_TEMP=%windir%\Temp"
set "USER_TEMP=%temp%"

echo Cleanup will target the following locations:
echo 1. System temp folder: %SYSTEM_TEMP%
echo 2. User temp folder: %USER_TEMP%
echo.
echo Press CTRL+C to abort or any key to continue...
pause > nul

echo.
echo ========================================================
echo Starting cleanup process...
echo ========================================================
echo.

:: Create log file
set "LOGFILE=%~dp0temp_cleanup_log.txt"
echo Windows Temp File Cleanup - %date% %time% > "%LOGFILE%"
echo. >> "%LOGFILE%"

:: Function to delete files from a directory
call :cleanup_directory "%SYSTEM_TEMP%" "System temporary files"
call :cleanup_directory "%USER_TEMP%" "User temporary files"

echo.
echo ========================================================
echo Cleanup process completed!
echo ========================================================
echo.
echo A log file has been created at:
echo %LOGFILE%
echo.
echo Press any key to exit...
pause > nul

goto :eof

:cleanup_directory
set "TARGET_DIR=%~1"
set "DIR_DESC=%~2"

echo.
echo Processing %DIR_DESC% in: %TARGET_DIR%
echo Processing %DIR_DESC% in: %TARGET_DIR% >> "%LOGFILE%"

:: Check if directory exists
if not exist "%TARGET_DIR%" (
    echo ERROR: %DIR_DESC% directory does not exist.
    echo ERROR: %DIR_DESC% directory does not exist. >> "%LOGFILE%"
    goto :eof
)

:: Count files before cleanup for reporting
set "FILE_COUNT=0"
for /f %%A in ('dir /a /b "%TARGET_DIR%" 2^>nul ^| find /c /v ""') do set "FILE_COUNT=%%A"
echo Found %FILE_COUNT% items in %DIR_DESC% directory.
echo Found %FILE_COUNT% items in %DIR_DESC% directory. >> "%LOGFILE%"

:: Delete files with error handling
echo Deleting files from %DIR_DESC%...
echo Deleting files from %DIR_DESC%... >> "%LOGFILE%"

:: Try using RMDIR for bulk removal first (faster)
rmdir /s /q "%TARGET_DIR%" 2>nul

:: Recreate the directory if it was completely removed
if not exist "%TARGET_DIR%" (
    mkdir "%TARGET_DIR%" >nul 2>&1
    echo Recreated %DIR_DESC% directory after cleanup.
    echo Recreated %DIR_DESC% directory after cleanup. >> "%LOGFILE%"
) else (
    :: If RMDIR didn't fully work, try individual file deletion
    echo Removing remaining files individually...
    echo Removing remaining files individually... >> "%LOGFILE%"
    
    :: Delete each file and folder individually with error handling
    for /f "delims=" %%i in ('dir /a /b "%TARGET_DIR%" 2^>nul') do (
        set "CURRENT_FILE=%%i"
        
        if exist "%TARGET_DIR%\%%i\*" (
            :: It's a directory
            rmdir /s /q "%TARGET_DIR%\%%i" >nul 2>&1
            if !errorlevel! neq 0 (
                echo Could not delete folder: %%i
                echo Could not delete folder: %%i >> "%LOGFILE%"
            )
        ) else (
            :: It's a file
            del /f /q "%TARGET_DIR%\%%i" >nul 2>&1
            if !errorlevel! neq 0 (
                echo Could not delete file: %%i
                echo Could not delete file: %%i >> "%LOGFILE%"
            )
        )
    )
)

:: Count files after cleanup for reporting
set "REMAINING_COUNT=0"
for /f %%A in ('dir /a /b "%TARGET_DIR%" 2^>nul ^| find /c /v ""') do set "REMAINING_COUNT=%%A"
set /a "DELETED_COUNT=%FILE_COUNT%-%REMAINING_COUNT%"

echo %DIR_DESC% cleanup completed.
echo Successfully deleted %DELETED_COUNT% items.
echo %REMAINING_COUNT% items could not be deleted (may be in use).
echo.
echo %DIR_DESC% cleanup completed. >> "%LOGFILE%"
echo Successfully deleted %DELETED_COUNT% items. >> "%LOGFILE%"
echo %REMAINING_COUNT% items could not be deleted (may be in use). >> "%LOGFILE%"
echo. >> "%LOGFILE%"

goto :eof
