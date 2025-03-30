# -*- coding: utf-8 -*-
import addpath
from simple_settings import settings

from common_modules.csv_w import write_csv
from common_modules.txt_r import read_txt
from common_modules.headline import print_headline
from common_modules.my_remove import remove_file

from functions.players import get_playersTournament
from functions.position import formatPosition
from functions.name import formatPlayerName
from functions.team import get_realTeam


__author__ = 'Vadim Arsenev'
__version__ = '1.0.0'
__data__ = '13.10.2021'


ORDER = list(map(lambda x: x.split(':')[0].strip(), \
    read_txt(settings.COLUMNS).split('\n')))


def realPlayers(players):
    """
    The main module for performing all operations of a request
       and writing to a file
    """
    print_headline(settings.RESULT_FILE[0], settings.COLUMNS, ORDER)
    for player in players['playerChoices']:
        # ***** Main query *****
        realPlayerId = player['realPlayer']['id']
        firstName, lastName, customName = \
            formatPlayerName(player['realPlayer'])
        position = formatPosition(player['position'])
        realTeamId = player['realTeamId']
        teamName, abbr = get_realTeam(players['realTeams'], realTeamId)
        lineup = player['lineup']
        gwPrice = player['price']
        form = player['form']
        currentGW = player['gameweek']
        bonus = '' # fake

        # Gameweek data dictionary. Data generation and writing to file
        data_gameweek = {
            'firstName': firstName,
            'lastName': lastName,
            'customName': customName,
            'teamName': teamName,
            'abbr': abbr,
            'position': position,
            'lineup': lineup,
            'gwPrice': gwPrice,
            'bonus': bonus,
            'realPlayerId': realPlayerId,
            'form': form,
            'currentGW': currentGW,
        }

        write_csv(settings.RESULT_FILE[0], \
            data_gameweek, ORDER)


def main(numTourn=None):
    """
    Request information about the players. General request
    """
    actual_players = get_playersTournament(numTourn)
    realPlayers(actual_players)

if __name__ == '__main__':
    remove_file(settings.RESULT_FILE[0])
    main(settings.NUMBER_TOURN)
