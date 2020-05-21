from django.db import models

class api_data(models.Model):
    title=models.CharField(max_length=100)
    category=models.CharField(max_length=150)
    color=models.CharField(max_length=100)
    size=models.PositiveIntegerField()

    def __str__(self):
        return self.title    