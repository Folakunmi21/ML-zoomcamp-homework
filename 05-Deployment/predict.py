
import pickle
from fastapi import FastAPI
import uvicorn
from typing import Dict, Any
from pydantic import BaseModel

class Client(BaseModel):
    lead_source: str
    number_of_courses_viewed: int
    annual_income: float

app = FastAPI(title="client_score_prediction")

#loading the model
with open('pipeline_v1.bin', 'rb') as f_in:
    pipeline = pickle.load(f_in)

#request
def predict_single(client:  Dict[str, Any]):
    result = pipeline.predict_proba([client]) [0,1]
    return float(result)
    
#reponse
@app.post("/client_score")
def predict(client:  Client):
    prob = predict_single(client.dict())

    return{
        "convert_probability": prob,
        "convert": bool(prob >= 0.5)
    }


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9696)
