from typing import Annotated
from pydantic import UUID4, BaseModel, Field
from datetime import datetime

class BaseSchema(BaseModel):
    class Config:
        extra = 'forbid'
        from_attributes = True

class OutMixin(BaseSchema):
    id: Annotated[UUID4, Field(description='Identificador')]
    created_ate: Annotated[datetime, Field(description='Data de criação')]