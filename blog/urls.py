from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.wpis_list, name='wpis_list'),
]
