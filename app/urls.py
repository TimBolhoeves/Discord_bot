from . import views
from django.urls import path

urlpatterns = [
    # Home
    path('', views.index, name='index'),

    path('botOn/<int:id>/', views.botOn, name='botOn'),
    path('botOff/<int:id>/', views.botOff, name='botOff'),
    
    # Auth
    path('login/', views.login, name='login'),
    path('login/post/', views.loginpost, name='loginpost'),
    path('logout/', views.logout, name='logout'),    
    #----
]