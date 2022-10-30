from django.urls import path
from . import views
from . import registation_view
from address.views import (
    load_district,
    load_upazila
)
from .dashboard import (
    VisitedAppointmentList,
    UnVisitedAppointmentList,
    AllPatientList,
    ProfileUpdate,
    DrProfileView,
)
from Core.views import (
    dr_change_password
)
urlpatterns = [
    path('', views.HomeView.as_view(), name='index'),
    path(
        'dashboard/', views.DoctorDashboard.as_view(), name='doctor_dashboard'
    ),
    path('services/', views.ServiceListView.as_view(), name="services"),
    path('services/<int:pk>/', views.ServiceDetailView.as_view(),
         name="service_details"),
    path('doctors/', views.DoctorListView.as_view(), name="doctors"),
    path('doctors/<int:pk>/', views.DoctorDetailView.as_view(),
         name="doctor_details"),
    path('faqs/', views.FaqListView.as_view(), name="faqs"),
    path('gallery/', views.GalleryListView.as_view(), name="gallery"),
    path('contact/', views.ContactView.as_view(), name="contact"),
    path(
        'registration/type/',
        registation_view.RegistrationPages.as_view(), name="registration_type"
    ),
    path(
        'login/', views.LoginView.as_view(), name="login"
    ),
    path(
        'logout/', views.logout_request, name="logout"
    ),
    path('load-district/', load_district, name='load_district'),
    path('load-upazila/', load_upazila, name='load_upazila'),
    path(
        'checked/appointment/list/',
        VisitedAppointmentList.as_view(), name='checked_appointment_list'
    ),
    path(
        'uncheck/appointment/list/',
        UnVisitedAppointmentList.as_view(), name='uncheck_appointment_list'
    ),
    path('patient/list/', AllPatientList.as_view(), name='patient_list'),


    path(
        'doctor/<int:pk>/update/',
        ProfileUpdate.as_view(), name='doctor_update'
    ),
    path('doctor/<int:pk>/view/', DrProfileView.as_view(), name='doctor_view'),
    path(
        'doctor/password/change/',
        dr_change_password, name='dr_change_password'
    ),


]
