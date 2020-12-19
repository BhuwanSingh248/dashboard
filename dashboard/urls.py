from django.urls import path
from . import views

urlpatterns = [
    path('',views.dashboard, name='index'),
    path('dashboard.html', views.dashboard, name = 'index'),
    path('icons.html', views.icons, name= 'icons'),
    path('notifications.html', views.notification, name = 'notification'),
    path('tables.html', views.tables, name = 'tables'),
    path('user.html', views.user, name = 'users'),

]