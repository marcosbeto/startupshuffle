from django.db import models

class launch_users(models.Model):
    startup_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
