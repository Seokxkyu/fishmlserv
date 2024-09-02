
def get_model_path():
    import os
    
    dir_name = os.path.dirname(__file__)
    model_name = f'{dir_name}/model.pkl'
    

    return model_name

    # 사용 fastapi main.py에서 아래와 같이 사용
    # from fishmlserv.model.manager import get_model_path
