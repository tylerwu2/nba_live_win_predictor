# pull play-by-play data for training win prediction model on live games
from nba_api.stats.endpoints import boxscoretraditionalv3
from nba_api.live.nba.endpoints import scoreboard, playbyplay
import pandas as pd


def pull_live_scoreboard():
    try:
        scoreboard_data = scoreboard.ScoreBoard().games.get_dict()['scoreboard']
        return pd.DataFrame(scoreboard_data)
    except Exception as e:
        print(f"Error pulling live scoreboard: {e}")
        return pd.DataFrame()  # Return an empty DataFrame in case of error

def pull_live_play_by_play():
    try:
        play_by_play = playbyplay.PlayByPlay().get_dict()['game']['actions'] # could also return game id here if needed 
        return pd.DataFrame(play_by_play)
    except Exception as e:
        print(f"Error pulling live play bby play: {e}")
        return pd.DataFrame()
