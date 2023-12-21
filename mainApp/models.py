from django.db import models

# Create your models here.

class RegisterUser(models.Model):
    name = models.CharField(max_length=90)
    phone = models.CharField(max_length=15, unique=True)
    preferred_language = models.CharField(max_length=90)
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ('-datetime',)