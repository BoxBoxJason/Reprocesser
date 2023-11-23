# -*- coding: utf-8 -*-
'''
Created on 11 oct. 2023

@author: BoxBoxJason
'''
from os.path import join,dirname,realpath
from os import environ
from sys import stdout
import logging
project_path = realpath(dirname(dirname(__file__)))
environ['REPROCESSER'] = project_path
from reprocess.ReprocessTennis import fillMenTennisDataELO,fillMenTennisDataMMR
##----------Logging setup----------##
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler(join(project_path,"logging.log")),
        logging.StreamHandler(stdout)
    ]
)

players_table_MMR = {}
games_table_MMR = {}
players_table_ELO = {}
games_table_ELO = {}

fillMenTennisDataMMR(games_table_MMR,players_table_MMR,'1991-2016')
fillMenTennisDataMMR(games_table_MMR,players_table_MMR,'2017')
fillMenTennisDataELO(games_table_ELO,players_table_ELO,'1991-2016')
fillMenTennisDataELO(games_table_ELO,players_table_ELO,'2017')
