from rest_framework import serializers
from .models import Nonprofit, EmailLog

class NonprofitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nonprofit
        fields = ['id', 'name', 'address', 'email']

class EmailLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailLog
        fields = ['id', 'recipient', 'subject', 'body', 'sent_at']

class BulkEmailSerializer(serializers.Serializer):
    nonprofit_emails = serializers.ListField(child=serializers.EmailField())
    template_body = serializers.CharField() 