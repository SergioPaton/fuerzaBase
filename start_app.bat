@echo off
REM Script para Windows - ejecutar con doble clic

REM Ir al directorio del proyecto
cd /d "%~dp0fuerza-base"

REM Iniciar backend (FastAPI)
echo Iniciando servidor backend...
start /b python -m uvicorn backend.app.main:app --reload --host 0.0.0.0 --port 8000 > backend.log 2>&1

REM Esperar a que arranque
timeout /t 5 /nobreak > nul

REM Iniciar frontend
echo Iniciando servidor frontend...
start /b cmd /c "cd frontend && npm run dev > frontend.log 2>&1"

echo Aplicacion iniciada!
echo Backend: http://localhost:8000
echo Frontend: http://localhost:5173
pause
