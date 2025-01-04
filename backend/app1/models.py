from django.db import models

class ShoppingItem(models.Model):
    name = models.CharField(max_length=100)
    amount = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name
