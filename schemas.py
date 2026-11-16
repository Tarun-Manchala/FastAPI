from pydantic import BaseModel, Field, ConfigDict,EmailStr, constr
from datetime import datetime

class UserBase(BaseModel):
    username: str = Field(min_length=1, max_length=50, description="The username of the user")
    email: EmailStr = Field(max_length=120, description="The email address of the user")

class UserCreate(UserBase):
    password : str = Field(min_length=8, max_length=24)

class UserPublic(BaseModel):
    model_config = ConfigDict(
        from_attributes=True,
    )
    id: int
    username: str
    image_file: str | None
    image_path: str

class UserPrivate(UserPublic):
    email:EmailStr

class UserUpdate(BaseModel):
    username: str | None = Field(default=None, min_length=1, max_length=50, description="The username of the user")
    email: EmailStr | None = Field(default=None, max_length=120, description="The email address of the user")
    image_file:str | None  = Field(default=None, minlength=1, max_length=200)
 
class Token(BaseModel):
    access_token : str
    token_type : str

class PostBase(BaseModel):
   
    title: str = Field(min_length=1, max_length=100, description="The title of the post")
    content: str = Field(min_length=1, max_length=1000, description="The content of the post")

    # published: bool = Field(default=True, description="Whether the post is published or not")

class PostCreate(PostBase):
    pass

class PostUpdate(BaseModel):
    title: str | None = Field(default=None, min_length=1, max_length=100)
    content: str | None=Field(default=None,min_length=1,max_length=1000)

class PostResponse(PostBase):
    model_config = ConfigDict(
        from_attributes=True,
    )
    id: int = Field(description="The unique identifier of the post")
    user_id : int
    date_posted: datetime
    author: UserPublic

