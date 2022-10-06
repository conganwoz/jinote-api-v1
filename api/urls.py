from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('hello/', views.say_hello),
    path('upload_note/', views.upload_note),
    path('download_notes/', views.download_notes),
    path('publish_notes/', views.publish_notes),
    path('<str:room_name>/', views.room, name='room'),
]
