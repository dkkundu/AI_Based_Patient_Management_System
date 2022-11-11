# PYTHON IMPORTS
import logging
# DJANGO IMPORTS
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from patient_ms.models import Patient
from ckeditor.fields import RichTextField

logger = logging.getLogger(__name__)


class DoctorPrescription(models.Model):
    doctor = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,
        blank=True, null=True, related_name="doctor_prescription"
    )
    patient = models.ForeignKey(
        Patient, on_delete=models.SET_NULL,
        blank=True, null=True, related_name="patient_prescription"
    )
    record = RichTextField()

    created_at = models.DateTimeField(
        _('Created At'), auto_now_add=True, null=True
    )
    last_updated = models.DateTimeField(
        _('Last Updated'), auto_now=True, null=True
    )

    def __str__(self):
        return f'Pt :{self.patient} Dr: {self.doctor}'


class RecordFile(models.Model):
    file_name = models.CharField(
        _('File Name'), max_length=500, null=True
    )
    record = models.ForeignKey(
        DoctorPrescription, on_delete=models.SET_NULL,
        blank=True, null=True, related_name="file"
    )
    document = models.FileField(
        upload_to='uploads/% Y/% m/% d/'
    )
    created_at = models.DateTimeField(
        _('Created At'), auto_now_add=True, null=True
    )

    def __str__(self):
        return self.file_name



