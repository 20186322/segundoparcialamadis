#Raisa Esther Neris De la Rosa 20186322

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, Text
from uuid import uuid4 as uuid4
import uvicorn

app= FastAPI()

post= []

class Post(BaseModel)
id: Optional[str]
Nombre: str
Telefono: str
Correo: Text

@app.get('/')
def read_root():
return {"Bienvenidos a mi segundo parcial": "Bienvenidos a mi API - Agenda de contacto"}

@app.get('/post')
def get_root():
    return posts

 @app.get('/post')
def save_post(post: Post):
    post.id = str (uuid())
    post.append(post.dict())
    return post [-1]

@app.get('/post/{post_id}')
def get_post(post_id: str):
    for post in posts:
        if post ["id"] == post_id:
            return post
            raise HTTPException(status_code=404, detail= "Item not found")


@app.delete('/post/{post_id}')
def detele_post(post_id: str):
    for index, post in enumerate (posts):
        if post ["id"] == post_id: 
            post.pop(index)
            return {"message": "El contacto se ha eliminado exitosamente"}
            raise HTTPException(status_code=404, detail= "Este contacto no existe")

@app.put('/post/{post_id}')
def update_post(post_id: str, updatePost: Post):
    for index, post in enumerate (posts):
        if post ["id"] == post_id:
            post[index]["Nombre"]= updatePost.dict()["Nombre"]
            post[index]["Telefono"]= updatePost.dict()["Telefono"]
            post[index]["Correo"]= updatePost.dict()["Correo"]
            return {"message": "El conatcto se ha actualizado exitosamente"}
            aise HTTPException(status_code=404, detail= "Este contacto no existe")