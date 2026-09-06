function InvestmentCard({ investments }) {
    return (
        <div className="result-card investment-card">
            <span className="card-label">Monthly Investment Requirements</span>
            <h3>What You Need to Invest</h3>

            <div className="investment-list">
                {Object.entries(investments).map(([goal, data]) => {
                    if (goal === "total" || !data) return null;

                    return (
                        <div className="investment-row" key={goal}>
                            <span>{goal}</span>

                            <strong>
                                ₹{Number(data.monthly_investment).toLocaleString(
                                    "en-IN",
                                    {
                                        minimumFractionDigits: 2,
                                        maximumFractionDigits: 2
                                    }
                                )}
                            </strong>
                        </div>
                    );
                })}
            </div>

            {investments.total && (
                <div className="investment-total">
                    <span>Total Required</span>

                    <strong>
                        ₹{Number(
                            investments.total.monthly_investment
                        ).toLocaleString("en-IN", {
                            minimumFractionDigits: 2,
                            maximumFractionDigits: 2
                        })}
                    </strong>
                </div>
            )}
        </div>
    );
}

export default InvestmentCard;