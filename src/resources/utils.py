# -*- coding: utf-8 -*-
'''
Project : Reprocesser
Package: resources
Module: utils
Author: BoxBoxJason
Date: 23/11/2023
'''

START_SKILL = 1500
START_DEVIATION = 350
def createPlayerMMR(players_table,player_slug):
    """
    @brief Creates a new player dict in the players table

    @param (dict) players_table : Database players table
    @param (str) player_slug : Source player slug (id)
    """
    players_table[player_slug] = {
        'ID':player_slug,
        'SKILL':START_SKILL,
        'SKILL_DEVIATION':START_DEVIATION,
        'PERF_HISTORY':[START_SKILL],
        'PERF_WEIGHT':[1/START_DEVIATION],
        'GAMES':[]
    }


def orderGamesTable(games_table):
    """
    @brief Orders the games table by dates and returns them

    @param (dict) games_table : Database games table

    @return (dict[]) games list ordered by date
    """
    games_table_list = []
    for game_dict in games_table.values():
        games_table_list.append(game_dict)

    games_table_list.sort(key = lambda x : x['DATE'])
    for i,game_dict in enumerate(games_table_list):
        games_table_list[i] = game_dict['ID']

    return games_table_list
