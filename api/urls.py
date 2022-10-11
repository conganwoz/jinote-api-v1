from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('upload_note/', views.upload_note),
    path('download_notes/', views.download_notes),
    path('<str:room_name>/', views.room, name='room'),
]
