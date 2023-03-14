from http import HTTPStatus

from django.http import HttpResponse, response


def index(request):
    if request == 'Get':
        return response.status_code, HTTPStatus.OK
    return HttpResponse('У меня получилось!')


def second_page(request):
    if request == 'Get':
        return response.status_code, HTTPStatus.OK
    return HttpResponse('А это вторая страница!')
