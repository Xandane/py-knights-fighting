from app.battle_generation.battle import Battle


def battle(config: dict) -> dict:
    lancelot = config["lancelot"]
    mordred = config["mordred"]
    arthur = config["arthur"]
    red_knight = config["red_knight"]
    result1 = Battle().generate_battle(lancelot, mordred)
    result2 = Battle().generate_battle(arthur, red_knight)
    final = {
        "Lancelot": max(
            0,
            result1.get(
                lancelot["name"],
                result1.get("Lancelot"),
            ),
        ),
        "Mordred": max(
            0,
            result1.get(
                mordred["name"],
                result1.get("Mordred"),
            ),
        ),
        "Arthur": max(
            0,
            result2.get(
                arthur["name"],
                result2.get("Arthur"),
            ),
        ),
        "Red Knight": max(
            0,
            result2.get(
                red_knight["name"],
                result2.get("Red Knight"),
            ),
        ),
    }

    return final
