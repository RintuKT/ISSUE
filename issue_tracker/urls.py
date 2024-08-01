from django.contrib import admin
from django.urls import include, path
from tracker import views as tracker_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', tracker_views.home, name='home'),
    path('tracker/', include('tracker.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='tracker/login.html'), name='login'),
    path('logout/', tracker_views.logout_view, name='logout'),
]
