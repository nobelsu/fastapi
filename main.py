from fastapi import FastAPI, HTTPException
from config.database import database, engine, metadata
from models.models import insurance_table
from schemas.schemas import Insurance, InsuranceIn
from typing import List

app = FastAPI()

@app.on_event("startup")
async def startup():
    await database.connect()
    metadata.create_all(engine) # what is an engine; what metadata?

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@app.post("/insurance/", response_model=Insurance) # what is the purpose of response_model here?
async def create_insurance(data: InsuranceIn):
    query = insurance_table.insert().values(**data.model_dump()) # what format is the data here in? 
    last_record_id = await database.execute(query)
    return {**data.model_dump(), "id": last_record_id}

@app.get("/insurance/", response_model=List[Insurance])
async def get_all():
    query = insurance_table.select()
    return await database.fetch_all(query)

@app.get("/insurance/{insurance_id}", response_model=Insurance)
async def get_one(insurance_id: int):
    query = insurance_table.select().where(insurance_table.c.id == insurance_id)
    result = await database.fetch_one(query)
    if result is None:
        raise HTTPException(status_code=404, detail="Insurance not found")
    return result

@app.put("/insurance/{insurance_id}", response_model=Insurance)
async def update_insurance(insurance_id: int, data: InsuranceIn):
    query = insurance_table.update().where(insurance_table.c.id == insurance_id).values(**data.model_dump())
    await database.execute(query)
    return {**data.model_dump(), "id": insurance_id}

@app.delete("/insurance/{insurance_id}")
async def delete_insurance(insurance_id: int):
    query = insurance_table.delete().where(insurance_table.c.id == insurance_id)
    await database.execute(query)
    return {"message": "Insurance deleted successfully"}

@app.delete("/insurance/")
async def delete_all():
    query = insurance_table.delete()
    await database.execute(query)
    return {"message": "All insurances deleted successfully"}