@echo off
REM Set the code page to UTF-8
chcp 65001

REM Set the PYTHONIOENCODING environment variable to utf-8
set PYTHONIOENCODING=utf-8

setlocal

:: Check if Python is installed
where python >nul 2>nul
if %ERRORLEVEL% neq 0 (
    echo Python not found. Installing Python...
    REM Download Python installer
    powershell -Command "Invoke-WebRequest -Uri 'https://www.python.org/ftp/python/3.9.13/python-3.9.13-amd64.exe' -OutFile 'python-installer.exe'"
    
    REM Install Python silently
    python-installer.exe /quiet InstallAllUsers=1 PrependPath=1
    
    REM Check if Python installation was successful
    where python >nul 2>nul
    if %ERRORLEVEL% neq 0 (
        echo Failed to install Python.
        exit /b 1
    )
)

:: Check if pip is installed
where pip >nul 2>nul
if %ERRORLEVEL% neq 0 (
    echo Pip not found. Installing pip...
    python -m ensurepip
    if %ERRORLEVEL% neq 0 (
        echo Failed to install pip.
        exit /b 1
    )
)

:: Check if requirements.txt exists
if exist "requirements.txt" (
    echo Installing dependencies from requirements.txt...
    pip install -r requirements.txt
    if %ERRORLEVEL% neq 0 (
        echo Failed to install dependencies.
        exit /b 1
    )
) else (
    echo requirements.txt not found.
    exit /b 1
)

:: Run the interface script
echo Running the interface script...
python interface.py
if %ERRORLEVEL% neq 0 (
    echo Failed to run the interface script.
    exit /b 1
)

endlocal
