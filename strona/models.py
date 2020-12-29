from django.db import models

# Create your models here.
class Filmy(models.Model):
    title = models.CharField(max_length = 100)
    image = models.ImageField(null = True, blank = True)
    description = models.TextField(blank = True)
    rate = models.CharField(max_length = 100)
    ticketPrice = models.DecimalField(max_digits = 12, decimal_places = 2)

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = "Film"
        verbose_name_plural = "Filmy"