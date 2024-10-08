def calc_win_ratio(wins=None, losses=None):
    if wins is not None and losses is not None:
        total = wins + losses
        return round((wins / total) * 100, 2) if total > 0 else 0
    return 0


def calc_kda(kills=None, assists=None, deaths=None):
    if kills is not None and assists is not None:
        if not deaths:
            return round((kills + assists), 2)
        return round((kills + assists) / deaths, 2)
    return 0


def save_position_changes(player: object, index: int) -> str:
    player.last_position_change = (index - player.last_position) * (-1)
    player.last_position = index
    player.save()
