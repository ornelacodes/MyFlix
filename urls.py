from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from movies import views as movie_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('movies.urls')),  
    path('admin/', admin.site.urls),
    path('', include('movies.urls')),

   
    path('login/', auth_views.LoginView.as_view(template_name='movies/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

   
    path('signup/', movie_views.signup_view, name='signup'),
]
