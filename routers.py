from fastapi import APIRouter, HTTPException
from typing import List
from schemas import NoteCreate, NoteUpdate, NoteResponse, NotesResponse
from crud import create_note, get_note, get_notes, update_note, delete_note
from database import get_db
from fastapi import Depends

router = APIRouter()

@router.post("/notes/", response_model=NoteResponse)
async def create_note_route(note: NoteCreate, db: Session = Depends(get_db)):
    return await create_note(note, db)

@router.get("/notes/", response_model=NotesResponse)
async def list_notes_route(db: Session = Depends(get_db)):
    return await get_notes(db)

@router.get("/notes/{note_id}", response_model=NoteResponse)
async def get_note_route(note_id: int, db: Session = Depends(get_db)):
    note = await get_note(note_id, db)
    if note is None:
        raise HTTPException(status_code=404, detail="Note not found")
    return note

@router.put("/notes/{note_id}", response_model=NoteResponse)
async def update_note_route(note_id: int, note: NoteUpdate, db: Session = Depends(get_db)):
    updated_note = await update_note(note_id, note, db)
    if updated_note is None:
        raise HTTPException(status_code=404, detail="Note not found")
    return updated_note

@router.delete("/notes/{note_id}", response_model=NoteResponse)
async def delete_note_route(note_id: int, db: Session = Depends(get_db)):
    deleted_note = await delete_note(note_id, db)
    if deleted_note is None:
        raise HTTPException(status_code=404, detail="Note not found")
    return deleted_note

# Add this line to ensure the router is correctly imported
note_router = router