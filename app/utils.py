import os
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

def configure_static_and_templates(app: FastAPI):
    current_dir = os.path.dirname(__file__)
    
    # Set up templates directory
    templates = Jinja2Templates(directory=os.path.join(current_dir, "templates"))
    
    # Set up static files directory
    static_files_path = os.path.join(current_dir, "static")
    app.mount("/static", StaticFiles(directory=static_files_path), name="static")
    
    return templates
