from pydantic import BaseModel
from pydantic import Field

class InputsRequest(BaseModel):
    text: str = Field(
        ..., example="Lorem Ipsum", description="Text to be summarized"
    )