"""criminal_investigation_tracker_with_suspect_prediction URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from admin_user import views
from officer import views as officer_views


urlpatterns = [
    path('administrator/', admin.site.urls), #admin:admin
    path('login/', views.login),
    path('logout/', views.logout),
    path('cases/<slug>', officer_views.detailCaseView),
    path('officer/',include('officer.urls')), #otest1:shanmukha

    path('admin-user/',include('admin_user.urls')),
]