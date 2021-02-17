from djmoney.models.fields import MoneyField
from django.db import models
from account.models import User

# Create your models here.



class movie(models.Model):
    title = models.CharField(max_length = 100)
    image = models.ImageField(null = True, blank = True, upload_to = "images/")
    description = models.TextField(blank = True)
    rate = models.CharField(max_length = 100)
    ticketPrice = MoneyField(max_digits = 14, decimal_places = 2, default_currency = 'PLN')
    ticketAvailability = models.BooleanField(default=True, verbose_name="dostępny")
    ticketQuantity = models.DecimalField(max_digits = 3, decimal_places = 0, default = 0)


    def __str__(self):
        return self.title


    class Meta:
        verbose_name = "movie"
        verbose_name_plural = "movies"


class Order(models.Model):
    customer = models.ForeignKey(User, on_delete = models.SET_NULL, blank = True, null = True)
    date_ordered = models.DateTimeField(auto_now_add = True)
    complete = models.BooleanField(default = False, null = True, blank = False)
    transaction_id = models.CharField(max_length = 6, null= True)

    def __str__(self):
        return str(self.id)

class OrderItem(models.Model):
    product = models.ForeignKey(movie, on_delete = models.SET_NULL, blank = True, null = True)
    order = models.ForeignKey(Order, on_delete = models.SET_NULL, blank = True, null = True)
    quantity = models.IntegerField(default = 0, null = True, blank = True)
    date_added = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.product.title



