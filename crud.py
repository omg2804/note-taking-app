from sqlalchemy.orm import Session
from models import NoteModel
from schemas import NoteCreate, NoteUpdate
from typing import List

async def create_note(note: NoteCreate, db: Session) -> NoteModel:
    db_note = NoteModel(**note.dict())
    db.add(db_note)
    db.commit()
    db.refresh(db_note)
    return db_note

async def get_notes(db: Session) -> List[NoteModel]:
    return db.query(NoteModel).all()

async def get_note(note_id: int, db: Session) -> NoteModel:
    return db.query(NoteModel).filter(NoteModel.id == note_id).first()

async def update_note(note_id: int, note: NoteUpdate, db: Session) -> NoteModel:
    db_note = db.query(NoteModel).filter(NoteModel.id == note_id).first()
    if db_note:
        for key, value in note.dict(exclude_unset=True).items():
            setattr(db_note, key, value)
        db.commit()
        db.refresh(db_note)
    return db_note

async def delete_note(note_id: int, db: Session) -> NoteModel:
    db_note = db.query(NoteModel).filter(NoteModel.id == note_id).first()
    if db_note:
        db.delete(db_note)
        db.commit()
    return db_note