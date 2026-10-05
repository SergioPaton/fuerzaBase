@echo off
REM Script para Windows - ejecutar con doble clic
setlocal enabledelayedexpansion

REM Detectar directorio del proyecto (donde está este .bat o su padre)
set "SCRIPT_DIR=%~dp0"
if exist "%SCRIPT_DIR%backend\app\main.py" (
    set "PROJECT_ROOT=%SCRIPT_DIR%"
) else if exist "%SCRIPT_DIR%fuerza-base\backend\app\main.py" (
    set "PROJECT_ROOT=%SCRIPT_DIR%fuerza-base"
) else (
    echo ERROR: No se encuentra el proyecto. Asegurate de que start_app.bat este en la raiz del repositorio o dentro de fuerza-base.
    pause
    exit /b 1
)

echo Directorio del proyecto: %PROJECT_ROOT%
cd /d "%PROJECT_ROOT%"

REM Usar Python del entorno virtual si existe
if exist "backend\.venv\Scripts\python.exe" (
    set "PYTHON_CMD=backend\.venv\Scripts\python.exe"
) else if exist ".venv\Scripts\python.exe" (
    set "PYTHON_CMD=.venv\Scripts\python.exe"
) else (
    set "PYTHON_CMD=python"
)

REM Iniciar backend
echo Iniciando backend en http://localhost:8000 ...
start /b cmd /c "%PYTHON_CMD% -m uvicorn backend.app.main:app --reload --host 0.0.0.0 --port 8000 > backend.log 2>&1"

REM Esperar a que arranque
timeout /t 6 /nobreak > nul

REM Iniciar frontend
echo Iniciando frontend en http://localhost:5173 ...
if exist "frontend\package.json" (
    start /b cmd /c "cd frontend && npm run dev > frontend.log 2>&1"
) else (
    echo ADVERTENCIA: No se encontro frontend/package.json
)

REM Esperar a que cargue
timeout /t 8 /nobreak > nul

REM Abrir navegador automaticamente
start http://localhost:5173

echo.
echo Aplicacion iniciada!
echo Backend: http://localhost:8000
echo Frontend: http://localhost:5173
echo.
echo Presiona cualquier tecla para detener los procesos...
pause > nul
