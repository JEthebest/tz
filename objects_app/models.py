from django.db import models

from profile_app.models import User
# Create your models here.


class Item(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    name = models.CharField(max_length=30)
    price = models.DecimalField(decimal_places=True, max_digits=10)

    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Items'