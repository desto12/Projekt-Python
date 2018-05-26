from django.db import models
from shop_app.models import Produkt


# Create your models here.
class Order(models.Model):
    name = models.CharField('Imię', max_length=30)
    surname = models.CharField('Nazwisko', max_length=30)
    email = models.EmailField()
    adres = models.CharField('Adres', max_length=30)
    code = models.CharField('Kod pocztwoy', max_length=30)
    city = models.CharField('Miasto', max_length=30)
    utworzono = models.DateTimeField(auto_now_add=True)
    zmieniono = models.DateTimeField(auto_now=True)
    pay = models.BooleanField('Stan Płatności', default=False)

    class Meta:
        ordering = ('-utworzono',)
        verbose_name = 'zamówienie'
        verbose_name_plural = 'zamówienia'

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE,)
    product = models.ForeignKey(Produkt, related_name='order_items', on_delete=models.CASCADE,)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity
