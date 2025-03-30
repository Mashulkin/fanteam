# -*- coding: utf-8 -*-
"""
Getting team name and abbreviation by ID in database
"""

__author__ = 'Vadim Arsenev'
__version__ = '1.0.0'
__data__ = '30.08.2022'


def fixBug(teamName,abbr):
    abbr = 'AVL' if abbr == 'AV' else abbr
    abbr = 'FUL' if teamName == 'Fulham' else abbr
    abbr = 'LEE' if teamName == 'Leeds' else abbr
    abbr = 'BRE' if teamName == 'Brentford' else abbr
    abbr = 'NOR' if teamName == 'Norwich' else abbr
    abbr = 'ATM' if teamName == 'Atletico Madrid' else abbr
    abbr = 'MCI' if abbr == 'MC' else abbr
    abbr = 'RBL' if teamName == 'Leipzig' else abbr
    abbr = 'SHK' if teamName == 'Shakhtar' else abbr
    abbr = 'RBU' if teamName == 'Salzburg' else abbr
    abbr = 'SHR' if teamName == 'Sheriff' else abbr
    abbr = 'YBO' if teamName == 'Young Boys' else abbr
    abbr = 'BEN' if teamName == 'Benfica' else abbr
    abbr = 'WLF' if teamName == 'Wolfsburg' else abbr
    abbr = 'TOT' if teamName == 'Tottenham' else abbr
    abbr = 'CLC' if teamName == 'Celtic' else abbr
    abbr = 'NAP' if teamName == 'Napoli' else abbr
    abbr = 'LEV' if teamName == 'Bayer Leverkusen' else abbr
    abbr = 'RAN' if teamName == 'Rangers' else abbr
    abbr = 'MAC' if teamName == 'Maccabi Haifa' else abbr
    abbr = 'ZAG' if teamName == 'Dinamo Zagreb' else abbr
    abbr = 'COP' if teamName == 'Copenhagen' else abbr
    abbr = 'VIK' if teamName == 'Viktoria Plzen' else abbr
    abbr = 'FLA' if abbr == 'FLO' else abbr
    abbr = 'NFO' if abbr == 'NTG' else abbr

    return teamName, abbr


def get_realTeam(teamsData, realTeamId):
    teamName, abbr = [''] * 2
    
    if teamsData is None:
        return teamName, abbr

    for team in teamsData:
        if team['id'] == realTeamId:
            teamName = team['name']
            try:
                abbr = team['abbr']
            except KeyError:
                abbr = abbr
            break
    
    teamName, abbr = fixBug(teamName, abbr)

    return teamName, abbr
