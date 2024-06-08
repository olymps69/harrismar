from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from app.utils import configure_static_and_templates

app = FastAPI()

# Configure templates and static files
templates = configure_static_and_templates(app)

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    """
    Root endpoint that serves the index.html template.
    """
    return templates.TemplateResponse("index.html", {"request": request})
