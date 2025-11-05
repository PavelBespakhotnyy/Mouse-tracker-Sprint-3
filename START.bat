@echo off
chcp 65001 >nul
title Mouse Tracker
color 0A

cls
echo.
echo ===============================================================
echo.
echo                  STARTING MOUSE TRACKER
echo.
echo ===============================================================
echo.

REM Check Python
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python not found!
    echo.
    echo Please run INSTALL.bat first
    echo.
    pause
    exit /b 1
)

REM Quick dependency check
python -c "import pynput, PIL, numpy, mss, cv2" >nul 2>&1
if errorlevel 1 (
    echo ERROR: Dependencies not installed!
    echo.
    echo Please run INSTALL.bat first
    echo.
    pause
    exit /b 1
)

echo Starting Mouse Tracker...
echo.
echo Close this window or press Ctrl+C to stop the app
echo ===============================================================
echo.

python mouse_tracker.py

if errorlevel 1 (
    echo.
    echo ===============================================================
    echo ERROR: An error occurred
    echo ===============================================================
    echo.
    pause
)

