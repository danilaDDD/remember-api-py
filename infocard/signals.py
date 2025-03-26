from django.db.models.signals import post_save
from django.dispatch import receiver

from infocard.models import InfoCard, Tag, InfoCardTag


@receiver(post_save, sender=InfoCardTag)
def post_save_info_card(sender, instance: InfoCardTag, **kwargs):
    instance.tag.account = instance.info_card.account
    instance.tag.save()