@echo off
REM Download and optimize images for TerraCrest Group
echo Downloading professional images from Unsplash...
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python is not installed or not in PATH.
    echo Please install Python from https://www.python.org/downloads/
    echo Make sure to check "Add Python to PATH" during installation.
    pause
    exit /b 1
)

REM Install required packages
echo Installing required packages (requests, Pillow)...
pip install requests Pillow --quiet

REM Run the download script
python download_images.py

if errorlevel 1 (
    echo.
    echo Error occurred during download. Please check your internet connection.
    pause
    exit /b 1
)

echo.
echo Success! Images have been downloaded and optimized.
pause
