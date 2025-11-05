@echo off
chcp 65001 >nul
title Installation Fix - Mouse Tracker
color 0E

echo.
echo ===============================================================
echo     Installation Fix
echo ===============================================================
echo.

REM Check Python
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python not found!
    pause
    exit /b 1
)

echo Python version:
python --version
echo.

echo WARNING: Compatibility issue detected
echo.
echo Python 3.14 is too new for some libraries.
echo Python 3.11 or 3.12 recommended
echo.
echo Continue installation with workaround? (y/n)
set /p continue="Your choice: "
if /i not "%continue%"=="y" (
    echo.
    echo Installation cancelled.
    pause
    exit /b 0
)

echo.
echo ===============================================================
echo Updating pip...
echo ===============================================================
python -m pip install --upgrade pip
echo.

echo ===============================================================
echo Installing libraries one by one (may take time)...
echo ===============================================================
echo.

echo [1/2] Installing pynput...
pip install pynput --no-cache-dir --verbose
echo.

echo [2/2] Installing other libraries (Pillow, numpy, mss, opencv)...
echo     Using pre-built binaries (this may take time)...
pip install Pillow numpy mss opencv-python --only-binary=:all:
if errorlevel 1 (
    echo WARNING: Error. Trying to install one by one...
    pip install Pillow --only-binary=:all:
    pip install numpy --only-binary=:all:
    pip install mss --only-binary=:all:
    pip install opencv-python --only-binary=:all:
)
echo.

echo ===============================================================
echo Checking installed libraries...
echo ===============================================================
echo.

python -c "import pynput; print('[OK] pynput installed')" 2>nul || echo [FAIL] pynput not installed
python -c "import PIL; print('[OK] Pillow:', PIL.__version__)" 2>nul || echo [FAIL] Pillow not installed
python -c "import numpy; print('[OK] numpy:', numpy.__version__)" 2>nul || echo [FAIL] numpy not installed
python -c "import mss; print('[OK] mss installed')" 2>nul || echo [FAIL] mss not installed
python -c "import cv2; print('[OK] opencv:', cv2.__version__)" 2>nul || echo [FAIL] opencv not installed

echo.
echo ===============================================================
echo Check completed
echo ===============================================================
echo.

python -c "import pynput, PIL, numpy, mss, cv2" >nul 2>&1
if errorlevel 1 (
    echo.
    echo ERROR: Not all libraries installed successfully.
    echo.
    echo RECOMMENDATIONS:
    echo.
    echo 1. Uninstall Python 3.14 and install Python 3.11 or 3.12
    echo    Download: https://www.python.org/downloads/
    echo.
    echo 2. Or use virtual environment with Python 3.11:
    echo    python -m venv venv
    echo    venv\Scripts\activate
    echo    pip install -r requirements.txt
    echo.
) else (
    echo.
    echo ===============================================================
    echo          Installation completed successfully!
    echo ===============================================================
    echo.
    echo Launch app: run_tracker.bat
    echo.
)

pause

