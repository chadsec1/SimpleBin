from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from app.database import get_db
from app.utils.id_gen import gen_unique_id
import os

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

os.makedirs("app/storage", exist_ok=True)

@router.get("/", response_class=HTMLResponse)
async def form(request: Request):
    return templates.TemplateResponse("form.html", {"request": request})

@router.post("/submit")
async def submit(request: Request, content: str = Form(...)):
    paste_id = gen_unique_id()
    db = get_db()
    db.execute(
        "INSERT INTO pastes (id, content) VALUES (?, ?)",
        (paste_id, content)
    )
    db.commit()
    return RedirectResponse(f"/paste/{paste_id}", status_code=303)

@router.get("/paste/{paste_id}", response_class=HTMLResponse)
async def read_paste(request: Request, paste_id: str):
    db = get_db()
    row = db.execute("SELECT content FROM pastes WHERE id = ?", (paste_id,)).fetchone()
    if not row:
        return HTMLResponse("Paste not found", status_code=404)
    return templates.TemplateResponse("view.html", {"request": request, "content": row["content"]})
