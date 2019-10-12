"""wick_authentication URL Configuration

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
from django.urls import path,include
from django.contrib.auth import views as auth_views
from users import views as user_views
from users.views import UsersListView, UsersUpdateView, UsersDeleteView, UsersCreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('homepage.urls')),
    path('register/', user_views.register1, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login-form.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('profile/', user_views.profile, name='profile'),
    path('overseer/', UsersListView.as_view(), name='overseer'),
    path('overseer/<int:pk>/update/', UsersUpdateView.as_view(), name='user-update'),
    path('overseer/<int:pk>/delete/', UsersDeleteView.as_view(), name='user-delete'),
    path('overseer/new/', UsersCreateView.as_view(), name='user-create'),
]
