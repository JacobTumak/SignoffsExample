from django.db import models
from django.contrib.auth.models import User
from signoffs.models import Signet
from signoffs.signoffs import SimpleSignoff


# Create your models here.
class EmployeeAvailabilityOld(models.Model):
    employee = models.ForeignKey(User, on_delete=models.CASCADE)
    availability = {
        'sunday': models.BooleanField(default=False),
        'monday': models.BooleanField(default=False),
        'tuesday': models.BooleanField(default=False),
        'wednesday': models.BooleanField(default=False),
        'thursday': models.BooleanField(default=False),
        'friday': models.BooleanField(default=False),
        'saturday': models.BooleanField(default=False)
                    }

    def update_days(self, days):
        for day in self.availability:
            self.availability[day] = False
            if day in days:
                self.availability[day] = True
        self.save()


class EmployeeAvailability(models.Model):
    sunday = models.BooleanField(default=False, name='Sunday')
    monday = models.BooleanField(default=False, name='Monday')
    tuesday = models.BooleanField(default=False, name='Tuesday')
    wednesday = models.BooleanField(default=False, name='Wednesday')
    thursday = models.BooleanField(default=False, name='Thursday')
    friday = models.BooleanField(default=False, name='Friday')
    saturday = models.BooleanField(default=False, name='Saturday')

    def update_days(self, days):
        for field in self._meta.get_fields():
            self.field = False
            if field.name.lower() in days:
                self.field = True
        self.save()


class Employee(models.Model):
    employee = models.ForeignKey(User, on_delete=models.CASCADE)
    availability = models.ForeignKey('EmployeeAvailability', on_delete=models.CASCADE, default=False)


availability_signoff = SimpleSignoff.register(id='availability_app.AvailabilitySignoff',
                                              signetModel='EmployeeSignet')


class EmployeeSignet(Signet):
    signoff_id = 'availability_app.AvailabilitySignoff'
    employee_availability = models.ForeignKey('EmployeeAvailability', on_delete=models.CASCADE)
