from django.contrib import admin
from .models import contact_form


class ContactFormAdmin(admin.ModelAdmin):
    list_display = (
        'email',
        'subject',
        'reason',
        'submission_date',
    )

admin.site.register(contact_form, ContactFormAdmin)
