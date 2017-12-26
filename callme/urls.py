from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'gainers', views.gainers, name='gainers'),
    url(r'losers', views.losers, name='losers'),
]
