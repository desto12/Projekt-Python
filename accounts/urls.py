from django.conf.urls import url
from django.contrib.auth.views import login,logout


urlpatterns = [
    #url(r'^register/$', register, name='register'),
    url(r'^login/$', login, {'template_name': 'accounts/login.html'}),
    url(r'^logout/$', logout, {'template_name': 'accounts/logout.html'})
]