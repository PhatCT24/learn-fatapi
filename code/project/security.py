from typing import Annotated

from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

class User(BaseModel):
    username : str
    email: str | None = None
    full_name: str | None = None 
    disabled: bool | None = None 

def decode_token(token):
    return User(
        username = token + "fakedecoded", email = "fat@gmail.com", full_name = "John Doe"
    )

async def get_User(token: Annotated[str, Depends(oauth2_scheme)]):
    user = decode_token(token)
    return user

@app.get("/users/me")
async def read_user(current_user: Annotated[User, Depends(get_User)]):
    return current_user