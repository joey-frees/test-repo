import matplotlib.pyplot as plt
import matplotlib
from import_fpl import df_season_team

matplotlib.use('TkAgg')

# Create the bar plot
plt.barh(df_season_team['team_x'], df_season_team['goals_scored_sum'], label = 'Goals')
plt.barh(df_season_team['team_x'], df_season_team['assists_sum'], left = df_season_team['goals_scored_sum'], label = 'Assists')

# Add labels and title
plt.xlabel('Team')
plt.ylabel('Combined goals/assists')
plt.title('Goals scored/assists by team')
plt.legend()

# Add custom style
plt.style.use('custom_style.mplstyle')

plt.show()

