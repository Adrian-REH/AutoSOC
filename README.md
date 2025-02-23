# SOC Incident Automation & Response

## Descripción
Este proyecto automatiza la detección, clasificación y respuesta ante incidentes de seguridad en un SOC. Utiliza Power Automate, Python y Bash para integrar herramientas de SIEM, APIs de Threat Intelligence y administración de servidores Linux, tambien orquesta contenedores y una webApp para testear su funcionamiento

## Características
✅ Automatización de respuesta a incidentes de ciberseguridad.  
✅ Integración con SIEM, APIs de Threat Intelligence y bases de datos.  
✅ Scripts en Linux (Bash/Python) para bloqueo y seguimiento de IPs.  
✅ Notificaciones automáticas a Microsoft Teams con Power Automate.  
✅ Buenas prácticas: SOLID, pruebas con pytest, documentación con Sphinx.
✅ Front e-comerce.
✅ Testear ataques y request validas.

## Tecnologías Utilizadas
- **Power Automate**: Captura alertas desde Outlook, SIEM o Syslog.  
- **Python + Bash**: Scripts para análisis y respuesta.  
- **APIs de Threat Intelligence**: Integración con VirusTotal, AbuseIPDB.  
- **SIEM (Splunk/ELK)**: Monitoreo y gestión de eventos.  (opcional)
- **Linux (iptables, fail2ban, logs)**: Seguridad en servidores.  
- **SQL Server / MongoDB**: Almacenamiento de incidentes.  
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
   pip install -r requirements.txt
   ```
3. Configurar credenciales en `config/`.
4. Ejecutar el script principal:  
   ```bash
   python scripts/incident_handler.py
   ```

## Licencia
Este proyecto está bajo la licencia MIT. Ver `LICENSE` para más detalles.

