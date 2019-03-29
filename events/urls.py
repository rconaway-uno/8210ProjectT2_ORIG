
from . import views
from django.conf.urls import url, include
from django.contrib import admin
#from django.contrib.auth import views
from django.urls import path
from django.contrib.auth import views as auth_views


app_name = 'events'

urlpatterns = [
    path('', views.home, name='home'),
    url(r'^home/$', views.home, name='home'),

    url(r'^admin_login/', views.admin_home, name='adminlogin'),
    url(r'^nurse_login/', views.nurse_home, name='nurselogin'),

    path('admin_home', views.admin_home, name='admin_home'),
    path('nurse_home', views.nurse_home, name='nurse_home'),
#change password urls
    path('accounts/password_change/',auth_views.PasswordChangeView.as_view(),name='password_change'),
    path('accounts/password_change/done/',auth_views.PasswordChangeDoneView.as_view(),name='password_change_done'),
    path('password_reset/',	auth_views.PasswordResetView.as_view(),	name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),	name='password_reset_done'),
    path('reset/<uidb64>/<token>/',	auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset/done/',	auth_views.PasswordResetCompleteView.as_view(),	name='password_reset_complete'),

    path('admin/user_option', views.user_option, name='user_option'),
    path('admin/nurse_list', views.nurse_list, name='nurse_list'),
    path('admin/users_list', views.users_list, name='users_list'),

    path('user/<int:pk>/edit/', views.user_edit, name='user_edit'),
    path('user/<username>/delete/', views.user_delete, name='user_delete'),
    path('user/create/', views.user_new, name='user_new'),
    path('nurse_home', views.nurse_home, name='nurse_home'),
    path('event_list', views.event_list, name='event_list'),
    path('event/<int:pk>/edit/', views.event_edit, name='event_edit'),
    path('event/create/', views.event_new, name='event_new'),
    path('event/<int:pk>/delete/', views.event_delete, name='event_delete'),
]


