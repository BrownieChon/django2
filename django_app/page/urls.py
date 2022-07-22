from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.chonpat, name='chonpat'),
    path('forms', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('register/regist/', views.regist, name='regist'),
    path('<int:members_id>', views.index_member, name='index_member'),
    path('logout/', views.logout, name='logout'),
    path('forget/', views.forget, name='forget'),
    path('forget/sent', views.forgetpassword, name='forgetpassword'),
    
]