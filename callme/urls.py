from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'gainers', views.gainers, name='gainers'),
    url(r'losers', views.losers, name='losers'),
    url(r'multop', views.multop, name='multop'),
    url(r'mulbot', views.mulbot, name='mulbot'),
    url(r'consol', views.consol, name='consol'),
]
