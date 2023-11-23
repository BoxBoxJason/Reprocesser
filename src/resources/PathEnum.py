# -*- coding: utf-8 -*-
'''
Project : Reprocesser
Package: resources
Module:  PathEnum
Usage: Contains project useful paths and path / files related functions

Author: BoxBoxJason
Date: 23/11/2023
'''

import os
from json import load,dump

class PathEnum:
    """
    PathEnum contains absolute paths to project files system
    """
    REPROCESSER = os.getenv('REPROCESSER')

    RESOURCES = os.path.join(REPROCESSER,'src','resources')

    CONFIG = os.path.join(RESOURCES,'config','config.json')

    DATA = os.path.join(REPROCESSER,'data')


def getDataPath(sport,folder_name,file_name):
    """
    Returns requested data resource absolute path

    @param (str) sport : sport folder name
    @param (str) folder_name : subfolder name
    @param (str) file_name : file name

    @return (path) Absolute path to resource
    """
    data_path = os.path.join(PathEnum.DATA,sport,folder_name,file_name)
    os.makedirs(os.path.dirname(data_path),511,True)
    return data_path


def getJsonObject(file_path):
    """
    Returns requested json file content

    @param (path) file_path : Absolute path to file

    @return (iterable) result from reading the json file
    """
    os.makedirs(os.path.dirname(file_path),511,True)
    result = {}
    if os.path.exists(file_path):
        with open(file_path,'r',encoding='utf-8') as json_file:
            result = load(json_file)

    return result


def dumpJsonObject(json_object,file_path):
    """
    Overwrites json object to file_path

    @param (iterable) json_object : JSON object to save in file
    @param (path) file_path : Absolute path to destination file
    """
    os.makedirs(os.path.dirname(file_path),511,True)
    with open(file_path,'w',encoding='utf-8') as json_file:
        dump(json_object,json_file,indent=2)
