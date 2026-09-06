function RecommendationCard({ recommendations }) {
    return (
        <div className="result-card recommendation-card">
            <div className="card-title-row">
                <div>
                    <span className="card-label">Smart Recommendations</span>
                    <h3>Plan Based on Your Timeline</h3>
                </div>
            </div>

            <div className="recommendation-list">
                {Object.entries(recommendations).map(([goal, data]) => (
                    <div className="recommendation-item" key={goal}>
                        <div className="recommendation-icon">
							<img
								src={`/images/${goal.toLowerCase()}.png`}
								alt={goal}
							/>
						</div>

                        <div className="recommendation-content">
                            <div className="recommendation-top">
                                <h4>{goal}</h4>
                                <span>{data.category}</span>
                            </div>

                            <p>{data.description}</p>
                        </div>
                    </div>
                ))}
            </div>
        </div>
    );
}

export default RecommendationCard;