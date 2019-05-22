# -*- coding: utf-8 -*-
"""
Created on Tue May 21 19:42:08 2019

@author: First Build
"""

import fpl, os
import pandas as pd
from utilities import team_converter, position_converter

gitpath = "A:\\Github\\fpl-data\\data\\2018_2019"

def get_player_meta(player):
    # initialiaze meta dictionary
    meta = {}
    src = player._additional
    
    # store data
    meta["player_id"] = src["id"]
    meta["web_name"] = src["web_name"]
    meta["team"] = team_converter(src["team"])
    meta["first_name"] = src["first_name"]
    meta["second_name"] = src["second_name"]
    meta["cost_end"] = src["now_cost"]/10
    meta["value_form"] = src["value_form"]
    meta["value_season"] = src["value_season"]
    meta["cost_change_start"] = src["cost_change_start"]
    meta["cost_start"] = meta["cost_end"]-meta["cost_change_start"]
    meta["dreamteam_count"] = src["dreamteam_count"]
    meta["selected_by_percent"] = src["selected_by_percent"]
    meta["total_points"] = src["total_points"]
    meta["ppg"] = src["points_per_game"]
    meta["minutes"] = src["minutes"]
    meta["goals_scored"] = src["goals_scored"]
    meta["assists"] = src["assists"]
    meta["clean_sheets"] = src["clean_sheets"]
    meta["goals_conceded"] = src["goals_conceded"]
    meta["own_goals"] = src["own_goals"]
    meta["penalties_saved"] = src["penalties_saved"]
    meta["penalties_missed"] = src["penalties_missed"]            
    meta["yellow_cards"] = src["yellow_cards"]
    meta["red_cards"] = src["red_cards"]
    meta["saves"] = src["saves"]
    meta["bonus"] = src["bonus"]
    meta["bps"] = src["bps"]
    meta["influence"] = src["influence"]
    meta["creativity"] = src["creativity"]
    meta["threat"] = src["threat"]
    meta["ict_index"] = src["ict_index"]
    meta["ea_index"] = src["ea_index"]
    meta["position"] = position_converter(src["element_type"])
    
    # store in list
    for key,entry in meta.items():
        meta[key] = [entry]
    
    df = pd.DataFrame.from_dict(meta, orient='index')
    df.columns=['value']
    df.index.name="entry"
    return(df)

# Loop over players, harvest meta data
players = fpl.FPL().get_players(player_ids=[20, 300])

for ply in players:
    meta_df = get_player_meta(ply)
    ply_name = meta_df.query("entry=='web_name'").iloc[0]["value"]
    
    # Check whether player directory exists
    player_path = os.path.join(gitpath, "Player", ply_name)
    if not os.path.exists(player_path):
        os.makedirs(player_path)
        
    meta_df.to_csv(os.path.join(player_path,"meta.csv"))
    
    


