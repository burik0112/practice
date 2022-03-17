from django.contrib import admin

from pages.models import ContactModel


@admin.register(ContactModel)
class ContactModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'messages', 'created_at']
    list_filter = ['name']
    search_fields = ['name', 'email']

