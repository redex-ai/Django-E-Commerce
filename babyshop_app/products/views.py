from django.db import models
from django.contrib.auth.models import User

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()

    def __str__(self):
        return f'Review by {self.user.username} for {self.product.name}'
