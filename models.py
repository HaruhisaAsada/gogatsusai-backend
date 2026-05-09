from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.sql import func
from db import Base


class Staff(Base):
    __tablename__ = "staffs"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False, unique=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())


class SalesRecord(Base):
    __tablename__ = "sales_records"
    id = Column(Integer, primary_key=True, index=True)
    item_name = Column(String(255), nullable=False)
    sold_at = Column(DateTime(timezone=True), nullable=False)
    quantity = Column(Integer, nullable=False)
    unit_price = Column(Integer, nullable=False)
    discount_amount = Column(Integer, nullable=False, default=0)
    created_at = Column(DateTime(timezone=True), server_default=func.now())


class ShiftSlot(Base):
    __tablename__ = "shift_slots"
    id = Column(Integer, primary_key=True, index=True)
    start_at = Column(DateTime(timezone=True), nullable=False)
    end_at = Column(DateTime(timezone=True), nullable=False)
    staff_id = Column(Integer, ForeignKey("staffs.id"), nullable=False)
    next_staff_id = Column(Integer, ForeignKey("staffs.id"), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())


class ShiftOverride(Base):
    __tablename__ = "shift_overrides"
    id = Column(Integer, primary_key=True, index=True)
    slot_id = Column(Integer, ForeignKey("shift_slots.id"), nullable=False)
    original_staff_id = Column(Integer, ForeignKey("staffs.id"), nullable=False)
    actual_staff_id = Column(Integer, ForeignKey("staffs.id"), nullable=False)
    reason = Column(String(255), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())


class ExpenseRecord(Base):
    __tablename__ = "expense_records"
    id = Column(Integer, primary_key=True, index=True)
    category = Column(String(120), nullable=False)
    amount = Column(Integer, nullable=False)
    spent_at = Column(DateTime(timezone=True), nullable=False)
    note = Column(String(255), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
