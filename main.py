import uvicorn
import numpy as np
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from utils.ml_model import CreditScoreClassifier


csc = CreditScoreClassifier('clean_data.csv')
csc.select_samples()
csc.train_model()
data=csc.data

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

# Instantiate the FastAPI app and Jinja2 templates
app = FastAPI()
templates = Jinja2Templates(directory="templates")

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
    
    user_info=InputData(Age=Age,
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
                        Occupation=Occupation
                        )
    data2=[  user_info.Age,
            user_info.Monthly_Inhand_Salary,
            int(user_info.Num_Bank_Accounts),
            int(user_info.Num_Credit_Card),
            user_info.Interest_Rate,
            user_info.Num_of_Loan,
            user_info.Delay_from_due_date,
            user_info.Num_of_Delayed_Payment,
            user_info.Changed_Credit_Limit,
            int(user_info.Num_Credit_Inquiries),
            int(user_info.Credit_Mix),
            user_info.Outstanding_Debt,
            user_info.Credit_Utilization_Ratio,
            user_info.Credit_History_Age,
            user_info.Payment_of_Min_Amount,
            user_info.Total_EMI_per_month,
            user_info.Amount_invested_monthly,
            user_info.Payment_Behaviour,
            user_info.Monthly_Balance,
            int(user_info.Occupation)]
    
    input_array = np.array(data2).reshape(1, -1)
    csc.predict(input_array)
    prediction=csc.pred[0]    
    if prediction==1:
        credit_score='Poor'
    elif prediction==2:
        credit_score='Standart'
    else:
        credit_score='Good'

    return templates.TemplateResponse("home.html", {"request": request,'credit_score':credit_score})

@app.post("/good", response_class=HTMLResponse)
async def button1(request: Request):
    good_customer=data[200:].sample(n=10)
    good_customer=good_customer.drop('Credit_Score', axis=1)
    csc.predict(good_customer)
    predictions=csc.pred
    good_customer = good_customer.astype(int)
    good_customer["Predictions"]=predictions
    good_customer["Predictions"]=good_customer['Predictions'].apply(map_rating)
    
    return templates.TemplateResponse("home.html", {"request": request, "df": good_customer,'good':'good'})

@app.post("/bad", response_class=HTMLResponse)
async def button1(request: Request):
    bad_customer=data[:100].sample(n=10)
    bad_customer=bad_customer.drop('Credit_Score', axis=1)
    csc.predict(bad_customer)
    predictions=csc.pred
    bad_customer = bad_customer.astype(int)
    bad_customer["Predictions"]=predictions
    bad_customer["Predictions"]=bad_customer['Predictions'].apply(map_rating)
    return templates.TemplateResponse("home.html", {"request": request, "df": bad_customer,'good':'good'})

@app.post("/standart", response_class=HTMLResponse)
async def button1(request: Request):
    standart_customer=data[100:200].sample(n=10)
    standart_customer=standart_customer.drop('Credit_Score', axis=1)
    csc.predict(standart_customer)
    predictions=csc.pred
    standart_customer = standart_customer.astype(int)
    standart_customer["Predictions"]=predictions
    standart_customer["Predictions"]=standart_customer['Predictions'].apply(map_rating) 
    return templates.TemplateResponse("home.html", {"request": request, "df": standart_customer,'good':'good'})


# Start the server
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
