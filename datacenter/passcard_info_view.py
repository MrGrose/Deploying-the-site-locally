from datacenter.models import Passcard, Visit
from datacenter.retrieve_and_format_duration import (format_duration,
                                                     is_visit_long)
from django.shortcuts import get_object_or_404, render
from django.utils import timezone


def passcard_info_view(request, passcode):

    passcard = get_object_or_404(Passcard, passcode=passcode)
    filter_visits = Visit.objects.filter(passcard=passcard)
    utc_now = timezone.now()
    this_passcard_visits = []
    for visit in filter_visits:
        leaved_at = visit.leaved_at if visit.leaved_at else utc_now
        delta_enter = leaved_at - visit.entered_at
        total_seconds = int(delta_enter.total_seconds())
        long_visit = is_visit_long(total_seconds)
        formatted_duration = format_duration(delta_enter)
        this_passcard_visits.append({
            'entered_at': visit.entered_at.strftime("%d-%m-%Y %H:%M"),
            'duration': formatted_duration,
            'is_strange': long_visit,
        })
    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
