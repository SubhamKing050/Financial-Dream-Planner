function GoalsCard({ goals }) {
    return (
        <div className="result-card goals-card">
            <div className="card-title-row">
                <div>
                    <span className="card-label">Future Goal Costs</span>
                    <h3>Your Dreams</h3>
                </div>
            </div>

            <div className="goals-result-grid">
                {Object.entries(goals).map(([goal, data]) => {
                    if (!data) return null;

                    return (
                        <div className="goal-result" key={goal}>
                            <div className="goal-result-icon">
                                {goal.charAt(0).toUpperCase()}
                            </div>

                            <div className="goal-result-info">
                                <h4>{goal}</h4>

                                <p>
                                    In {data.years} years
                                </p>

                                <strong>
                                    ₹{Number(data.future_cost).toLocaleString(
                                        "en-IN",
                                        {
                                            minimumFractionDigits: 2,
                                            maximumFractionDigits: 2
                                        }
                                    )}
                                </strong>
                            </div>
                        </div>
                    );
                })}
            </div>
        </div>
    );
}

export default GoalsCard;