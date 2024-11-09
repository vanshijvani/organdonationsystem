# api/urls.py
from django.urls import path
from .views import DonorCreateView, RecipientCreateView
from .views import SignupView, LoginView, LogoutView, HomePageView
from rest_framework_simplejwt.views import TokenRefreshView
urlpatterns = [
    # Donor endpoints
    path('donors/register/', DonorCreateView.as_view(), name='donor-register'),

    # Recipient endpoints
    path('recipients/register/', RecipientCreateView.as_view(), name='recipient-register'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('home/', HomePageView.as_view(), name='home'), 
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Refresh JWT token
]