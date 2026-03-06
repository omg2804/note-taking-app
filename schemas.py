from pydantic import BaseModel
from typing import List, Optional

class NoteBase(BaseModel):
    title: str
    content: str

class NoteCreate(NoteBase):
    pass

class NoteUpdate(NoteBase):
    title: Optional[str] = None
    content: Optional[str] = None

class NoteResponse(NoteBase):
    id: int

    class Config:
        orm_mode = True

class NotesResponse(BaseModel):
    notes: List[NoteResponse]