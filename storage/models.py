from django.db import models

class Size(models.Model):
    name = models.TextField(unique=True)

    def __str__(self):
        return self.name
    
class Color(models.Model):
    name = models.TextField(unique=True)

    def __str__(self):
        return self.name

class Storage(models.Model):
    storage_id = models.BigAutoField(primary_key=True)
    name = models.TextField(blank=True)
    code = models.TextField(blank=True, null=True, unique=True)
    category = models.TextField(blank=True)
    size = models.ManyToManyField(Size, blank=True, related_name="size_storage")
    unit_price = models.FloatField(default=0)
    inventory = models.IntegerField(default=0)
    color = models.ManyToManyField(Color, blank=True, related_name="color_storage")

    def __str__(self):
        return self.name