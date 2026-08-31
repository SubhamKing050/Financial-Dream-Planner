# ==========================================
# INVESTMENT CATEGORY RECOMMENDATION
# ==========================================


# ==========================================
# TIME-HORIZON RULES
# ==========================================

SHORT_TERM_MAX_YEARS = 3
MEDIUM_TERM_MAX_YEARS = 7


# ==========================================
# RECOMMEND CATEGORY
# ==========================================

def recommend_category(years):
    """
    Recommend a broad educational investment
    category based on the goal timeline.

    Project rules:

    0 - 3 years:
        Lower-volatility /
        capital-preservation-oriented

    More than 3 - 7 years:
        Diversified balanced

    More than 7 years:
        Diversified long-term growth-oriented

    These are educational categories only.
    They are not financial advice.
    """

    if years <= 0:
        raise ValueError(
            "Goal timeline must be greater than 0 years."
        )

    if years <= SHORT_TERM_MAX_YEARS:

        return {
            "category": "Short-term",
            "description":
                "Lower-volatility / "
                "capital-preservation-oriented"
        }

    elif years <= MEDIUM_TERM_MAX_YEARS:

        return {
            "category": "Medium-term",
            "description":
                "Diversified balanced"
        }

    else:

        return {
            "category": "Long-term",
            "description":
                "Diversified long-term "
                "growth-oriented"
        }


# ==========================================
# RECOMMEND FOR MULTIPLE GOALS
# ==========================================

def recommend_for_goals(goal_data):
    """
    Generate recommendations for multiple goals.

    Expected input:

        {
            "marriage": {
                "years": 5
            },

            "car": {
                "years": 4
            },

            "home": {
                "years": 10
            }
        }
    """

    recommendations = {}

    for goal, data in goal_data.items():

        years = data["years"]

        recommendation = recommend_category(
            years
        )

        recommendations[goal] = {
            "years": years,
            "category":
                recommendation["category"],
            "description":
                recommendation["description"]
        }

    return recommendations


# ==========================================
# TEST
# ==========================================

if __name__ == "__main__":

    example_goals = {

        "marriage": {
            "years": 5
        },

        "car": {
            "years": 4
        },

        "home": {
            "years": 10
        }
    }

    recommendations = recommend_for_goals(
        example_goals
    )

    print("\n==========================================")
    print("INVESTMENT CATEGORY RECOMMENDATION")
    print("==========================================")

    for goal, data in recommendations.items():

        print(f"\n{goal.upper()}")

        print(
            f"Timeline: "
            f"{data['years']} years"
        )

        print(
            f"Category: "
            f"{data['category']}"
        )

        print(
            f"Approach: "
            f"{data['description']}"
        )

    print("\n------------------------------------------")

    print(
        "NOTE: These are broad educational "
        "categories, not financial advice."
    )