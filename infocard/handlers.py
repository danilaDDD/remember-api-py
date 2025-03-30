from django.db.models import QuerySet
from rest_framework.exceptions import ValidationError
from rest_framework.request import Request

from common.utils import parsed_date
from infocard.models import Remember


class RememberHandler:
    def list(self, request: Request) -> QuerySet:
        params = self.prepare_params(request)

        remembers = Remember.objects.filter(
            info_card__account_id=params['account_id'],)

        remembers_ids = [r.id for r in remembers.filter(date=params['date'])]
        remembers_ids += [r.id for r in remembers.filter(date__lt=params['date']).exclude(status=Remember.STATUS_TRUE)]

        return (Remember.objects
                .filter(id__in=remembers_ids, info_card__closed=False)
                .select_related('info_card').order_by('-date'))

    def prepare_params(self, request: Request) -> dict:
        params = request.GET
        try:
            if params.get('date') is None:
                raise ValueError('Не передана дата')
            result = {'date': parsed_date(params['date']), 'account_id': request.user.id}

            return result

        except ValueError as e:
            raise ValidationError(e)

