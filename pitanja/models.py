from django.db import models
import datetime

class Osoba(models.Model):
    ime = models.CharField(max_length=50)
    godine = models.IntegerField(default = 2)

    def __str__ (self):
        return self.ime


class Pitanje(models.Model):
    ime = models.ForeignKey(Osoba, on_delete=models.CASCADE)
    naslov = models.CharField(max_length=300)
    tekst_pitanja = models.CharField(max_length=2000)
    vrijeme_objavljivanja = datetime.datetime.now()

    def __str__ (self):
        return self.naslov