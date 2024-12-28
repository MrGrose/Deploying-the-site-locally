from datacenter.models import Passcard, Visit
from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from datacenter.retrieve_and_format_duration import format_duration, is_visit_long


def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard, passcode=passcode)
    filter_visits = Visit.objects.filter(passcard=passcard)
    
    this_passcard_visits = [process_visit(visit) for visit in filter_visits]
    
    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    
    return render(request, 'passcard_info.html', context)


def get_visit_duration(visit):
    utc_now = timezone.now()
    leaved_at = visit.leaved_at if visit.leaved_at else utc_now
    delta_enter = leaved_at - visit.entered_at
    return delta_enter


def process_visit(visit):
    duration = get_visit_duration(visit)
    total_seconds = int(duration.total_seconds())
    return {
        'entered_at': visit.entered_at.strftime("%d-%m-%Y %H:%M"),
        'duration': format_duration(duration),
        'is_strange': is_visit_long(total_seconds),
    }
