from fastapi import APIRouter, Depends
from sqlalchemy import func
from sqlalchemy.orm import Session
from db import get_db
from models import SalesRecord, ExpenseRecord
from schemas import ProfitReport

router = APIRouter(prefix="/reports", tags=["reports"])


@router.get("/profit", response_model=ProfitReport)
def profit_report(db: Session = Depends(get_db)):
    sales = db.query(func.sum(SalesRecord.quantity * SalesRecord.unit_price)).scalar() or 0
    expenses = db.query(func.sum(ExpenseRecord.amount)).scalar() or 0
    return ProfitReport(
        total_sales=int(sales),
        total_expenses=int(expenses),
        profit=int(sales - expenses),
    )
