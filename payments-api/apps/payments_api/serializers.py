from rest_framework import serializers
from apps.payments_api.models import PaymentCredit, PaymentDebt


class PaymentsFileUploadSerializer(serializers.Serializer):
    file = serializers.FileField()
    origin = serializers.CharField()
    type = serializers.CharField()
    requester = serializers.CharField()

    class Meta:
        fields = ["file", "origin", "type", "requester"]


class PaymentDebtSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentDebt
        fields = "__all__"


class PaymentCreditSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentCredit
        fields = ["debt_id", "paid_at", "paid_amount", "paid_by"]
