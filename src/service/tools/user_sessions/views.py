from rest_framework.response import Response
from rest_framework.decorators import api_view
from .handle_email import send_email
import requests
from .models import UserSession
from rest_framework import status
from .serializers import UserSessionSerializer
from rest_framework.exceptions import ValidationError
from .services import save_one_session, delete_all_session_by_ip


@api_view(['GET'])
def list_sessions(request):
    sessions = UserSession.objects.all()
    serializer = UserSessionSerializer(sessions, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def save_session(request):
    session = save_one_session(request.data, request.data.get("ip"))

    if session:
        return Response(session, status=status.HTTP_201_CREATED)

    return Response(session, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_session_by_ip(request):
    session = delete_all_session_by_ip(request.data)

    if session:
        return Response(session, status=status.HTTP_200_OK)

    return Response(session, status=status.HTTP_400_BAD_REQUEST)
