from django.urls import path
from officer import views

urlpatterns = [
    path('', views.home),
    path('viewAllCases', views.viewAllCases),
    path('addSuspect', views.addSuspect),
]