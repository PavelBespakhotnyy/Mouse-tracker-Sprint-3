@echo off
chcp 65001 >nul
title Установка зависимостей Mouse Tracker
color 0B

echo.
echo ╔══════════════════════════════════════════════════════════╗
echo ║     📦 Установка зависимостей Mouse Tracker             ║
echo ╚══════════════════════════════════════════════════════════╝
echo.

REM Проверка Python
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ ОШИБКА: Python не найден!
    echo.
    echo Скачайте и установите Python:
    echo https://www.python.org/downloads/
    echo.
    echo ⚠️  При установке обязательно отметьте "Add Python to PATH"
    echo.
    pause
    exit /b 1
)

echo ✅ Python найден:
python --version
echo.

echo Обновление pip...
python -m pip install --upgrade pip
echo.

echo Установка зависимостей из requirements.txt...
echo.
pip install -r requirements.txt
echo.

if errorlevel 1 (
    echo.
    echo ❌ Ошибка при установке зависимостей.
    echo.
    echo Попробуйте установить вручную:
    echo pip install pynput Pillow numpy mss opencv-python
    echo.
) else (
    echo.
    echo ╔══════════════════════════════════════════════════════════╗
    echo ║           ✅ Установка завершена успешно!               ║
    echo ╚══════════════════════════════════════════════════════════╝
    echo.
    echo Теперь вы можете запустить приложение:
    echo - Двойной клик на run_tracker.bat
    echo - Или выполнить: python mouse_tracker.py
    echo.
)

pause

