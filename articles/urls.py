# -*- coding: utf-8 -*-
from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.base, name='base'),
    path('index/', views.index, name='index'),
    path('tabs/', views.tabs, name='tabs'),
    path('widget/', views.widget, name='widget'),
    path('table/', views.table, name='table'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('_404/', views._404, name='_404'),
    path('sign/', views.sign, name='sign'),
    path('resume/', views.resume, name='resume'),
    path('inbox/', views.inbox, name='inbox'),
    path('compose/', views.compose, name='compose'),
    path('editor/', views.editor, name='editor'),
    path('chart/', views.chart, name='chart'),
    path('ribbon/', views.ribbon, name='ribbon'),
    path('blank/', views.blank, name='blank'),
    path('project/', views.project, name='project'),
    path('_500/', views._500, name='_500'),
]