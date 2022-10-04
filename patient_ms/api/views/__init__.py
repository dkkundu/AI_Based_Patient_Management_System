from .doctor_appointment import DoctorAppointmentAPIView
from .get_doctor_appointment_list import DoctorTodaysAppointmentAPIView
from .medicin_record import MedicalRecordAPIView

__all__ = [
    DoctorAppointmentAPIView,
    DoctorTodaysAppointmentAPIView,
    MedicalRecordAPIView
]
