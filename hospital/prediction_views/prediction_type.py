import datetime
from django.urls import reverse_lazy
from patient_ms.models import Patient
from django.views.generic import TemplateView
from patient_ms.models import DoctorAppointment
from hospital.models import Doctor
from hospital.forms import DoctorFormUpdate
from django.contrib import messages
import logging

logger = logging.getLogger(__name__)


class PredictionType(TemplateView):
    model = DoctorAppointment
    template_name = 'dashboard/prediction/type.html'


