from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NonprofitViewSet, SendBulkEmailView, EmailLogListView

router = DefaultRouter()
router.register(r'nonprofits', NonprofitViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('send-bulk-email/', SendBulkEmailView.as_view(), name='send-bulk-email'),
    path('emails/', EmailLogListView.as_view(), name='email-logs'),
] 