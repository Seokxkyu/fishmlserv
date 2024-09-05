
def get_model_path():
    import os
    
    this_path = os.path.abspath(__file__)
    dir_name = os.path.dirname(this_path)
    # model_name = f'{dir_name}/model.pkl'
    model_name = dir_name + "/model.pkl"

    return model_name

    # 사용 fastapi main.py에서 아래와 같이 사용
    # from fishmlserv.model.manager import get_model_path

def load_model(k=5):
    global fish_model
    global k_val
    if (fish_model is None) | (kval != k):
        model_path = get_model_path(k)
        with open(model_path, "rb") as f:
            fish_model = pickle.load(f)

    k_val = k
    return fish_model

def run_prediction(l: float, w: float, k=5, mean=[27.055102040816323, 444.50000000000017], std=[10.137746423175521, 324.77757223763376]):
    """
    주어진 물고기의 길이(l)와 무게(w)를 기반으로 해당 물고기의 종류를 예측하는 함수.

    Args:
        l (float): 물고기의 길이.
        w (float): 물고기의 무게.
        k (int): 근접 이웃 상수

    Returns:
        str: 예측된 물고기의 종류로, '도미' 또는 '빙어' 중 하나를 반환.

    동작:
    1. 사전 학습된 모델의 경로를 가져온다.
    2. 해당 경로에서 모델을 불러온다.
    3. 불러온 모델을 사용하여 주어진 길이와 무게에 대해 예측을 수행한다.
    4. 예측 결과에 따라 '도미' 또는 '빙어'를 반환한다.
    """
    m = load_model(k)

    data = np.array([l, w])
    data_scaled =  (data - mean) / std
    p = m.predict([data_scaled])

    if p[0] == 1:
        fish_class = "도미"
    else:
        fish_class = "빙어"

    return fish_class
