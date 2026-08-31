# ==========================================
# FEASIBILITY ANALYSIS
# ==========================================


# ==========================================
# GOAL STATUS RULES
# ==========================================

def classify_goal(required_amount, available_capacity):
    """
    Classify a financial goal based on the
    required monthly investment and the
    available monthly investment capacity.

    Status rules:

    Achievable:
        Required amount <= available capacity

    Challenging:
        Required amount is more than the available
        capacity but the gap is relatively small.

    Highly Challenging:
        Required amount is significantly higher
        than the available capacity.
    """

    if available_capacity <= 0:

        return "Highly Challenging"

    ratio = required_amount / available_capacity

    if ratio <= 1:
        return "Achievable"

    elif ratio <= 1.5:
        return "Challenging"

    else:
        return "Highly Challenging"


# ==========================================
# CALCULATE SAVING CAPACITY
# ==========================================

def calculate_saving_capacity(
    monthly_salary,
    saving_percentage
):
    """
    Calculate the amount available for investment
    based on the user's monthly salary and selected
    saving percentage.
    """

    if monthly_salary < 0:
        raise ValueError(
            "Monthly salary cannot be negative."
        )

    if saving_percentage < 0 or saving_percentage > 100:
        raise ValueError(
            "Saving percentage must be between 0 and 100."
        )

    available_capacity = (
        monthly_salary *
        saving_percentage /
        100
    )

    return round(available_capacity, 2)


# ==========================================
# ANALYZE INDIVIDUAL GOALS
# ==========================================

def analyze_goals(
    investment_results,
    available_capacity
):
    """
    Analyze every financial goal and calculate:

    - Required monthly investment
    - Available capacity
    - Surplus / shortfall
    - Goal status
    """

    results = {}

    for goal, data in investment_results.items():

        # Ignore the total entry
        if goal == "total":
            continue

        required_amount = data[
            "monthly_investment"
        ]

        difference = (
            available_capacity -
            required_amount
        )

        if difference >= 0:

            surplus = round(
                difference,
                2
            )

            shortfall = 0

        else:

            surplus = 0

            shortfall = round(
                abs(difference),
                2
            )

        status = classify_goal(
            required_amount,
            available_capacity
        )

        results[goal] = {

            "required_monthly_investment":
                required_amount,

            "available_investment_capacity":
                available_capacity,

            "monthly_surplus":
                surplus,

            "monthly_shortfall":
                shortfall,

            "status":
                status
        }

    return results


# ==========================================
# COMPLETE FEASIBILITY ANALYSIS
# ==========================================

def analyze_feasibility(
    monthly_salary,
    saving_percentage,
    investment_results
):
    """
    Perform the complete feasibility analysis.

    Inputs:

        monthly_salary
        saving_percentage
        investment_results

    Returns:

        Available investment capacity
        Total required investment
        Overall surplus/shortfall
        Individual goal analysis
    """

    # --------------------------------------
    # Calculate available capacity
    # --------------------------------------

    available_capacity = calculate_saving_capacity(
        monthly_salary,
        saving_percentage
    )

    # --------------------------------------
    # Calculate total requirement
    # --------------------------------------

    total_required = investment_results[
        "total"
    ]["monthly_investment"]

    # --------------------------------------
    # Calculate overall difference
    # --------------------------------------

    overall_difference = (
        available_capacity -
        total_required
    )

    if overall_difference >= 0:

        overall_surplus = round(
            overall_difference,
            2
        )

        overall_shortfall = 0

    else:

        overall_surplus = 0

        overall_shortfall = round(
            abs(overall_difference),
            2
        )

    # --------------------------------------
    # Analyze individual goals
    # --------------------------------------

    goal_analysis = analyze_goals(
        investment_results,
        available_capacity
    )

    # --------------------------------------
    # Overall status
    # --------------------------------------

    if overall_difference >= 0:

        overall_status = "Achievable"

    elif total_required <= available_capacity * 1.5:

        overall_status = "Challenging"

    else:

        overall_status = "Highly Challenging"

    # --------------------------------------
    # Return complete result
    # --------------------------------------

    return {

        "monthly_salary":
            round(monthly_salary, 2),

        "saving_percentage":
            saving_percentage,

        "available_investment_capacity":
            available_capacity,

        "total_monthly_requirement":
            total_required,

        "monthly_surplus":
            overall_surplus,

        "monthly_shortfall":
            overall_shortfall,

        "overall_status":
            overall_status,

        "goals":
            goal_analysis
    }


# ==========================================
# TEST
# ==========================================

if __name__ == "__main__":

    # Example data from the
    # investment calculator

    example_investments = {

        "marriage": {
            "future_cost": 1000000,
            "years": 5,
            "monthly_investment": 13608.42
        },

        "car": {
            "future_cost": 800000,
            "years": 4,
            "monthly_investment": 13524.70
        },

        "home": {
            "future_cost": 5000000,
            "years": 10,
            "monthly_investment": 27321.44
        },

        "total": {
            "monthly_investment": 54454.56
        }
    }

    # Example salary
    monthly_salary = 60000

    # User wants to save 20%
    saving_percentage = 20

    result = analyze_feasibility(
        monthly_salary,
        saving_percentage,
        example_investments
    )

    print("\n==========================================")
    print("FEASIBILITY ANALYSIS")
    print("==========================================")

    print(
        f"\nMonthly Salary: "
        f"₹{result['monthly_salary']:,.2f}"
    )

    print(
        f"Saving Percentage: "
        f"{result['saving_percentage']:.2f}%"
    )

    print(
        f"Available Investment Capacity: "
        f"₹{result['available_investment_capacity']:,.2f}"
    )

    print(
        f"\nTotal Monthly Requirement: "
        f"₹{result['total_monthly_requirement']:,.2f}"
    )

    print(
        f"Monthly Surplus: "
        f"₹{result['monthly_surplus']:,.2f}"
    )

    print(
        f"Monthly Shortfall: "
        f"₹{result['monthly_shortfall']:,.2f}"
    )

    print(
        f"Overall Status: "
        f"{result['overall_status']}"
    )

    print("\n------------------------------------------")
    print("GOAL-WISE ANALYSIS")
    print("------------------------------------------")

    for goal, data in result["goals"].items():

        print(f"\n{goal.upper()}")

        print(
            f"Required Investment: "
            f"₹{data['required_monthly_investment']:,.2f}"
        )

        print(
            f"Available Capacity: "
            f"₹{data['available_investment_capacity']:,.2f}"
        )

        print(
            f"Surplus: "
            f"₹{data['monthly_surplus']:,.2f}"
        )

        print(
            f"Shortfall: "
            f"₹{data['monthly_shortfall']:,.2f}"
        )

        print(
            f"Status: "
            f"{data['status']}"
        )