from django.urls import path, include, re_path
from women import views

urlpatterns = [
    path('', views.index, name='home'),  #http://127.0.0.1:8000
    path('about/', views.about, name='about'),
    path('cats/<int:cat_id>/', views.categories, name='cats_id'),  #http://127.0.0.1:8000/cats/123
    path('cats/<slug:cat_slug>/', views.categories_by_slug, name='cats'),  #http://127.0.0.1:8000/cats/123abc
    re_path(r'^archive/(?P<year>[0-9]{4})/', views.archive, name='archive'),  #http://127.0.0.1:8000/archive/2005/


]