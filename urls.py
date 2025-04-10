from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),  # добавляем сюда путь для аутентификации
    path('', include('main.urls')),
]
