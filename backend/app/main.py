from fastapi import FastAPI, Path
import app.tickets as tk

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

