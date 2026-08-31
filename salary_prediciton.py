import joblib


# ==========================================
# 1. LOAD TRAINED MODEL
# ==========================================

MODEL_PATH = "best_salary_model.pkl"

model = joblib.load(MODEL_PATH)


# ==========================================
# 2. SALARY PREDICTION FUNCTION
# ==========================================

def predict_salary(age, city, education, job_role):

    user_data = {
        "Age": [age],
        "City": [city],
        "Education": [education],
        "Job_Role": [job_role]
    }

    salary = model.predict(
        __import__("pandas").DataFrame(user_data)
    )[0]

    return round(float(salary), 2)


# ==========================================
# 3. TEST THE MODEL
# ==========================================

if __name__ == "__main__":

    salary = predict_salary(
        age=22,
        city="Bangalore",
        education="B.Tech",
        job_role="Software Engineer"
    )

    print("\n===================================")
    print("SALARY PREDICTION")
    print("===================================")

    print(f"Predicted Monthly Salary: ₹{salary:,.2f}")