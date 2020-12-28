from django.db import models

# Create your models here.
class Filmy(models.Model):
    title = models.CharField(max_length = 100)
    description = models.TextField(blank = True)
    rate = models.CharField(max_length = 100)
    price = models.DecimalField(max_digits = 12, decimal_places = 2)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Film"
        verbose_name_plural = "Filmy"