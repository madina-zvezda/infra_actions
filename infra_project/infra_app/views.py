from http import HTTPStatus

from django.http import HttpResponse, response


def index(request):
    return request, HttpResponse('У меня получилось!')


def second_page(request):
    return request, HttpResponse('А это вторая страница!')
