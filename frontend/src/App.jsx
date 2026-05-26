import {useEffect, useState} from "react"
import Scoreboard from "./components/Scoreboard"
import WinProbability from "./components/WInProbability"
import PlayByPlayFeed from "./components/PlayByPlayFeed"

export default function App() {
  /* keep track of current game state, setGameState to modify gameState  */
  const [gameState, setGameState] = useState(null) 
  /* keep track of play by play history, setHistory to modify play by play history  */
  const [history, setHistory] = useState([])

  useEffect(() => {
    const fetchData = async () => {
      const res = await fetch('http://localhost:5000/live_data')
      const data = await res.json() 
      setGameState(data)
      setHistory(prev => [...prev, {win_pct: data.win_pct, time: data.clock}])
    }

    fetchData()
    const interval = setInterval(fetchData, 15000)
    return () => clearInterval(interval)
  }, [])

  if (!gameState) return (
    <div className="min-h-screen bg-gray-950 flex items-center justify-center text-white">
      Loading game...
    </div>
  )

  return (
    <div className="min-h-screen bg-gray-950 flex items-center justify-center">
      <h1 className="text-white text-3xl font-bold">NBA Live Predictor</h1>
      <div className="max-w-4xl mx-auto space-y-4">
        <Scoreboard data={gameState}/>
        <WinProbability history={history}/>
        <PlayByPlayFeed plays={gameState.plays}/>
      </div>
    </div>
  )
}