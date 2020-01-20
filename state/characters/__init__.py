"""
Персонаж:
- у персонажа есть общие характеристики: Сила, Ловкость, Живучесть, Мудрость, Сила воли, Интеллект
- у персонажа есть ресурсные характеристики: Здоровье, Выносливость, Мана
- ресурсные характеристики расходуются на совершение действий
- общие характеристики влияют на ресурсные характеристики и на различные действия персонажа

- применяя навык, развивает его
- развивая навык, персонаж получает уровень навыка
- уровень навыка влияет на эффективность его применения
- все навыки при повышении своего уровня влияют на прогресс развития одной или нескольких общих характеристик
- накапливая достаточный уровень навыка, песонаж повышает общую характеристику

- у персонажа нет уровня.
- фактическая сила персонажа определяется его навыками и экипировкой.

"""

from state.characters.base import Character

__all__ = ['PlayableCharacterState', 'NonPlayableCharacter']


class PlayableCharacterState(Character):
    DEFAULT_NAME = 'Player'


class NonPlayableCharacter(Character):
    pass


if __name__ == "__main__":
    from pprint import PrettyPrinter

    pp = PrettyPrinter(indent=4)

    name = "Tuenut"
    character = PlayableCharacterState()
    character.name = name

    print("Your rpg is %s" % character.name)

    print("Your rpg stats:")
    pp.pprint({
        "strength": character.atributes.strength.points,
        "agility": character.atributes.agility.points,
        "vitality": character.atributes.vitality.points,
        "wisdom": character.atributes.wisdom.points,
        "willpower": character.atributes.willpower.points,
        "intellect": character.atributes.intellect.points,
    })

    pp.pprint({
        'HP': "%s/%s" % (character.atributes.health.current, character.atributes.health.total_points),
        'SP': "%s/%s" % (character.atributes.stamina.current, character.atributes.stamina.total_points),
        'MP': "%s/%s" % (character.atributes.mana.current, character.atributes.mana.total_points)
    })
