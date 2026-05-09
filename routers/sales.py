from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db import get_db
from models import SalesRecord
from schemas import SalesCreate, SalesOut

router = APIRouter(prefix="/sales", tags=["sales"])

def calculate_discount(item_name: str, quantity: int) -> int:
    if item_name == "レモネード":
        return (quantity // 2) * 100
    return 0


@router.post("", response_model=SalesOut)
def create_sales(payload: SalesCreate, db: Session = Depends(get_db)):
    discount_amount = calculate_discount(payload.item_name, payload.quantity)
    row = SalesRecord(**payload.model_dump(), discount_amount=discount_amount)
    db.add(row)
    db.commit()
    db.refresh(row)

    return SalesOut(
        id=row.id,
        item_name=row.item_name,
        sold_at=row.sold_at,
        quantity=row.quantity,
        unit_price=row.unit_price,
        discount_amount=row.discount_amount,
        total_amount=(row.quantity * row.unit_price) - row.discount_amount,
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
            discount_amount=r.discount_amount,
            total_amount=(r.quantity * r.unit_price) - r.discount_amount,
        )
        for r in rows
    ]
