from django.db import models
from django.contrib.auth.models import User
from .models import Product  # Assuming Product is in the same models.py file

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField()
    comment = models.TextField()

    def __str__(self):
        return f"Review by {self.user.username} for {self.product.name}"
