from django.contrib import admin
from .models import Order, OrderItem

# Register your models here.
class OrderItem(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'surname', 'email', 'adres', 'code', 'city', 'pay','utworzono' , 'zmieniono']
    list_filter = ['pay', 'utworzono' , 'zmieniono']
    inlines = [OrderItem]
admin.site.register(Order, OrderAdmin)