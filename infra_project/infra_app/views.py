from django.http import HttpResponse


def index(request):
    return request, HttpResponse('У меня получилось!')


def second_page(request):
    return request, HttpResponse('А это вторая страница!')
