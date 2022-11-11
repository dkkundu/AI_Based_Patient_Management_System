# PYTHON IMPORTS
import logging
# DJANGO IMPORTS
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator
from django.conf import settings
from address.models import District, Division, Upazila


# CORE IMPORTS

logger = logging.getLogger(__name__)


class Patient(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,
        blank=True, null=True, related_name="patient_data"
    )

    name = models.CharField(
    _("Patient Name"), max_length=120, null=True, blank=True
    )
    age = models.PositiveIntegerField(
        _("Patient Age"), null=True, blank=True
    )
    picture = models.ImageField(
        upload_to="Patient/", null=True, blank=True
    )
    nid = models.CharField(
        _('National ID'), max_length=17, unique=True, blank=True, null=True,
        validators=[RegexValidator(
            r'^(\d{10}|\d{13}|\d{17})$',
            message='Numeric 10/13/17 digits (ex: 1234567890)'
        )]
    )
    division = models.ForeignKey(
        Division, models.SET_NULL,
        related_name='patient_division',
        null=True
    )
    district = models.ForeignKey(
        District, models.SET_NULL,
        related_name='patient_district',
        null=True
    )
    upazila = models.ForeignKey(
        Upazila, models.SET_NULL,
        related_name='patient_upazila',
        null=True
    )
    post_code = models.PositiveIntegerField(
        null=True,
        help_text='Numeric 4 digits (ex: 1234)',
        validators=[RegexValidator(
            r"^[\d]{4}$", message='Numeric 4 digits (ex: 1234)'
        )]
    )
    address = models.TextField(
        null=True, help_text='Ex: 2/17, Mirpur-11'
    )

    def __str__(self):
        return str(self.name)

    @property
    def get_full_address(self):
        save_present_address = ''
        if self.address:
            save_present_address = ''.join(self.address)
        if self.upazila:
            save_present_address += f', {self.upazila} ,'
        if self.district:
            save_present_address += f' {self.district}'
        if self.post_code:
            save_present_address += f' - {self.post_code} ,'
        if self.division:
            save_present_address += f'{self.division} ,'
        save_present_address += 'Bangladesh '

        return save_present_address

