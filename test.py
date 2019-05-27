# -*- coding: utf-8 -*-
"""
Created on Sun May 26 17:07:00 2019

@author: First Build
"""

import fpl, os, copy
import pandas as pd
import numpy as np
from utilities import team_converter, position_converter

gitpath = "A:\\Github\\fpl-data\\data\\2018_2019"



class Player(object):
    """
    A class representing a player in the Fantasy Premier League.
    """
    def __init__(self, name):
        self.name=name
        self.meta=pd.read_csv(os.path.join(gitpath, "Player", self.name, "meta.csv"))
        self.data=pd.read_csv(os.path.join(gitpath, "Player", self.name, "data.csv"))
        
        self.params = {
            'start' : None,
            'score' : None,
            'assist' : None
        }
        
    def init_params(self):
        # Probability of starting a game (Bernoulli)
        minutes = self.data['minutes']
        started = [min>60 for min in minutes]
        
        self.params['start'] = np.mean(started)
        
        # Probability of scoring given you were playing (Bernoulli)
        goals = self.data.loc[self.data['minutes']>10]['goals_scored']
        scored = [goal>0 for goal in goals]
                
        self.params['score'] = np.mean(scored)
        
        # Probability of assist, given you were playing (Bernoulli)
        assists = self.data.loc[self.data['minutes']>10]

test = Player('Hazard')    
test.init_params()