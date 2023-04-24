import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/button1", response_class=HTMLResponse)
async def button1(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "button": "1"})

@app.post("/button2", response_class=HTMLResponse)
async def button2(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "button": "2"})

@app.post("/button3", response_class=HTMLResponse)
async def button3(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "button": "3"})

@app.post("/button4", response_class=HTMLResponse)
async def button4(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "button": "4"})


# Start the server
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
