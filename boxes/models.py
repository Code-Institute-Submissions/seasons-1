from django.db import models

# Create your models here.


class Season(models.Model):
    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name


class Boxes(models.Model):
    season = models.ForeignKey('Season', null=True, blank=True, on_delete=models.SET_NULL)
    box_name = models.CharField(max_length=254)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    description = models.TextField()
    size = models.CharField(max_length=254)
    fruit = models.TextField()
    veg = models.TextField()
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.box_name

