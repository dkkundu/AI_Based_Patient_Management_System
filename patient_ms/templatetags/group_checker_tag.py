from django import template
import logging
from hospital.uility import user_has_group
from patient_ms.variable import (
    doctor_group,
    patient_group
)
logger = logging.getLogger(__name__)
register = template.Library()


@register.filter
def is_doctor(user):
    print(user)
    return user_has_group(user, doctor_group)


@register.filter
def is_patient(user):
    return user_has_group(user, patient_group)

