from models import Animal, AnimalRequest 
from typing import Optional
from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import Session
from routers import animales, empleados



    
app = FastAPI(
    title = "API de Animales y Empleados",
    version = "0.0.1",
    description= "Una API que habla de animales y empleados",              
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
)

app.include_router(animales.routers)
app.include_router(empleados.routers)

@app.get("/")
async def read_root():
    return {"Esta es mi API de Animales y Empleados"}

@app.post("/")
async def clear_animales():
    return {"Luego poner el clear de la api de animales y empleados"}

@app.post("/")
async def actualizar_animales(animal_request: AnimalRequest, session: Session = Depends(get_session)):
    nuevo_animal = Animal(**animal_request.model_dump())
    session.add(nuevo_animal)
    session.commit()
    session.refresh(nuevo_animal)
    return {"Actualizar api"}

@app.get("/")
async def leer_animales():

    return {"Leer los elementos encontrados en la api"}

@app.get("/")
async def leer_empleados(empleados_request: Optional[EmpleadosRequest] = None, session: Session = Depends(get_session)):
    session = Session()
    # session.(empleados_request)
    if empleados_id not in empleados_db:
        raise HTTPException(status_code=404, 
        detail="Usuario no encontrado"
        )
    return {"Usuario encontrado": empleados_db[empleados_id]}

@app.get("/")
async def clear_empleados():
    return {"Leer los elementos encontrados en la api"}

@app.get("/")
async def actualizar_animales():
    return {"Leer los elementos encontrados en la api"}

@app.get("/")
async def crear_empleados(empleados_request: EmpleadosRequest, session: Session = Depends(get_session)):
    nuevo_empleado = Empleado(**empleados_request.model_dump())
    session.add(nuevo_empleado)
    session.commit()
    session.refresh(nuevo_empleado)
    return {"Empleado creado": nuevo_empleado}



