import logging
from django.views.generic import (
    UpdateView, View
)
from django.contrib.auth.mixins import (
    UserPassesTestMixin, LoginRequiredMixin
)
from django.contrib import messages
from django.urls import reverse_lazy
from django.shortcuts import render, HttpResponseRedirect
from patient_ms.models import Patient
from patient_ms.forms import PatientUpdateForm
logger = logging.getLogger(__name__)


class PatientProfile(
    UserPassesTestMixin,
    LoginRequiredMixin,
    View
):
    template_name = 'patient/profile.html'
    model = Patient

    def test_func(self):
        """Tests if the user is active"""
        return self.request.user.is_active  # any active user

    def get(self, request):
        try:
            object = self.model.objects.filter(
                user=self.request.user
            )
        except Exception as e:
            logger.debug(self.request, f'Request user not Patient {e}')
            messages.warning(request, 'Please Login with Patient Account ')
            return HttpResponseRedirect('index')

        context = {
            "object": object,
        }
        return render(request, self.template_name, context)


class PatientInfoUpdate(
    UserPassesTestMixin,
    LoginRequiredMixin,
    UpdateView
):
    template_name = 'patient/update_patient.html'
    model = Patient
    form_class = PatientUpdateForm

    def test_func(self):
        """Tests if the user is active"""
        return self.request.user.is_active  # any active user

    def get_success_url(self):
        messages.success(self.request, "Successfully Updated")
        logger.debug("Successfully Updated")
        return reverse_lazy("patient_ms:patient_profile")
