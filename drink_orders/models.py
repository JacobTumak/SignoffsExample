from django.db import models
from signoffs.models import Signet
from signoffs.signoffs import SimpleSignoff
from signoffs.models import SignoffField


DrinkOrderSignoff = SimpleSignoff.register(id='drink_orders.DrinkOrderSignoff')


class DrinkOrderModel(models.Model):
    drink_choice = models.CharField()
    signoff, signet = SignoffField(DrinkOrderSignoff)
