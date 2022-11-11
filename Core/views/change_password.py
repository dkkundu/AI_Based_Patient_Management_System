from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy


def dr_change_password(request):
    template_name = 'dashboard/profile/password_change.html'
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!, '
                                      'Please Login with new Password')
            return redirect(
                reverse_lazy(
                    'doctor_view',
                    kwargs={'pk': request.user.doctor.pk}
                )
            )
        else:
            messages.warning(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, template_name, {
        'form': form
    })