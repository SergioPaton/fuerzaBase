@echo off
setlocal EnableDelayedExpansion

REM --- Detectar raiz del proyecto consolidado ---
set "SCRIPT_DIR=%~dp0"
if exist "%SCRIPT_DIR%fuerza-base\backend\app\main.py" (
    set "PROJECT_ROOT=%SCRIPT_DIR%fuerza-base"
) else if exist "%SCRIPT_DIR%backend\app\main.py" (
    set "PROJECT_ROOT=%SCRIPT_DIR%"
) else (
    echo ERROR: No se encuentra el proyecto (falta backend/app/main.py).
    pause
    exit /b 1
)

echo Proyecto detectado: %PROJECT_ROOT%
cd /d "%PROJECT_ROOT%"

REM --- Verificar Python / entorno virtual ---
if exist "backend\.venv\Scripts\python.exe" (
    set "PYTHON_CMD=backend\.venv\Scripts\python.exe"
) else if exist ".venv\Scripts\python.exe" (
    set "PYTHON_CMD=.venv\Scripts\python.exe"
) else (
    echo Creando entorno virtual para backend...
    python -m venv backend\.venv
    set "PYTHON_CMD=backend\.venv\Scripts\python.exe"
    echo Instalando dependencias de Python...
    call %PYTHON_CMD% -m pip install --upgrade pip >nul 2>&1
    call %PYTHON_CMD% -m pip install -r backend\requirements.txt > backend_install.log 2>&1
)

REM --- Verificar Node / frontend ---
where npm >nul 2>&1
if errorlevel 1 (
    echo ERROR: npm no encontrado. Instala Node.js.
    pause
    exit /b 1
)

if not exist "frontend\node_modules" (
    echo Instalando dependencias del frontend...
    cd frontend
    call npm install > frontend_install.log 2>&1
    cd ..
)

REM --- Iniciar backend (ventana independiente) ---
echo Iniciando backend en http://localhost:8000 ...
start "Backend FastAPI" cmd /c "%PYTHON_CMD% -m uvicorn backend.app.main:app --reload --host 0.0.0.0 --port 8000 > backend.log 2>&1"

REM --- Esperar backend ---
timeout /t 3 /nobreak >nul

REM --- Iniciar frontend (ventana independiente) ---
echo Iniciando frontend en http://localhost:5173 ...
start "Frontend React" cmd /c "cd frontend && npm run dev > frontend.log 2>&1"

REM --- Esperar y verificar puerto 5173 ---
echo Esperando que el frontend responda...
for /L %%i in (1,1,10) do (
    netstat -an 2>nul | findstr ":5173" >nul
    if not errorlevel 1 (
        echo Frontend listo en puerto 5173.
        goto :abrir
    )
    timeout /t 2 /nobreak >nul
)

:abrir
echo Abriendo navegador en http://localhost:5173 ...
start http://localhost:5173

echo.
echo ==========================================
echo Aplicacion Fuerza Base iniciada con exito!
echo Backend:  http://localhost:8000
echo Frontend: http://localhost:5173
echo ==========================================
echo Revisa backend.log y frontend.log si hay avisos.
