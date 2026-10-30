from pydantic import BaseModel, Field
from typing import Literal

class TicketCreate(BaseModel):
    customer_id: int = Field(gt=0)
    subject: str = Field(min_length=5, max_length=100)
    description: str = Field(min_length=10, max_length=1000)
    service_type: Literal["mobile","broadband","dth"] = Field(description="Type of service for the ticket")
