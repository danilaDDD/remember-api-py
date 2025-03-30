from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from infocard.models import InfoCard, InfoCardTag, Remember


@receiver(post_save, sender=InfoCardTag)
def save_info_card_tag(sender, instance: InfoCardTag, **kwargs):
    instance.tag.account = instance.info_card.account
    instance.tag.save()

@receiver(pre_save, sender=InfoCard)
def save_remember(sender, instance: InfoCard, **kwargs):
    instance.update_tags_text()
