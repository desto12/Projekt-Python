from django.contrib import admin
from .models import Category, Produkt


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['nazwa', 'slug']
    prepopulated_fields = {'slug': ('nazwa',)}


admin.site.register(Category, CategoryAdmin)


class ProduktAdmin(admin.ModelAdmin):
    list_display = ['nazwa', 'slug', 'cena', 'stan', 'dostępność', 'utworzono', 'aktualizacja']
    list_filter = ['dostępność', 'utworzono', 'aktualizacja']
    list_editable = ['cena', 'stan', 'dostępność']
    prepopulated_fields = {'slug': ('nazwa',)}


admin.site.register(Produkt, ProduktAdmin)