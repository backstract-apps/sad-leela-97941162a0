from pydantic import BaseModel,Field,field_validator

import datetime

import uuid

from typing import Any, Dict, List,Optional,Tuple,Union

import re

class MaysonPlatformAuth(BaseModel):
    email: Optional[str]=None
    password: Optional[str]=None
    is_verified: Optional[str]=None
    created_at: Optional[datetime.time]=None


class ReadMaysonPlatformAuth(BaseModel):
    email: Optional[str]=None
    password: Optional[str]=None
    is_verified: Optional[str]=None
    created_at: Optional[datetime.time]=None
    class Config:
        from_attributes = True


class MaysonPlatformAuthOtp(BaseModel):
    email: Optional[str]=None
    otp: Optional[str]=None
    validity: Optional[str]=None
    created_at: Optional[datetime.time]=None


class ReadMaysonPlatformAuthOtp(BaseModel):
    email: Optional[str]=None
    otp: Optional[str]=None
    validity: Optional[str]=None
    created_at: Optional[datetime.time]=None
    class Config:
        from_attributes = True


class Users(BaseModel):
    email: str
    password: str
    phone: Optional[str]=None
    created_at: Optional[datetime.time]=None


class ReadUsers(BaseModel):
    email: str
    password: str
    phone: Optional[str]=None
    created_at: Optional[datetime.time]=None
    class Config:
        from_attributes = True




class PostUsers(BaseModel):
    email: str = Field(..., max_length=100)
    password: str = Field(..., max_length=100)
    phone: Optional[str]=None
    created_at: Optional[Any]=None

    class Config:
        from_attributes = True



class PutUsersUserId(BaseModel):
    user_id: Union[int, float] = Field(...)
    email: str = Field(..., max_length=100)
    password: str = Field(..., max_length=100)
    phone: Optional[str]=None
    created_at: Optional[Any]=None

    class Config:
        from_attributes = True



# Query Parameter Validation Schemas

class GetUsersUserIdQueryParams(BaseModel):
    """Query parameter validation for get_users_user_id"""
    user_id: int = Field(..., ge=1, description="User Id")

    class Config:
        populate_by_name = True


class DeleteUsersUserIdQueryParams(BaseModel):
    """Query parameter validation for delete_users_user_id"""
    user_id: int = Field(..., ge=1, description="User Id")

    class Config:
        populate_by_name = True
