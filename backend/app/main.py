from fastapi import FastAPI, Path
import app.tickets as tk
from app.schemas import TicketCreate

app = FastAPI()

@app.get("/health")
def health_check():
    return {
  "status": "ok",
  "service": "connecttel-api"
    }

@app.get("/tickets/{number}")
def get_ticket_id(number: int = Path(ge=1, le=999999)):
    return {"ticket_id": tk.create_ticket_id(number)}

@app.post("/tickets", status_code=201)
def create_ticket(ticket: TicketCreate):
    return ticket.model_dump()