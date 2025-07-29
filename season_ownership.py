# -*- coding: utf-8 -*-
import addpath
from simple_settings import settings

from common_modules.json_rw import json_read
from common_modules.csv_w import write_csv
from common_modules.txt_r import read_txt
from common_modules.headline import print_headline
from common_modules.my_remove import remove_file

import sys

from functions.position import formatPosition
from functions.name import formatPlayerName
from functions.team import get_realTeam
from functions.points import formatData
from functions.players import write_playersToFile, get_playerData


__author__ = 'Vadim Arsenev'
__version__ = '1.0.0'
__data__ = '16.09.2021'


ORDER = list(map(lambda x: x.split(':')[0].strip(), \
    read_txt(settings.COLUMNS_OWN).split('\n')))


def get_playerInfo(playerInfo, gameweek):
    realMatchId, gwPrice, realTeamId, gwPoints, minutesPlayed, realTeamId_rival, \
        teamNameRival, abbrRival, fieldTeam = [''] * 9
    # realMatchId, realTeamId
    try:
        for match in playerInfo['realMatches']:
            if match['gameweek'] == gameweek:
                realMatchId = match['id']
                break
    except TypeError:
        pass

    if realMatchId == '':
        return gwPrice, gwPoints, minutesPlayed, teamNameRival, abbrRival, fieldTeam

    # gwPrice
    try:
        for item in playerInfo['matchPrices']:
            if item['realMatchId'] == realMatchId:
                gwPrice = item['price']
                realTeamId = item['realTeamId']
                break
    except TypeError:
        pass

    # gwPoints, minutesPlayed
    if playerInfo['realPlayerMatchStats'] is None:
        return gwPrice, gwPoints, minutesPlayed, teamNameRival, abbrRival, fieldTeam

    for item in playerInfo['realPlayerMatchStats']:
        try:
            if item['realMatchId'] == realMatchId:
                gwPoints = item['totalPoints']
                minutesPlayed = item['minutesPlayed']
                break
        except KeyError:
            continue

    # fieldTeam, realTeamId_rival
    for item in playerInfo['realMatches']:
        if item['id'] == realMatchId:
            if item['realTeamIds'][0] == realTeamId:
                fieldTeam = 'H'
                realTeamId_rival = item['realTeamIds'][1]
            else:
                fieldTeam = 'A'
                realTeamId_rival = item['realTeamIds'][0]
            break

    teamNameRival, abbrRival = get_realTeam(playerInfo['realTeams'], realTeamId_rival)

    return gwPrice, gwPoints, minutesPlayed, teamNameRival, abbrRival, fieldTeam


def get_ownership(playerInfo):
    try:
        selectedRatio = playerInfo['tournamentPlayerStats']['selectedRatio']
        captainedRatio = playerInfo['tournamentPlayerStats']['captainedRatio']
    except TypeError:
        selectedRatio, captainedRatio = [''] * 2
    return selectedRatio, captainedRatio


def realPlayers(players, gameweek, skipNonPlaying, numTourn, enableNumTourn):
    kindOfSport = players['seasons'][-1]['league']['sport']
    season_id = players['seasons'][-1]['id']
    print_headline(settings.RESULT_FILE_OWN[0], settings.COLUMNS_OWN, ORDER)
    for player in players['playerSeasons']:
        # skipping non-participating players
        if player['playerStatus'] == -1:
            continue
        try:
            seasonPrice = player['seasonPrice']['price']
        except KeyError:
            continue
        # ***** Main query *****
        realPlayerId = player['realPlayer']['id']
        firstName, lastName, customName = formatPlayerName(player['realPlayer'])
        totalPoints = player['totalPoints']
        position = formatPosition(player['position'])
        realTeamId = player['seasonPrice']['realTeamId']
        teamName, abbr = get_realTeam(players['realTeams'], realTeamId)

        print(firstName, lastName)
        playerInfo = get_playerData(realPlayerId, season_id, gameweek, numTourn)
        gwPrice, gwPoints, minutesPlayed, teamNameRival, abbrRival, fieldTeam = \
            get_playerInfo(playerInfo, gameweek)

        # if gwPrice == '':
        #     continue

        # skipping non-playing players
        if minutesPlayed == 0 or minutesPlayed == '':
            if skipNonPlaying:
                continue
            else:
                minutesPlayed = ''

        if enableNumTourn:
            selectedRatio, captainedRatio = get_ownership(playerInfo)
        else:
            selectedRatio, captainedRatio = [''] * 2

        # Gameweek data dictionary. Data generation and writing to file
        data_gameweek = {
            'realPlayerId': realPlayerId,
            'firstName': firstName,
            'lastName': lastName,
            'teamName': teamName,
            'abbr': abbr,
            # 'teamNameRival': teamNameRival,
            'abbrRival': abbrRival,
            'position': position,
            'gwPoints': gwPoints,
            'gameweek': gameweek,
            'gwPrice': gwPrice,
            'fieldTeam': fieldTeam,
            'selectedRatio': selectedRatio,
            'captainedRatio': captainedRatio,
            'seasonPrice': seasonPrice,
            'totalPoints': totalPoints,
            'minutesPlayed': minutesPlayed,
        }

        data_gameweek = formatData(kindOfSport, data_gameweek)

        write_csv(''.join(settings.RESULT_FILE_OWN), data_gameweek, ORDER)


def main(gameweek=1, numTourn=1000000, skipNonPlaying=False, enableNumTourn=True):
    actual_players = json_read(settings.PLAYERS_FILE)
    realPlayers(actual_players, gameweek, skipNonPlaying, numTourn, enableNumTourn)


if __name__ == '__main__':
    remove_file(settings.RESULT_FILE_OWN[0])
    write_playersToFile(settings.SEASON_ID)
    main(sys.argv[1], settings.NUMBER_TOURN)
