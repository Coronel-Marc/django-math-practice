from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('practice/<str:category>/', views.practice, name='practice'),
]
