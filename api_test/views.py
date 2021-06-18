from django.shortcuts import render

# Create your views here.
from django.views.decorators.http import require_http_methods
from django.core import serializers
from django.http import JsonResponse
import json
from .models import Book

from .models import Book

def test(request):
    return JsonResponse({"status":0,"message":"jsdfo"})

def ret_book(request):
    if request.method == "GET":
        books = Book.objects.all()
        json = serializers.serialize('json',books)
        return JsonResponse({"status":0,"data":json})