from django.db import models

# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()
    stock = models.IntegerField()
    image = models.URLField()

    def __str__(self):
        return self.title


class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    total = models.IntegerField()

    def __str__(self):
        return self.name
