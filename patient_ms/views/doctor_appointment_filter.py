from django.shortcuts import render
from hospital.models import Doctor


def doctor_filter(request):
    templates_name = 'appointment/appointment_filter.html'
    speciality = request.GET.get('speciality')
    division = request.GET.get('division')
    district = request.GET.get('district')
    upazila = request.GET.get('upazila')

    quarry_object = Doctor.objects.all()

    if speciality:
        if speciality == 0:
            quarry_object = quarry_object
        else:
            quarry_object = quarry_object.filter(
                speciality=speciality
            )
    if division:
        if division == 0:
            quarry_object = quarry_object
        else:
            quarry_object = quarry_object.filter(
                division=division
            )
    if district:
        if district ==0:
            quarry_object = quarry_object
        else:
            quarry_object = quarry_object.filter(
                district=district
            )
    if upazila:
        if upazila == 0:
            quarry_object = quarry_object
        else:
            quarry_object = quarry_object.filter(
                upazila=upazila
            )
    context = {
        "object_list": quarry_object
    }
    return render(request, templates_name, context)
