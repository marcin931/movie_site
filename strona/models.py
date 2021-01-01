from django.db import models

# Create your models here.
class movie(models.Model):
    title = models.CharField(max_length = 100)
    image = models.ImageField(null = True, blank = True, upload_to = "images/")
    description = models.TextField(blank = True)
    rate = models.CharField(max_length = 100)
    ticketPrice = models.DecimalField(max_digits = 12, decimal_places = 2)

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = "movie"
        verbose_name_plural = "movies"

