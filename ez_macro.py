"""
    Easily and quickly create copy-paste macros.
"""


def print_helper(func):
    """ Decorator for printing macros. """

    def wrapped(*args, **kwargs):
        _arg_str = ', '.join([*args])
        print(f'------- {_arg_str} {func.__name__} -------')
        print('--------------------------------------------\n')
        print(func(*args, **kwargs))
        print('\n--------------------------------------------')

    return wrapped


@print_helper
def hover_over(spell: str,
               stopcast: bool = False,
               dismount: bool = True,
               ) -> str:
    """ Hover over target. """
    macro = f'#showtooltip {spell}\n'
    if stopcast:
        macro += '/stopcast\n'
    if dismount:
        macro += '/dismount\n'
    macro += f'/use [@mouseover, harm, nodead][@target, harm, nodead] {spell}'
    return macro


@print_helper
def heal_harm(heal_spell: str,
              harm_spell: str,
              stopcast: bool = False,
              dismount: bool = True,
              ) -> str:
    """ Heal or harm depending on hover target. """
    macro = f'#showtooltip {heal_spell}\n'
    if stopcast:
        macro += '/stopcast\n'
    if dismount:
        macro += '/dismount\n'
    macro += f'/use [@mouseover,nodead,help] {heal_spell}; '
    macro += f'[@mouseover, harm, nodead][@target, harm, nodead]  {harm_spell}; '
    macro += f'[@target, help, nodead][@player] {heal_spell}'
    return macro


@print_helper
def smart_travel(travel_spell: str,
                 swim_spell: str = None,
                 stopcast: bool = True,
                 ) -> str:
    """ Smart mount or use a travel spell. """
    macro = f'#showtooltip {travel_spell}\n'
    if stopcast:
        macro += '/stopcast\n'
    if swim_spell is not None:
        macro += f'/cast [swimming] {swim_spell}\n'
    macro += f'/cast [indoors] {travel_spell}\n'
    macro += f'/cast [flyable, nocombat] Summon Random Favorite Mount\n'
    macro += f'/cast [combat, outdoors] {travel_spell}\n'
    macro += f'/use [nocombat, outdoors, noswimming, noflyable] Summon Random Favorite Mount\n'
    macro += f'/dismount [mounted]\n'
    return macro


if __name__ == "__main__":

    # # Shaman
    # hover_over('Windshear', stopcast=True)
    # hover_over('Earth Shield')
    # heal_harm('Riptide', 'Flame Shock')
    # heal_harm('Chain Heal', 'Chain Lightning')
    # heal_harm('Healing Burst', 'Lava Burst')
    # heal_harm('Healing Wave', 'Lightning Bolt')
    # smart_travel('Ghost Wolf', swim_spell='Water Walking')
    
    # Rogue
    hover_over('Shuriken Toss', stopcast=True)
    hover_over('Shadowstep', stopcast=True)
    hover_over('Shadowstrike', stopcast=True)
    
