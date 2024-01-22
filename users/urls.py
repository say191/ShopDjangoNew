from django.urls import path
from users.views import LoginView, LogoutView, RegisterView, EmailVerify, UserUpdateView, generate_new_password
from users.apps import UsersConfig

app_name = UsersConfig.name
urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('verify_email/<str:email_token>/', EmailVerify.as_view(), name='verify_email'),
    path('profile/', UserUpdateView.as_view(), name='profile'),
    path('profile/generatepass/', generate_new_password, name='generate_new_password')
]