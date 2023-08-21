from django.db import models

class Order(models.Model):
    item = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.item} - {self.quantity}개"
