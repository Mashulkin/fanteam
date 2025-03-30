# -*- coding: utf-8 -*-
import addpath
from simple_settings import settings

from common_modules.csv_w import write_csv
from common_modules.txt_r import read_txt
from common_modules.headline import print_headline
from common_modules.my_remove import remove_file

import sys

from functions.fantasy import get_tournament
from functions.fantasy import get_tournInfo, get_fantasyTeam
from functions.points import formatData


__author__ = 'Vadim Arsenev'
__version__ = '1.0.0'
__data__ = '31.10.2021'


ORDER = list(map(lambda x: x.split(':')[0].strip(), \
    read_txt(settings.COLUMNS_BOARD).split('\n')))


def get_addTeamData(teamId, gameweek):
    fantasyTeamData = get_fantasyTeam(teamId, gameweek)
    whiteLabel = fantasyTeamData['fantasyTeam']['user']['whiteLabel']['name']

    return whiteLabel


def get_roundData(teamId, pageData):
    for item in pageData['gameweeks']:
        roundRank, roundScore, totalScoreRound = [''] * 3
        if teamId == int(item['fantasyTeamId']):
            roundRank = item['roundRank']
            roundScore = item['roundScore']
            totalScoreRound = item['totalScore']
            break

    return roundRank, roundScore, totalScoreRound


def fantasyTeamInfo(fantasyTeamData, kindOfSport, gameweek, whiteLabelBase, pageData):
    teamId = fantasyTeamData['id']
    rank = fantasyTeamData['rank']
    fantasyTeamName = fantasyTeamData['name']
    score = fantasyTeamData['score']
    payout = fantasyTeamData['payout']

    roundRank, roundScore, totalScoreRound = get_roundData(teamId, pageData)

    whiteLabelId = fantasyTeamData['user']['whiteLabelId']
    try:
        whiteLabel = whiteLabelBase[whiteLabelId]
    except KeyError:
        whiteLabelName = get_addTeamData(teamId, gameweek)
        whiteLabelBase.update({whiteLabelId: whiteLabelName})
        whiteLabel = whiteLabelBase[whiteLabelId]

    data = {
        'rank': rank,
        'fantasyTeamName': fantasyTeamName,
        'score': score,
        'payout': payout,
        'whiteLabel': whiteLabel,
        'roundRank': roundRank,
        'roundScore': roundScore,
        'totalScoreRound': totalScoreRound,
        'gameweek': gameweek,
        'teamId': teamId,
    }
    data = formatData(kindOfSport, data)

    write_csv(''.join(settings.RESULT_FILE_BOARD), data, ORDER)

    return whiteLabelBase


def tournInfo(data, gameweek):
    kindOfSport = data['seasons'][-1]['league']['sport']
    totalFantasyTeams = data['tournament']['fantasyTeamsCount']
    print_headline(settings.RESULT_FILE_BOARD[0], settings.COLUMNS_BOARD, ORDER)

    whiteLabelBase = {}
    if totalFantasyTeams % 20 == 0:
        pages = totalFantasyTeams // 20
    else:
        pages = totalFantasyTeams // 20 + 1

    for page in range(0, pages):
        if __name__ == '__main__':
            print(page, end=' ')
            sys.stdout.flush()
        pageData = get_tournInfo(gameweek, settings.NUMBER_TOURN, page)
        fantasyTeams = pageData['fantasyTeams']

        for item in fantasyTeams:
            whiteLabelBase = fantasyTeamInfo(
                item, kindOfSport, gameweek, whiteLabelBase, pageData)


def main(numTourn, gameweek):
    tournamentInfo = get_tournament(numTourn)
    tournInfo(tournamentInfo, gameweek)


if __name__ == '__main__':
    remove_file(settings.RESULT_FILE_BOARD[0])
    main(settings.NUMBER_TOURN, sys.argv[1])
