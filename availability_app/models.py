from django.db import models
from django.contrib.auth.models import User
from signoffs.models import Signet
from signoffs.signoffs import SimpleSignoff


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class EmployeeAvailability(models.Model):
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE)
    DAYS = {'sun':'Sunday',
            'mon':'Monday',
            'tue':'Tuesday',
            'wed':'Wednesday',
            'thur':'Thursday',
            'fri':'Friday',
            'sat':'Saturday'}
    sunday = models.BooleanField(default=False, name='Sunday')
    monday = models.BooleanField(default=False, name='Monday')
    tuesday = models.BooleanField(default=False, name='Tuesday')
    wednesday = models.BooleanField(default=False, name='Wednesday')
    thursday = models.BooleanField(default=False, name='Thursday')
    friday = models.BooleanField(default=False, name='Friday')
    saturday = models.BooleanField(default=False, name='Saturday')

    def __str__(self):
        return f"{self.employee.user.username}'s Availability"

    def get_availability(self):
        return {field.name: getattr(self, field.name) for field in self.get_day_fields()}

    def get_day(self):
        return getattr(self, self.name)

    def get_day_fields(self):
        return [field for field in self._meta.get_fields() if field.name in self.DAYS.values()]

    def update_days(self, days):
        for field in self.get_day_fields():
            if field.name.lower() in days:
                setattr(self, field.name, True)
            else:
                setattr(self, field.name, False)



availability_signoff = SimpleSignoff.register(id='availability_app.AvailabilitySignoff',
                                              signetModel='EmployeeAvailabilitySignet')

class EmployeeAvailabilitySignet(Signet):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    signoff_id = 'availability_app.AvailabilitySignoff'
