
from models import NoteModel
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker


class Crud:
    # get all the notes from db
    async def get_all(self, async_session:async_sessionmaker[AsyncSession]):
        async with async_session() as session:
            statement = select(NoteModel).order_by(NoteModel.id)
            result = await session.execute(statement)
            return result.scalars()
    
     # get note_model by id
    async def get_by_id(self, async_session:async_sessionmaker[AsyncSession], note_model_id:str):
        async with async_session() as session:
            statement = select(NoteModel).filter(NoteModel.id == note_model_id)
            result = await session.execute(statement)
            return result.scalars().one()

    # create note_model object
    async def add(self, async_session:async_sessionmaker[AsyncSession], note_model:NoteModel):
        async with async_session() as session:
            session.add(note_model)
            await session.commit()
        return note_model
    
    # update notemodel by id
    async def update(self, async_session:async_sessionmaker[AsyncSession], note_model_id, data):
        async with async_session() as session:
            statement = select(NoteModel).filter(NoteModel.id == note_model_id)
            result = await session.execute(statement)
            note_model = result.scalars().one()
            note_model.title = data["title"]
            note_model.content = data["content"]
            await session.commit()
            return note_model
            
    # delete notemodel by id
    async def delete(self, async_session:async_sessionmaker[AsyncSession], note_model:NoteModel):
        async with async_session() as session:
            await session.delete(note_model)
            await session.commit()
        return {}
   
