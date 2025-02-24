from .models import UserSession
from .serializers import UserSessionSerializer
from rest_framework.exceptions import ValidationError

def save_one_session(request_data):
    try:
        sessions_count = UserSession.objects.filter(ip=request_data.get("ip")).count()
        serializer = UserSessionSerializer(data=request_data)
        
        if serializer.is_valid():
            if sessions_count > 4:
                serializer.validated_data['is_blocked'] = True
            else:
                serializer.validated_data['is_blocked'] = False
            serializer.save()
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