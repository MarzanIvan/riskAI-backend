from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# ----------------- Инвестиции ------------------
class InvestmentForm(BaseModel):
    f_Text: str
    f_Target: str
    f_Company: str
    f_Name: str
    f_Phone: str
    f_Mail: str

@app.post("/api/submit_investment/")
async def submit_investment(data: InvestmentForm):

    return 1

# ----------------- Страхование ------------------
class Policyholder(BaseModel):
    name: str
    age: str
    gender: str
    smoker: bool
    region: str
    history_of_claims: str
    previous_claims_amount: str

class InsurancePolicy(BaseModel):
    policy_id: str
    type: str
    coverage_amount: str
    premium: str
    start_date: str
    end_date: str

class UnderwritingData(BaseModel):
    number_of_claims_this_year: str
    days_between_policy_and_first_claim: str
    duplicate_contact_info_found: bool
    vin_suspect: bool
    claim_amount: str
    loss_ratio: str
    behavior_pattern: str

class FinancialMetrics(BaseModel):
    total_premium_collected: str
    total_claims_paid: str
    active_policies: str
    technical_reserves: str
    eligible_own_funds: str
    scr: str
    solvency_ratio: str
    financial_assets: str
    liabilities: str

class InsuranceForm(BaseModel):
    policyholder: Policyholder
    insurance_policy: InsurancePolicy
    underwriting_data: UnderwritingData
    financial_metrics: FinancialMetrics

@app.post("/api/insurance_form/")
async def submit_insurance_form(data: InsuranceForm):

    return 2

# ----------------- Кредитование ------------------
class CreditForm(BaseModel):
    fio: str
    passport: str
    income: float
    requested_amount: float
    term: int

@app.post("/api/credit_form/")
async def submit_credit_form(data: CreditForm):

    return 3

## to start uvicorn main:app --host 0.0.0.0 --port 8000