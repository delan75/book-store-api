from django.urls import path
from .api import BookListApi, BookCreateApi, BookUpdateApi, BookDeleteApi


urlpatterns = [
    path('list/', BookListApi, name='books'),
    path('create/', BookCreateApi, name='create'),
    path('update/<int:id>/', BookUpdateApi, name='update'),
    path('delete/<int:id>/', BookDeleteApi, name='delete'),
    
]
