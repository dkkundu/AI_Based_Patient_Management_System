from django import forms
from patient_ms.models import DoctorAppointment


class DoctorAppointmentForm(forms.ModelForm):
    class Meta:
        model = DoctorAppointment
        exclude = [
            'patient',
            "serial_number",
            "is_visited",
            'appointment_close_time'
        ]
        widgets = {
            'division': forms.Select(attrs={
                'id': 'division'
            }),
            'district': forms.Select(attrs={
                'id': 'district'
            }),
            'upazila': forms.Select(attrs={
                'id': 'upazila'
            }),
            'appointment_day': forms.DateInput(
                attrs={
                    'type': 'date'
                }),
            'appointment_time': forms.TimeInput(
                attrs={
                    'type': 'time'
                })
        }

    def __init__(self, *args, **kwargs):
        super(DoctorAppointmentForm, self).__init__(*args, **kwargs)
        self.fields['doctor'].required = True
        self.fields['appointment_day'].required = True
        self.fields['appointment_time'].required = True
        self.fields['speciality'].required = True

