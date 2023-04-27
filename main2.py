import uvicorn
import numpy as np
import pandas as pd
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from utils.ml_model import CreditScoreClassifier


# Instantiate the FastAPI app and Jinja2 templates
app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Load the data
data = pd.read_csv('clean_data.csv')

# Create an instance of the classifier
csc = CreditScoreClassifier(data)
csc.select_samples()
csc.train_model()

# create a function to map the values
def map_rating(value):
    if value == 1:
        return 'Poor'
    elif value == 2:
        return 'Standard'
    elif value == 3:
        return 'Good'
    else:
        return 'Unknown'

# Define the input schema
class InputData(BaseModel):
    Age: int
    Monthly_Inhand_Salary: int
    Num_Bank_Accounts: str
    Num_Credit_Card: str
    Interest_Rate: int
    Delay_from_due_date: int
    Num_of_Delayed_Payment: int
    Changed_Credit_Limit: int
    Num_Credit_Inquiries: str
    Credit_Mix: str
    Outstanding_Debt: int
    Credit_Utilization_Ratio: int
    Credit_History_Age: int
    Total_EMI_per_month: int
    Amount_invested_monthly: int
    Monthly_Balance:int
    Occupation: str
    Num_of_Loan: int
    Payment_of_Min_Amount:int
    Payment_Behaviour:int

# Define the home page route
@app.get("/")
async def read_form(request: Request):
    return templates.TemplateResponse("home.html", {"request": request, "hello_world": True})


@app.post("/", response_class=HTMLResponse)
async def home( request: Request,
                Age:int = Form(...),
                Monthly_Inhand_Salary: int = Form(...),
                Num_Bank_Accounts: str = Form(...),
                Num_Credit_Card: str = Form(...),
                Interest_Rate: int = Form(...),
                Delay_from_due_date: int = Form(...),
                Num_of_Delayed_Payment: int = Form(...),
                Changed_Credit_Limit: int = Form(...),
                Num_Credit_Inquiries: str = Form(...),
                Credit_Mix: str = Form(...),
                Outstanding_Debt: int = Form(...),
                Credit_Utilization_Ratio: int = Form(...),
                Credit_History_Age: int = Form(...),
                Total_EMI_per_month: int = Form(...),
                Amount_invested_monthly: int = Form(...),
                Monthly_Balance:int = Form(...),
                Num_of_Loan:int = Form(...),
                Payment_of_Min_Amount:int = Form(...),
                Payment_Behaviour:int = Form(...),
                Occupation: str = Form(...)):
    
    user_info = InputData(Age=Age,
                          Monthly_Inhand_Salary=Monthly_Inhand_Salary,
                           Num_Bank_Accounts=Num_Bank_Accounts,
                          Num_Credit_Card=Num_Credit_Card,
                          Interest_Rate=Interest_Rate,
                          Delay_from_due_date=Delay_from_due_date,
                          Num_of_Delayed_Payment=Num_of_Delayed_Payment,
                          Changed_Credit_Limit=Changed_Credit_Limit,
                          Num_Credit_Inquiries=Num_Credit_Inquiries,
                          Credit_Mix=Credit_Mix,
                          Outstanding_Debt=Outstanding_Debt,
                          Credit_Utilization_Ratio=Credit_Utilization_Ratio,
                          Credit_History_Age=Credit_History_Age,
                          Total_EMI_per_month=Total_EMI_per_month,
                          Amount_invested_monthly=Amount_invested_monthly,
                          Monthly_Balance=Monthly_Balance,
                          Num_of_Loan=Num_of_Loan,
                          Payment_of_Min_Amount=Payment_of_Min_Amount,
                          Payment_Behaviour=Payment_Behaviour,
                          Occupation=Occupation)