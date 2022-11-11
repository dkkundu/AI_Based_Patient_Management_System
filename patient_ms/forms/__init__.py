from .patient import (
    PatientForm,
    PatientUpdateForm
)
from .doctor_prescription import (
    DoctorPrescriptionForm,
    record_file_formset
)
from .doctor_appointment import DoctorAppointmentForm
__all__ = [
    PatientForm,
    PatientUpdateForm,
    DoctorAppointmentForm,
    DoctorPrescriptionForm,
    record_file_formset
]
