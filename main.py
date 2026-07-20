from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

ROOT = Path(__file__).parent

app = FastAPI(title='QuantumLab Course')

app.mount('/modules', StaticFiles(directory=str(ROOT / 'modules')), name='modules')

templates = Jinja2Templates(directory=str(ROOT / 'templates'))


@app.get('/', response_class=HTMLResponse)
async def learn(request: Request):
    return templates.TemplateResponse(request, 'learn.html')
