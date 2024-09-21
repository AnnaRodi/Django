from django.http import HttpResponse, Http404, HttpResponseNotFound, HttpRequest, HttpResponsePermanentRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

menu = ['О сайте', 'Добавить статью', 'Обратная связь', 'Войти']

def index(request):  # HttpRequest
    data ={ 'title': 'Главная страница',
            'menu': menu,
            }
    return render(request, 'women/index.html', context = data)

def about(request):  # HttpRequest
    return render(request, 'women/about.html', { 'title': 'О сайте'})

def categories(request, cat_id):
    return HttpResponse(f"<h1>Статьи по категориям</h1><p >id:{cat_id}</p>")

def categories_by_slug(request, cat_slug):
    if request.POST:
        print(request.POST)
    return HttpResponse(f"<h1>Статьи по категориям</h1><p >slug:{ cat_slug }</p>")

def archive(request, year):
    if int(year)>2023:
        url_redirect = reverse('cats', args = ('music', ))
        return HttpResponsePermanentRedirect(url_redirect)

    return HttpResponse(f"<h1>Архив по годам</h1><p >{year}</p>")

def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


