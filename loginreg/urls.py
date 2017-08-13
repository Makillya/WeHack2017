from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register$', views.register, name = "register"),
    url(r'^login$', views.login, name = "login"),
    url(r'^profile$', views.login, name = "profile"),
    url(r'^success$', views.login, name = "success"),
    url(r'^logout$', views.logout, name = "logout"),
]
