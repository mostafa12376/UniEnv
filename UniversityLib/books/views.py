from django.shortcuts import render
from django.http import HttpResponse
from pages.models import Book

# Create your views here.
def index(request):
    return HttpResponse(Book.objects.get(id = 2).Borrower)

