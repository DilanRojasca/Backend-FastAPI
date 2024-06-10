from fastapi import FastAPI
from routers import products, users
from fastapi.staticfiles import StaticFiles

app = FastAPI()

#routers

app.include_router(products.router)
app.include_router(users.router)

#recursos estaticos
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
async def root():
    return "Hola FastAPI!"
#Url local: 127.0.0.1:8000/url

@app.get("/url")
async def url():
    return {"Url_predica" : "https://open.spotify.com/episode/2eaR354XkuRjQHGPZLbsSg?si=b47e174b288643ba"}

#iniciar server uvicorn main:app --reload


#Detener server: CTRL + C

#Documentacion Swagger: 127.0.0.1:8000/docs
#Documentacion Redocly: 127.0.0.1:8000/redoc