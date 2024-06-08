from django.urls import path
from . import views


urlpatterns = [
    path('', views.BookAPIList.as_view(), name='book-list')
]