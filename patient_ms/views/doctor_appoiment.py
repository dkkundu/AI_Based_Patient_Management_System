import logging
import datetime
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.views.generic import CreateView
from django.contrib.auth.mixins import (
    UserPassesTestMixin, LoginRequiredMixin, PermissionRequiredMixin
)
from django.contrib import messages
from patient_ms.models import DoctorAppointment
from patient_ms.forms import DoctorAppointmentForm
logger = logging.getLogger(__name__)


class DoctorAppointment(
    UserPassesTestMixin,
    LoginRequiredMixin,
    CreateView
):
    model = DoctorAppointment
    form_class = DoctorAppointmentForm
    template_name = 'appointment/index.html'

    def test_func(self):
        """Tests if the user is active"""
        return self.request.user.is_active  # any active user

    def form_valid(self, form):
        appointment_day = form.cleaned_data.get("appointment_day").strftime("%Y-%m-%d")
        doctor = form.cleaned_data.get("doctor")
        serial = 1
        try:
            save_object = self.model.objects.filter(
                appointment_day__contains=appointment_day,
                doctor=doctor
            ).last()
            if save_object:
                if save_object.serial_number > 0:
                    serial = serial + save_object.serial_number
        except Exception as e:
            logger.debug(self.request, f"Unable to get Doctor as {e}")
            redirect(self.get_error_url())

        save_form = form.save(commit=False)
        save_form.patient = self.request.user
        save_form.serial_number = serial
        save_form.save()
        return super(DoctorAppointment, self).form_valid(form)

    def get_success_url(self):
        messages.success(
            self.request,
            "Successfully Appointment Taken, "
            "Please Download the appointment letter"
        )
        logger.debug("Successfully Updated")
        return reverse_lazy(
                    "patient_ms:appointment_confirmation",
                    kwargs={'pk': self.object.pk}
        )

    def get_error_url(self):
        messages.warning(self.request, "Unable to take Appointment")
        logger.debug("Unable to get Appointment")
        return reverse_lazy("index")

