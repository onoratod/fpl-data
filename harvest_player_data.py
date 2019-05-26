# -*- coding: utf-8 -*-
"""
Created on Sun May 26 13:51:05 2019

@author: First Build
"""


import fpl, os, copy
import pandas as pd
import numpy as np
from utilities import team_converter, position_converter

gitpath = "A:\\Github\\fpl-data\\data\\2018_2019"


data_shell = {
                "kickoff_time_formatted" : [],
                "team_h_score" : [],
                "team_a_score" : [],
                "was_home" : [],
                "total_points" : [],
                "value" : [],
                "selected" : [],
                "transfers_in" : [],
                "transfers_out" : [],
                "transfers_balance" : [],
                "minutes" : [],
                "goals_scored" : [],
                "assists" : [],
                "clean_sheets" : [],
                "goals_conceded" : [],
                "own_goals" : [],
                "penalties_saved" : [],
                "yellow_cards" : [],
                "red_cards" : [],
                "saves" : [],
                "bonus" : [],
                "bps" : [],
                "influence" : [],
                "creativity" : [],
                "threat" : [],
                "ict_index" : [],
                "ea_index" : [],
                "open_play_crosses" : [],
                "big_chances_created" : [],
                "clearances_blocks_interceptions" : [],
                "recoveries" : [],
                "key_passes" : [],
                "tackles" : [],
                "winning_goals" : [],
                "attempted_passes" : [],
                "completed_passes" : [],
                "penalties_conceded" : [],
                "big_chances_missed" : [],
                "errors_leading_to_goal" : [],
                "tackled" : [],
                "offside" : [],
                "target_missed" : [],
                "fouls" : [],
                "dribbles" : [],
                "fixture" : [],
                "opponent_team" : []
            }

def get_player_data(player):
    # initialiaze data dictionary
    data = copy.deepcopy(data_shell)
    history = player.history
    
    for gw in range(0, len(history)):
        for key, value in data.items():
            data[key].append(history[gw][key])
    
    # Convert some data
    data["opponent_team"] = [team_converter(opp) for opp in data["opponent_team"]]
    data["value"] = [val/10 for val in data["value"]]
    
    # Balance the data on gameweeks
    data_df = pd.DataFrame.from_dict(data)
    data_df = data_df.append(pd.Series([np.nan]*len(data_df.columns), index=list(data_df.columns)), ignore_index=True)
    data_df.index = data_df.index+1
    
    # Rename some columns
    data_df.rename(index=str, columns= {"kickoff_time_formatted" : "kickoff_time",
                               "team_h_score" : 'home_score',
                               "team_a_score" : 'away_score'})
    
    return data_df



# Loop over players, harvest meta data
players = fpl.FPL().get_players()

for ply in players:
    ply_data = get_player_data(ply)
    ply_name = ply.name
    
    print("Harvesting... " + ply_name)
        
    # Check whether player directory exists
    player_path = os.path.join(gitpath, "Player", ply_name)
    if not os.path.exists(player_path):
        os.makedirs(player_path)
        
    ply_data.to_csv(os.path.join(player_path,"data.csv"))
    