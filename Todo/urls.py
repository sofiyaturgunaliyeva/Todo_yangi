from django.contrib import admin
from django.urls import path
from asosiy.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('plans/', hamma_todo),
    path('', login_view, name = 'login'),
    path('logout/', logout_view),
    path('reja_ochir/<int:son>/', reja_ochir),
    path('register/', register),
]
