import fire
from sklearn.neighbors import KNeighborsClassifier
from fishmlserv.model.manager import get_model_path
import pickle

def prediction(length: float, weight: float):
    
    model_path=get_model_path()
    
    with open(model_path, 'rb') as f:
        fish_model=pickle.load(f)
    
    data=[[length, weight]]
    
    prediction=fish_model.predict(data)
    
    mapping={0: '빙어', 1: '도미'}
    
    mapped_prediction=mapping[prediction[0]]
    
    return mapped_prediction

def main():
    fire.Fire(prediction)
