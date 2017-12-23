from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls import url

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^pai/', include('callme.urls')),

]