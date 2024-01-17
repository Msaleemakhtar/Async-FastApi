from pydantic import BaseModel, ConfigDict
from datetime import datetime


# schema for returning the Note_model

class GetModel(BaseModel):
    id:str
    title:str
    content:str
    date_created:datetime

    model_config = ConfigDict(
      from_attribute = True  
    )
        
# schema for creating Not_model   

class CreateModel(BaseModel):
    title :str
    content: str

    model_config = ConfigDict(
        from_attributes= True,
        json_schema_extra={
            "example":{
                "title":"Sample title",
                "content" : "Sample content"
            }
        }
    )
