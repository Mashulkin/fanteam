# -*- coding: utf-8 -*-
"""
Real player name formatting on Fanteam 
"""


__author__ = 'Vadim Arsenev'
__version__ = '1.0.1'
__data__ = '29.07.2025'


def formatPlayerName(player):
    try:
        firstName = player['firstName'].strip()
    except KeyError:
        firstName = ''
    except AttributeError:
        firstName = ''

    try:
        lastName = player['lastName'].strip()
    except KeyError:
        lastName = ''
    except AttributeError:
        lastName = ''

    try:
        customName = player['customName'].strip()
    except KeyError:
        customName = ''
    except AttributeError:
        customName = ''

    if lastName == '':
        lastName = customName

    return firstName, lastName, customName
