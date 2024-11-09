from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response 
from rest_framework import status
from rest_framework import generics 
from .models import donors, recipients
from .serializers import DonorSerializer, RecipientSerializer
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserRegisterSerializer
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login, logout

class DonorCreateView(generics.CreateAPIView):
    queryset = donors.objects.all()
    serializer_class = DonorSerializer

class RecipientCreateView(generics.CreateAPIView):
    queryset = recipients.objects.all()
    serializer_class = RecipientSerializer

class SignupView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = UserRegisterSerializer

class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            refresh = RefreshToken.for_user(user)
            login(request, user)
            return Response({
                "refresh": str(refresh),
                "access": str(refresh.access_token),
                "user_id": user.id,
                "username": user.username,
                "email": user.email,
            }, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)

class LogoutView(APIView):
    def post(self, request):
        logout(request)
        return Response({"message": "Logged out successfully"}, status=status.HTTP_200_OK)

class HomePageView(APIView):
    def get(self, request):
        return Response({"message": "Welcome to the home page!"})
