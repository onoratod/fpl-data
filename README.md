# fpl-data
Archive of data from FPL API. 

# FPL API 

Here we document the various endpoints of the public FPL API. 

- [Endpoints](#endpoints)
- [Bootstrap Static](#bootstrap-static)
  + [Attributes](#attributes)
    - [`events` - Array](#-events----array)
    - [`game_settings` - JSON Object](#-game-settings----json-object)
    - [`phases` - Array](#-phases----array)
    - [`teams` - Array](#-teams----array)
    - [`total_players` - Integer](#-total-players----integer)
    - [`elements` - Array](#-elements----array)
    - [`element_stats` - Array](#-element-stats----array)
    - [`element_types` - Array](#-element-types----array)
- [Fixtures](#fixtures)
- [Gameweek Fixtures](#gameweek-fixtures)
- [Gameweek Live](#gameweek-live)
- [League Classic](#league-classic)
  + [Attributes](#attributes-1)
    - [`league` - JSON Object](#-league----json-object)
    - [`new_entries` - JSON Object](#-new-entries----json-object)
    - [`standings` - JSON Object](#-standings----json-object)

## Endpoints 

- https://fantasy.premierleague.com/api/bootstrap-static/
- https://fantasy.premierleague.com/api/fixtures/
- https://fantasy.premierleague.com/api/fixtures/?event={event_id}
- https://fantasy.premierleague.com/api/event/{event_id}/live/
- https://fantasy.premierleague.com/api/leagues-classic/{league_id}/standings/
- https://fantasy.premierleague.com/api/element-summary/{element_id}/
- https://fantasy.premierleague.com/api/entry/{entry_id}/
- https://fantasy.premierleague.com/api/entry/{entry_id}/cup/
- https://fantasy.premierleague.com/api/entry/{entry_id}/history/


## Bootstrap Static

This is the main JSON dump for FPL data. The response is a JSON object. Example response:

```javascript
{
  'events' : [...],
  'game_settings' : {...},
  'phases' : [...],
  'teams' : [...],
  'total_players' : 7618904,
  'elements' : [...],
  'element_stats' : [...],
  'element_types' : [...]
}
```

### Attributes

#### `events` - Array

Array of FPL events or gameweeks represented by JSON Objects. Example:

```javascript
{
  'id' : 1, 
  'name' : 'Gameweek 1', 
  'deadline_time' : '2019-08-09T18:00:00Z', 
  'average_entry_score' : 65, 
  'finished' : true, 
  'data_checked' : false, 
  'highest_scoring_entry' : 3493085, 
  'deadline_time_epoch' : 1565373600, 
  'deadline_time_game_offset' : 0, 
  'highest_score' : 142, 
  'is_previous' : false, 
  'is_current' : false, 
  'is_next' : false, 
  'chip_plays' : [
      {'chip_name' : '3xc', 'num_played' : 271367}, 
      {'chip_name' : 'bboost', 'num_played' : 128770}
    ],
  'most_selected' : 183, 
  'most_transferred_in: 1, 
  'top_element' : 214, 
  'top_element_info' : {
      'id' : 214, 
      'points' : 20
    },
  'transfers_made' : 0, 
  'most_captained' : 191, 
  'most_vice_captained' : 189
}
```

#### `game_settings` - JSON Object

Info on FPL game and various rules represented by JSON Object. Example:

```javascript
{
  'league_join_private_max' : 25,
  'league_join_public_max' : 5, 
  'league_max_size_public_classic' : 20, 
  'league_max_size_private_h2h' : 16, 
  'league_max_size_private_h2h2' : 16, 
  'league_max_ko_rounds_private_h2h2' : 3, 
  'league_prefix_publice' : 'League', 
  'league_points_h2h_win : 3, 
  'league_points_h2h_lose' : 0, 
  'league_points_h2h_draw' : 1, 
  'league_ko_first_instead_of_random' : false, 
  'cup_start_event_id' : 17, 
  'cup_stop_event_id' : 38, 
  'cup_qualifying_method' : 'event' ,
  'cup_type' : 'random', 
  'squad_squadplay' : 11, 
  'squad_squadsize' : 15, 
  'squad_team_limit' : 3, 
  'squad_total_spend' : 1000, 
  'ui_currencty_multiplier' : 10, 
  'ui_use_special_shirts' : true, 
  'ui_special_shirt_exclusions' : [], 
  'stats_form_days' : 30, 
  'sys_vice_captain_enabled' : true, 
  'transfers_sell_on_fee' : 0.5, 
  'league_h2h_tiebreak_stats' : [
      '+goals_scored', 
      '-goals_conceded'
    ],
  'timezone' : UTC 
}
```

#### `phases` - Array

Array of JSON Objects with info on gameweek starts and stops for each month. Example:

```javascript
[
  {
    'id' : 1, 
    'name' : 'Overall', 
    'start_event' : 1, 
    'stop_event' : 47
  },
  ...
]
```

#### `teams` - Array

Array of JSON Objects with info on teams. Example: 

```javascript
[
  {
    'code' : 3, 
    'draw' : 0, 
    'form' : null, 
    'id' : 1, 
    'loss' : 0, 
    'name' : 'Arsenal',
    'played' : 0, 
    'points' : 0,
    'position' : 0,
    'short_name' : 'ARS',
    'strength' : 4, 
    'team_division' : null, 
    'unavailable' : false, 
    'win' : 0 ,
    'strength_overall_home' : 1180, 
    'strength_overall_away' : 1240, 
    'strength_attack_home' : 1170, 
    'strength_attack_away' : 1170, 
    'strength_defence_home' : 1150, 
    'strength_defence_away' : 1200, 
    'pulse_id' : 1
  },
  ...
]
```

#### `total_players` - Integer 

Total number of players registered to play FPL. 

#### `elements` - Array

Array of elements (football players) represented by JSON Objects. Example: 

```javascript
[
  {
    'chance_of_playing_next_round' : 100, 
    'chance_of_playing_this_round' : 100, 
    'code' : 225796, 
    'cost_change_event' : 0, 
    'cost_change_event_fall' : 9, 
    'cost_change_start' : -1, 
    'cost_change_start_fall' : 1, 
    'dreamteam_count' : 1, 
    'element_type' : 2, 
    'ep_next' : '1.2', 
    'ep_this' : '0.7', 
    'event_points' : 0, 
    'first_name' : 'Reece', 
    'form' : '1.2',
    'id' : 506, 
    'in_dreamteam' : false, 
    'news' : '', 
    'news_added' : '2020-01-18T19:30:18.538805Z',
    'now_cost' : 49, 
    'photo' : '225796.jpg', 
    'points_per_game' : '2.5',
    'second_name' : 'James', 
    'selected_by_percent' : '0.8', 
    'special' : false, 
    'squad_number' : null, 
    'status' : 'a', 
    'team' : 6, 
    'team_code' : 8, 
    'total_points' : 55, 
    'transfers_in' : 174743, 
    'transfers_in_event' : 329, 
    'transfers_out' : 128339, 
    'transfers_out_event' : 367, 
    'value_form' : '0.2', 
    'value_season' : '11.2', 
    'web_name' : 'James', 
    'minutes' : 1330, 
    'goals_scored' : 0, 
    'assists' : 2, 
    'clean_sheets' : 4, 
    'goals_conceded' : 18, 
    'own_goals' : 0, 
    'penalties_saved' : 0, 
    'penalties_missed' : 0, 
    'yellow_cards' : 1, 
    'red_cards' : 0, 
    'saves' : 0, 
    'bonues' : 5, 
    'bps' : 332, 
    'influence' : '317.6',
    'creativity' : '368.4', 
    'threat' : '134.0', 
    'ict_index' : '82.2', 
    'influence_rank' : 226, 
    'influence_rank_type' : 62, 
    'creativity_rank' : 105, 
    'creativity_rank_type' : 20, 
    'threat_rank' : 242, 
    'threat_rank_type' : 62, 
    'ict_index_rank' : 193, 
    'ict_index_rank_type' : 52
  }, 
  ...
]
```

#### `element_stats` - Array

Array of element (player) statistics types. Example:

```javascript
[
  {
    'label' : 'Minutes played', 
    'name' : 'minutes'
  },
  ...
]
```

#### `element_types` - Array

Array of element (player) type (positions) info. Example:

```javascript
[
  {
    'id' : 1, 
    'plural_name' : 'Goalkeepers', 
    'plural_name_short' : 'GKP',
    'singular_name' : 'Goalkeeper', 
    'singular_name_short' : 'GKP', 
    'squad_select' : 2, 
    'squad_min_play' : 1, 
    'squad_max_play' : 1, 
    'ui_shirt_specific' : true, 
    'sub_positions_locked' : [12],
    'element_count' : 73
  }, 
  ...
]
```

## Fixtures

This endpoint contains information for premier league fixtures for the current season.
The response is an Array of fixtures represented as JSON Objects. Example:

```javascript
[
  {
    'code' : 1059702, 
    'event' : 1, 
    'finished' : true, 
    'finished_provisional' : true, 
    'id' : 1, 
    'kickoff_time' : '2019-08-09T19:00:00Z',
    'minutes' : 90, 
    'provisional_start_time' : false, 
    'started' : true,
    'team_a' : 14, 
    'team_a_score' : 1, 
    'team_h' : 10, 
    'team_h_score' : 4, 
    'stats' : [
        {
          'identifier' : 'goals_scored', 
          'a' : [
              {
                'value' : 1, 
                'element' : 278
              }
            ],
          'h' : [
              {
                'value' : 1, 
                'element' : 183
              }, 
              {
                'value' : 1, 
                'element' : 188
              },
              {
                'value' : 1, 
                'element' : 191
              }
            ]
        },
        ...
      ],
    'team_h_difficulty' : 2, 
    'team_a_difficulty' : 5
  },
  ...
]
```

## Gameweek Fixtures

This endpoint returns an Array of premier league fixtures and statistics for a given gameweek represented
as JSON Objects. These follow the same format as for general fixtures. 

## Gameweek Live

This endpoint returns an Array of element (player) statistics for a given gameweek.
Example: 

```javascript
[
  {
    'id' : 14, 
    'stats' : {
        'minutes' : 90,
        'goals_scored' : 0, 
        'assists' : 0, 
        'clean_sheets' : 1, 
        'goals_conceded' : 0,
        'own_goals' : 0, 
        'penalties_saved' : 0,
        'penalties_missed' : 0,
        'yellow_cards' : 0,
        'red_cards' : 0,
        'saves' : 2, 
        'bonus' : 1, 
        'bps' : 27, 
        'influence' : '18.0', 
        'creativity' : '0.0',
        'threat' : '0.0',
        'ict_index' : '1.8',
        'total_points' : 7,
        'in_dreamteam' : false
      },
    'explain' : [
        {
          'fixture' : 10,
          'stats' : [
              {
                'identifier' : 'minutes', 
                'points' : 2,
                'value' : 90
              },
              {
                'identifier' : 'clean_sheets', 
                'points' : 4, 
                'value' : 1
              },
              {
                'identifier' : 'bonus',
                'points' : 1,
                'value' : 1
              }
            ]
        }
      ]
  }
]
```

## League Classic

This endpoint returns info on a classic league represented by a JSON Object. The leauge id for the 
overall league is **314**. Example:

```javascript
{
  'league' : {...},
  'new_entries' : {...},
  'standings' : {...}
}
```

### Attributes

#### `league` - JSON Object

JSON Object with basic info for the given league. Example:

```javascript
{
  'id' : 314, 
  'name' : 'Overall', 
  'created' : '2019-06-25T11:25:49.714514Z,
  'closed' : false, 
  'max_entries' : null,
  'league_type' : 's', 
  'scoring' : 'c', 
  'admin_entry' : null,
  'start_event' : 1, 
  'code_privacy' : 'p',
  'rank' : null, 
}
```

#### `new_entries` - JSON Object

JSON Object with info on new entries for a given league. Example: 

```javascript
{
  'has_next' : false, 
  'page' : 1, 
  'results' : []
}
```

#### `standings` - JSON Object

JSON Object with info on standings for given league for a given page of players in that league (sorted by points). Example:

```javascript
{
  'has_next' : true,
  'page' : 1, 
  'results' : [
    {
      'id' : 122032, 
      'event_total' : 23, 
      'player_name' : 'John Doe',
      'rank' : 1,
      'rank_sort' : 1, 
      'total' : 2451,
      'entry' : 24513, 
      'entry_name' : 'Aúpa Atleti' 
    },
    ...
  ] 
}
```

You can navigate to different pages of the league standings with the `?page_standings={page}` extension
to the endpoint URL. For instance, to go the 10th page of the overall rankings you would navigate to:

```
https://fantasy.premierleague.com/api/leagues-classic/314/standings/?page_standings=10
```

## Player

This endpoint returns current and historic information for a given element (player) represented as a JSON Object. Example:

```javascript
{
  'fixtures' : [...],
  'history' : [...],
  'history_past' : [...]
}
```

### Attributes

#### `fixtures` - Array

Array of upcoming fixtures, represented as JSON Objects, for the given element for the current season. Example:

```javascript
[
  {
    'id' : 364, 
    'code' : 1060065, 
    'team_h' : 10, 
    'team_h_score' : null, 
    'team_a' : 6, 
    'team_a_score' : null,
    'event' : 46, 
    'finished' : false, 
    'minutes' : 0,
    'provisional_start_time' : false, 
    'kickoff_time' : '2020-07-22T19:15:00Z',
    'event_name' : 'Gameweek 37+',
    'is_home' : true,
    'difficulty' : 4
  }, 
  ...
]
```

#### `history` - Array

Array of past fixutes, represented as JSON Objects, for the given element in the current season. Example:

```javascript
[
  {
    'element' : 191, 
    'fixture' : 1, 
    'opponent_team' : 14, 
    'total_points' : 12, 
    'was_home' : true,
    'kickoff_time' : '2019-08-09T19:00:00Z', 
    'team_h_score' : 4, 
    'team_a_score' : 1, 
    'round' : 1, 
    'minutes' : 90,
    'goals_scored' : 1, 
    'assists' : 1, 
    'clean_sheets' : 0, 
    'goals_conceded' : 0, 
    'own_goals' : 0, 
    'penalties_saved' : 0,
    'penalties_missed' : 0, 
    'yellow_cards' : 0, 
    'red_cards' : 0,
    'saves' : 0,
    'bonus' : 2, 
    'bps' : 40,
    'influence' : '54.8',
    'creativity' : '39.7', 
    'threat' : '39.0', 
    'ict_index' : '13.4',
    'value' : 125, 
    'transfers_balance' : 0,
    'selected' : 2375465,
    'transfers_in' : 0,
    'transfers_out' : 0
  }, 
  ...
]
```


#### `history_past` - Array

Array of historic FPL performances, represented as JSON Objects, for the given element. Example: 

```javascript
[
  {
    'season_name' : '2013/14',
    'element_code' : 118748, 
    'start_cost' : 65, 
    'end_cost' : 55,
    'total_points' : 31, 
    'minutes' : 501, 
    'goals_scored' : 2, 
    'assists' : 1, 
    'clean_sheets' : 1, 
    'goals_conceded' : 2, 
    'own_goals' : 0,
    'penalties_saved' : 0,
    'penalties_missed' : 0,
    'yellow_cards' : 1,
    'red_cards' : 0,
    'saves' : 0,
    'bonus' : 3,
    'bps' : 25, 
    'influence' : '0.0',
    'creativity' : '0.0',
    'threat' : '0.0',
    'ict_index' : '0.0'
  },
  ...
]
```

## Entry

This endpoint returns general information for a given entry (FPL player), represented by a JSON Object. Example:

```javascript
{
  'id' : 1356078, 
  'joined_time' : '2019-07-22T17:21:21.127744Z',
  'started_time' : 1, 
  'favourite_team' : null,
  'player_first_name' : 'John',
  'player_last_name' : 'Doe',
  'player_region_id' : 229,
  'player_region_name' : 'USA',
  'player_region_iso_code_short' : 'US', 
  'player_region_iso_code_long' : 'USA', 
  'summary_overall_'points' : 2135, 
  'summary_overall_rank' : 149677,
  'summary_event_points' : 24, 
  'summary_event_rank' : 1844270, 
  'current_event' : 46, 
  'leagues' : {
    'classic' : [
      {
        'id' : 249, 
        'name' : 'USA',
        'short_name' : 'region-229',
        'created' : '2019-06-25T11:25:48.745601Z', 
        'closed' : false, 
        'rank' : null,
        'max_entries' : null,
        'league_type' : 's',
        'scoring' : 'c',
        'admin_entry' : null,
        'start_event' : 1, 
        'entry_rank' : 5699,
        'entry_last_rank' : 5619, 
        'entry_can_leave' : false,
        'evntry_can_admin' : false, 
        'entry_can_invite' : false
      },
      ...
    ],
    'h2h' : [],
    'cup' : {
      'matches' : [
        {
          'id' : 46396468, 
          'entry_1_entry' : 1356078, 
          'entry_1_name' : 'Go Team',
          'entry_1_player_name' : 'John Doe',
          'entry_1_points' : 59,
          'entry_1_win' : 0,
          'entry_1_draw' : 0,
          'entry_1_loss' : 0,
          'entry_1_total' : 0,
          'entry_2_entry' : 266049, 
          'entry_2_name' : 'Goo Team',
          'entry_2_player_name' : 'Jane Doe',
          'entry_2_points' : 71, 
          'entry_2_win' : 0,
          'entry_2_draw' : 0,
          'entry_2_loss' : 0,
          'entry_2_total' : 0,
          'is_knockout' : true, 
          'winner' : 266049,
          'seed_value' : null,
          'event' : 22,
          'tiebreak' : null
        },
        ...
      ],
      'status' : {
        'qualification_event' : 16,
        'qualification_numbers' : 4194304,
        'qualifcation_rank' : 3115989, 
        'qualification_state' : 'QUALIFIED'
      }
    }
  },
  'name' : 'Go Team',
  'kit' : null,
  'last_deadline_bank' : 3,
  'last_deadline_value' : 1068,
  'last_deadline_total_transfers' : 62
}
```

## Entry Cup

This endpoint returns information about an entry's cup histroy for the current season, represented as JSON Object. The `cup_matches` array follows the same format as the `matches` entry under `leagues` > `cup` in the entry endpoint. The `cup_status` array follows the same format as the `status` entry under `leagues` > `cup` in the entry endpoint. Example:

```javascript
{
  'cup_matches' : [...],
  'cup_status' : {...}
}
```
