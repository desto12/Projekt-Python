from django.db import models

# Create your models here.
class Category(models.Model):
    nazwa = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, unique=True, db_index=True)
    utworzono = models.DateTimeField(auto_now_add=True)
    zaktalizowano = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('nazwa',)
        verbose_name = 'kategoria'
        verbose_name_plural = 'kategorie'

    def __str__(self):
        return self.nazwa


class Produkt(models.Model):
    kategoria = models.ForeignKey(Category, related_name='produkty', on_delete=models.CASCADE)
    nazwa = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)
    opis = models.TextField(blank=True)
    cena = models.DecimalField(max_digits=10, decimal_places=2)
    dostępność = models.BooleanField(default=True)
    stan = models.PositiveIntegerField()
    utworzono = models.DateTimeField(auto_now_add=True)
    aktualizacja = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='produkty/%Y/%m/%d', blank=True)

    class Meta:
        ordering = ('nazwa',)
        verbose_name = 'produkt'
        verbose_name_plural = 'produkty'
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.nazwa