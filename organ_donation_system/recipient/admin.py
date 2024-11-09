
from django.contrib import admin
from recipient.models import recipients

admin.site.register(recipients)
class RecipientAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'contact_number', 'date_of_birth', 'gender', 'blood_group', 'organ_needed', 'address']
