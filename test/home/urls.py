from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name="IndexView"),
    path('guatemala/', views.GuatemalaView.as_view(), name="GuatemalaView"),
]
