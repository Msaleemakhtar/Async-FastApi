from db import engine
from models import NoteModel
from schema import GetModel, CreateModel
from crud import Crud 

from fastapi import FastAPI
from sqlalchemy.ext.asyncio import async_sessionmaker

import uuid
from typing import List
from http import HTTPStatus


app = FastAPI(title="Note Model Api", description= " This is a simple Note taking service , all crud operation has been done")

session = async_sessionmaker(bind=engine, expire_on_commit=False)

db = Crud()

@app.get("/notes", response_model=List[GetModel])
async def get_all_notes():
    note_models = await db.get_all(session)
    return note_models

@app.post("/notes", status_code= HTTPStatus.CREATED, response_model=CreateModel)
async def create_note_model(data:CreateModel)->dict:
    new_data = NoteModel(
        id = str(uuid.uuid4()),
        title = data.title,
        content = data.content
    )

    new_model = await db.add(session, new_data)
    return new_model

@app.get("/note/{note_model_id}", response_model=GetModel)
async def get_Model_by_Id(note_model_id)->dict:
    model_by_id = await db.get_by_id(session, note_model_id)
    return model_by_id


@app.patch("/notes/{note_model_id}")
async def update_model(note_model_id:str, data:CreateModel):
    update_model_note = await db.update(session,note_model_id, data={"title":data.title, "content":data.content})
    return update_model_note

@app.delete("/notes/{note_model_id}")
async def delete_note(note_model_id)->None:
    note_model = await db.get_by_id(session, note_model_id)
    result = await db.delete(session, note_model)
    return result