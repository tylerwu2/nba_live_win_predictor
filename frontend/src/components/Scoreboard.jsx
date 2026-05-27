export default function Scoreboard({data}) {
    return (
        <div className="bg-gray-700 rounded-xl p-4">
            <div className="flex justify-between text-white space-x-2 text-2x1 font-bold">
                <span>{data.home_team} {data.home_score}</span>
                <span>{data.away_team} {data.away_score}</span>
            </div>
        </div>
    )
}