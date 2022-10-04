from django import forms
from django.forms import formset_factory
from patient_ms.models import (
    DoctorPrescription,
    RecordFile
)


class DoctorPrescriptionForm(forms.ModelForm):
    class Meta:
        model = DoctorPrescription
        fields = [
            'record',
        ]

    def __init__(self, *args, **kwargs):
        super(DoctorPrescriptionForm, self).__init__(*args, **kwargs)
        self.fields['record'].required = True
        self.fields['record'].label = False


class RecordFileForm(forms.ModelForm):
    class Meta:
        model = RecordFile
        fields = [
            'file_name',
            'document',
        ]

    def __init__(self, *args, **kwargs):
        super(RecordFileForm, self).__init__(*args, **kwargs)
        self.fields['file_name'].required = True
        self.fields['document'].required = True


record_file_formset = formset_factory(
    RecordFileForm, extra=1
)
