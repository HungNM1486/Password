from django.urls import path
from .views import home_view, add_password_view, delete_password_view

urlpatterns = [
    path('home/', home_view, name='home'),
    path('add/', add_password_view, name='add_password'),
    path('delete/<int:entry_id>/', delete_password_view, name='delete_password'),
]
