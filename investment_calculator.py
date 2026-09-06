# ==========================================
# MONTHLY INVESTMENT CALCULATOR
# ==========================================


# ==========================================
# CONFIGURATION
# ==========================================

# Expected annual investment return
# Used only for educational calculation
EXPECTED_ANNUAL_RETURN = 0.08


# ==========================================
# CALCULATE MONTHLY INVESTMENT
# ==========================================

def calculate_monthly_investment(
    future_cost,
    years,
    annual_return=EXPECTED_ANNUAL_RETURN
):
    """
    Calculate the monthly investment required
    to reach a future financial goal.

    Formula:

        FV = P × [((1 + r)^n - 1) / r]

    Therefore:

        P = FV × r / ((1 + r)^n - 1)

    Where:

        FV = Future goal cost
        P  = Monthly investment
        r  = Monthly return rate
        n  = Number of months

    The calculation assumes monthly investments
    and monthly compounding.
    """

    # --------------------------------------
    # Validate inputs
    # --------------------------------------

    if future_cost <= 0:
        raise ValueError(
            "Future cost must be greater than 0."
        )

    if years <= 0:
        raise ValueError(
            "Goal timeline must be greater than 0 years."
        )

    if annual_return < 0:
        raise ValueError(
            "Annual return cannot be negative."
        )

    # --------------------------------------
    # Convert annual return to monthly return
    # --------------------------------------

    monthly_return = annual_return / 12

    # --------------------------------------
    # Calculate number of months
    # --------------------------------------

    number_of_months = years * 12

    # --------------------------------------
    # Calculate monthly investment
    # --------------------------------------

    if monthly_return == 0:

        monthly_investment = (
            future_cost / number_of_months
        )

    else:

        monthly_investment = (
            future_cost * monthly_return
            /
            (
                (1 + monthly_return)
                ** number_of_months
                - 1
            )
        )

    return round(monthly_investment, 2)


# ==========================================
# CALCULATE INVESTMENTS FOR ALL GOALS
# ==========================================

def calculate_goal_investments(goal_costs):
    """
    Calculate the monthly investment required
    for every selected financial goal.

    Expected input:

        {
            "marriage": {
                "current_cost": 890000,
                "years": 5,
                "future_cost": 916975.00
            },

            "car": {
                "current_cost": 1260000,
                "years": 4,
                "future_cost": 1290458.00
            }
        }

    Returns the monthly investment required
    for each goal and the total requirement.
    """

    results = {}

    total_monthly_investment = 0

    # --------------------------------------
    # Calculate each goal
    # --------------------------------------

    for goal, data in goal_costs.items():

        future_cost = data["future_cost"]
        years = data["years"]

        monthly_investment = (
            calculate_monthly_investment(
                future_cost=future_cost,
                years=years
            )
        )

        results[goal] = {

            "future_cost":
                future_cost,

            "years":
                years,

            "monthly_investment":
                monthly_investment
        }

        total_monthly_investment += (
            monthly_investment
        )

    # --------------------------------------
    # Add total investment requirement
    # --------------------------------------

    results["total"] = {

        "monthly_investment":
            round(total_monthly_investment, 2)
    }

    return results


# ==========================================
# TEST
# ==========================================

if __name__ == "__main__":

    # Example future goal costs
    example_goals = {

        "marriage": {
            "current_cost": 1000000,
            "years": 5,
            "future_cost": 1003000
        },

        "car": {
            "current_cost": 800000,
            "years": 4,
            "future_cost": 801920
        },

        "home": {
            "current_cost": 5000000,
            "years": 10,
            "future_cost": 5030000
        }
    }

    # Calculate investments
    investments = (
        calculate_goal_investments(
            example_goals
        )
    )

    # --------------------------------------
    # Display results
    # --------------------------------------

    print("\n==========================================")
    print("MONTHLY INVESTMENT CALCULATOR")
    print("==========================================")

    print(
        f"\nExpected Annual Return: "
        f"{EXPECTED_ANNUAL_RETURN * 100:.2f}%"
    )

    for goal, data in investments.items():

        if goal == "total":
            continue

        print(
            f"\n{goal.upper()}"
        )

        print(
            f"Future Cost          : "
            f"₹{data['future_cost']:,.2f}"
        )

        print(
            f"Timeline             : "
            f"{data['years']} years"
        )

        print(
            f"Monthly Investment   : "
            f"₹{data['monthly_investment']:,.2f}"
        )

    print("\n------------------------------------------")

    print(
        f"TOTAL MONTHLY INVESTMENT: "
        f"₹{investments['total']['monthly_investment']:,.2f}"
    )

    print("------------------------------------------")

    print(
        "\nNOTE: This is an educational calculation "
        "and does not guarantee investment returns."
    )