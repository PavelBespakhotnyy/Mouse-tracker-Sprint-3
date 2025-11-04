@echo off
chcp 65001 >nul
title Исправление установки - Mouse Tracker
color 0E

echo.
echo ╔══════════════════════════════════════════════════════════╗
echo ║     🔧 Исправление установки зависимостей               ║
echo ╚══════════════════════════════════════════════════════════╝
echo.

REM Проверка Python
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ ОШИБКА: Python не найден!
    pause
    exit /b 1
)

echo ✅ Версия Python:
python --version
echo.

echo ⚠️  ВНИМАНИЕ: Обнаружена проблема совместимости
echo.
echo Python 3.14 слишком новый для некоторых библиотек.
echo Рекомендуется Python 3.11 или 3.12
echo.
echo Продолжить установку с обходным решением? (y/n)
set /p continue="Ваш выбор: "
if /i not "%continue%"=="y" (
    echo.
    echo Установка отменена.
    pause
    exit /b 0
)

echo.
echo ════════════════════════════════════════════════════════════
echo Обновление pip...
echo ════════════════════════════════════════════════════════════
python -m pip install --upgrade pip
echo.

echo ════════════════════════════════════════════════════════════
echo Установка библиотек по одной (может занять время)...
echo ════════════════════════════════════════════════════════════
echo.

echo [1/2] Установка pynput...
pip install pynput --no-cache-dir --verbose
echo.

echo [2/2] Установка остальных библиотек (Pillow, numpy, mss, opencv)...
echo     Используем готовые бинарные файлы (это может занять время)...
pip install Pillow numpy mss opencv-python --only-binary=:all:
if errorlevel 1 (
    echo ⚠️  Ошибка. Пробуем установить по одной...
    pip install Pillow --only-binary=:all:
    pip install numpy --only-binary=:all:
    pip install mss --only-binary=:all:
    pip install opencv-python --only-binary=:all:
)
echo.

echo ════════════════════════════════════════════════════════════
echo Проверка установленных библиотек...
echo ════════════════════════════════════════════════════════════
echo.

python -c "import pynput; print('✅ pynput: установлен')" 2>nul || echo ❌ pynput не установлен
python -c "import PIL; print('✅ Pillow:', PIL.__version__)" 2>nul || echo ❌ Pillow не установлен
python -c "import numpy; print('✅ numpy:', numpy.__version__)" 2>nul || echo ❌ numpy не установлен
python -c "import mss; print('✅ mss: установлен')" 2>nul || echo ❌ mss не установлен
python -c "import cv2; print('✅ opencv:', cv2.__version__)" 2>nul || echo ❌ opencv не установлен

echo.
echo ════════════════════════════════════════════════════════════
echo Проверка завершена
echo ════════════════════════════════════════════════════════════
echo.

python -c "import pynput, PIL, numpy, mss, cv2" >nul 2>&1
if errorlevel 1 (
    echo.
    echo ❌ Не все библиотеки установлены успешно.
    echo.
    echo 📋 РЕКОМЕНДАЦИИ:
    echo.
    echo 1. Удалите Python 3.14 и установите Python 3.11 или 3.12
    echo    Скачать: https://www.python.org/downloads/
    echo.
    echo 2. Или используйте виртуальное окружение с Python 3.11:
    echo    python -m venv venv
    echo    venv\Scripts\activate
    echo    pip install -r requirements.txt
    echo.
) else (
    echo.
    echo ╔══════════════════════════════════════════════════════════╗
    echo ║           ✅ Установка завершена успешно!               ║
    echo ╚══════════════════════════════════════════════════════════╝
    echo.
    echo Запустите приложение: run_tracker.bat
    echo.
)

pause

