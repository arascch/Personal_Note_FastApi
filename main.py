from sqlmodel import Session
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