from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.utils.translation import gettext as _
from players.models import Player, RankingLog
from lavava.settings.email import EMAIL_HOST_USER


@receiver(post_save, sender=Player)
def save_player_ranking_log(sender, instance, created, **kwargs):
    if created:
        RankingLog.objects.create(player=instance)

        try:
            send_mail(
                _("New user registered!"),
                _("%(username)s has registered on the site")
                % {"username": instance.username},
                None,
                recipient_list=[EMAIL_HOST_USER],
                fail_silently=False,
            )
        except Exception as e:
            print(e)
