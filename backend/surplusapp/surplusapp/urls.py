"""
URL configuration for surplusapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.homepage),
    # path('dislogin',views.dislogin),
    # path('soulogin',views.soulogin),
    path('souhome',views.souhome,name="SOUHOME"),
    path('loginauth',views.usrlogin, name="DISHOME"),
    path('slogin',views.sourceloginpage, name="SLOG"),
    path('dlogin',views.disloginpage, name="DLOG"),
    path('regis',views.regisource,name="REGISOURCE"),
    path('regid',views.regidist,name="REGIDISTRIBUTOR"),
    path('sousignup', views.source_signup_view, name="sousignup"),
    path('home',views.successpage,name='home'),
    path('debug',views.debugall),
    path('regsignup', views.reg_signup_view, name="regsignup"),
    path('check_username/', views.chkusername, name='check_username'),
    path('registersource', views.source_signup_view2),
    path('accounts/login/check-auth',views.check_auth),
    path('check-auth',views.check_auth),
    path('api/add_listing/', views.add_listing, name='add_listing'),
    path('api/get_card_data/', views.get_card_data, name='get_card_data'),
]
