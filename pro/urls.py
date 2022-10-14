from django.contrib import admin
from django.urls import path,include
from website.views import home
from login.views import loginn
urlpatterns = [
    path('login/',loginn),
    path('',include('base.urls')),
    path('admin/', admin.site.urls),
]
