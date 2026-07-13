from pydantic import BaseModel
from typing import Any

class MeetingRequestDTO(BaseModel):
    room_name: str
    floor: str
    capacity: int
    status: str

class APIResponse(BaseModel):
    statusCode: int
    error: Any | None = None
    message: str
    data: Any | None = None

def notice_api(statusCode: int, error:Any, message: str, data: Any):
    return APIResponse(
        statusCode=statusCode,
        error=error,
        message=message,
        data=data)