# calendar_app/views.py

from django.http import JsonResponse
from .models import Event
from django.shortcuts import render

def calendar_view(request):
    events = Event.objects.all()
    return render(request, 'calendar_app/calendar.html', {'events': events})

def events_api(request):
    events = Event.objects.all()
    events_data = []
    for event in events:
        events_data.append({
            'title': event.title,
            'start': event.start_time.isoformat(),
            'end': event.end_time.isoformat()
        })
    return JsonResponse(events_data, safe=False)
