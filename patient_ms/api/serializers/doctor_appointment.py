import datetime
from rest_framework import serializers
from patient_ms.models import DoctorAppointment


class DoctorAppointmentSerializer(serializers.Serializer):
    speciality_id = serializers.IntegerField()
    division_id = serializers.IntegerField()
    district_id = serializers.IntegerField()
    upazila_id = serializers.IntegerField()
    doctor_id = serializers.IntegerField()
    patient_id = serializers.IntegerField()
    problem = serializers.CharField()
    appointment_day = serializers.DateField(initial=datetime.date.today)
    appointment_time = serializers.TimeField(initial=datetime.date.today)



class DoctorsTodaysAppointmentSerializer(serializers.Serializer):
    doctor_id = serializers.IntegerField()


class RecordCreateSerializer(serializers.Serializer):
    doctor_id = serializers.IntegerField()
    patient_id = serializers.IntegerField()
    record = serializers.CharField()


