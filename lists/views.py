from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home_page(req):
    # return HttpResponse("")
    return render(req,'index.html')