from django.conf.urls import url
from . import views
from django.urls import path

app_name = 'patients'

urlpatterns = [
    path('patient_list', views.patient_list, name='patient_list'),
    path('patient/<int:pk>/edit/', views.patient_edit, name='patient_edit'),
    path('patient/create/', views.patient_new, name='patient_new'),
    path('patient/<int:pk>/delete/', views.patient_delete, name='patient_delete'),
    

]
