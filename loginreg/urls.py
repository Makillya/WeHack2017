from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register$', views.register, name = "register"),
    url(r'^login$', views.login, name = "login"),
    url(r'^profile$', views.profile, name = "profile"),
    url(r'^search$', views.search, name = "search"),
    url(r'^logout$', views.logout, name = "logout"),
]
