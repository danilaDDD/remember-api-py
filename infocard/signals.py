from django.db.models.signals import post_save
from django.dispatch import receiver

from infocard.models import InfoCardTag


@receiver(post_save, sender=InfoCardTag)
def save_info_card_tag(sender, instance: InfoCardTag, **kwargs):
    instance.tag.account = instance.info_card.account
    instance.tag.save()
    instance.info_card.update_tags_text()
    instance.info_card.save()