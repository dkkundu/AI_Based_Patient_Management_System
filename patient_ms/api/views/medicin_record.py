import logging
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from patient_ms.models import DoctorPrescription, Patient
from patient_ms.api.serializers import RecordCreateSerializer
from hospital.models import Doctor
from Core.models import User
logger = logging.getLogger(__name__)


class MedicalRecordAPIView(APIView):
    model = DoctorPrescription
    serializer_class = RecordCreateSerializer
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
            record = serializer.data.get('record')
            try:
                data_record = self.model.objects.create(
                    patient=patient.patient_data, doctor=doctor.user,
                    record=record,
                )
            except Exception as e:
                logger.info(f"record create Faild {e}")
                data_record = None
            if data_record:
                return Response({
                    'status': 200,
                    'message': f'New Record Added by {doctor.name}',
                })
        return Response({
            'status': 500,
            'message': 'Appointment create Failed',
        })
