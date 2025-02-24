# Usa Debian Bookworm Slim como base
FROM debian:bookworm-slim

# Variables de entorno
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    DEBIAN_FRONTEND=noninteractive

# Instalar dependencias del sistema y Python 3
RUN apt-get update && apt-get install -y \
    python3 python3-pip python3-venv python3-dev \
    libpq-dev gcc \
    && rm -rf /var/lib/apt/lists/*

# Establecer directorio de trabajo
WORKDIR /app

# Copiar archivos de requerimientos
COPY requirements.txt /app/

# Crear un entorno virtual e instalar dependencias
RUN python3 -m venv /app/venv && \
    /app/venv/bin/pip install --no-cache-dir --upgrade pip && \
    /app/venv/bin/pip install --no-cache-dir -r requirements.txt

# Copiar el código fuente
COPY . /app/

# Exponer el puerto 8000
EXPOSE 8000

# Comando de inicio con Gunicorn
CMD ["/app/venv/bin/gunicorn", "app.wsgi:application", "--bind", "0.0.0.0:8000"]
