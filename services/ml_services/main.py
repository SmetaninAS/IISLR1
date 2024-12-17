import random
from fastapi import FastAPI
from api_handler import FastAPIHandler
from prometheus_fastapi_instrumentator import Instrumentator
from prometheus_client import Histogram, Gauge, Counter, Summary

app = FastAPI()
app.handler = FastAPIHandler()

@app.get('/')
def root_dir():
    return({'Hello': 'world'})

instrumentator = Instrumentator()
instrumentator.instrument(app).expose(app)

prediction_metric = Histogram(
    'prediction_metric_histogram',
    'histogram of predicted prices',
    buckets=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
)

@app.post('/api/prediction')
def make_prediction(car_id: int, item_features: dict):
    prediction = app.handler.predict(item_features)

    prediction_metric.observe(prediction)
    return ({
             'price': prediction,
             'car_id': car_id
            })