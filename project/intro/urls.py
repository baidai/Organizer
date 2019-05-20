from django.urls import path
from . import views 



app_name = 'intro'  

urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('register/', views.register, name="register"),
    path('logout/', views.logout_request, name="logout"),
    path('login/', views.login_request, name="login"),
    path('pic/', views.upload, name="Upload"),
    path('new/', views.new, name="new"),
    path('list/', views.list, name="list"),
] 


