from django.urls import path
from . views import UserCreateApi, UserLoginApi, protectedView

urlpatterns = [
    path('create/', UserCreateApi, name='create'),
    path('login/', UserLoginApi, name='login'),
    path('protected/', protectedView, name='protected'),
]