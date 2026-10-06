@echo off
title Fuerza Base - Launcher
set "SCRIPT_DIR=%~dp0"
if exist "%SCRIPT_DIR%fuerza-base\backend\app\main.py" (
    set "PROJECT_ROOT=%SCRIPT_DIR%fuerza-base"
) else if exist "%SCRIPT_DIR%backend\app\main.py" (
    set "PROJECT_ROOT=%SCRIPT_DIR%"
) else (
    echo ERROR
    exit /b 1
)
echo ====================================================
echo  Iniciando Fuerza Base...
echo ====================================================
cd /d "%PROJECT_ROOT%"
if not exist "backend\.venv\Scripts\python.exe" (
    echo Creando venv...
) else (
    echo [1/3] Entorno virtual de Python OK.
)
where npm >nul 2>&1
if errorlevel 1 (
    echo ERROR
    exit /b 1
)
if not exist "frontend\node_modules" (
    echo Instalando...
) else (
    echo [2/3] Dependencias de frontend OK.
)
echo [3/3] Lanzando Backend y Frontend...
start "Fuerza Base - Backend" /d "%PROJECT_ROOT%" cmd /k "backend\.venv\Scripts\python.exe -m uvicorn backend.app.main:app --reload --host 127.0.0.1 --port 8000"
start "Fuerza Base - Frontend" /d "%PROJECT_ROOT%\frontend" cmd /k "npm run dev"
ping 127.0.0.1 -n 4 >nul
echo Abriendo navegador en http://localhost:5173 ...
start http://localhost:5173
echo.
echo ====================================================
echo  Fuerza Base iniciada con exito!
echo  Backend:  http://127.0.0.1:8000
echo  Frontend: http://localhost:5173
echo ====================================================
