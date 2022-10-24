from lib2to3.pytree import Base
from logging.handlers import RotatingFileHandler
import numpy as np

import bentoml
from bentoml.io import JSON, NumpyNdarray


from pydantic import BaseModel


#model_ref = bentoml.sklearn.get('mlzoomcamp_homework:qtzdz3slg6mwwdu5')
model_ref = bentoml.sklearn.get('mlzoomcamp_homework:jsi67fslz6txydu5')

model_runner = model_ref.to_runner()

svc = bentoml.Service('credit_card_classifier', runners=[model_runner])

@svc.api(input=NumpyNdarray(), output=NumpyNdarray())
def classify(app_data):
    result = model_runner.predict.run(app_data)
    print(result)
    return result