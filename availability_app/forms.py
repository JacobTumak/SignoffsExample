from django import forms


class EmployeeAvailabilityForm(forms.Form):
    availability = {'monday': forms.BooleanField(required=False),
                   'tuesday': forms.BooleanField(required=False),
                   'wednesday': forms.BooleanField(required=False),
                   'thursday': forms.BooleanField(required=False),
                   'friday': forms.BooleanField(required=False),
                   'saturday': forms.BooleanField(required=False),
                   'sunday': forms.BooleanField(required=False)}


