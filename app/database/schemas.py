from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class ItemAnimal(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

    model_config = {
        "Example": {
            "examples": [
                {
                    "name": "Animal",
                    "description": "***",
                }
            ]
        }
    }
class ItemEmpleado(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "name": "Empleado",
                    "description": "***",
                }
            ]
        }
    }


@app.put("/items/{item_id}")
async def update_animal(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results

@app.put("/items/{item_id}")
async def update_empleado(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results