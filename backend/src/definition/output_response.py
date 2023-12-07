from typing import List

from pydantic import BaseModel
from pydantic import Field

class OutputRequest(BaseModel):
    input_text: str = Field(
        ..., example="Lorem Ipsum", description="Text to be summarized"
    )
    summary: str = Field(
        ..., example="Lorem", description="Summarized text"
    )
    additional_information: List[str] = Field(
        ..., example=["Entities: pippo"], description="Text to be summarized"
    )