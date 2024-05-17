from djongo import models
from accounts.models import CustomUser


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=32)
    price = models.FloatField()
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return self.name + " " + str(self.price)


class Cart(models.Model):
    user = models.OneToOneField(CustomUser, related_name='cart_user', on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, related_name='cart_products')

    def __str__(self):
        return self.user.email

