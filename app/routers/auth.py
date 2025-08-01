from fastapi import FastAPI
from pydantic import BaseModel, Field, usernameStr, HTTPException, Depends, status

app = FastAPI()

class UsuarioId(BaseModel):
    username: str
    contraseña: str
    nombre_completo: str | None = None
    
class UserarioOut(BaseModel):
    username: str
    nombre_completo: str | None = None
    
class UsuarioBD(BaseModel):
    id: int
    username: str
    nombre_completo: str | None = None
    contraseña_hash: str
    
def contraseña_hash(contraseña: str) -> str:
    return "contraseña" + contraseña_hash 

def usuario_guardado(usuario_in: UsuarioId) -> UsuarioBD:
    contraseña_hashed = contraseña_hash(usuario_dentro.contraseña)
    user_in_db = UserInDB(**user_in.dict(), hashed_password=hashed_password)
    print (f"Usuario guardado: {user_in_db}")
    return user_in_db
    return {"message": "Usuario guardado correctamente"}

@app.post("/usuarios/", response_model=UsuarioOut)
async def crear_usuario(usuario_in: UsuarioId):
    usuario_bd = usuario_guardado(usuario_in)
    return usuario_bd

def obtener_usuario(db, username: str):
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)

async def obtener_usuario(token: Annotated[str, Depends(outh2_scheme)]):
    usuario = fake_decode_token(token)
    if not usuario:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return usuario

async def obtener_usuario_actual(
    current_user: Annotated[User, Depends(obtener_usuario)],
):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive User")
    return current_user

@app.get("/usuarios/me", response_model=UsuarioOut)
async def read_user_me(
   current_user: Annotated[User, Depends(obtener_usuario_actual)],
):
  return current_user
  