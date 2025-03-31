import pandas as pd

df = pd.read_csv(r"C:\Users\joefr\Documents\FPL Data\cleaned_merged_seasons.csv")

df_season = df[df['season_x'] == '2023-24']

df_season_team = df_season.groupby('team_x').agg(
    {'goals_scored':'sum',
     'assists':'sum',
     'yellow_cards':'sum',
     'red_cards':'sum',
     'own_goals':'sum',
     'saves':'sum',
     'penalties_missed':'sum',
     'penalties_saved':'sum'}).rename(
    columns={'goals_scored':'goals_scored_sum',
             'assists':'assists_sum',
             'yellow_cards':'yellow_cards_sum',
             'red_cards':'red_cards_sum',
             'own_goals':'own_goals_sum',
             'saves':'saves_sum',
             'penalties_missed':'penalties_missed_sum',
             'penalties_saved':'penalties_saved_sum'
             }).reset_index()

df_season_players = df_season.groupby('name').agg(
    {'goals_scored':'sum',
     'assists':'sum',
     'yellow_cards':'sum',
     'red_cards':'sum',
     'own_goals':'sum',
     'saves':'sum',
     'penalties_missed':'sum',
     'penalties_saved':'sum',
     'influence':'mean',
     'creativity':'mean',
     'minutes':'mean'}).rename(
    columns={'goals_scored':'goals_scored_sum',
             'assists':'assists_sum',
             'yellow_cards':'yellow_cards_sum',
             'red_cards':'red_cards_sum',
             'own_goals':'own_goals_sum',
             'saves':'saves_sum',
             'penalties_missed':'penalties_missed_sum',
             'penalties_saved':'penalties_saved_sum',
             'influence':'influence_mean',
             'creativity':'creativity_mean',
             'minutes':'minutes_mean'
             }).reset_index()