@echo off
title Fuerza Base - Launcher
set "SCRIPT_DIR=%~dp0"
if exist "%SCRIPT_DIR%fuerza-base\backend\app\main.py" (
    set "PROJECT_ROOT=%SCRIPT_DIR%fuerza-base"
) else if exist "%SCRIPT_DIR%backend\app\main.py" (
    set "PROJECT_ROOT=%SCRIPT_DIR%"
) else (
    echo ERROR: No se encuentra la estructura del proyecto.
    exit /b 1
)
echo ====================================================
echo  Iniciando Fuerza Base...
echo ====================================================
cd /d "%PROJECT_ROOT%"
if not exist "backend\.venv\Scripts\python.exe" (
    echo [1/3] Creando entorno virtual de Python...
    python -m venv backend\.venv
    call backend\.venv\Scripts\pip install -r backend\requirements.txt
) else (
    echo [1/3] Entorno virtual de Python OK.
)
where npm >nul 2>&1
if errorlevel 1 (
    echo ERROR: Node.js/npm no encontrado en el PATH.
    exit /b 1
)
if not exist "frontend\node_modules" (
    echo [2/3] Instalando dependencias de frontend...
    cd /d "%PROJECT_ROOT%\frontend"
    npm install
    cd /d "%PROJECT_ROOT%"
) else (
    echo [2/3] Dependencias de frontend OK.
)
echo [3/3] Lanzando Backend y Frontend...
rem Cambiado --host 127.0.0.1 por 0.0.0.0 para permitir conexiones desde el proxy de Vite
start "Fuerza Base - Backend" /d "%PROJECT_ROOT%" cmd /k "backend\.venv\Scripts\python.exe -m uvicorn backend.app.main:app --reload --host 0.0.0.0 --port 8000"
start "Fuerza Base - Frontend" /d "%PROJECT_ROOT%\frontend" cmd /k "npm run dev"
echo Esperando a que los servidores inicien...
ping 127.0.0.1 -n 6 >nul
echo Abriendo navegador en http://localhost:5173 ...
start http://localhost:5173
echo.
echo ====================================================
echo  Fuerza Base iniciada con exito!
echo  Backend:  http://127.0.0.1:8000
echo  Frontend: http://localhost:5173
echo ====================================================
