from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
from src.connection import query

app = FastAPI()


class User(BaseModel):
    """User BaseModel"""
    USER_ID: int
    FIRST_NAME: Union[str, None] = None
    LAST_NAME: Union[str, None] = None


@app.get("/users")
def get_users():
    results: User = query('SELECT * FROM users WHERE FIRST_NAME = %s OR LAST_NAME = %s', ['ANDREW', 'LI'])
    print(results)    
    return results