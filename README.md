# Detección y mitigación de bots en una arquitectura distribuida
El sistema detecta cuando un bot intenta realizar pagos y responde de forma automatizada:

1️⃣ Frontend detecta la actividad del bot y alerta al servicio de monitoreo.
2️⃣ El servicio de monitoreo rastrea la IP y, si detecta abuso, publica un mensaje en RabbitMQ.
3️⃣ Nginx recibe la notificación y bloquea la IP para evitar futuros intentos maliciosos.

🛠️ Tecnologías utilizadas:
✅ Backend: Python Django, Stripe
✅ Cola de Mensajería: RabbitMQ
✅ Frontend: JavaScript
✅ Proxy: Nginx
✅ Controllers-web: C++
✅ Scripting: Python, Bash
✅ Infraestructura: Docker

## Estructura del Proyecto
```
AutoSoc/

```

## Instalación y Uso
1. Clonar el repositorio:  
   ```bash
   git clone https://github.com/tu_usuario/AutoSoc.git
   cd AutoSoc
   ```
2. Instalar dependencias:
   ```bash
   docker compose up -d
   ```
3. Test:
   ```bash
   py attack_webdriver_alert.py https://store.local.com
   ```

## Licencia
Este proyecto está bajo la licencia MIT. Ver `LICENSE` para más detalles.

