# -*- coding: utf-8 -*-
"""
Getting player information from the Fanteam database
"""
from simple_settings import settings
from common_modules.parser import Parser
from common_modules.json_rw import json_write


__author__ = 'Vadim Arsenev'
__version__ = '1.0.0'
__data__ = '02.08.2021'


def get_playersTournament(tournamet_id):
    url = f'{settings.API_URL}/tournaments/{tournamet_id}/players?'
    requests_players = Parser(url, settings.REQUESTS_ARGS)
    players = requests_players.parser_result()
    return players


def get_players(season_id):
    url = f'{settings.API_URL}/seasons/{season_id}/players'
    requests_players = Parser(url, settings.REQUESTS_ARGS)
    players = requests_players.parser_result()
    return players


def get_playerData(realPlayerId, season_id, gameweek, numTourn=None):
    if numTourn:
        url = f'{settings.API_URL}/real_players/{realPlayerId}?season_id={season_id}&' + \
            f'round={gameweek}&tournament_id={numTourn}'
    else:
        url = f'{settings.API_URL}/real_players/{realPlayerId}?season_id={season_id}'
    requests_playerInfo = Parser(url, settings.REQUESTS_ARGS)
    playerInfo = requests_playerInfo.parser_result()
    return playerInfo


def write_playersToFile(season_id='387'):
    players = get_players(season_id)
    json_write(settings.PLAYERS_FILE, players)
