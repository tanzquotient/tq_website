from django.contrib import admin

from events.models import *

from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

def copy_event(modeladmin, request, queryset):
    for event in queryset:
        event.name = event.name + " (Copy)"
        event.date = event.date + datetime.timedelta(days=7)
        event.id = None
        event.save()
copy_event.short_description = "Create copy of selected events"