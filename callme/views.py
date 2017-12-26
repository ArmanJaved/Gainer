from __future__ import unicode_literals
from django.http import HttpResponse
from callme import gai
from callme import los

from django.shortcuts import render

def gainers(request):

    var1 = request.get_full_path()
    print (var1)
    gai.main()
    return HttpResponse("<h1> Done !!! </h1>")

# Create your views here.


def losers(request):

    var1 = request.get_full_path()
    print (var1)
    los.main()
    return HttpResponse("<h1> Done !!! </h1>")