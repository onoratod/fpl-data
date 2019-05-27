# -*- coding: utf-8 -*-
"""
Created on Sun May 26 17:37:19 2019

@author: First Build
"""


import fpl, os, copy
import pandas as pd
import numpy as np
from utilities import team_converter, position_converter

gitpath = "A:\\Github\\fpl-data\\data\\2018_2019"

data_shell = {
            'team_h_score' : [],
            'team_a_score' : [],
            'was_home' : [],
            'opponent_team' : []
        }

def get_team_data(team):
    
    data=copy.deepcopy(data_shell)
    
    # Get fixtures from team's player
    team.get_players()
    fixtures = team.players[0].history
    
    # Get fixture data
    for fixt in fixtures:
        for k,v in data.items():
            data[k].append(fixt[k])
    
    # Get opponent names
    data['opponent_team'] = [team_converter(opp) for opp in data['opponent_team']]
    
    # Make dataframe
    data_df = pd.DataFrame.from_dict(data)
    
    # Team/opponent score
    data_df['team_score']=0
    data_df['opponent_score']=0
    
    data_df.loc[data_df['was_home'] == True, 'team_score'] = data_df.loc[data_df['was_home'] == True, 'team_h_score']
    data_df.loc[data_df['was_home'] == False, 'team_score'] = data_df.loc[data_df['was_home'] == False, 'team_a_score']
    
    data_df.loc[data_df['was_home'] == True, 'opponent_score'] = data_df.loc[data_df['was_home'] == True, 'team_a_score']
    data_df.loc[data_df['was_home'] == False, 'opponent_score'] = data_df.loc[data_df['was_home'] == False, 'team_h_score']
    
    data_df.drop(['team_h_score', 'team_a_score'], axis=1, inplace=True)

    # Make index gameweek
    data_df.index += 1
    
    return data_df



# Loop over teams, harvest data
teams = fpl.FPL().get_teams()

for team in teams:
    team_data = get_team_data(team)
    team_name = team.name
    
    print("Harvesting... " + team_name)
        
    # Check whether team directory exists
    team_path = os.path.join(gitpath, "Team", team_name)
    if not os.path.exists(team_path):
        os.makedirs(team_path)
        
    team_data.to_csv(os.path.join(team_path,"data.csv"))
