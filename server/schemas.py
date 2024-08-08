from pydantic import BaseModel, field_validator

class User(BaseModel):
    username: str
    email: str
    disabled: bool = None

    @field_validator("username")
    def validate_username(cls, v):
        if len(v) < 3:
            raise ValueError("Username must be at least 3 characters long")
        return v