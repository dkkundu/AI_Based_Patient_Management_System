import logging

from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.mixins import (
    UserPassesTestMixin, LoginRequiredMixin, PermissionRequiredMixin
)
from django.contrib import messages
from django.urls import reverse_lazy
from patient_ms.models import (
    DoctorPrescription,
    Patient
)
logger = logging.getLogger(__name__)


class ViewAllSavedRecord(
    UserPassesTestMixin,
    LoginRequiredMixin,
    View
):
    template_name = 'dashboard/record/record_view.html'
    model = DoctorPrescription

    def test_func(self):
        """Tests if the user is active"""
        return self.request.user.is_active  # any active user

    def get(self, request, pk):
        print("--------------------", pk)

        try:
            patient_object = Patient.objects.get(
                pk=pk
            )
            objects_list = self.model.objects.filter(
                patient=patient_object
            ).order_by('-created_at')
            print("--------------------", patient_object)
            print("--------------------", objects_list)
        except Exception as e:
            logging.debug(request, f'Unable to get data {e}')
            objects_list = None

        context ={
            "objects_list": objects_list,
            "patient": patient_object
        }
        return render(request, self.template_name, context)

