from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db import get_db
from models import ExpenseRecord
from schemas import ExpenseCreate, ExpenseOut

router = APIRouter(prefix="/expenses", tags=["expenses"])


@router.post("", response_model=ExpenseOut)
def create_expense(payload: ExpenseCreate, db: Session = Depends(get_db)):
    row = ExpenseRecord(**payload.model_dump())
    db.add(row)
    db.commit()
    db.refresh(row)
    return row


@router.get("", response_model=list[ExpenseOut])
def list_expenses(db: Session = Depends(get_db)):
    return db.query(ExpenseRecord).order_by(ExpenseRecord.spent_at.desc()).all()
