import mlflow
import pickle as pkl

# Работаем с MLflow локально
TRACKING_SERVER_HOST = "127.0.0.1"
TRACKING_SERVER_PORT = 5002

registry_uri = f"http://{TRACKING_SERVER_HOST}:{TRACKING_SERVER_PORT}"
tracking_uri = f"http://{TRACKING_SERVER_HOST}:{TRACKING_SERVER_PORT}"

mlflow.set_tracking_uri(tracking_uri)   
mlflow.set_registry_uri(registry_uri)   

RUN_NAME = '4ed8272dd3ec41ec826347fabee01980'
loaded_model = mlflow.sklearn.load_model(f'runs:/{RUN_NAME}/models')

with open('model2.pkl', 'wb+') as f:
    pkl.dump(loaded_model, f)