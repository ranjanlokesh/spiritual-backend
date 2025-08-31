from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import Session, select
from models import Reflection
from database import engine, create_db_and_tables

app = FastAPI()

create_db_and_tables()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Spiritual Manifesto API with SQLite is live"}

@app.post("/submit-insight")
def submit_insight(insight: str = Form(...)):
    reflection = Reflection(insight=insight)
    with Session(engine) as session:
        session.add(reflection)
        session.commit()
        session.refresh(reflection)
    return {"status": "success", "id": reflection.id}

@app.get("/reflections")
def get_reflections():
    with Session(engine) as session:
        reflections = session.exec(select(Reflection)).all()
    return {"reflections": [r.insight for r in reflections]}