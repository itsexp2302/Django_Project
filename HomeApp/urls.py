from django.contrib import admin
from django.urls import path, include
from .import views
app_name = "main"

urlpatterns = [

    path('', views.MainHome, name='MainHome'),
    path('details/<int:id>/',views.detail,name='detail'),
    path('addreview/<int:id>/', views.add_review, name='add_review')
]