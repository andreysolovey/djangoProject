from django.db.models import *
from django.contrib.auth.models import User


class Pay(Model):
    bank_account = CharField(max_length=13, null=False)
    card_number = CharField(max_length=19, null=False)
    validity = CharField(max_length=13, null=False)
    cvc = CharField(max_length=13, null=False)
    amount_to_pay = CharField(max_length=13, null=False)
    date = DateField()
    payment_status = BooleanField(default=True)

