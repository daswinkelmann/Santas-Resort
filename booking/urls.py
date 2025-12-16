from django.urls import path
from . import views

urlpatterns = [
    path('stay/', views.book_stay, name='book_stay'),
    path('activities/', views.book_activities, name='book_activities'),
]
