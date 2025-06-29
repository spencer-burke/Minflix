from sqlmodel import Field, SQLModel, Relationship
from typing import List, Optional

class Film(SQLModel, table=True):
    """
        Data model for the films

        Attributes:
            id (Optional[int]): the film id
            title (str): title of the film
            length (int): length of the film
            image_name (str): the name of the film image
            file_name (str): the name of the film video
            producer (str): the producer of the film
            name (Optional[str]): name for backwards compatibility
    """
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    length: int
    image_name: str
    file_name: str
    producer: str
    name: str