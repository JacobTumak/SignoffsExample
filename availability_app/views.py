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

        employee, created = models.Employee.objects.get_or_create(user=request.user)

        employee.availability.update_days(selected_days)

        # try:
        #     employee_availability_instance = models.EmployeeAvailability.objects.get(employee=request.user)
        # except models.EmployeeAvailability.DoesNotExist:
        #     employee_availability_instance = models.EmployeeAvailability.objects.create(employee=request.user)
        #
        # employee_availability_instance.update_days(selected_days)

        sig, created = models.EmployeeSignet.objects.get_or_create(user=request.user,
                                                            signoff_id=models.availability_signoff.id,
                                                            employee_availability=employee_availability_instance)


        return HttpResponse(f"""Availabilty submitted for the following days {employee_availability_instance.availability}""")
    return HttpResponse('Day Selection Failed')


def all_availabilities(request):
    all_employees = Employee.objects.all()

    return render(request, 'all_availabilities.html', {'all_employees': all_employees})



# @login_required
# def submit_day_selection_view(request):
#
#     try:
#         employee_availability_instance = EmployeeAvailability.objects.get(employee=request.user)
#     except EmployeeAvailability.DoesNotExist:
#         employee_availability_instance = EmployeeAvailability.objects.create(employee=request.user)
#
#     if request.method == 'POST':
#         form = EmployeeAvailabilityForm(request.POST)
#
#         if form.is_valid():
#             print(form.cleaned_data)
#             employee_availability_instance.days = form.cleaned_data
#             employee_availability_instance.save()
#
#     else:
#         form = EmployeeAvailabilityForm(initial={'availability': employee_availability_instance.get_days_list()})
#
#     context = {'days': days, 'form': form}
#
#     return render(request, template, context)




