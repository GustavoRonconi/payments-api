from urllib.parse import urlparse

from rest_framework import serializers
from payments_api.clients import s3_client
from payments_api.settings import PRE_SIGNED_URL_TTL_IN_SECONDS


class PaymentsFileUploadSerializer(serializers.Serializer):
    file = serializers.FileField()
    origin = serializers.CharField()
    type = serializers.CharField()
    requester = serializers.CharField()

    class Meta:
        fields = ["file", "origin", "type", "requester"]


class PreSignedUrlField(serializers.URLField):
    def extract_name_and_object_key(self, url):
        parsed_url = urlparse(url)
        bucket = parsed_url.netloc

        if "s3.amazonaws.com" not in bucket:
            raise serializers.ValidationError("Invalid S3 URL")

        bucket = bucket.split("s3")[0]
        if bucket:
            bucket = bucket[:-1]
        object_key = parsed_url.path.lstrip("/")
        return bucket, object_key

    def to_representation(self, value):
        bucket_name, object_key = self.extract_name_and_object_key(value)
        if not bucket_name or not object_key:
            return super().to_representation(value)

        bucket = s3_client.bucket(bucket_name)
        return bucket.files.pre_sign_url_from_file(
            object_key, expires_in=PRE_SIGNED_URL_TTL_IN_SECONDS
        )
