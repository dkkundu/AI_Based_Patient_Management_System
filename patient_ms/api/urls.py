from django.urls import path
from patient_ms.api.views import (
    DoctorAppointmentAPIView,
    DoctorTodaysAppointmentAPIView,
    MedicalRecordAPIView
)

app_name = 'patient_ms_api'
urlpatterns = [
    path(
        'doctor-appointment/',
        DoctorAppointmentAPIView.as_view(), name='doctor_appointment'
    ),
    path(
        'dr-todays-appointment/',
        DoctorTodaysAppointmentAPIView.as_view(), name='doctor_todays_appointment'
    ),
    path('add-record/', MedicalRecordAPIView.as_view(), name='add_record'),

]
