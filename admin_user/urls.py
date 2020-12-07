from django.urls import path
from admin_user import views


urlpatterns = [
    path('', views.home),
    path('create', views.create),
    path('retrieve', views.retrieve),
    path('addCase', views.addCase),
]