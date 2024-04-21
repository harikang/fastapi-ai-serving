from fastapi import FastAPI
from src.routers.house import house_router
app = FastAPI()
#fastapi함수를 실행시키면, 
#fastapi서버가 열리는데 그 서버를 app이라는 변수에 담겠다.

#app이라는 서버를 길을 붙여서 다른 py파일을 실행하도록
#라우터를 붙여줄 수 있음
app.include_router(house_router,prefix = "/house")
#house라는 경로를 타면 house_router로 길을 연결해줌. 
#원하는 resource단위로 pre_fix를 선언.
#prefix는 경로만 지정하는 것.
#app이랑 house_router를 연결하게 됨 .app-house_router
#만약에 여러개의 길을 붙이고 싶으면,
#app.include_router(user,prefix="/use")
@app.get("/") #@는 데코레이터라고 부른다. 
#백엔드는 이런 @패턴을 많이 사용함. 
#서버 : 서비스를 제공하는 컴퓨터 
#클라이언트가 get이라는 서비스를 request get으로 요청 
#함수나 클래스, 변수들을 꾸며주는 역할
#get = read , post = create, put = update, delete (= delete), patch( =update) 
async def root():
    return {"message": "Hello World"}

@app.get("/user")
async def getUser():
    arr = [1,2,3]
    arr.pop()
    return arr