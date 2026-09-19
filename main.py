from sqlmodel import Session , select
from fastapi.responses import RedirectResponse
from models import User , Note
from fastapi import FastAPI , Request , Form
from database import engine
from fastapi.templating import Jinja2Templates 


app = FastAPI()

templates = Jinja2Templates(directory="templates")

def make_hash(password:str):
    return password + "scrambled!"


@app.post("/register")
def register(username: str=Form(...) , password: str=Form(...)):
    scrambled = make_hash(password)
    new_user = User(username = username , hashed_password = scrambled)
    with Session(engine) as session:
        session.add(new_user)
        session.commit()

    return RedirectResponse(url="/login",status_code=303)

@app.get("/register")
def show_register_page(request: Request):
    return templates.TemplateResponse(name="register.html", request=request)

@app.get("/login")
def show_login_page(request:Request):
    return templates.TemplateResponse(name = "login.html" , request=request)

@app.post("/login")
def login(username:str=Form(...) , password:str=Form(...)):
    with Session(engine) as session:
        statement = select(User).where(User.username == username)
        db_user = session.exec(statement).first()

        scrambled_attempt = make_hash(password)
        if db_user and db_user.hashed_password == scrambled_attempt:
            return {"message":"login sucessful!"}
        else:
            return {"error":"Invalid username or password"}
    