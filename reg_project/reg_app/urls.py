from django.contrib import admin
from django.urls import path

from reg_app.views import get


urlpatterns = [
    path('register/',get),
    # path('createuser/', createuser),
    # path('<int:pk>', reg)
]

