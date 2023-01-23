from django.db import models
from django.apps import apps


class TransactionManager(models.Manager):
    def get_total_related_credits(self, debt_id, **kwargs):
        payment_credit_model = apps.get_model("payments_api", "PaymentCredit")
        related_credits = payment_credit_model.objects.filter(debt_id=debt_id)

        return sum((i.paid_amount for i in related_credits))

    def set_debt_status(self, debt_id, **kwargs):
        payment_debt_model = apps.get_model("payments_api", "PaymentDebt")

        related_debt = payment_debt_model.objects.get(pk=debt_id)

        related_debt.status = "payed"
        related_debt.save()

        return related_debt
