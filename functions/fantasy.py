# -*- coding: utf-8 -*-
"""
Getting tournament information from the Fanteam database
"""
from simple_settings import settings
from common_modules.parser import Parser


__author__ = 'Vadim Arsenev'
__version__ = '1.0.0'
__data__ = '30.10.2021'


def get_tournament(numTourn):
    url = f'{settings.API_URL}/tournaments/{numTourn}'
    requests_tournamentInfo = Parser(url, settings.REQUESTS_ARGS)
    tournamentInfo = requests_tournamentInfo.parser_result()
    return tournamentInfo


def get_tournInfo(gameweek, numTourn, page=0):
    url = f'{settings.API_URL}/tournaments/{numTourn}?requestParentLeaderboard=true&round={gameweek}&page={page}'
    requests_tournamentInfo = Parser(url, settings.REQUESTS_ARGS)
    tournamentInfo = requests_tournamentInfo.parser_result()
    return tournamentInfo


def get_tournInfoUser(gameweek, numTourn, username, page=0):
    url = f'{settings.API_URL}/tournaments/{numTourn}?requestParentLeaderboard=true&round={gameweek}&search={username}&page={page}'
    requests_tournamentInfo = Parser(url, settings.REQUESTS_ARGS)
    tournamentInfo = requests_tournamentInfo.parser_result()
    return tournamentInfo


def get_fantasyTeam(teamId, gameweek):
    url = f'{settings.API_URL}/fantasy_teams/{teamId}?round={gameweek}'
    requests_fantasyTeam = Parser(url, settings.REQUESTS_ARGS)
    fantasyTeam = requests_fantasyTeam.parser_result()
    return fantasyTeam
