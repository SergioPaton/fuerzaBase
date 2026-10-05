#!/usr/bin/env bash
set -euo pipefail

# Ir al directorio donde esta este script
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Si el script esta dentro de fuerza-base, usar ese; si esta fuera, entrar
if [ -f "$SCRIPT_DIR/backend/app/main.py" ]; then
    PROJECT_ROOT="$SCRIPT_DIR"
elif [ -f "$SCRIPT_DIR/fuerza-base/backend/app/main.py" ]; then
    PROJECT_ROOT="$SCRIPT_DIR/fuerza-base"
else
    echo "ERROR: No se encuentra el proyecto."
    exit 1
fi

cd "$PROJECT_ROOT"

# Entorno virtual
if [ ! -d "backend/.venv" ]; then
    echo "Creando entorno virtual..."
    python3 -m venv backend/.venv
    source backend/.venv/bin/activate
    pip install -r backend/requirements.txt
else
    source backend/.venv/bin/activate
fi

# Dependencias frontend
if [ ! -d "frontend/node_modules" ]; then
    echo "Instalando frontend..."
    (cd frontend && npm install)
fi

# Migraciones
echo "Aplicando migraciones..."
alembic upgrade head || echo "Advertencia: migraciones fallaron"

# Iniciar backend
echo "Iniciando backend..."
nohup python -m uvicorn backend.app.main:app --reload --host 0.0.0.0 --port 8000 > backend.log 2>&1 &
BACKEND_PID=$!

# Iniciar frontend
echo "Iniciando frontend..."
nohup bash -c 'cd frontend && npm run dev' > frontend.log 2>&1 &
FRONTEND_PID=$!

sleep 8

# Abrir navegador
case "$(uname -s)" in
    Darwin) open http://localhost:5173 ;;
    Linux)   xdg-open http://localhost:5173 ;;
    *) echo "Abre manualmente: http://localhost:5173" ;;
esac

echo "Servicios iniciados (Backend PID: $BACKEND_PID, Frontend PID: $FRONTEND_PID)"
echo "Presiona Ctrl+C para detener esta ventana (los servicios siguen corriendo)."
wait
