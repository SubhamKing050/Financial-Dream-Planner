# ==========================================
# FINANCIAL DREAM PLANNER - AI AGENT
# ==========================================

import ollama

from salary_prediciton import predict_salary
from future_cost import calculate_goal_costs
from investment_calculator import calculate_goal_investments
from feasibility import analyze_feasibility
from recommendation import recommend_for_goals


# ==========================================
# OLLAMA CONFIGURATION
# ==========================================

MODEL_NAME = "qwen3:0.6b"


# ==========================================
# RUN FINANCIAL ANALYSIS
# ==========================================

def generate_financial_plan(
    age,
    city,
    area_type,
    education,
    job_role,
    salary,
    saving_percentage,
    marriage_years=None,
    car_years=None,
    home_years=None
):
    """
    Generate a complete financial plan.

    The deterministic Python modules perform
    all numerical calculations.

    Ollama is used only to explain the
    calculated results in natural language.
    """

    # --------------------------------------
    # STEP 1: Salary Prediction
    # --------------------------------------

    predicted_salary = predict_salary(
        age=age,
        city=city,
        education=education,
        job_role=job_role
    )

    # --------------------------------------
    # STEP 2: Future Goal Costs
    # --------------------------------------

    goal_costs = calculate_goal_costs(
        city=city,
        area_type=area_type,
        marriage_years=marriage_years,
        car_years=car_years,
        home_years=home_years
    )

    # --------------------------------------
    # STEP 3: Monthly Investments
    # --------------------------------------

    investment_results = calculate_goal_investments(
        goal_costs
    )

    # --------------------------------------
    # STEP 4: Feasibility
    # --------------------------------------

    feasibility_results = analyze_feasibility(
        monthly_salary=predicted_salary,
        saving_percentage=saving_percentage,
        investment_results=investment_results
    )

    # --------------------------------------
    # STEP 5: Investment Categories
    # --------------------------------------

    recommendation_input = {}

    for goal, data in goal_costs.items():

        if data is not None:

            recommendation_input[goal] = {
                "years": data["years"]
            }

    recommendations = recommend_for_goals(
        recommendation_input
    )

    # --------------------------------------
    # STEP 6: Prepare Results
    # --------------------------------------

    results = {

        "input": {
            "age": age,
            "city": city,
            "area_type": area_type,
            "education": education,
            "job_role": job_role,
            "current_salary": salary,
            "saving_percentage": saving_percentage
        },

        "predicted_salary":
            predicted_salary,

        "future_goal_costs":
            goal_costs,

        "investment_requirements":
            investment_results,

        "feasibility":
            feasibility_results,

        "recommendations":
            recommendations
    }

    # --------------------------------------
    # STEP 7: Generate AI Explanation
    # --------------------------------------

    explanation = generate_explanation(
        results
    )

    results["ai_explanation"] = explanation

    return results


# ==========================================
# OLLAMA EXPLANATION
# ==========================================

