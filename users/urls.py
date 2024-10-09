from django.urls import path

from users import views
from users.views import appointment_history

app_name = 'users'

urlpatterns = [
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('registration/', views.UserRegistrationView.as_view(), name='registration'),
    path('profile/', views.UserProfileView.as_view(), name='profile'),
    path('users-cart/', views.UserCartView.as_view(), name='users_cart'),
    path('logout/', views.logout, name='logout'),
    path('users/book_appointment/', views.book_appointment, name='book_appointment'),
    path('appointment_history/', views.appointment_history, name='appointment_history'),
    path('appointment_success/', views.appointment_success, name='appointment_success')
]

