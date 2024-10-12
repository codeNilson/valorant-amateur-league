from django.db.models.signals import post_save
from django.dispatch import receiver
from players.models import Player, RankingLog


@receiver(post_save, sender=Player)
def save_player_ranking_log(sender, instance, created, **kwargs):
    if created:
        RankingLog.objects.create(player=instance)
