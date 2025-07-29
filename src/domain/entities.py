from datetime import datetime
from enum import StrEnum

from pydantic import BaseModel, HttpUrl
from pydantic import UUID4


class FileStatus(StrEnum):
    PENDING = "pending"
    PROCESSING = "processing"
    COMPLETED = "completed"
    FAILED = "failed"


class File(BaseModel):
    id: UUID4
    url: HttpUrl
    status: FileStatus
    created_at: datetime
    updated_at: datetime
