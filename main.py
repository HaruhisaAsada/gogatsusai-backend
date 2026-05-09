from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import inspect, text
from db import Base, engine
from routers import staffs, sales, shifts, expenses, reports

Base.metadata.create_all(bind=engine)
inspector = inspect(engine)
sales_columns = {col["name"] for col in inspector.get_columns("sales_records")}
if "discount_amount" not in sales_columns:
    with engine.begin() as conn:
        conn.execute(text("ALTER TABLE sales_records ADD COLUMN discount_amount INTEGER NOT NULL DEFAULT 0"))

app = FastAPI(title="gogatsusai-api")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "https://gogatsusai-frontend.vercel.app/",
    ],
    allow_origin_regex=r"https://.*\.vercel\.app",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(staffs.router)
app.include_router(sales.router)
app.include_router(shifts.router)
app.include_router(expenses.router)
app.include_router(reports.router)


@app.get("/health")
def health_check():
    return {"status": "ok"}
