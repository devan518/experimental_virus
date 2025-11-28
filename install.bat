@echo off
setlocal enabledelayedexpansion

:: Determine the directory where this .bat script is located
set SCRIPT_DIR=%~dp0
echo Script directory: %SCRIPT_DIR%

:: Check if Python is installed
echo Checking for Python...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python not found. Installing Python...

    :: Download Python installer
    powershell -command "Invoke-WebRequest 'https://www.python.org/ftp/python/3.12.2/python-3.12.2-amd64.exe' -OutFile 'python_installer.exe'"

    echo Running Python installer silently...
    python_installer.exe /quiet InstallAllUsers=1 PrependPath=1 Include_test=0

    echo Waiting for installation to complete...
    timeout /t 10 >nul

    echo Python installed.
) else (
    echo Python already installed.
)

:: Verify python now exists
python --version
if %errorlevel% neq 0 (
    echo ERROR: Python failed to install.
    pause
    exit /b
)

:: Upgrade pip
echo Upgrading pip...
python -m pip install --upgrade pip

:: Install pyinstaller
echo Installing PyInstaller...
python -m pip install pyinstaller

echo PyInstaller installed.

:: Run pyinstall.py from this folder
echo Running pyinstall.py...
python "%SCRIPT_DIR%pyinstall.py"

echo Done! Results should be inside the 'dist' folder.
pause
