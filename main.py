from fastapi import FastAPI
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse

app = FastAPI()

app.mount("/static",StaticFiles(directory="./public/static"),name = "static")


@app.get("/", response_class=HTMLResponse)
async def root():
    html_address = "./public/static/html/index.html"
    return FileResponse(html_address, status_code=200)

@app.get("/update")
async def update(profile: str = 'W8x15', bolt: str = "7/8", n_bolts: int = 4,fit: bool = True):
    from placa_base.figure import figure
    img = figure(profile = profile,bolt=bolt, n_bolts=n_bolts,fit=fit)
    img.savefig("image.png")
    return FileResponse("image.png", filename="image.png")


origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "http://127.0.0.1:8000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)