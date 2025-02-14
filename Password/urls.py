from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('', RedirectView.as_view(url='home/')),  # Chuyển hướng đường dẫn trống đến /home/
    path('', include('password_manager.urls')),
]
