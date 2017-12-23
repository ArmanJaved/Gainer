from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'gain', views.index, name='index'),
]
