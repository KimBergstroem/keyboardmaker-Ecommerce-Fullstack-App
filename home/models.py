from django.db import models

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
