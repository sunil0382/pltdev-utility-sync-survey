from pydantic import BaseModel, Field, UUID4
from typing import Optional
from datetime import datetime


class UtilityServiceRequestSchema(BaseModel):
    utility_number: str = Field(
        ...,
        max_length=70,
        description="Unique utility number",
        example="UNAD-00000000212240",
    )
    account_number: int = Field(
        ...,
        description="Account number associated with the request",
        example=1234567890,
    )
    region: str = Field(
        ...,
        max_length=20,
        description="Region where the request was made",
        example="East",
    )
    status: int = Field(
        ...,
        description="Status ID representing the current status of the request",
        example=2,
    )
    slug: UUID4 = Field(
        ...,
        description="Unique UUID for the request",
        example="f47ac10b-58cc-4372-a567-0e02b2c3d479",
    )
    customer: object = Field(
        ..., description="Customer ID associated with the request", example=1001
    )
    premise: int = Field(
        ..., description="Premise ID where the service is requested", example=2001
    )
    created_at: Optional[datetime] = Field(
        None,
        description="Timestamp when it was created",
        example="2024-10-07T10:20:30Z",
    )
    updated_at: Optional[datetime] = Field(
        None,
        description="Timestamp when it was updated",
        example="2024-10-07T12:20:30Z",
    )

    class Config:
        orm_mode = True  # Enables Pydantic to work with ORM models
