from sqlmodel import Field, SQLModel
from typing import Optional
from datetime import datetime

class FilmUser(SQLModel, table=True):
    """
    The table for the users of the application

    Attributes:
        id (Optional[int]): the id of the film user
        username (str): the username of the user which is also the email
        password (str): the password of the user
        date_registered (datetime.datetime): the date the user was registered
    """
    id: Optional[int] = Field(default=None, primary_key=True)
    
    username: str
    password: str
    date_registered: datetime
