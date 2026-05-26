export default function Scoreboard({homeTeam, awayTeam, homeScore, awayScore}) {
    return (
        <div className="bg-gray-900 rounded-xl p-4">
            <div className="flex justify-between text-white text-2x1 font-bold">
                <span>{homeTeam} {homeScore}</span>
                <span>{awayTeam} {awayScore}</span>
            </div>
        </div>
    )
}