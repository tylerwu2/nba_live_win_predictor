# NBA Live Win Predictor, app startup, and routing

import jsonify

from flask import Flask, render_template, request
from flask_cors import CORS
import torch
from train.py import WinPredictor, data
from stats.py import pull_live_data

# load model weights so only need to pull play-by-play data and box score data in main.py to make predictions and inference at runtime in live games, no need to retrain model every time
model = WinPredictor()
model.load_state_dict(torch.load('weights.pth'))
model.eval()

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    with torch.no_grad():
        prob = model(features)

    return jsonify({'win_pct': prob.item()})

cache = {}

@app.route('/live-data')
def live_data_and_predict():
    data = pull_live_data()
    
    with torch.no_grad():
        prob = model(data)
    return jsonify({'win_pct': prob.item(), 'clock':data})

if __name__ == '__main__':
    app.run(debug=True)

