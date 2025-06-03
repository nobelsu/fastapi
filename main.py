from fastapi import FastAPI
from pydantic import BaseModel
# import duckdb

app = FastAPI()
# db = duckdb.connect("data/insurances.db")

class Insurance(BaseModel):
    id: int
    policy_number: str
    provider: str
    holder_name: str

insurances = []
insuranceCount = 0

@app.get("/insurance")
async def get_insurances():
    global insurances
    return {"insurances": insurances}

@app.get("/insurance/{insurance_id}")
async def get_insurance(insurance_id: int):
    global insurances
    for insurance in insurances:
        if insurance.id == insurance_id:
            return {"insurance": insurance}
    return {"error": "Insurance not found"}

@app.post("/insurance")
async def create_insurance(insurance: Insurance):
    global insurances, insuranceCount
    insurance.id = insuranceCount
    insuranceCount += 1
    insurances.append(insurance)
    return {"insurance": insurance}

@app.delete("/insurance/{insurance_id}")
async def delete_insurance(insurance_id: int):
    global insurances
    insurances = [ins for ins in insurances if ins.id != insurance_id]
    return {"message": "Insurance deleted successfully"}

@app.put("/insurance/{insurance_id}")
async def update_insurance(insurance_id: int, insurance_new: Insurance):
    global insurances
    for index, insurance in enumerate(insurances):
        if insurance.id == insurance_id:
            insurances[index] = insurance_new
            return {"insurance": insurance_new}
    return {"error": "Insurance not found"}