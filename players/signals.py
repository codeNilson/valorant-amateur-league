from django.db.models.signals import post_save
from players.models import Player, RankingLog
from django.dispatch import receiver


@receiver(post_save, sender=Player)
def save_player_ranking_log(sender, instance, created, **kwargs):
    if created:
        RankingLog.objects.create(player=instance)
