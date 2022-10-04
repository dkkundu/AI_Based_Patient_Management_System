from .doctor_appoiment import DoctorAppointment
from .doctor_appointment_filter import doctor_filter
from .add_record import DoctorPrescriptionView
from .record_view import ViewAllSavedRecord
from .patient_profile import (
    PatientProfile,
    PatientInfoUpdate,
)
from .get_pdf import render_pdf
from .appointment_confirmation_letter import AppointmentConfirmationLetterView
from .get_serial_record import ForgetAppointmentSerialView
from .download_appoiment_copy import AppointmentCopyPDFView
__all__ = [
    PatientInfoUpdate,
    PatientInfoUpdate,
    DoctorAppointment,
    DoctorPrescriptionView,
    doctor_filter,
    ViewAllSavedRecord,
    PatientProfile,
    ForgetAppointmentSerialView,
    AppointmentConfirmationLetterView,
    render_pdf,
    AppointmentCopyPDFView
]
