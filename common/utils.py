from datetime import datetime

date_format = '%Y-%m-%d'

def parsed_date(day: str) -> datetime.date:
    return datetime.strptime(day, date_format).date()

