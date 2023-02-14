from django.http import HttpResponse


def item_list(request):
    return HttpResponse('<body>Список элементов в каталоге</body>')


def item_detail(request, variable):
    return HttpResponse(
        f'<body>Подробно элемент об элементе {variable}' '</body>'
    )
