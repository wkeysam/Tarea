from fastapi import Depends
from sqlmodel import SQLModel, Field, create_engine

class Animales(SQLModel):
    id: int = Field(default=None, primary_key=True)
    nombre: str = Field(sa_column_kwargs={"unique": True, "nullable": False})
    especie: str = Field(default="Animal", nullable=False, max_length=50)
    

class Empleados(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    nombre: str = Field(sa_column_kwargs={"unique": True, "nullable": False})
    rol: str = Field(nullable=False, max_length=255)
    lead: str = Field(sa_column_kwargs={"unique": True, "nullable": False})


db_name = "api.db"
db_url = f"sqlite:///app/{db_name}"

engine = create_engine(db_url, echo=True)

if __name__ == "__main__":
 SQLModel.metadata.create_all(engine)


