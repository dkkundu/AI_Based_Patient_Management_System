import logging
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from patient_ms.api.serializers import DoctorAppointmentSerializer
from patient_ms.models import DoctorAppointment
from address.models import District, Division, Upazila
from hospital.models import Doctor, Speciality
from Core.models import User
# from rest_framework.authentication import (
#     TokenAuthentication,
#     SessionAuthentication
# )
# from rest_framework.permissions import AllowAny
logger = logging.getLogger(__name__)


class DoctorAppointmentAPIView(APIView):
    model = DoctorAppointment
    serializer_class = DoctorAppointmentSerializer
    # authentication_classes = [TokenAuthentication, SessionAuthentication]

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            patient = get_object_or_404(
                User, pk=serializer.data.get('patient_id')
            )
            doctor = get_object_or_404(
                Doctor, pk=serializer.data.get('doctor_id')
            )
            speciality = get_object_or_404(
                Speciality, pk=serializer.data.get('speciality_id')
            )

            division = get_object_or_404(
                Division, pk=serializer.data.get('division_id')
            )
            district = get_object_or_404(
                District, pk=serializer.data.get('district_id')
            )
            upazila = get_object_or_404(
                Upazila, pk=serializer.data.get('upazila_id')
            )
            appointment_day = serializer.data.get('appointment_day')
            serial = 1
            try:
                save_object = self.model.objects.filter(
                    appointment_day__contains=appointment_day,
                    doctor=doctor
                ).last()
                if save_object:
                    if save_object.serial_number > 0:
                        serial = serial + save_object.serial_number
            except Exception as e:
                logger.debug(self.request, f"Unable to get Doctor as {e}")

            try:
                appointment = self.model.objects.create(
                    patient=patient, speciality=speciality,
                    division=division, district=district, upazila=upazila, doctor=doctor,
                    problem=serializer.data.get('problem'), appointment_day=appointment_day,
                    appointment_time=serializer.data.get('appointment_time'),
                    serial_number=serial
                )
            except Exception as e:
                logger.info(f"appointment create Faild {e}")
                appointment = None
            if appointment:
                return Response({
                    'status': 200,
                    'message': f'Appointment create Taken From {doctor.name}',
                    'serial_number': serial,
                })
        return Response({
            'status': 500,
            'message': 'Appointment create Failed',
        })

