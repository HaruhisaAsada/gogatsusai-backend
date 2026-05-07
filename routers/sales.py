from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db import get_db
from models import SalesRecord
from schemas import SalesCreate, SalesOut

router = APIRouter(prefix="/sales", tags=["sales"])


@router.post("", response_model=SalesOut)
def create_sales(payload: SalesCreate, db: Session = Depends(get_db)):
    row = SalesRecord(**payload.model_dump())
    db.add(row)
    db.commit()
    db.refresh(row)
    return SalesOut(
        id=row.id,
        item_name=row.item_name,
        sold_at=row.sold_at,
        quantity=row.quantity,
        unit_price=row.unit_price,
        total_amount=row.quantity * row.unit_price,
    )


@router.get("", response_model=list[SalesOut])
def list_sales(db: Session = Depends(get_db)):
    rows = db.query(SalesRecord).order_by(SalesRecord.sold_at.desc()).all()
    return [
        SalesOut(
            id=r.id,
            item_name=r.item_name,
            sold_at=r.sold_at,
            quantity=r.quantity,
            unit_price=r.unit_price,
            total_amount=r.quantity * r.unit_price,
        )
        for r in rows
    ]
