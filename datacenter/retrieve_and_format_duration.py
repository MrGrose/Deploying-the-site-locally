from django.utils import timezone


def get_duration(visits):
    utc_now = timezone.now()
    moscow_time = timezone.localtime(utc_now)
    for visit in visits:
        if visit.leaved_at is None:
            delta_enter = moscow_time-visit.entered_at
    return delta_enter


def format_duration(duration):
    total_seconds = int(duration.total_seconds())
    hours, remainder = divmod(total_seconds, 3600)
    minutes, _ = divmod(remainder, 60)
    return f'{hours:02}ч {minutes:02}мин'
