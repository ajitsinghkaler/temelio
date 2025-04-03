from django.shortcuts import render
from rest_framework import viewsets, views, generics
from rest_framework.response import Response
from .models import Nonprofit, EmailLog
from .serializers import NonprofitSerializer, EmailLogSerializer, BulkEmailSerializer
from .tasks import send_and_log_email

# Create your views here.

class NonprofitViewSet(viewsets.ModelViewSet):
    queryset = Nonprofit.objects.all()
    serializer_class = NonprofitSerializer

class SendBulkEmailView(views.APIView):
    def post(self, request):
        serializer = BulkEmailSerializer(data=request.data)
        if serializer.is_valid():
            nonprofit_emails = serializer.validated_data['nonprofit_emails']
            template_body = serializer.validated_data['template_body']
            nonprofits = Nonprofit.objects.filter(email__in=nonprofit_emails)
            for nonprofit in nonprofits:
                email_body = template_body.format(name=nonprofit.name, address=nonprofit.address)
                send_and_log_email(nonprofit.id, email_body)
            return Response({'message': 'Bulk emails scheduled for sending.'})
        return Response(serializer.errors, status=400)

class EmailLogListView(generics.ListAPIView):
    queryset = EmailLog.objects.all()
    serializer_class = EmailLogSerializer
