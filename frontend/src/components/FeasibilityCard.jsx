function FeasibilityCard({ feasibility }) {
    const status = feasibility.overall_status;

    let statusClass = "status-high";

    if (status === "Achievable") {
        statusClass = "status-achievable";
    } else if (status === "Challenging") {
        statusClass = "status-challenging";
    }

    return (
        <div className={`result-card feasibility-card ${statusClass}`}>
            <div className="feasibility-header">
                <div>
                    <span className="card-label">Financial Feasibility</span>
                    <h3>Can You Afford Your Dreams?</h3>
                </div>

                <div className="status-badge">
                    {status}
                </div>
            </div>

            <div className="feasibility-grid">

                <div className="feasibility-item">
                    <span>Investment Capacity</span>
                    <strong>
                        ₹{Number(
                            feasibility.available_investment_capacity
                        ).toLocaleString("en-IN", {
                            minimumFractionDigits: 2,
                            maximumFractionDigits: 2
                        })}
                    </strong>
                </div>

                <div className="feasibility-item">
                    <span>Total Required</span>
                    <strong>
                        ₹{Number(
                            feasibility.total_monthly_requirement
                        ).toLocaleString("en-IN", {
                            minimumFractionDigits: 2,
                            maximumFractionDigits: 2
                        })}
                    </strong>
                </div>

                <div className="feasibility-item">
                    <span>Monthly Surplus</span>
                    <strong>
                        ₹{Number(
                            feasibility.monthly_surplus
                        ).toLocaleString("en-IN", {
                            minimumFractionDigits: 2,
                            maximumFractionDigits: 2
                        })}
                    </strong>
                </div>

                <div className="feasibility-item">
                    <span>Monthly Shortfall</span>
                    <strong>
                        ₹{Number(
                            feasibility.monthly_shortfall
                        ).toLocaleString("en-IN", {
                            minimumFractionDigits: 2,
                            maximumFractionDigits: 2
                        })}
                    </strong>
                </div>

            </div>

            <div className="feasibility-message">
                {status === "Achievable" && (
                    <p>
                        Your current saving capacity is sufficient to meet
                        the planned investment requirements.
                    </p>
                )}

                {status === "Challenging" && (
                    <p>
                        Your goals are possible, but your current investment
                        capacity is below the required amount.
                    </p>
                )}

                {status === "Highly Challenging" && (
                    <p>
                        Your current investment capacity is significantly
                        below the amount required for these goals.
                    </p>
                )}
            </div>
        </div>
    );
}

export default FeasibilityCard;