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

<<<<<<< HEAD
def pull_live_play_by_play():
    try:
        play_by_play = playbyplay.PlayByPlay().get_dict()['game']['actions'] # could also return game id here if needed 
        return pd.DataFrame(play_by_play)
    except Exception as e:
        print(f"Error pulling live play bby play: {e}")
        return pd.DataFrame()
=======
def pull_play_by_play_data(game_id):
    play_by_play_v3 = playbyplayv3.PlayByPlayV3(game_id=game_id)
    return play_by_play_v3

# export data to csv for training
>>>>>>> b2c8f99a7cec11ba30c093ee6226bd23ca4a306b
