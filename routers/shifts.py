from datetime import datetime, timezone
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db import get_db
from models import ShiftSlot, ShiftOverride
from schemas import ShiftSlotCreate, ShiftSlotOut, ShiftOverrideCreate, ShiftOverrideOut

router = APIRouter(prefix="/shifts", tags=["shifts"])


@router.post("/slots", response_model=ShiftSlotOut)
def create_shift_slot(payload: ShiftSlotCreate, db: Session = Depends(get_db)):
    row = ShiftSlot(**payload.model_dump())
    db.add(row)
    db.commit()
    db.refresh(row)
    return row


@router.get("/slots", response_model=list[ShiftSlotOut])
def list_shift_slots(db: Session = Depends(get_db)):
    return db.query(ShiftSlot).order_by(ShiftSlot.start_at.asc()).all()


@router.get("/current", response_model=ShiftSlotOut | None)
def current_shift(db: Session = Depends(get_db)):
    now = datetime.now(timezone.utc)
    row = (
        db.query(ShiftSlot)
        .filter(ShiftSlot.start_at <= now, ShiftSlot.end_at >= now)
        .order_by(ShiftSlot.start_at.asc())
        .first()
    )
    return row


@router.post("/overrides", response_model=ShiftOverrideOut)
def create_override(payload: ShiftOverrideCreate, db: Session = Depends(get_db)):
    slot = db.query(ShiftSlot).filter(ShiftSlot.id == payload.slot_id).first()
    if not slot:
        raise HTTPException(status_code=404, detail="Shift slot not found")

    row = ShiftOverride(
        slot_id=payload.slot_id,
        original_staff_id=slot.staff_id,
        actual_staff_id=payload.actual_staff_id,
        reason=payload.reason,
    )
    db.add(row)
    db.commit()
    db.refresh(row)
    return row


@router.get("/overrides", response_model=list[ShiftOverrideOut])
def list_overrides(db: Session = Depends(get_db)):
    return db.query(ShiftOverride).order_by(ShiftOverride.created_at.desc()).all()
