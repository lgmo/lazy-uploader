from datetime import UTC, datetime
import os
from uuid import uuid4

from pydantic import BaseModel, HttpUrl

from config import get_settings
from domain.entities import File, FileStatus


class FileCreateSchema(BaseModel):
    name: str
    content: bytes

    def to_entity(self) -> File:
        now = datetime.now(UTC)
        settings = get_settings()
        final_name, extension = os.path.splitext(self.name)
        file_id = uuid4()
        url = HttpUrl(
            f"{settings.storage_base_url}/{final_name}_{file_id.hex}{extension}"
        )
        return File(
            id=file_id,
            status=FileStatus.PENDING,
            url=url,
            created_at=now,
            updated_at=now,
            **self.model_dump(exclude={"name"}),
        )
