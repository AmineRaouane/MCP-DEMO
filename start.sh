#!/bin/bash

set -e

echo "Starting The MCP Server ..."

# Set default environment variables if not set
export HOST=${HOST:-0.0.0.0}
export PORT=${PORT:-8000}

echo "Configuration:"
echo "  Host: $HOST"
echo "  Port: $PORT"

echo "Starting with Gunicorn..."
exec gunicorn --workers=1 --worker-class uvicorn.workers.UvicornWorker -b $HOST:$PORT main:app
