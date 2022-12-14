from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User

class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=100)
    friendly_name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name
    
    def get_friendly_name(self):
        return self.friendly_name

class Country(models.Model):

    class Meta:
        verbose_name_plural = 'Countries'

    name = models.CharField(max_length=100)
    friendly_name = models.CharField(max_length=100, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
    
    def get_friendly_name(self):
        return self.friendly_name

class Product(models.Model):
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL
        )
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    size = models.IntegerField()
    country = models.ForeignKey(
        'Country', null=True, blank=True, on_delete=models.SET_NULL
        )
    abv = models.DecimalField(max_digits=4, decimal_places=2)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    sku = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name


class ProductReview(models.Model):

    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    review = models.TextField(max_length=500)
    user_name = models.CharField(max_length=50, null=True, blank=True)
    rating = models.IntegerField(choices=RATING_CHOICES)

    def __str__(self):
        return self.review
