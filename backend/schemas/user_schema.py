from pydantic import BaseModel

class UserRegister(BaseModel):
    name: str
    phone: str
    email: str
    password: str
    vehicle_type: str
    platform: str

class UserLogin(BaseModel):
    email: str
    password: str