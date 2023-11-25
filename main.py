from fastapi import FastAPI
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.mount("/public",StaticFiles(directory="./public"),name = "public")
app.mount("/static",StaticFiles(directory="./public/static"),name = "static")

@app.get("/", response_class=HTMLResponse)
async def root():
    html_address = "./public/static/html/index.html"
    return FileResponse(html_address, status_code=200)


@app.get("/update")
def update(profile: str = 'W8x15', bolt: str = "7/8", n_bolts: int = 4,fit: bool = True):
    from placa_base.figure import figure
    img = figure(profile = profile,bolt=bolt, n_bolts=n_bolts,fit=fit)
    img.savefig("imagen.png")
    return FileResponse('imagen.png', filename="image.png")


@app.get("/dxf")
def dxf(profile: str = 'W8x15', bolt: str = "7/8", n_bolts: int = 4,fit: bool = True):
    from placa_base.figure import dxf
    
    dxf = dxf(profile = profile,bolt=bolt, n_bolts=n_bolts,fit=fit)
    dxf.saveas("drawing.dxf")
    return FileResponse('drawing.dxf', filename="drawing.dxf")

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