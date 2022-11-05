from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=64, unique=True)
    toppings = models.TextField()
    price = models.DecimalField(max_digits=999, decimal_places=2)
    sale = models.BooleanField(default=False)
    description = models.TextField()
    votes = models.PositiveIntegerField()

    def __str__(self):
        return self.name

