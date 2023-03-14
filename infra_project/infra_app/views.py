from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse('У меня получилось!')


def second_page(request):
    return HttpResponse('А это вторая страница!')
