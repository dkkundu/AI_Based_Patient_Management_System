from django.contrib import admin
from patient_ms.models import (
    Patient,
    DoctorAppointment,
    DoctorPrescription,
    RecordFile
)


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = [
        'name', 'age', 'nid', 'division', 'district',
        'upazila'
    ]


@admin.register(DoctorAppointment)
class DoctorAppointmentAdmin(admin.ModelAdmin):
    list_display = [
        'patient', 'doctor', 'appointment_time', 'serial_number', 'is_visited',
    ]


@admin.register(DoctorPrescription)
class DoctorPrescriptionAdmin(admin.ModelAdmin):
    list_display = [
        'patient', 'doctor', 'created_at',
    ]


@admin.register(RecordFile)
class RecordFileAdmin(admin.ModelAdmin):
    list_display = [
        'file_name', 'record', 'created_at',
    ]
