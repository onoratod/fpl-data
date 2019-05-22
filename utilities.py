# -*- coding: utf-8 -*-
"""
Created on Tue May 21 19:52:48 2019

@author: First Build
"""

def team_converter(team_id):
    """
    Converts a team's ID to their actual name.
    """
    if team_id == 1:
        return "Arsenal"
    elif team_id == 2:
        return "Bournemouth"
    elif team_id == 3:
        return "Brighton"
    elif team_id == 4:
        return "Burnley"
    elif team_id == 5:
        return "Cardiff"
    elif team_id == 6:
        return "Chelsea"
    elif team_id == 7:
        return "Crystal Palace"
    elif team_id == 8:
        return "Everton"
    elif team_id == 9:
        return "Fulham"
    elif team_id == 10:
        return "Huddersfield"
    elif team_id == 11:
        return "Leicester"
    elif team_id == 12:
        return "Liverpool"
    elif team_id == 13:
        return "Man City"
    elif team_id == 14:
        return "Man Utd"
    elif team_id == 15:
        return "Newcastle"
    elif team_id == 16:
        return "Southampton"
    elif team_id == 17:
        return "Spurs"
    elif team_id == 18:
        return "Watford"
    elif team_id == 19:
        return "West Ham"
    return "Wolves"

def position_converter(position):
    """
    Converts a player's `element_type` to their actual position.
    """
    if position == 1:
        return "Goalkeeper"
    elif position == 2:
        return "Defender"
    elif position == 3:
        return "Midfielder"
    else:
        return "Forward"

