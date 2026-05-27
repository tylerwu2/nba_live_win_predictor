export default function PlayByPlayFeed({playbyplayfeed = []}) {
    return (
        <div className="bg-gray-100 rounded-xl p-4"> 
            {playbyplayfeed.map((play, index) => (
                <p key={index}>{play}</p>
            ))}
        </div>
    );
}