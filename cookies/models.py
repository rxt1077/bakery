from django.db import models

class Cookie(models.Model):
    cookie_type = models.CharField(max_length=200)
    amount = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    nut_free = models.BooleanField(default=True)

