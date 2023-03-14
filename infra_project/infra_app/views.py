from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, '/', HttpResponse('У меня получилось!'))


def second_page(request):
    return render(request, '/second_page/', HttpResponse('А это вторая страница!'))
