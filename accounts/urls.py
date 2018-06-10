from django.conf.urls import url
from django.contrib.auth.views import login,logout
from. import views

app_name = 'accounts'


urlpatterns = [
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', login, {'template_name': 'accounts/login.html'}, name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^profile/$', views.profile, name='profile')
]