from django.http import HttpResponse


def index(request):
    return (request, '/', HttpResponse('У меня получилось!'))


def second_page(request):
    return request, '/second_page/', HttpResponse('А это вторая страница!')
