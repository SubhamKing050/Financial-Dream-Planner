import { useState } from "react";

import Header from "./components/Header";
import InputForm from "./components/InputForm";
import SalaryCard from "./components/SalaryCard";
import GoalsCard from "./components/GoalsCard";
import InvestmentCard from "./components/InvestmentCard";
import FeasibilityCard from "./components/FeasibilityCard";
import RecommendationCard from "./components/RecommendationCard";
import AIExplanation from "./components/AIExplanation";

import { generateFinancialPlan } from "./services/api";

function App() {
    const [result, setResult] = useState(null);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState("");

    async function handleGeneratePlan(data) {
        setLoading(true);
        setError("");
        setResult(null);

        try {
            const response = await generateFinancialPlan(data);
            setResult(response);
        } catch (err) {
            setError(
                "Unable to generate the financial plan. Please make sure the FastAPI backend is running."
            );
        } finally {
            setLoading(false);
        }
    }

    return (
        <div className="app">

            <Header />

            <main className="main-container">

                <InputForm
                    onSubmit={handleGeneratePlan}
                    loading={loading}
                />

                {error && (
                    <div className="error-message">
                        {error}
                    </div>
                )}

                {result && (
                    <section className="results-section">

                        <div className="section-heading">
                            <span>02</span>
                            <div>
                                <h2>Your Financial Plan</h2>
                                <p>
                                    Here is the plan generated from your
                                    financial profile.
                                </p>
                            </div>
                        </div>

                        <div className="summary-grid">

                            <SalaryCard
                                salary={result.predicted_salary}
                            />

                            <div className="result-card capacity-card">
                                <span className="card-label">
                                    Monthly Investment Capacity
                                </span>

                                <h3>
                                    ₹{Number(
                                        result.feasibility
                                            .available_investment_capacity
                                    ).toLocaleString("en-IN", {
                                        minimumFractionDigits: 2,
                                        maximumFractionDigits: 2
                                    })}
                                </h3>

                                <p>
                                    Based on your saving percentage
                                </p>
                            </div>

                            <div className="result-card required-card">
                                <span className="card-label">
                                    Total Monthly Requirement
                                </span>

                                <h3>
                                    ₹{Number(
                                        result.investment_requirements
                                            .total.monthly_investment
                                    ).toLocaleString("en-IN", {
                                        minimumFractionDigits: 2,
                                        maximumFractionDigits: 2
                                    })}
                                </h3>

                                <p>
                                    Required for all selected goals
                                </p>
                            </div>

                        </div>

                        <FeasibilityCard
                            feasibility={result.feasibility}
                        />

                        <GoalsCard
                            goals={result.future_goal_costs}
                        />

                        <InvestmentCard
                            investments={result.investment_requirements}
                        />

                        <RecommendationCard
                            recommendations={result.recommendations}
                        />

                        <AIExplanation
                            explanation={result.ai_explanation}
                        />

                    </section>
                )}

            </main>

            <footer className="footer">
                Financial Dream Planner • AI-powered financial planning
            </footer>

        </div>
    );
}

export default App;