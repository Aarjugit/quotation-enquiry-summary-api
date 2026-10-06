from typing import Any

from pydantic import BaseModel, ConfigDict


class AISummaryRequest(BaseModel):
    model_config = ConfigDict(extra="allow")

    enquiries: list[dict[str, Any]]