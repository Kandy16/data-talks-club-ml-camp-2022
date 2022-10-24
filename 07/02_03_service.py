from lib2to3.pytree import Base
from logging.handlers import RotatingFileHandler
import numpy as np

import bentoml
from bentoml.io import JSON


from pydantic import BaseModel

class UserProfile(BaseModel):
    name:str
    age:int
    country:str
    rating:float

model_ref = bentoml.xgboost.get('credit_risk_model:2t6jamstuwz2rshc')
dv = model_ref.custom_objects['dictVectorizer']

model_runner = model_ref.to_runner()

svc = bentoml.Service('credit_card_classifier', runners=[model_runner])

@svc.api(input=JSON(pydantic_model=UserProfile), output=JSON())
def classify(app_data):
    vector = dv.transform(app_data.dict())
    prediction = model_runner.predict.run(vector)

    result = prediction[0]

    if result > 0.5:
        return {
            'status':'Declined'
        }
    else:
        return {
            'status':'Accepted'
        }

input = {
  "name": "Tim",
  "age": 37,
  "country": "US",
  "rating": 3.14
}
