function AIExplanation({ explanation }) {
    return (
        <div className="result-card ai-explanation">
            <div className="ai-header">
                <div className="ai-icon">
					<img
						src="/images/ai.png"
						alt="AI"
					/>
				</div>

                <div>
                    <span className="card-label">AI Insight</span>
                    <h3>Your Financial Summary</h3>
                </div>
            </div>

            <p className="ai-text">
                {explanation}
            </p>
        </div>
    );
}

export default AIExplanation;