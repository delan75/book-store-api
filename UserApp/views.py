from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.contrib.auth import authenticate, login, logout
from rest_framework.authtoken.models import Token


@api_view(['POST'])
def UserCreateApi(request):
    data = request.data
    User.objects.create_user(username=data['username'], password=data['password'])
    return Response({
        'message': 'User created successfully'},
        status=status.HTTP_201_CREATED
    )

@api_view(['POST'])
def UserLoginApi(request):
    data = request.data
    user = authenticate(username=data['username'], password=data['password'])
    if user is not None:
        login(request, user)

        token,create = Token.objects.get_or_create(user=user)

        return Response({
            'message': 'User logged in successfully',
            'token': token.key
        })
    else:
        return Response({
            'message': 'Invalid credentials'
        }, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['GET'])
def protectedView(request):
    if request.user.is_authenticated:
        return Response({
            'message': 'This is a protected view',
            'user': 'you are logged in as ' + request.user.username
        })
    else:
        return Response({
            'message': 'You are not authenticated'
        }, status=status.HTTP_401_UNAUTHORIZED)