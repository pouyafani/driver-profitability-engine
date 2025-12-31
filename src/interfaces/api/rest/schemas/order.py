from pydantic import BaseModel, conint
from uuid import UUID
from typing import Literal

class CreateOrderRequest(BaseModel):
    customer_id: UUID
    quantity: conint(gt=0, le=1000)
    currency: Literal["EUR", "USD"]

    class Config:
        extra = "forbid"

