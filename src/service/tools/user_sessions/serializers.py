from rest_framework import serializers
from .models import UserSession

class UserSessionSerializer(serializers.ModelSerializer):
    screen = serializers.JSONField(write_only=True)  # Acepta el objeto `screen`, pero no lo devuelve

    class Meta:
        model = UserSession
        fields = [
            'ip', 'user_agent', 'language', 'platform',
            'screen', 'timestamp', 'security_level', 'alert_type', 'is_blocked'
        ]

    def create(self, validated_data):
        screen_data = validated_data.pop('screen', None)
        if screen_data is not None:
            validated_data['screen_width'] = screen_data.get('width')
            validated_data['screen_height'] = screen_data.get('height')
        else:
            raise serializers.ValidationError("Screen data is required.")
        return UserSession.objects.create(**validated_data)
