from pydantic import BaseModel, Field


class CustomerSchema(BaseModel):
    customer_id: int = Field(
        None, description="Unique ID of the customer", example=1001
    )
    first_name_en: str = Field(
        None, max_length=250, description="First name of the customer", example="John"
    )
    last_name_en: str = Field(
        None, max_length=250, description="Last name of the customer", example="Doe"
    )
    primary_contact_number: str = Field(
        None,
        max_length=200,
        description="Primary contact number",
        example="+1234567890",
    )
    email: str = Field(
        None,
        max_length=200,
        description="Email address of the customer",
        example="john.doe@example.com",
    )

    class Config:
        orm_mode = True  # Enables Pydantic to work with ORM models
