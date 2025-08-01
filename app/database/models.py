from sqlmodel import SQLModel, Field, create_engine
from typing import Optional

class ApiAnimales(SQLModel, table=True):
    id: Optional[int] = Field(None, primary_key=True)
    name: str
    description: Optional[str]
    tareas: str
    lead: str

class ApiEmpleados(SQLModel, table=True):
    id: Optional[int] = Field(None, primary_key=True)
    name: str
    description: Optional[str]
    tareas: str
    lead: str
