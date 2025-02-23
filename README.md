# SOC Incident Automation & Response

## Descripción
Este proyecto automatiza la detección, clasificación y respuesta ante incidentes de seguridad en un SOC. Utiliza Power Automate, Python y Bash para integrar herramientas de SIEM, APIs de Threat Intelligence y administración de servidores Linux.

## Características
✅ Automatización de respuesta a incidentes de ciberseguridad.  
✅ Integración con SIEM, APIs de Threat Intelligence y bases de datos.  
✅ Scripts en Linux (Bash/Python) para bloqueo de IPs y gestión de usuarios.  
✅ Notificaciones automáticas a Microsoft Teams o Telegram.  
✅ Dashboard para visualización de incidentes en Flask/FastAPI.  
✅ Buenas prácticas: SOLID, pruebas con pytest, documentación con Sphinx.  

## Tecnologías Utilizadas
- **Power Automate**: Captura alertas desde Outlook, SIEM o Syslog.  
- **Python + Bash**: Scripts para análisis y respuesta.  
- **APIs de Threat Intelligence**: Integración con VirusTotal, AbuseIPDB.  
- **SIEM (Splunk/ELK)**: Monitoreo y gestión de eventos.  
- **Linux (iptables, fail2ban, logs)**: Seguridad en servidores.  
- **SQL Server / MongoDB**: Almacenamiento de incidentes.  
- **pytest, flake8, Sphinx**: Pruebas y documentación.  

## Estructura del Proyecto
```
AutoSoc/
├── README.md  # Documentación del proyecto
├── LICENSE  # Licencia del proyecto
├── scripts/  # Scripts de automatización
│   ├── incident_handler.py  # Script principal
│   ├── block_ip.sh  # Bloqueo de IPs en Linux
│   ├── disable_user.py  # Deshabilita usuario en Active Directory
│   ├── send_alerts.py  # Envía notificaciones a Teams/Telegram
│   ├── fetch_threat_intel.py  # Consulta APIs de Threat Intelligence
├── tests/  # Pruebas unitarias con pytest
├── docs/  # Documentación con Sphinx
├── config/  # Configuración del sistema
├── logs/  # Registro de actividad
├── web/  # Dashboard en Flask/FastAPI (opcional)
├── .gitignore  # Archivos a excluir
├── requirements.txt  # Librerías necesarias
├── docker-compose.yml  # Contenedor con SIEM y herramientas
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

