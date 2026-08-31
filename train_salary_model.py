import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline

from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor

from sklearn.metrics import mean_absolute_error, r2_score


# ==========================================
# 1. LOAD DATASET
# ==========================================

DATA_PATH = "Data/salary_data.csv"

df = pd.read_csv(DATA_PATH)

print("\nDataset loaded successfully!")
print("Dataset shape:", df.shape)

# Remove unnecessary columns
df = df.drop(columns=["Unnamed: 5"], errors="ignore")


# ==========================================
# 2. DISPLAY DATASET INFORMATION
# ==========================================

print("\nDataset columns:")
print(df.columns.tolist())

print("\nFirst 5 rows:")
print(df.head())


# ==========================================
# 3. DEFINE FEATURES AND TARGET
# ==========================================

X = df.drop(columns=["Monthly_Salary"])
y = df["Monthly_Salary"]


# ==========================================
# 4. DEFINE CATEGORICAL COLUMNS
# ==========================================

categorical_columns = [
    "City",
    "Education",
    "Job_Role"
]

numeric_columns = [
    "Age"
]


# ==========================================
# 5. PREPROCESSING
# ==========================================

preprocessor = ColumnTransformer(
    transformers=[
        (
            "categorical",
            OneHotEncoder(handle_unknown="ignore"),
            categorical_columns
        ),
        (
            "numeric",
            "passthrough",
            numeric_columns
        )
    ]
)


# ==========================================
# 6. DEFINE MODELS
# ==========================================

models = {
    "Linear Regression": LinearRegression(),

    "Decision Tree": DecisionTreeRegressor(
        random_state=42
    ),

    "Random Forest": RandomForestRegressor(
        n_estimators=100,
        random_state=42
    )
}


# ==========================================
# 7. TRAIN-TEST SPLIT
# ==========================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)


# ==========================================
# 8. TRAIN AND COMPARE MODELS
# ==========================================

results = {}

print("\n==========================================")
print("MODEL COMPARISON")
print("==========================================")

for name, model in models.items():

    pipeline = Pipeline(
        steps=[
            ("preprocessor", preprocessor),
            ("model", model)
        ]
    )

    # Train model
    pipeline.fit(X_train, y_train)

    # Predict
    predictions = pipeline.predict(X_test)

    # Evaluation
    mae = mean_absolute_error(y_test, predictions)
    r2 = r2_score(y_test, predictions)

    results[name] = {
        "model": pipeline,
        "MAE": mae,
        "R2": r2
    }

    print(f"\n{name}")
    print(f"MAE : ₹{mae:,.2f}")
    print(f"R²  : {r2:.4f}")


# ==========================================
# 9. SELECT BEST MODEL
# ==========================================

# Higher R² is better.
# If R² values are close, lower MAE is preferred.

best_model_name = max(
    results,
    key=lambda name: (
        results[name]["R2"],
        -results[name]["MAE"]
    )
)

best_model = results[best_model_name]["model"]


print("\n==========================================")
print("BEST MODEL")
print("==========================================")

print("Selected model:", best_model_name)
print(f"MAE: ₹{results[best_model_name]['MAE']:,.2f}")
print(f"R² : {results[best_model_name]['R2']:.4f}")


# ==========================================
# 10. SAVE BEST MODEL
# ==========================================

MODEL_PATH = "best_salary_model.pkl"

joblib.dump(
    best_model,
    MODEL_PATH
)

print("\nBest model saved successfully!")
print("File:", MODEL_PATH)