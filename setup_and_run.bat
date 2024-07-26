@echo off
REM Set the code page to UTF-8
chcp 65001

REM Set the PYTHONIOENCODING environment variable to utf-8
set PYTHONIOENCODING=utf-8

setlocal

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
