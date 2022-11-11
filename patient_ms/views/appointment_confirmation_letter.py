import logging
from django.views.generic import DetailView
from django.contrib.auth.mixins import (
    UserPassesTestMixin, LoginRequiredMixin
)
from patient_ms.models import DoctorAppointment
logger = logging.getLogger(__name__)


class AppointmentConfirmationLetterView(
    UserPassesTestMixin,
    LoginRequiredMixin,
    DetailView
):
    template_name = 'appointment/appointement_letter.html'
    model = DoctorAppointment

    def test_func(self):
        """Tests if the user is active"""
        return self.request.user.is_active  # any active user

