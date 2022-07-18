
from django.db import models

# Create your models here.
class Pokemon(models.Model):
    name = models.CharField(max_length=30)

    
    class PokemonType(models.TextChoices):
    
       WATER= ("WATER", "WA"),
       GRASS= ("GRASS", "GR"),
       GHOST= ("GHOST", "GH"),
       STEEL= ("STEEL","ST"),
       FARIY= ("FAIRY","FA"),
    Pokemon_Type= models.CharField(
        max_length=200,
        choices=PokemonType.choices,
    )
    hp=models.PositiveBigIntegerField(default=0)
    active=models.BooleanField(default=True)
    name_fr=models.CharField(max_length=30, default="")
    name_ar=models.CharField(max_length=30, default="")
    name_jp=models.CharField(max_length=30, default="")
    created_at=models.DateTimeField(auto_now_add=True)
    modified_at=models.DateTimeField(auto_now=True)

