from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import check_password
from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from .models import User
from .serializers import *

# Create your views here.


@api_view(['GET'])
def index(request):
    return Response('ok',status=status.HTTP_200_OK)


class RegisterUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterUserSerializer
    permission_classes = (AllowAny,)


class LoginView(generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = LoginSerializer
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
       
        user = User.objects.get(phone = request.data['phone'])
        if user is not None:
            if user.check_password(request.data['password']) is True:
                if user.is_active:
                    login(request, user)
                    return Response({'logged_in':True,'user':user.id})
                else:
                    # Return a 'disabled account' error message
                    return Response({'detail':'not active'})
            return Response({'status':'password not valid'})
        else:
            return Response({'detail':'user not exists'})


@api_view(['GET'])
def logoutView(request):
    logout(request)
    return Response({'logged_out':True})
