from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.say_hello),
    path('upload_note/', views.upload_note),
    path('download_notes/', views.download_notes)
]
