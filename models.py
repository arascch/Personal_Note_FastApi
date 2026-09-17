from sqlmodel import SQLModel , Field

class User(SQLModel , table = True):
    id : int |None = Field(default=None , primary_key=True)
    username: str
    hashed_password: str
    privilege : str = "user"
