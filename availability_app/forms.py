from django import forms
from availability_app import models


class EmployeeAvailabilityForm(forms.Form):
    model = models.Employee
    fields = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']