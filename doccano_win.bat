@echo off
setlocal enabledelayedexpansion

:: Check if Python is already installed
python --version > nul 2>&1
if %errorlevel% equ 0 (
    echo Python is already installed
    goto :installrequirements
)

echo Python not found. Installing Python...

:: Download Python installer
set PYTHON_VERSION=3.11.8
set PYTHON_URL=https://www.python.org/ftp/python/%PYTHON_VERSION%/python-%PYTHON_VERSION%-amd64.exe
set INSTALLER_PATH=%TEMP%\python-installer.exe

echo Downloading Python from %PYTHON_URL%...
powershell -Command "(New-Object Net.WebClient).DownloadFile('%PYTHON_URL%', '%INSTALLER_PATH%')"

:: Install Python
echo Installing Python...
start /wait "" "%INSTALLER_PATH%" /quiet InstallAllUsers=1 PrependPath=1 Include_pip=1

:: Clean up
del "%INSTALLER_PATH%"

:: Verify installation
python --version
if %errorlevel% neq 0 (
    echo Failed to install Python
    exit /b 1
)

:installrequirements
echo Installing requirements...
python -m pip install --upgrade pip
pip install doccano