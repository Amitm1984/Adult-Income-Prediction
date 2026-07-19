import joblib
import pandas as pd
from fastapi import FastAPI
from fastapi.responses import FileResponse
from schema import AdultIncome


app = FastAPI(
     title = "Adult income prediction API",
    description = "Predicts the income if it is <=50K or >50K from preprocessing and logistic regression",
    version='1.0.0'
)

model = joblib.load("model/adult_salary_pipeline.joblib")
    
@app.get("/")
def home():
    return FileResponse("static/index.html")


@app.get("/health")
def health():
    return{"status":"okk"}
   
@app.post("/predict")
def predict(adult:AdultIncome):
    data = pd.DataFrame([adult.model_dump()])
    prediction = int(model.predict(data)[0])
    confidence = float(model.predict_proba(data)[0][prediction])
    label = ">50K" if prediction == 1 else "<=50K"
    return {"prediction":prediction,"label":label,"confidence":round(confidence,3)}
