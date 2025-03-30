# -*- coding: utf-8 -*-
"""
Formatting game data
"""

__author__ = 'Vadim Arsenev'
__version__ = '1.0.4'
__data__ = '14.11.2022'


def formatPointsFootball(points):
    try:
        points = '{:.2f}'.format(float(points))
    except TypeError:
        points = ''
    except ValueError:
        points = ''
    
    return points


def formatPointsBasket(points):
    try:
        points = '{:.2f}'.format(float(points))
    except TypeError:
        points = ''
    except ValueError:
        points = ''
    
    return points


def formatPointsHockey(points):
    try:
        points = '{:.2f}'.format(float(points))
    except TypeError:
        points = ''
    except ValueError:
        points = ''
    
    return points


def formatZero(item):
    try:
        item = item if float(item) != 0 else ''
    except ValueError:
        pass

    return item


def formatPursuit(item):
    try:
        item = ''
    except ValueError:
        pass

    return item


def formatRatio(ratio):
    try:
        if float(ratio) != 0:
            ratio = '{:.2f}'.format(float(ratio))
        else:
            ratio = ''
    except ValueError:
        ratio = ''
    
    return ratio


def formatBench(benchPosition):
    benchPosition = benchPosition if benchPosition != 'sub_goalkeeper' else 'subG'

    return benchPosition


def formatData(kindOfSport, data):
    # Formatting Points by type of sport
    sport = kindOfSport.split('_')[0]
    if sport == 'basket':
        try:
            data['score'] = formatPointsBasket(data['score'])
        except KeyError:
            pass

    elif sport == 'hockey':
        try:
            data['score'] = formatPointsHockey(data['score'])
        except KeyError:
            pass

    else:
        try:
            data['totalPoints'] = formatPointsFootball(data['totalPoints'])
        except KeyError:
            pass

        try:
            data['gwPoints'] = formatPointsFootball(data['gwPoints'])
        except KeyError:
            pass

        try:
            data['score'] = formatPointsFootball(data['score'])
        except KeyError:
            pass

        try:
            data['roundScore'] = formatPointsFootball(data['roundScore'])
        except KeyError:
            pass

        try:
            data['totalScoreRound'] = formatPointsFootball(data['totalScoreRound'])
        except KeyError:
            pass

    # selected and captained
    try:
        data['selectedRatio'] = formatRatio(data['selectedRatio'])
    except KeyError:
        pass

    try:
        data['captainedRatio'] = formatRatio(data['captainedRatio'])
    except KeyError:
        pass

    # formating zero data
    try:
        data['minutesPlayed'] = formatZero(data['minutesPlayed'])
    except KeyError:
        pass

    try:
        data['gwGoal'] = formatZero(data['gwGoal'])
    except KeyError:
        pass

    try:
        data['goal'] = formatZero(data['goal'])
    except KeyError:
        pass

    try:
        data['gwAssist'] = formatZero(data['gwAssist'])
    except KeyError:
        pass

    try:
        data['gwCleanSheet'] = formatZero(data['gwCleanSheet'])
    except KeyError:
        pass

    try:
        data['gwImpact'] = formatZero(data['gwImpact'])
    except KeyError:
        pass

    try:
        data['gwKeeperSave'] = formatZero(data['gwKeeperSave'])
    except KeyError:
        pass

    try:
        data['shotOnTarget'] = formatZero(data['shotOnTarget'])
    except KeyError:
        pass

    # Bench position
    try:
        data['benchPosition'] = formatBench(data['benchPosition'])
    except KeyError:
        pass

    # payout
    try:
        data['payout'] = formatZero(data['payout'])
    except KeyError:
        pass
    except TypeError:
        data['payout'] = ''

    # # pursuit
    # if kindOfSport != 'pursuit':
    #     try:
    #         data['bonusPoint'] = formatPursuit(data['bonusPoint'])
    #     except KeyError:
    #         pass

    return data


def formatCaptaincyMain(captaincy, points, playCap):
    if captaincy == 'captain':
        captaincy = 'C'
    elif captaincy == 'vice_captain':
        captaincy = 'VC'
    else:
        captaincy = ''
    
    if playCap:
        if captaincy == 'C':
            try:
                points = float(points) * 2
            except TypeError:
                points = points
                playCap = False
    else:
        if captaincy == 'VC':
            try:
                points = float(points) * 2
            except TypeError:
                points = points
    
    return captaincy, points, playCap


def formatCaptaincy(data, playCap):
    try:
        data['captaincy'], data['points'], playCap = \
            formatCaptaincyMain(data['captaincy'], data['points'], playCap)
    except KeyError:
        pass

    return data, playCap
