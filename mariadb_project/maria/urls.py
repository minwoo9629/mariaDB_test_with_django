from . import views
from django.urls import path

urlpatterns = [
    path('', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout, name='logout'),
    path('search/', views.search, name='search'),
]
