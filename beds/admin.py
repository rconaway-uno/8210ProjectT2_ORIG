from django.contrib import admin

from .models import Bed
from events.models import Organization, Event

# Register your models here.
class BedList(admin.ModelAdmin):
    list_display=('event', 'org', 'org_name', 'bed_type', 'initial_num', 'num_used', 'num_available')
    list_filter=('event', 'org_name', 'bed_type')
    ordering=['bed_type', 'num_available', 'org_name' ]

admin.site.register(Bed)