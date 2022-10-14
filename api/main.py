# HOWTO: uvicorn app.main:app --host 0.0.0.0 --port 5002 --reload
from fastapi import FastAPI, Request
from fastapi.exceptions import HTTPException
from fastapi.middleware.cors import CORSMiddleware
from . import payload
from . import loading_data as ld 
from pydantic import BaseModel
import pandas as pd
import numpy as np

CORS_CONFIG = {
    "allow_origins": ["*"],
    "allow_methods": ["*"],
    "allow_headers": ["*"],
    "allow_credentials": True,
}
app = FastAPI(
    title="Clicks Prediction API",
    description="""Predict Number of clicks using post Data""",
    version="0.1.0")

app.add_middleware(CORSMiddleware, **CORS_CONFIG)

@app.get("/")
def read_root():
    """
    Root endpoint to test if the server is running. Returns a simple message.
    """
    return {"Status": "Online"}

class Item(BaseModel):
    min_booking_duration:float 
    rooms:int
    deposit:float
    area:float
    price: float = 1.0
    number_of_pics:int
    cleaning_fee:float
    district:str
    first_pic_category:str

@app.post("/clicks")
def get_number_of_clicks(item: Item):
    output = payload.PAYLOAD
    try:
        item.district = ld.district_mapping[item.district]
        output["district_popularity"] = item.district
    except: 
        raise HTTPException(400, f"Unsupported district code")

    pic_category = item.first_pic_category
    if f"first_pic_category_{pic_category}" in output.keys():
        output[f"first_pic_category_{pic_category}"] = 1

    for key in dict(item).keys():
        output[key] = dict(item)[key]
    
    output["deposit_ratio"] = output["deposit"]/output["price"]
    del output["first_pic_category"]
    del output["district"]

    prediction_row = pd.DataFrame(output, index=[0])
    # Using Same Scaler as in Training
    rescaledX = ld.MinMaxScaler.transform(prediction_row)
    X = pd.DataFrame(rescaledX, index=prediction_row.index, columns=prediction_row.columns)
    # Using the model to predict
    clicks = ld.model_xgb.predict(X)
    return {"clicks" : int(clicks[0])}
