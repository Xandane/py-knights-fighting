from app.battle_generation.battle import Battle


def battle(config: dict) -> dict:
    lancelot = config["lancelot"]
    mordred = config["mordred"]
    arthur = config["arthur"]
    red_knight = config["red_knight"]
    result1 = Battle().generate_battle(lancelot, mordred)
    result2 = Battle().generate_battle(arthur, red_knight)
    battles = [
        (lancelot, result1),
        (mordred, result1),
        (arthur, result2),
        (red_knight, result2),
    ]
    final = {}
    for knight_cfg, res in battles:
        name = knight_cfg["name"]
        hp = res.get(name, res.get(name.title()))
        raw_hp = res.get(name, res.get(name.title(), 0))
        hp = max(0, raw_hp)
        final[name] = hp

    return final
