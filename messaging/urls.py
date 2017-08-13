from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^addMessage/(?P<id>\d+)$', views.addMessage, name='addMessage'),
]
