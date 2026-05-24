# pull play-by-play data for training win prediction model on live games
from nba_api.stats.endpoints import playbyplayv3
from nba_api.stats.endpoints import boxscoretraditionalv3
from nba_api.live.nba.endpoints import scoreboard
import pandas as pd


def pull_live_data():
    try:
        scoreboard_data = scoreboard.ScoreBoard().games.get_dict()['scoreboard']
        return pd.DataFrame(scoreboard_data)
    except Exception as e:
        print(f"Error pulling live data: {e}")
        return pd.DataFrame()  # Return an empty DataFrame in case of error

def pull_play_by_play_data(game_id):
    play_by_play_v3 = playbyplayv3.PlayByPlayV3(game_id=game_id)
    return play_by_play_v3

# export data to csv for training

def export_data_to_csv(data, filename):
    data.to_csv(filename, index=False)