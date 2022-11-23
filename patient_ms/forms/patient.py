from django import forms
from patient_ms.models import Patient


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = [
            "name",
            "age",
            "nid",
        ]
        widgets = {
            'nid': forms.TextInput(
                attrs={'placeholder': 'Numeric 10/13/17 digits (ex: 1234567890)'}
            ),
        }

    def __init__(self, *args, **kwargs):
        super(PatientForm, self).__init__(*args, **kwargs)
        self.fields["name"].required = True
        self.fields["age"].required = True
        self.fields["nid"].required = True


class PatientUpdateForm(forms.ModelForm):
    class Meta:
        model = Patient
        exclude = [
            'user'
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
            'post_code': forms.TextInput(attrs={
                'id': 'post_code'
            }),
            'address': forms.Textarea(attrs={
                'id': 'address',
                'rows': 2
            }),

        }

    def __init__(self, *args, **kwargs):
        super(PatientUpdateForm, self).__init__(*args, **kwargs)
        self.fields["age"].required = True
        self.fields["nid"].required = True
