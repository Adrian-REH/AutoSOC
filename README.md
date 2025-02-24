# SOC Incident Automation

## Descripción
Este proyecto automatiza la detección, clasificación y respuesta ante incidentes de seguridad en un SOC. Utiliza Power Automate, Python y Bash para integrar para bloquear IPS y Automatizar usando Apis, tambien orquesta contenedores y una webApp para testear el funcionamiento del sistema y las Alertas.

## Características
✅ Automatización de respuesta a incidentes de ciberseguridad.  
✅ Scripts en Linux (Bash/Python) para bloqueo y seguimiento de IPs.  
✅ Notificaciones automáticas a email con Power Automate.
✅ Buenas prácticas: SOLID, pruebas con pytest, documentación.
✅ Front pasarela de pago.
✅ Testear uso de bots(con WebDriver).

## Tecnologías Utilizadas
- **Power Automate**: Captura request desde Service.
- **Python + Bash**: Scripts para análisis y respuesta.
- **Linux (iptables, fail2ban, logs)**: Seguridad en servidores.
- **pytest, flake8, Sphinx**: Pruebas y documentación.
- **JavaScript**: App e-commerce de ejemplo.
- **Docker**: Infrastructura y Orquestador.

## Estructura del Proyecto
```
AutoSoc/

```

## Instalación y Uso
1. Clonar el repositorio:  
   ```bash
   git clone https://github.com/tu_usuario/SOC-Incident-Automation.git
   cd AutoSoc
   ```
2. Instalar dependencias:
   ```bash
   docker compose up -d
   ```

## Licencia
Este proyecto está bajo la licencia MIT. Ver `LICENSE` para más detalles.

