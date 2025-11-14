import datetime
import keyboard
import cv2
import pyautogui
import time
import signal
import sys
import numpy as np
import re
import json
from ahk import AHK
from enum import Enum
import os
from os.path import exists
import math
import copy
import random
from functools import reduce

def canUserUsePlaythrough(playthrough):
    map_name = playthrough["fileConfig"]["map"]
    gamemode = playthrough["fileConfig"]["gamemode"]

    if (
        "unlocked_maps" in userConfig
        and map_name in userConfig["unlocked_maps"]
        and userConfig["unlocked_maps"][map_name] == False
    ):
        return False

    if (
        "unlocked_difficulties" in userConfig
        and not userConfig["unlocked_difficulties"][playthrough["fileConfig"]["gamemode"]]
    ):
        return False

    if "unlocked_towers" in userConfig:
        pass

    prereq_map = {
        'primary_only': 'easy',
        'deflation': 'primary_only',
        'military_only': 'medium',
        'reverse': 'medium',
        'apopalypse': 'military_only',
        'magic_monkeys_only': 'hard',
        'double_hp_moabs': 'magic_monkeys_only',
        'half_cash': 'double_hp_moabs',
        'alternate_bloons_rounds': 'hard',
        'impoppable': 'alternate_bloons_rounds',
        'chimps': 'impoppable',
    }

    if gamemode in prereq_map:
        prereq_gamemode = prereq_map[gamemode]
        prereq_earned = userConfig.get("medals", {}).get(map_name, {}).get(prereq_gamemode, False)
        if not prereq_earned:
            return False

    return True

def getMedalStatus(mapname, gamemode):
    return (
        mapname in userConfig["medals"]
        and gamemode in userConfig["medals"][mapname]
        and userConfig["medals"][mapname][gamemode] == True
    )

if exists("userconfig.json"):
    userConfig = json.load(open("userconfig.json"))