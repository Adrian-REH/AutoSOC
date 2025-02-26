# Usa Debian Bookworm Slim como base
FROM debian:bookworm-slim

# Variables de entorno
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    DEBIAN_FRONTEND=noninteractive \
    DJANGO_SETTINGS_MODULE=app.settings

# Instalar dependencias del sistema y Python 3
RUN apt-get update && apt-get install -y \
    curl \
    python3 python3-pip python3-venv python3-dev \
    libpq-dev gcc \
    && rm -rf /var/lib/apt/lists/*

# Establecer directorio de trabajo
WORKDIR /app

# Copiar archivos de requerimientos

COPY /tools/ /tmp/app/

COPY /script/entrypoint.sh /entrypoint.sh

RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]

# Exponer el puerto 8000
EXPOSE 9090

# Comando de inicio con Gunicorn
CMD ["/app/venv/bin/gunicorn", "app.wsgi:application", "--bind", "0.0.0.0:9090"]
