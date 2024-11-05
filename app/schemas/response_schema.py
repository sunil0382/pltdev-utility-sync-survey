from typing import TypedDict, Dict, Any


class ResponseSchema(TypedDict):
    code: int
    message: str
    data: Dict[str, Any]
