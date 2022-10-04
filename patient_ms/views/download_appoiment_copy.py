from django.views.generic import DetailView
from patient_ms.views.get_pdf import render_pdf
from patient_ms.models import DoctorAppointment


class AppointmentCopyPDFView(DetailView):
    model = DoctorAppointment
    template_name = 'appointment/download.html'

    def get(self, request, pk, ):
        save_object = self.model.objects.get(
            pk=pk
        )
        context = {
            'object': save_object,
        }
        return render_pdf(
            request, self.template_name, context, 'appointment_copy'
        )
