from datetime import datetime

from django.http import Http404

date_format = '%Y-%m-%d'

def parsed_date(day: str) -> datetime.date:
    return datetime.strptime(day, date_format).date()

def get_or_404(model, **kwargs):
    """
    Get an object from the queryset or raise a 404 error if not found.
    """
    try:
        return model.objects.get(**kwargs)
    except model.DoesNotExist:
        raise Http404(f"{model.__name__} not found. by {kwargs}")

