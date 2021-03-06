from django.conf.urls import url
from django.contrib import admin
from . import views
from .admin import user_admin

app_name = 'shop'

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^user-admin/', user_admin.urls),
    url(r'^$', views.product_list, name='product_list'),
    url(r'^(?P<category_slug>[-\w]+)/$', views.product_list, name='product_list_by_category'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.product_detail, name='product_detail'),
]