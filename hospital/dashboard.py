import datetime
from django.urls import reverse_lazy
from patient_ms.models import Patient
from django.views.generic import ListView, UpdateView, DetailView
from patient_ms.models import DoctorAppointment
from hospital.models import Doctor
from hospital.forms import DoctorFormUpdate
from django.contrib import messages
import logging

logger = logging.getLogger(__name__)


class VisitedAppointmentList(ListView):
    model = DoctorAppointment
    template_name = 'dashboard/appointment/vistied.html'

    def get_queryset(self):
        today = datetime.date.today()
        qs = self.model.objects.filter(
            doctor__user=self.request.user,
            appointment_day=today, is_visited=True
        )

        return qs


class UnVisitedAppointmentList(ListView):
    model = DoctorAppointment
    template_name = 'dashboard/appointment/not_vistied.html'

    def get_queryset(self):
        today = datetime.date.today()
        qs = self.model.objects.filter(
            doctor__user=self.request.user,
            appointment_day=today, is_visited=False
        )
        for x in qs:
            print("--------------", x.patient.patient_data.name)
        return qs


class AllPatientList(ListView):
    model = Patient
    template_name = 'dashboard/patient/list.html'


class ProfileUpdate(UpdateView):
    model = Doctor
    form_class = DoctorFormUpdate
    template_name = 'dashboard/profile/profile.html'

    def get_success_url(self):
        messages.success(self.request, "Successfully Updated")
        logger.debug("Successfully Updated")
        return reverse_lazy("index")


class DrProfileView(DetailView):
    model = Doctor
    template_name = 'dashboard/profile/profile_view.html'
