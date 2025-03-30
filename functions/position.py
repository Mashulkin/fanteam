# -*- coding: utf-8 -*-
"""
Real player position formatting on Fanteam 
"""


__author__ = 'Vadim Arsenev'
__version__ = '1.0.0'
__data__ = '02.08.2021'


def formatPosition(positionName):
    positionName = positionName.split('_')
    try:
        position = positionName[1][0].upper() + positionName[0][0].upper()
    except IndexError:
        position = positionName[0][0].upper()

    # for football and hockey
    position = 'GK' if position == 'G' else position

    # for baseball
    position = 'OF' if position == 'O' else position
    position = '1B' if position == 'BF' else position
    position = '2B' if position == 'BS' else position
    position = '3B' if position == 'BT' else position

    return position
