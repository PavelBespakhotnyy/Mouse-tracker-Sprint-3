@echo off
chcp 65001 >nul
title Mouse Tracker - One-Click Install
color 0B

echo.
echo ===============================================================
echo.
echo          MOUSE TRACKER - ONE-CLICK INSTALLER
echo.
echo ===============================================================
echo.
echo Welcome! This will install everything you need.
echo.

REM Check Python
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python not found!
    echo.
    echo Please install Python from:
    echo https://www.python.org/downloads/
    echo.
    echo Recommended: Python 3.11 or 3.12
    echo.
    echo WARNING: Remember to check "Add Python to PATH" during installation
    echo.
    pause
    exit /b 1
)

echo Python found:
python --version
echo.
echo NOTE: Python 3.11-3.12 recommended, but newer versions may work
echo.

REM Check if dependencies already installed
echo Checking existing dependencies...
echo.

set DEPS_OK=1

python -c "import pynput" >nul 2>&1
if errorlevel 1 (
    set DEPS_OK=0
    echo   [ ] pynput - not installed
) else (
    echo   [OK] pynput - already installed
)

python -c "import PIL" >nul 2>&1
if errorlevel 1 (
    set DEPS_OK=0
    echo   [ ] Pillow - not installed
) else (
    echo   [OK] Pillow - already installed
)

python -c "import numpy" >nul 2>&1
if errorlevel 1 (
    set DEPS_OK=0
    echo   [ ] numpy - not installed
) else (
    echo   [OK] numpy - already installed
)

python -c "import mss" >nul 2>&1
if errorlevel 1 (
    set DEPS_OK=0
    echo   [ ] mss - not installed
) else (
    echo   [OK] mss - already installed
)

python -c "import cv2" >nul 2>&1
if errorlevel 1 (
    set DEPS_OK=0
    echo   [ ] opencv - not installed
) else (
    echo   [OK] opencv - already installed
)

echo.

if %DEPS_OK%==1 (
    echo ===============================================================
    echo          ALL DEPENDENCIES ALREADY INSTALLED!
    echo ===============================================================
    echo.
    echo Nothing to install. You're ready to go!
    echo.
    echo To start the app: Double-click START.bat
    echo.
    pause
    exit /b 0
)

echo Some dependencies are missing. Installing now...
echo.

REM Update pip
echo [1/2] Updating pip...
python -m pip install --upgrade pip --quiet
echo.

REM Install missing packages
echo [2/2] Installing packages (this may take a minute)...
echo.

python -c "import pynput" >nul 2>&1 || pip install pynput --quiet
python -c "import PIL" >nul 2>&1 || pip install Pillow --only-binary=:all: --quiet
python -c "import numpy" >nul 2>&1 || pip install numpy --only-binary=:all: --quiet
python -c "import mss" >nul 2>&1 || pip install mss --quiet
python -c "import cv2" >nul 2>&1 || pip install opencv-python --only-binary=:all: --quiet

echo.
echo ═══════════════════════════════════════════════════════════════
echo Verifying installation...
echo ═══════════════════════════════════════════════════════════════
echo.

python -c "import pynput; print('[OK] pynput')" 2>nul || echo [FAIL] pynput failed
python -c "import PIL; print('[OK] Pillow:', PIL.__version__)" 2>nul || echo [FAIL] Pillow failed
python -c "import numpy; print('[OK] numpy:', numpy.__version__)" 2>nul || echo [FAIL] numpy failed
python -c "import mss; print('[OK] mss')" 2>nul || echo [FAIL] mss failed
python -c "import cv2; print('[OK] opencv:', cv2.__version__)" 2>nul || echo [FAIL] opencv failed

echo.

python -c "import pynput, PIL, numpy, mss, cv2" >nul 2>&1
if errorlevel 1 (
    echo ===============================================================
    echo               INSTALLATION HAD ISSUES
    echo ===============================================================
    echo.
    echo Please try:
    echo 1. Run as Administrator
    echo 2. Check scripts\install_fix.bat for detailed installation
    echo.
) else (
    echo ===============================================================
    echo          INSTALLATION COMPLETED SUCCESSFULLY!
    echo ===============================================================
    echo.
    echo You're all set!
    echo.
    echo To start the app: Double-click START.bat
    echo.
)

pause

