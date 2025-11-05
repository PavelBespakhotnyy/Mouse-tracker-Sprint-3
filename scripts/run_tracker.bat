@echo off
chcp 65001 >nul
title Mouse Tracker
color 0A

echo.
echo ===============================================================
echo          Mouse Tracker
echo ===============================================================
echo.
echo Launching application...
echo.

REM Check for Python
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python not found!
    echo.
    echo Please install Python from https://www.python.org/
    echo During installation check "Add Python to PATH"
    echo.
    pause
    exit /b 1
)

REM Check dependencies
echo Checking dependencies...
python -c "import pynput, PIL, numpy, mss, cv2" >nul 2>&1
if errorlevel 1 (
    echo.
    echo WARNING: Required libraries not installed.
    echo Install now? (y/n)
    set /p install="Your choice: "
    if /i "%install%"=="y" (
        echo.
        echo Installing dependencies...
        pip install -r requirements.txt
        echo.
        echo Dependencies installed!
        echo.
    ) else (
        echo.
        echo To install manually run: pip install -r requirements.txt
        pause
        exit /b 1
    )
)

REM Launch application
echo.
echo Starting Mouse Tracker...
echo.
python mouse_tracker.py

if errorlevel 1 (
    echo.
    echo ERROR: An error occurred while launching the application.
    echo.
)

pause

