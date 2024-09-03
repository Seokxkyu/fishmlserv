import fire
from sklearn.neighbors import KNeighborsClassifier
from fishmlserv.model.manager import get_model_path
import pickle

def prediction(l: float, w: float):
    """
    주어진 물고기의 길이(l)와 무게(w)를 기반으로 해당 물고기의 종류를 예측하는 함수.

    Args:
        l (float): 물고기의 길이.
        w (float): 물고기의 무게.

    Returns:
        str: 예측된 물고기의 종류로, '도미' 또는 '빙어' 중 하나를 반환.

    동작:
    1. 사전 학습된 모델의 경로를 가져온다.
    2. 해당 경로에서 모델을 불러온다.
    3. 불러온 모델을 사용하여 주어진 길이와 무게에 대해 예측을 수행한다.
    4. 예측 결과에 따라 '도미' 또는 '빙어'를 반환한다.
    """
    model_path=get_model_path()
    
    with open(model_path, 'rb') as f:
        fish_model=pickle.load(f)
    
    data=[[l, w]]
    
    prediction=fish_model.predict(data)
    mapping={0: '빙어', 1: '도미'}
    
    mapped_prediction=mapping[prediction[0]]
    return mapped_prediction

def main():
    fire.Fire(prediction)

