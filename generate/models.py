from django.db import models

class AvatarComponent(models.Model):
    name = models.CharField(max_length=100)  # E.g., "Eye 1", "Mouth 2"
    svg_content = models.TextField()
    # Other fields as needed
