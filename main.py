from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from financial_agent import generate_financial_plan

app = FastAPI(
    title="Financial Dream Planner",
    description="AI-powered financial goal planning system",
    version="1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class FinancialRequest(BaseModel):

    age: int
    city: str
    area_type: str
    education: str
    job_role: str
    current_salary: float
    saving_percentage: float

    marriage_years: int | None = None
    car_years: int | None = None
    home_years: int | None = None


@app.get("/")
def home():

    return {
        "message": "Financial Dream Planner API is running"
    }


@app.post("/financial-plan")
def financial_plan(request: FinancialRequest):

    result = generate_financial_plan(
        age=request.age,
        city=request.city,
        area_type=request.area_type,
        education=request.education,
        job_role=request.job_role,
        salary=request.current_salary,
        saving_percentage=request.saving_percentage,
        marriage_years=request.marriage_years,
        car_years=request.car_years,
        home_years=request.home_years
    )

    return result