# 간단한 홈페이지 제공
# 1. module 가져오기
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

# 2. Fastapi 객체 생성, 전역변수 생성
app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# 3. 라우팅 구성/정의
@app.get("/")
def home(req:Request):
    # 홈페이지 요청
    # -> index.html을 읽어서 req 데이터를 전달하여 동적 html 구성
    # -> 응답 (return) -> 클라이언트 브라우저에게 전달 -> 랜더링, Dom Tree
    # -> 브라우저 해석 화면에 그리기 -> 클라이언트는 응답결과를 화면에서 볼 수 있다.
    # return templates.TemplateResponse("index.html", {"request": req})
    return templates.TemplateResponse(
        request=req, 
        name="index.html"
    )

# 2. index.html 직접 요청
@app.get("/index.html")
def index_page(req: Request):
    return templates.TemplateResponse(
        request=req, 
        name="index.html"
    )

# 3. index2.html 요청
@app.get("/index2.html")
def index2_page(req: Request):
    return templates.TemplateResponse(
        request=req, 
        name="index2.html"
    )

# 4. index3.html 요청
@app.get("/index3.html")
def index3_page(req: Request):
    return templates.TemplateResponse(
        request=req, 
        name="index3.html"
    )


@app.get("/auth/login")
def login(req: Request):
    return templates.TemplateResponse(
        request=req, 
        name="login.html"
    )

'''
# 동적으로도 가능
@app.get("/{page_name}.html")
def render_page(page_name: str, req: Request):
    # /index2.html 요청 시 templates/index2.html 렌더링
    return templates.TemplateResponse(
        request=req,
        name=f"{page_name}.html"
    )
'''