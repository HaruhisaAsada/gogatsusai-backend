from datetime import datetime
from pydantic import BaseModel, Field


class StaffCreate(BaseModel):
    name: str


class StaffOut(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True


class SalesCreate(BaseModel):
    item_name: str
    sold_at: datetime
    quantity: int = Field(gt=0)
    unit_price: int = Field(ge=0)


class SalesOut(BaseModel):
    id: int
    item_name: str
    sold_at: datetime
    quantity: int
    unit_price: int
    discount_amount: int
    total_amount: int


class ShiftSlotCreate(BaseModel):
    start_at: datetime
    end_at: datetime
    staff_id: int
    next_staff_id: int | None = None


class ShiftSlotOut(BaseModel):
    id: int
    start_at: datetime
    end_at: datetime
    staff_id: int
    next_staff_id: int | None

    class Config:
        from_attributes = True


class ShiftOverrideCreate(BaseModel):
    slot_id: int
    actual_staff_id: int
    reason: str | None = None


class ShiftOverrideOut(BaseModel):
    id: int
    slot_id: int
    original_staff_id: int
    actual_staff_id: int
    reason: str | None
    created_at: datetime

    class Config:
        from_attributes = True


class ExpenseCreate(BaseModel):
    category: str
    amount: int = Field(ge=0)
    spent_at: datetime
    note: str | None = None


class ExpenseOut(BaseModel):
    id: int
    category: str
    amount: int
    spent_at: datetime
    note: str | None

    class Config:
        from_attributes = True


class ProfitReport(BaseModel):
    total_sales: int
    total_expenses: int
    profit: int
