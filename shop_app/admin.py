from django.contrib import admin
from .models import Category, Produkt
from django.contrib.admin import AdminSite



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

class UserAdmin(AdminSite):
    list_display = ['nazwa', 'slug', 'cena', 'stan', 'dostępność', 'utworzono', 'aktualizacja']
    list_filter = ['dostępność', 'utworzono', 'aktualizacja']
    list_editable = ['cena', 'stan', 'dostępność']
    prepopulated_fields = {'slug': ('nazwa',)}

    AdminSite.site_title = "Panel Pracownika"
    AdminSite.index_title = "Zarządzanie produktami"

    def has_permission(self, request):
        """
        Removed check for is_staff.
        """
        return request.user.is_active

user_admin = UserAdmin(name='user-admin')
user_admin.register(Produkt)