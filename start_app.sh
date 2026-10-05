#!/bin/bash

# Cambiar a root del proyecto
cd fuerza-base

# Iniciar el backend (FastAPI con uvicorn)
echo "Iniciando servidor backend..."
python -m uvicorn backend.app.main:app --reload --host 0.0.0.0 --port 8000 > backend.log 2>&1 &

# Esperar a que el backend se inicie
sleep 5

# Iniciar el frontend (React Dev Server)
echo "Iniciando servidor frontend..."
cd frontend
npm run dev > frontend.log 2>&1 &

echo "¡Todo listo! La aplicación está corriendo:"
echo "Backend: http://localhost:8000"
echo "Frontend: http://localhost:5173"
