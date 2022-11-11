# PYTHON IMPORTS
import logging
# DJANGO IMPORTS
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from address.models import District, Division, Upazila
from hospital.models import Doctor, Speciality

# CORE IMPORTS

logger = logging.getLogger(__name__)


class DoctorAppointment(models.Model):
    patient = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,
        blank=True, null=True, related_name="appointment"
    )
    speciality = models.ForeignKey(
        Speciality, on_delete=models.PROTECT,
        blank=True, null=True, related_name="appointment_speciality"
    )
    division = models.ForeignKey(
        Division, models.SET_NULL,
        related_name='appointment_division',
        blank=True, null=True,
    )
    district = models.ForeignKey(
        District, models.SET_NULL,
        related_name='appointment_district',
        blank=True, null=True,
    )
    upazila = models.ForeignKey(
        Upazila, models.SET_NULL,
        related_name='appointment_upazila',
        blank=True, null=True,
    )
    doctor = models.ForeignKey(
        Doctor, on_delete=models.SET_NULL,
        blank=True, null=True,
    )
    problem = models.CharField(
        _("Problem"), max_length=500, null=True, blank=True
    )
    appointment_day = models.DateField(
        _('Appointment Day'), null=True, blank=True
    )
    appointment_time = models.TimeField(
        _('Appointment Time'), null=True, blank=True
    )
    appointment_close_time = models.DateField(
        _('Appointment Close Time'), null=True, blank=True
    )
    serial_number = models.PositiveIntegerField(
        _('Serial Number'), default=0
    )
    is_visited = models.BooleanField(
        _('Is Doctor Check'), default=False
    )

    def __str__(self):
        return f'{self.patient}- Dr:({self.doctor}), Time: {self.appointment_time}'


