
from django.contrib import admin
from .models import TimeSlot

@admin.register(TimeSlot)
class TimeSlotAdmin(admin.ModelAdmin):
    list_display = (
        'day',
        'start_time',
        'end_time',
        'subject',
        'faculty_name',
        'classroom',
    )
    list_filter = ('day', 'subject')
    search_fields = ('subject', 'faculty_name', 'classroom')
