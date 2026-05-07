from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db import get_db
from models import Staff
from schemas import StaffCreate, StaffOut

router = APIRouter(prefix="/staffs", tags=["staffs"])


@router.post("", response_model=StaffOut)
def create_staff(payload: StaffCreate, db: Session = Depends(get_db)):
    staff = Staff(name=payload.name)
    db.add(staff)
    db.commit()
    db.refresh(staff)
    return staff


@router.get("", response_model=list[StaffOut])
def list_staffs(db: Session = Depends(get_db)):
    return db.query(Staff).order_by(Staff.id.asc()).all()
