from django.shortcuts import render, get_object_or_404
from . models import Event
# Create your views here.

def index(request):

    events = Event.objects.all
    context ={
        'events': events
    }
    return render(request, 'wild/index.html', context)

def details(request, event_id):
    events = get_object_or_404(Event, pk=event_id)

    return render(request, 'wild/details.html', {'events':events})


def update_album(request, event_id):
    events = get_object_or_404(Event, pk=event_id)
    events.save()
    return request('wild:index')



def delete_event(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    event.delete()
    return request('wild: index')










