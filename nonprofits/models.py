from django.db import models

# Create your models here.

class Nonprofit(models.Model):
    name = models.CharField(max_length=200)
    address = models.TextField()
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name

class EmailLog(models.Model):
    recipient = models.ForeignKey(Nonprofit, on_delete=models.CASCADE)
    subject = models.CharField(max_length=200)
    body = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Email sent to {self.recipient.email} at {self.sent_at}"
