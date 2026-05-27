# NBA Live Win Predictor, app startup, and routing

import jsonify

from flask import Flask, render_template, request
import torch
from train.py import WinPredictor, data
from stats.py import pull_live_scoreboard, pull_live_play_by_play

# load model weights so only need to pull play-by-play data and box score data in main.py to make predictions and inference at runtime in live games, no need to retrain model every time
model = WinPredictor()
model.load_state_dict(torch.load('weights.pth'))
model.eval()

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    with torch.no_grad():
        prob = model(features)

    return jsonify({'win_pct': prob.item()})

cache = {} # store last live update data in cache in case api endpoint hasn't updated 

@app.route('/live-data')
def live_data():
    scoreboard = pull_live_scoreboard()
    play_by_play = pull_live_play_by_play()

    live_data = {"win_pct": scoreboard, "time_left": play_by_play['clock'], "quarter": play_by_play['period'], homeTeam}

    return jsonify(live_data)

if __name__ == '__main__':
    app.run(debug=True)

