from django.db import models

# Create your models here.

class Region(models.Model):
    year = models.IntegerField(default=0)
    population = models.IntegerField(default=0)
    nb_lits_touristiques = models.IntegerField(default=0)
    chomage = models.IntegerField(default=0)
    activity = models.IntegerField(default=0)
    nb_medecin = models.IntegerField(default=0)
    nuitees_touristiques = models.IntegerField(default=0)
    nb_eleves_primaire = models.IntegerField(default=0)
    nb_eleves_college = models.IntegerField(default=0)
    nb_eleves_lycee = models.IntegerField(default=0)



