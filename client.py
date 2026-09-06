import requests


# ==========================================
# CONFIGURATION
# ==========================================

API_URL = "http://127.0.0.1:8000/financial-plan"


# ==========================================
# GET USER INPUT
# ==========================================

print("\n==========================================")
print("       FINANCIAL DREAM PLANNER")
print("==========================================")

print("\nEnter your personal information")
print("------------------------------------------")

age = int(input("Age: "))

city = input("City: ")

area_type = input(
    "Area Type (Central/Suburban/Peripheral): "
)

education = input(
    "Education (B.Tech/M.Tech/MBA/etc.): "
)

job_role = input(
    "Job Role (Software Engineer/Data Scientist/etc.): "
)

current_salary = float(
    input("Current Monthly Salary (₹): ")
)

saving_percentage = float(
    input("Percentage of salary you want to save (%): ")
)


# ==========================================
# GOAL INPUTS
# ==========================================

print("\nEnter your financial goal timelines")
print("------------------------------------------")

print(
    "Enter 0 if you do not want to include "
    "a particular goal."
)

marriage_years = int(
    input("Marriage goal in how many years: ")
)

car_years = int(
    input("Car goal in how many years: ")
)

home_years = int(
    input("Home goal in how many years: ")
)


# ==========================================
# PREPARE REQUEST
# ==========================================

data = {

    "age": age,

    "city": city,

    "area_type": area_type,

    "education": education,

    "job_role": job_role,

    "current_salary": current_salary,

    "saving_percentage": saving_percentage,

    "marriage_years":
        marriage_years if marriage_years > 0 else None,

    "car_years":
        car_years if car_years > 0 else None,

    "home_years":
        home_years if home_years > 0 else None
}


# ==========================================
# SEND REQUEST TO FASTAPI
# ==========================================

try:

    response = requests.post(
        API_URL,
        json=data
    )

    # Check whether API returned successfully
    response.raise_for_status()

    result = response.json()


# ==========================================
# HANDLE ERRORS
# ==========================================

except requests.exceptions.ConnectionError:

    print("\nERROR: Could not connect to the API.")

    print(
        "Make sure the FastAPI server is running."
    )

    exit()


except requests.exceptions.HTTPError:

    print("\nERROR: The API returned an error.")

    print(
        f"Status Code: {response.status_code}"
    )

    print(
        response.text
    )

    exit()


# ==========================================
# DISPLAY RESULT
# ==========================================

print("\n==========================================")
print("       FINANCIAL PLAN GENERATED")
print("==========================================")

print("\nYour financial plan has been generated.")

print("\n------------------------------------------")
print("RAW API RESPONSE")
print("------------------------------------------")

print(result)