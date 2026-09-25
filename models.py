from sqlmodel import SQLModel , Field
from datetime import datetime

class User(SQLModel , table = True):
    id : int |None = Field(default=None , primary_key=True)
    username: str
    hashed_password: str
    privilege : str = "user"

class Note(SQLModel , table = True):
    id:int |None=Field(default=None , primary_key=True)
    title : str
    content: str
    is_important : bool = False
    created_at :datetime= Field(default_factory=datetime.now)
    user_id : int= Field(foreign_key="user.id")