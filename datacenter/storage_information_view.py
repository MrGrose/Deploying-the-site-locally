from datacenter.models import Visit
from datacenter.retrieve_and_format_duration import (format_duration,
                                                     get_duration)
from django.shortcuts import render


def storage_information_view(request):
    visits = Visit.objects.filter(leaved_at=None)
    non_closed_visits = []
    for visit in visits:
        duration = get_duration(visit.entered_at)
        formatted_duration = format_duration(duration)
        non_closed_visits.append({
                'who_entered': visit.passcard,
                'entered_at': visit.entered_at.strftime("%d %B %Y %H:%M"),
                'duration': formatted_duration,
            })
    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
