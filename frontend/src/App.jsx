import {useEffect, useState} from "react"
import Scoreboard from "./components/Scoreboard"
import WinProbability from "./components/WInProbability"
import PlayByPlayFeed from "./components/PlayByPlayFeed"

export default function App() {

  const gameState = {
    home_team: "Lakers",
    away_team: "Warriors",
    home_score: 102,
    away_score: 98,
    clock: "4:32",
    win_pct: 73,
    plays: [
      "LeBron James makes driving layup",
      "Stephen Curry misses 3PT jump shot",
      "Anthony Davis defensive rebound"
    ]
  }

  const history = [
    { win_pct: 45, time: "12:00" },
    { win_pct: 52, time: "8:00" },
    { win_pct: 61, time: "4:00" },
    { win_pct: 73, time: "1:00" }
  ]
  // /* keep track of current game state, setGameState to modify gameState  */
  // const [gameState, setGameState] = useState(null) 
  // /* keep track of play by play history, setHistory to modify play by play history  */
  // const [history, setHistory] = useState([])

  // useEffect(() => {
  //   const fetchData = async () => {
  //     const res = await fetch('http://localhost:5000/live_data')
  //     const data = await res.json() 
  //     setGameState(data)
  //     setHistory(prev => [...prev, {win_pct: data.win_pct, time: data.clock}])
  //   }

  //   fetchData()
  //   const interval = setInterval(fetchData, 15000)
  //   return () => clearInterval(interval)
  // }, [])

  // if (!gameState) return (
  //   <div className="min-h-screen bg-gray-950 flex items-center justify-center text-white">
  //     Loading game...
  //   </div>
  // )

  return (
    <div className="min-h-screen bg-gray-950 flex flex-col items-center p-6 space-y-6">
      <h1 className="text-white text-3xl font-bold">
        NBA Live Predictor</h1>
        <Scoreboard data={gameState}/>
        {/* <WinProbability history={history}/> */}
        <PlayByPlayFeed playbyplayfeed={gameState.plays}/>
    </div>
  )
}