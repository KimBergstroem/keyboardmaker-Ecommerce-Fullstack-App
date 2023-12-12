from django.db import models
from django.utils import timezone


class contact_form(models.Model):
    """
    Model for contact form
    """
    CONTACT_CHOICES = [
        ('order', 'Order Tracking'),
        ('order', 'Order Issue'),
        ('general', 'General Query'),
        ('complaint', 'Complaint'),
        ('return', 'Return Request'),
    ]
    reason = models.CharField(max_length=15, choices=CONTACT_CHOICES)
    email = models.EmailField()
    subject = models.CharField(max_length=150)
    message = models.TextField(max_length=700)
    submission_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Contact Form"


class SubscribedUsers(models.Model):
    """
    Model for storing subscribed users information
    """
    email = models.EmailField(unique=True, max_length=100)
    created_date = models.DateTimeField('Date created', default=timezone.now)

    def __str__(self):
        return self.email
