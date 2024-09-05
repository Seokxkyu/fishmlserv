from typing import Union
from fastapi import FastAPI
import fire 
import pickle

app = FastAPI()

from fishmlserv.model.manager import get_model_path, run_prediction

model = get_model_path()
### 모델 불러오기

with open(model, "rb") as f:
    fish_model = pickle.load(f)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/fish")
def fish(length: float, weight: float):
    """
    물고기 종류 판별기
    
    Args:
        length (float): 물고기 길이 (cm)
        weight (float): 물고기 무게 (g)

    Returns:
        dict: 물고기 종류를 담은 딕셔너리
    """
    prediction = fish_model.predict([[length, weight]])

    fish_class = "빙어"
    
    if prediction[0] == 1:
        fish_class = "도미"

    return {
                "prediction": fish_class,
                "length": length,
                "weight": weight
            }

