import pandas as pd
import numpy as np

matches = pd.read_csv("ipl-matches.csv")
print(matches.head())

def teams_api():
    teams = list(set(list(matches['Team1'].unique()) + list(matches['Team2'].unique())))
    teams_dict = {
        'teams':teams
    }
    return teams_dict

def team_vs_team(team1,team2):
  teams = list(set(list(matches['Team1'].unique()) + list(matches['Team2'].unique())))
  if team1 in teams and team2 in teams:
    team1vteam2 = matches[((matches['Team1'] == team1) & (matches['Team2'] == team2)) | ((matches['Team1'] == team2) & (matches['Team2'] == team1))]
    total_matches = team1vteam2.shape[0]
    team1_wins = team1vteam2['WinningTeam'].value_counts()[team1]
    team2_wins = team1vteam2['WinningTeam'].value_counts()[team2]
    draws = total_matches - (team1_wins + team2_wins)

    return {
        'total_matches' : total_matches,
        f'{team1}_wins': int(team1_wins),
        f'{team2}_wins':int(team2_wins),
        'draws':int(draws)
    }
  else:
     return {
        'message':'Invalid team name'
     }
