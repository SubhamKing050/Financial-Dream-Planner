import pandas as pd


# ==========================================
# CONFIGURATION
# ==========================================

DATA_PATH = "Data/city_goal_costs.csv"

# Assignment requirement:
# 0.06% annual inflation
INFLATION_RATE = 0.0006


# ==========================================
# LOAD DATASET
# ==========================================

df = pd.read_csv(DATA_PATH)


# ==========================================
# FUTURE COST CALCULATION
# ==========================================

def calculate_future_cost(current_cost, years):
    """
    Calculate the future cost of a goal using
    the project's fixed annual inflation rate.

    Formula:
        Future Cost = Current Cost × (1 + inflation)^years
    """

    future_cost = current_cost * (
        (1 + INFLATION_RATE) ** years
    )

    return round(future_cost, 2)


# ==========================================
# GET CITY COSTS
# ==========================================

def get_city_costs(city, area_type):
    """
    Find the current Marriage, Car and Home
    costs for the selected city and area type.
    """

    matching_rows = df[
        (df["City"].str.lower() == city.lower()) &
        (df["Area_Type"].str.lower() == area_type.lower())
    ]

    if matching_rows.empty:
        raise ValueError(
            f"No cost data found for City='{city}' "
            f"and Area_Type='{area_type}'."
        )

    row = matching_rows.iloc[0]

    return {
        "marriage": float(row["Marriage_Cost_Current"]),
        "car": float(row["Car_Cost_Current"]),
        "home": float(row["Home_Cost_Current"])
    }


# ==========================================
# CALCULATE ALL FUTURE GOAL COSTS
# ==========================================

def calculate_goal_costs(
    city,
    area_type,
    marriage_years=None,
    car_years=None,
    home_years=None
):
    """
    Calculate future costs for the selected goals.

    Each goal is calculated separately because
    the timelines can be different.
    """

    current_costs = get_city_costs(
        city,
        area_type
    )

    result = {}

    # --------------------------------------
    # Marriage
    # --------------------------------------

    if marriage_years is not None:

        result["marriage"] = {
            "current_cost": current_costs["marriage"],
            "years": marriage_years,
            "future_cost": calculate_future_cost(
                current_costs["marriage"],
                marriage_years
            )
        }

    # --------------------------------------
    # Car
    # --------------------------------------

    if car_years is not None:

        result["car"] = {
            "current_cost": current_costs["car"],
            "years": car_years,
            "future_cost": calculate_future_cost(
                current_costs["car"],
                car_years
            )
        }

    # --------------------------------------
    # Home
    # --------------------------------------

    if home_years is not None:

        result["home"] = {
            "current_cost": current_costs["home"],
            "years": home_years,
            "future_cost": calculate_future_cost(
                current_costs["home"],
                home_years
            )
        }

    return result


# ==========================================
# TEST THE FUNCTION
# ==========================================

if __name__ == "__main__":

    try:

        costs = calculate_goal_costs(
            city="Bangalore",
            area_type="Central",
            marriage_years=5,
            car_years=4,
            home_years=10
        )

        print("\n==========================================")
        print("FUTURE GOAL COST CALCULATOR")
        print("==========================================")

        print(
            f"\nInflation Rate: "
            f"{INFLATION_RATE * 100:.2f}% per year"
        )

        for goal, data in costs.items():

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

    except ValueError as error:

        print(f"\nError: {error}")