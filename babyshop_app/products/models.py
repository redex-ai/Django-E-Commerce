from django.db import models
from django.conf import settings

class Category(models.Model):
    name = models.CharField(max_length=50, null=True)
    slug = models.SlugField(max_length=50, unique=True, null=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=80)
    description = models.TextField()
    image = models.ImageField(upload_to="products/%Y/%m/%d/", default="products/broken-1.png")
    date = models.DateField(auto_now=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.ForeignKey(Category, null=True, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name

class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField()
    comment = models.TextField()

    def __str__(self):
        return f'Review by {self.user.username} for {self.product.name}'
