# Usa debian:bookworm-slim como base
FROM debian:bookworm-slim

ENV DEBIAN_FRONTEND=noninteractive

# Instala Nginx y otras dependencias necesarias
RUN apt-get update && apt-get install -y \
    nginx \
    python3 python3-pip python3-venv \
    supervisor \
    && rm -rf /var/lib/apt/lists/* \
    && ln -sf /dev/stdout /var/log/nginx/access.log \
    && ln -sf /dev/stderr /var/log/nginx/error.log 


# Crear un entorno virtual de Python y activar
RUN python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

RUN pip install --no-cache-dir pika requests supervisor

# Copia los archivos de configuración personalizados
COPY /tools/nginx.conf /etc/nginx/nginx.conf
COPY /tools/default.conf /etc/nginx/conf.d/default.conf
COPY /tools/certs /etc/nginx/certs

COPY /tools/supervisord.conf /etc/supervisor/supervisord.conf
COPY /tools/rabbitmq_consumer.py /rabbitmq_consumer.py

# Expone el puerto 443
EXPOSE 443

# Inicia Nginx en primer plano
#CMD ["nginx", "-g", "daemon off;"]
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/supervisord.conf"]

