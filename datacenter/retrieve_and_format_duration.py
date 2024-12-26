from django.utils import timezone
from datetime import timedelta


def get_duration(visits):
    if visits:
        return timezone.localtime()-visits
    return timedelta(0)


def format_duration(duration):
    total_seconds = int(duration.total_seconds())
    hours, remainder = divmod(total_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f'{hours:02}ч {minutes:02}мин {seconds:02}cек'


def is_visit_long(visit, minutes=60):
    return visit > minutes * 60
