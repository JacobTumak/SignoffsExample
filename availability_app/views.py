from django.shortcuts import render, HttpResponse, get_object_or_404
from django.views import generic
from django.contrib.auth.decorators import login_required
from .forms import EmployeeAvailabilityForm
from availability_app import models
import pprint


@login_required
def home_view(request):
    days = ['Sunday',
            'Monday',
            'Tuesday',
            'Wednesday',
            'Thursday',
            'Friday',
            'Saturday',]
    return render(request, 'avail_select.html', {'days': days})


@login_required
def submit_day_selection_view(request):
    if request.method == 'POST':
        selected_days = request.POST.getlist('day')

        employee, _ = models.Employee.objects.get_or_create(user=request.user)

        employee_availability, _ = models.EmployeeAvailability.objects.get_or_create(employee=employee)

        employee_availability.update_days([day.lower() for day in selected_days])

        # employee_availability.monday.

        employee_availability.save()

        # Having issues with this raising "nonetype object has no attribute get_full_name()"
        # sig, _ = models.EmployeeAvailabilitySignet.objects.get_or_create(employee=employee,
        #                                                                        signoff_id=models.availability_signoff.id)


        return HttpResponse(f"""Availabilty submitted for the following days {employee_availability.get_availability()}""")
    return HttpResponse('Day Selection Failed')


def all_availabilities(request):
    all_availabilities = models.EmployeeAvailability.objects.all()

    return render(request, 'all_availabilities.html', {'all_availabilities': all_availabilities})
