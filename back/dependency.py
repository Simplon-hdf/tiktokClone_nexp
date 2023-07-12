from jose import jwt
from jose.exceptions import JOSEError
from fastapi import HTTPException, Depends, Security
from fastapi.security.api_key import APIKeyHeader
from dotenv import load_dotenv
import os

from pydantic import BaseModel

load_dotenv()

token_key = APIKeyHeader(name="Autorization")

class Token(BaseModel):
    token: str

def get_current_token(auth_key: str = Security(token_key)):
    return auth_key    

async def has_access(current_token: Token = Depends(get_current_token)):
    token = current_token.split()[1]

    try:
        jwt.decode(token, key = os.getenv("SECRET_KEY"), algorithms=["HS256"])
    except JOSEError as e:
        raise HTTPException(status_code = 401, detail = str(e))
