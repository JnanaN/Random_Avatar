from django.db import models

class Eye(models.Model):
    eye_svg = models.TextField()

    def __str__(self):
        return f"{self.id}.svg"
class Mouth(models.Model):
    mouth_svg = models.TextField()

    def mouth__str__(self):
        return f"{self.id}.svg"



