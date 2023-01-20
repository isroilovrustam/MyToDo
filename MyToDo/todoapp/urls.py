from django.urls import path
from .views import index, edit, created, delete, registration, login_view, logout_view

urlpatterns = [
    path('', index, name='index'),
    path('edit/<int:pk>/', edit, name='edit'),
    path('created/', created, name='created'),
    path('delete/<int:pk>/', delete, name='delete'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('registration/', registration, name='registration'),
]
