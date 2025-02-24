from django.db import models

class UserSession(models.Model):
    ip = models.GenericIPAddressField()
    user_agent = models.CharField(max_length=255)
    language = models.CharField(max_length=10)
    platform = models.CharField(max_length=10)
    screen_width = models.IntegerField()
    screen_height = models.IntegerField()
    timestamp = models.DateTimeField()
    security_level = models.CharField(max_length=10)
    alert_type = models.CharField(max_length=50)
    is_blocked = models.BooleanField(default=False)
