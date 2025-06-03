from pydantic import BaseModel

class InsuranceIn(BaseModel):
    policy_number: str
    holder_name: str
    provider: str

class Insurance(InsuranceIn):
    id: int
