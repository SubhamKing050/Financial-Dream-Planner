function SalaryCard({ salary }) {
    return (
        <div className="result-card salary-card">
            <span className="card-label">Predicted Monthly Salary</span>

            <h3>
                ₹{Number(salary).toLocaleString("en-IN", {
                    minimumFractionDigits: 2,
                    maximumFractionDigits: 2
                })}
            </h3>

            <p>
                Estimated from your profile
            </p>
        </div>
    );
}

export default SalaryCard;