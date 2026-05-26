# NBA Live Win Predictor

## Real-Time Updates

## Frontend: React, Tailwind, Recharts

## Backend: Flask/FastAPI, PyTorch, Pandas, Websockets

## Frontend Structure: 

## Backend Structure:

## Hosted on GitHub Pages

## Architecture

| Notebooks | Backend (Flask) | Frontend (React) |
|-----------|----------------|------------------|
| Fetch historical play-by-play data | Load model weights at startup | Poll `/gamestate` every 15s |
| Preprocess + feature engineer → save scaler | `/predict` endpoint runs inference | Scoreboard |
| Train PyTorch model → save `.pth` | `/live` endpoint polls NBA API + caches | Win Probability Chart |
| | | Play-by-Play Feed |
| | | Box Score |

## Stack
- **Model**: PyTorch (binary classifier, pre-trained)
- **Backend**: Flask + nba_api
- **Frontend**: React + Tailwind + Recharts
