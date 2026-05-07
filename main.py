from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from db import Base, engine
from routers import staffs, sales, shifts, expenses, reports

Base.metadata.create_all(bind=engine)

app = FastAPI(title="gogatsusai-api")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
    ],
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
