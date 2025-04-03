from background_task import background
from .models import Nonprofit, EmailLog

@background
def send_and_log_email(nonprofit_id, email_body):
    nonprofit = Nonprofit.objects.get(id=nonprofit_id)
    # Simulate sending email
    print(f"Sent email to {nonprofit.email}: {email_body}")
    # Log the email
    EmailLog.objects.create(recipient=nonprofit, subject="Grant Notification", body=email_body) 