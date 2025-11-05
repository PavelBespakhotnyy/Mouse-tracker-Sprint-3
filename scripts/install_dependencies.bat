@echo off
chcp 65001 >nul
title Mouse Tracker Dependencies Installation
color 0B

echo.
echo Mouse Tracker Dependencies Installation
echo.

REM Check Python
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python not found!
    echo.
    echo Download and install Python:
    echo https://www.python.org/downloads/
    echo.
    echo WARNING: During installation check "Add Python to PATH"
    echo.
    pause
    exit /b 1
)

echo Python found:
python --version
echo.

echo Updating pip...
python -m pip install --upgrade pip
echo.

echo Installing dependencies from requirements.txt...
echo.
pip install -r requirements.txt
echo.

if errorlevel 1 (
    echo.
    echo ERROR: Failed to install dependencies.
    echo.
    echo Try to install manually:
    echo pip install pynput Pillow numpy mss opencv-python
    echo.
) else (
    echo.
    echo Installation completed successfully!
    echo.
    echo Now you can launch the app:
    echo - Double-click run_tracker.bat
    echo - Or run: python mouse_tracker.py
    echo.
)

pause

