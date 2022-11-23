from django import forms
from hospital.models import Doctor


class DoctorForm(forms.ModelForm):

    class Meta:
        model = Doctor
        fields = [
            "name",
            "picture",
            'speciality',
            'doctor_id'

        ]

    def __init__(self, *args, **kwargs):
        super(DoctorForm, self).__init__(*args, **kwargs)
        self.fields["name"].required = True
        self.fields["picture"].required = True
        self.fields["speciality"].required = True


class DoctorFormUpdate(forms.ModelForm):

    class Meta:
        model = Doctor
        exclude = ['user']
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
                }),
            'details': forms.Textarea(
                attrs={'rows': 3, 'cols': 5}
            ),

        }

    def __init__(self, *args, **kwargs):
        super(DoctorFormUpdate, self).__init__(*args, **kwargs)
        self.fields["name"].required = True
        self.fields["picture"].required = True
        self.fields["present_hospital"].required = True
        self.fields["speciality"].required = True
        self.fields['address'].widget.attrs['rows'] = 3
