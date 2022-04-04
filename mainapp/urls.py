from django.contrib import admin
from django.urls import URLPattern
from django.urls import path
from .views import Dashboard, home
import users.views as user_views

import users.views as user_views

urlpatterns = [
path('admin/', admin.site.urls),
path('',home, name = 'home'),
path('account/profile/', user_views.profile, name = 'profile'),
path('accounts/profile/', user_views.usersprofile, name = 'userprofile'),
path('register/',user_views.Register, name = 'register'),
path('dashboard/', Dashboard.as_view(), name = 'dashboard'),
# path('student_enrol/', user_views.studentform, name = 'studentenrol'),
path('logout_view/', user_views.logoutView, name = 'logoutview'),
]

