#!/usr/bin/env pythonpi
import os
import sys


def main():
    """Punto de entrada principal para las tareas de \
        administración de Django."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "No se pudo importar Django. ¿Está instalado y \
                en el entorno virtual activo?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
