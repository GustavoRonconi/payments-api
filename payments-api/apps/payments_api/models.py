from django.db import models
from apps.payments_api.choices import PaymentDebtStatus
from apps.payments_api.managers import TransactionManager


class PaymentDebt(models.Model):
    serializer = "apps.payments_api.serializers.PaymentDebtSerializer"

    debt_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    government_id = models.BigIntegerField()
    email = models.EmailField()
    debt_amount = models.DecimalField(max_digits=10, decimal_places=2)
    debt_due_date = models.DateField()
    status = models.CharField(
        max_length=32, choices=PaymentDebtStatus.choices, default=PaymentDebtStatus.OPEN
    )


class PaymentCredit(models.Model):
    serializer = "apps.payments_api.serializar.PaymentCreditSerializar"

    credit_id = models.AutoField(primary_key=True)
    debt_id = models.ForeignKey(
        PaymentDebt, related_name="payment_credit", on_delete=models.CASCADE
    )
    paid_at = models.DateTimeField()
    paid_amount = models.DecimalField(max_digits=10, decimal_places=2)
    paid_by = models.CharField(max_length=100)

    objects = TransactionManager()
