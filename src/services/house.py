import xgboost as xgb
import pandas as pd
from typing import List

# XGBRegressor 모델을 불러온다.
loaded_model = xgb.XGBRegressor()

# colab에서 학습시킨 모델의 가중치 파일을 불러와서 모델에 적용시킨다.
loaded_model.load_model('src/models/xgb_model.json')

async def runModel(crim : float, rm : float) -> float: 
  #->에 쓰여있는게 return type이 어떤 자료형인지를 미리 선언해줌.
  # 미리 준비된 input 데이터(임시). 나중에는 Http Request에 담아서 보낼 것이다.
    dic = {
        "CRIM": [crim],#criminal 변수 선언
        "ZN": [18.0],
        "INDUS": [22.37],
        "CHAS": [0],
        "NOX": [0.145],
        "RM": [rm],#방의 개수 변수 선언
        "AGE": [66.7],
        "DIS": [4.291],
        "RAD": [13],
        "TAX": [333.333],
        "PTRATIO": [21.0],
        "B": [197.6],
        "LSTAT": [23.4],
    }

    # dictionary 형태를 DataFrame 형태로 변환한다.
    input = pd.DataFrame.from_dict(dic, orient='columns')

    # input 값을 이용해서 예측값을 만들고, z에 대입한다.  
    z = loaded_model.predict(input)

    # 변수 z의 타입이 numpy이기 때문에 list로 바꿔준다.
    result: List[float] = z.tolist() #json파일은 list만 받음

    return result[0] 