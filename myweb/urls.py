"""myweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from myapp import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'myapp', views.myappViewSet)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('page/', views.page),
    path('login/', views.login),
    path('register/', views.register),
    path('signin/', views.signin),
    path('signup/', views.signup),
    path('logout/', views.logout, name='logout'),
    # path(r'^admin/', admin.site.urls),
    # path(r'^$', sayhello),
    path('rank/', views.rank, name='rank'),
    path('member/', views.member, name='member'), 
    path('change/', views.change),
    path('report/', views.qa, name='report_issue'),
    path('qa/', views.qa, name='qa'),
    path('point_use/', views.point_use_view, name='point_use_view'),
    path('userbuy/', views.userbuy),
    #path('savebuy/', views.savebuy),
    path('C_usehistory/', views.C_usehistory),
    #api----------------------------
    path('api2/', views.api2, name='api2'),
    path('Login_and_AddSession/', views.Login_and_AddSession, name='Login_and_AddSession'),
    path('loginpage/', views.login2_view),
    path('login2', views.login2),
    path('GDPR/', views.GDPR), 
    path('api/', include(router.urls))
]
