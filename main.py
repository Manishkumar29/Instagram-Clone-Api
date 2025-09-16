from fastapi import FastAPI
from db import models
from db.database import engine
from routers import comment, user as users,post #made changes 'as users' to make code work
from sqlalchemy.sql.functions import user
from fastapi.staticfiles import StaticFiles
from auth import authentication
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.include_router(users.router) # here also' as users' chnaged
app.include_router(post.router)
app.include_router(authentication.router)
app.include_router(comment.router)

@app.get("/")
def root():
    return "Hello WOrld!"


#cors aloows to access orfin
origins =[
    'http://localhost:3000',
    'http://127.0.0.1:3000',
    'http://192.168.36.1:3000'

    
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

models.Base.metadata.create_all(engine)

app.mount('/images',StaticFiles(directory='images'),name='images') # mount folder