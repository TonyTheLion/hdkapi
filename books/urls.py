from django.urls import path

from . import views

urlpatterns = [
        path('', views.index, name = 'index'),
        path('published/<int:order>', views.published_date, name = 'published_date'),
        path('title/<int:order>', views.title, name='title')
        ]
