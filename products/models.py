from django.db import models

from users.models import User


class Categories(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name = 'categories'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Products(models.Model):
    name = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='media')
    category_id = models.ForeignKey(to=Categories, on_delete=models.CASCADE, verbose_name='category')

    class Meta:
        verbose_name = 'products'
        verbose_name_plural = 'products'

    def __str__(self):
        return self.name


class BasketQuerySet(models.QuerySet):
    def total_quantity(self):
        list_q = [i.quantity for i in self]
        return sum(list_q)

    def total_sum(self):
        sum_products = 0
        for basket_object in self:
            sum_products = sum_products + basket_object.quantity * basket_object.product.price
        return sum_products


class Basket(models.Model):
    product = models.ForeignKey(to=Products, on_delete=models.CASCADE)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    objects = BasketQuerySet.as_manager()

    def __str__(self):
        return f'Product: {self.product.name}'

    def sum(self):
        return self.quantity * self.product.price
