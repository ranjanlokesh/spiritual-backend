from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import Session, select
from models import Reflection, AIReflection, AIReflectionCreate
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

# ✅ Existing insight submission
@app.post("/submit-insight")
def submit_insight(insight: str = Form(...)):
    reflection = Reflection(insight=insight)
    with Session(engine) as session:
        session.add(reflection)
        session.commit()
        session.refresh(reflection)
    return {"status": "success", "id": reflection.id}

# ✅ Existing insight retrieval
@app.get("/reflections")
def get_reflections():
    with Session(engine) as session:
        reflections = session.exec(select(Reflection)).all()
    return {"reflections": [r.insight for r in reflections]}

# ✅ New: Save AI reflection
@app.post("/save-reflection")
def save_ai_reflection(reflection: AIReflectionCreate):
    new_reflection = AIReflection(prompt=reflection.prompt, response=reflection.response)
    with Session(engine) as session:
        session.add(new_reflection)
        session.commit()
        session.refresh(new_reflection)
    return {"status": "success", "id": new_reflection.id}

# ✅ New: Get AI reflections
@app.get("/get-reflections")
def get_ai_reflections():
    with Session(engine) as session:
        reflections = session.exec(select(AIReflection)).all()
    return {
        "reflections": [
            {"prompt": r.prompt, "response": r.response}
            for r in reflections
        ]
    }