def generate_explanation(results):
    """
    Generate a short, clean AI explanation.

    Python calculations are the source of truth.
    Ollama only explains the already-calculated results.
    """

    feasibility = results["feasibility"]
    investments = results["investment_requirements"]

    summary = f"""
Predicted monthly salary: ₹{results['predicted_salary']:,.2f}

Available monthly investment capacity: ₹{feasibility['available_investment_capacity']:,.2f}

Total monthly investment required: ₹{investments['total']['monthly_investment']:,.2f}

Monthly shortfall: ₹{feasibility['monthly_shortfall']:,.2f}

Overall status: {feasibility['overall_status']}
"""

    prompt = f"""
You are a financial planning assistant.

Write a clean and concise explanation of the financial plan.

STRICT RULES:

1. Write EXACTLY 2 sentences.
2. Use ONLY the information provided below.
3. Do NOT calculate anything.
4. Do NOT change, round, reinterpret, or convert any number.
5. Copy all numbers exactly as provided.
6. The "Overall status" is FINAL and authoritative.
7. Never call the plan achievable unless the status is exactly "Achievable".
8. If the status is "Challenging", clearly say the plan is challenging.
9. If the status is "Highly Challenging", clearly say the plan is highly challenging.
10. If the monthly shortfall is greater than ₹0.00, mention the exact shortfall.
11. Keep the language simple and professional.
12. Do not use headings or bullet points.
13. Do not provide specific stock or investment product recommendations.
14. Do not give professional financial advice.

FINANCIAL DATA:

{summary}

Write EXACTLY 2 sentences and nothing else.
"""

    try:

        response = ollama.chat(
            model=MODEL_NAME,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response["message"]["content"].strip()

    except Exception as error:

        return (
            "Unable to generate AI explanation. "
            f"Error: {error}"
        )

# ==========================================
# DISPLAY RESULTS
# ==========================================

def display_financial_plan(results):
    """
    Display the financial plan in the terminal.
    """

    print("\n==========================================")
    print("       FINANCIAL DREAM PLANNER")
    print("==========================================")

    # --------------------------------------
    # Predicted Salary
    # --------------------------------------

    print("\nPREDICTED MONTHLY SALARY")
    print("------------------------------------------")

    print(
        f"₹{results['predicted_salary']:,.2f}"
    )

    # --------------------------------------
    # Future Goal Costs
    # --------------------------------------

    print("\nFUTURE GOAL COSTS")
    print("------------------------------------------")

    for goal, data in results[
        "future_goal_costs"
    ].items():

        if data is None:
            continue

        print(f"\n{goal.upper()}")

        print(
            f"Current Cost : "
            f"₹{data['current_cost']:,.2f}"
        )

        print(
            f"Timeline     : "
            f"{data['years']} years"
        )

        print(
            f"Future Cost  : "
            f"₹{data['future_cost']:,.2f}"
        )

    # --------------------------------------
    # Investment Requirements
    # --------------------------------------

    print("\nMONTHLY INVESTMENT REQUIREMENTS")
    print("------------------------------------------")

    for goal, data in results[
        "investment_requirements"
    ].items():

        if goal == "total":
            continue

        print(
            f"{goal.title():12} "
            f"₹{data['monthly_investment']:,.2f}"
        )

    print(
        "\nTotal Required: "
        f"₹{results['investment_requirements']['total']['monthly_investment']:,.2f}"
    )

    # --------------------------------------
    # Feasibility
    # --------------------------------------

    print("\nFEASIBILITY")
    print("------------------------------------------")

    feasibility = results["feasibility"]

    print(
        f"Available Capacity: "
        f"₹{feasibility['available_investment_capacity']:,.2f}"
    )

    print(
        f"Monthly Surplus: "
        f"₹{feasibility['monthly_surplus']:,.2f}"
    )

    print(
        f"Monthly Shortfall: "
        f"₹{feasibility['monthly_shortfall']:,.2f}"
    )

    print(
        f"Overall Status: "
        f"{feasibility['overall_status']}"
    )

    # --------------------------------------
    # Recommendations
    # --------------------------------------

    print("\nRECOMMENDATIONS")
    print("------------------------------------------")

    for goal, data in results[
        "recommendations"
    ].items():

        print(
            f"{goal.title():12} "
            f"{data['category']} - "
            f"{data['description']}"
        )

    # --------------------------------------
    # AI Explanation
    # --------------------------------------

    print("\nAI EXPLANATION")
    print("------------------------------------------")

    print(
        results["ai_explanation"]
    )


# ==========================================
# TEST
# ==========================================

if __name__ == "__main__":

    try:

        result = generate_financial_plan(

            age=25,

            city="Bangalore",

            area_type="Central",

            education="B.Tech",

            job_role="Software Engineer",

            salary=50000,

            saving_percentage=20,

            marriage_years=5,

            car_years=4,

            home_years=10
        )

        display_financial_plan(
            result
        )

    except Exception as error:

        print("\nERROR:")
        print(error)