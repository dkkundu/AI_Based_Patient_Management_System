import logging

from django.urls import reverse_lazy
from django.views.generic import (
    View
)
from django.contrib.auth.mixins import (
    UserPassesTestMixin, LoginRequiredMixin
)
from django.contrib import messages
from django.shortcuts import render, HttpResponseRedirect, redirect
from patient_ms.models import DoctorAppointment
logger = logging.getLogger(__name__)


class ForgetAppointmentSerialView(
    UserPassesTestMixin,
    LoginRequiredMixin,
    View
):
    template_name = 'patient/get_last_serial.html'
    model = DoctorAppointment

    def test_func(self):
        """Tests if the user is active"""
        return self.request.user.is_active  # any active user

    def get(self, request):
        last_appitment = self.model.objects.filter(
            patient=self.request.user
        ).last()

        context = {
            "last_appitment": last_appitment,
        }
        return render(request, self.template_name, context)

    def post(self, request):
        try:
            appointment_time = request.POST.get('appointment_day')
            print("--------", appointment_time)
            appointment = self.model.objects.filter(
                patient=self.request.user,
                appointment_day=appointment_time
            ).last()
        except Exception as e:
            logger.debug(self.request, f'Unable to get Appointment {e}')
            messages.warning(
                self.request, "Unable to get data"
            )
            return redirect('patient_ms:appointment_forget')

        if appointment:
            return HttpResponseRedirect(
                reverse_lazy(
                    "patient_ms:appointment_confirmation",
                    kwargs={'pk': self.appointment.pk}
                )
            )
        else:
            messages.warning(
                self.request, "Dont have any Appointment on Searching date"
            )
        return redirect('patient_ms:appointment_forget')





