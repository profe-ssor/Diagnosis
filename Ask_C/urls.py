from django.urls import path
from . import views

urlpatterns = [
    path('', views.register, name="register_page"),
    path('login_page/', views.login_page, name="login_page"),
     path('logout_page/', views.logout_page, name="logout_page"),

    path('index/', views.index, name="index_page"),
    path('add-patient/', views.add_patient, name="add-patient"),
    path('appointment/', views.appointment, name="meet"),
    path('patient-list/', views.patient_list, name="patient-list"),
    path('doctor/', views.doctor, name="doctor"),
    path('contact/', views.contact, name="contact"),
    path('in-patient/', views.inpatient, name="in-patient"),
    path('out-patient/', views.outpatient, name="out-patient"),

    path('update<str:pk>/', views.update_Patientlist, name="update"),
    path('upload/', views.upload, name="upload"),
    path('delete<str:pk>/', views.deleteTask, name="delete"),
]
