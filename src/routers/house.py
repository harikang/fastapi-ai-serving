from fastapi import APIRouter
from src.services.house import runModel
#길을 붙여주는 예를 house_router랑 router 변수를 담을거다. 
house_router = router = APIRouter() #router와 house_router라는 
#나의 경로를 지정할 것이다. 
#house라는 변수에 
#house/price/predict로 get 요청이 들어오면 실행
@router.get('/price/predict')
async def get_prediction_of_house_price(crim:float, rm : float):
    price = await runModel(crim, rm) #async와 await를 같이 써야함. 
    return price