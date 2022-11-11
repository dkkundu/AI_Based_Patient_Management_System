import logging
from rest_framework.views import APIView
from patient_ms.api.serializers import DoctorsTodaysAppointmentSerializer
from patient_ms.models import DoctorAppointment
from django.shortcuts import get_object_or_404
from hospital.models import Doctor
import datetime
from rest_framework.response import Response

logger = logging.getLogger(__name__)


class DoctorTodaysAppointmentAPIView(APIView):
    model = DoctorAppointment
    serializer_class = DoctorsTodaysAppointmentSerializer

    # authentication_classes = [TokenAuthentication, SessionAuthentication]

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        datalist = []
        if serializer.is_valid():
            doctor = get_object_or_404(
                Doctor, pk=serializer.data.get('doctor_id')
            )
            appointment_list = self.model.objects.filter(
                doctor=doctor, appointment_day=datetime.date.today()
            )
            patient = ''
            serial_number = ''
            appointment_time = ''
            problem = ''

            for appointment in appointment_list:
                dr_appointment = {
                    'patient_id': appointment.patient.pk,
                    'patient_name': appointment.patient.patient_data.name,
                    'patient_picture': appointment.patient.patient_data.picture.url,
                    'patient_age': appointment.patient.patient_data.age,
                    'patient_phone': appointment.patient.phone,
                    'serial_number': appointment.serial_number,
                    'appointment_time': appointment.appointment_time,
                    'problem': appointment.problem,
                }
                datalist.append(dr_appointment)

            return Response({
                'status': 200,
                'message': 'Successfully Appointment List get',
                'data': datalist
            })

        return Response({
            'status': 500,
            'message': 'Failed to get Appointment List',
        })



