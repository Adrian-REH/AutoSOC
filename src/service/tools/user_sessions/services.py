from .models import UserSession
from .serializers import UserSessionSerializer
from rest_framework.exceptions import ValidationError

def save_one_session(request_data, ip):
    try:
        if isinstance(request_data, dict):
            # Actualizamos la clave "ip" con el valor de ip
            request_data["ip"] = ip
        else:
            # Si no es un diccionario, debes convertirlo o ajustarlo según tu caso
            # Ejemplo: si es un objeto de tipo serializer, puedes hacer algo como:
            request_data = dict(request_data)  # Convertir a dict (si es un objeto)
            request_data["ip"] = ip
        sessions_count = UserSession.objects.filter(ip=ip).count()
        serializer = UserSessionSerializer(data=request_data)

        if serializer.is_valid():
            instance = serializer.save(is_blocked=(sessions_count > 2))
            return {
                'alert_count': sessions_count,
                'session_data': serializer.data
            }
        else:
            raise ValidationError(serializer.errors)
    except Exception as e:
        # Log the error message here
        print(f"Error: {str(e)}")
    return None


def delete_all_session_by_ip(request_data):
    try:
        sessions_to_delete = UserSession.objects.filter(ip=request_data.get("ip"))
        
        deleted_count, _ = sessions_to_delete.delete()
        return deleted_count
    except Exception as e:
        # Log the error message here
        print(f"Error: {str(e)}")
    return None