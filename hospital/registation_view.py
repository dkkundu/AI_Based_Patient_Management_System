import logging
from django.shortcuts import render
from django.contrib import messages
from django.views.generic import View
from django.contrib.auth.models import Group
from hospital.forms import DoctorForm
from Core.forms import CommonSignupForm
from patient_ms.forms import PatientForm
logger = logging.getLogger(__name__)


class RegistrationPages(View):
    template_name = 'hospital/registation.html'

    def get(self, request, *args, **kwargs):
        context = {
            "form": DoctorForm,
            "signup": CommonSignupForm,
            "form_patient": PatientForm,
            "signup_patient": CommonSignupForm,

        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = DoctorForm(request.POST, request.FILES or None)
        signup_form = CommonSignupForm(request.POST or None)

        form_patient = PatientForm(request.POST or None)
        signup_patient = CommonSignupForm(request.POST or None)

        if form_patient.is_valid() and signup_patient.is_valid():
            patient_group, is_create = Group.objects.get_or_create(
                name='Patient')
            save_user = signup_patient.save()
            save_user.groups.add(patient_group)
            obj = form_patient.save(commit=False)
            obj.user = save_user
            obj.save()
            try:
                patient_group, is_create = Group.objects.get_or_create(name='Patient')
                save_user = signup_patient.save()
                save_user.groups.add(patient_group)
                obj = form_patient.save(commit=False)
                obj.user = save_user
                obj.save()
                messages.success(self.request, "Account successfully created")
                logger.debug(self.request, "Account successfully created")
            except Exception as e:
                logger.error(f"Unable to create account: {e}")
                messages.warning(self.request, "Unable to create account")
                logger.debug(self.request, "Unable to create account")

        elif form.is_valid() and signup_form.is_valid():
            try:
                doctor_group, is_create = Group.objects.get_or_create(name='Doctor')
                save_user = signup_form.save()
                save_user.groups.add(doctor_group)
                obj = form.save(commit=False)
                obj.user = save_user
                obj.save()
                messages.success(self.request, "Account successfully created")
                logger.debug(self.request, "Account successfully created")
            except Exception as e:
                logger.error(f"Unable to create account: {e}")
                messages.warning(self.request, "Unable to create account")
                logger.debug(self.request, "Unable to create account")
        else:
            print("signup_form Doctor-----", signup_form.errors)
            print("form----- Doctor", form.errors)
            print("form_patient-----", form_patient.errors)
            print("CommonSignupForm-----", CommonSignupForm.errors)
            messages.warning(
                self.request, f"Invalid data for NID and Password"


            )
            logger.debug(self.request, "Unable to create account")

        context = {
            "form": form,
            "signup": signup_form,
            "form_patient": PatientForm,
            "signup_patient": signup_patient,

        }
        return render(request, self.template_name, context)


