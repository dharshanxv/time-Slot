
from django.shortcuts import render
from .models import TimeSlot

def timetable_view(request):
    slots = TimeSlot.objects.all().order_by('day', 'start_time')

    search_query = request.GET.get('search', '')
    selected_day = request.GET.get('day', '')

    if search_query:
        slots = slots.filter(subject__icontains=search_query)

    if selected_day:
        slots = slots.filter(day=selected_day)

    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

    context = {
        'slots': slots,
        'days': days,
        'search_query': search_query,
        'selected_day': selected_day,
    }

    return render(request, 'timetable/timetable.html', context)
