from sqlalchemy import Table, Column, Integer, String, Float
from config.database import metadata

insurance_table = Table(
    "insurances",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("policy_number", String(50)),
    Column("holder_name", String(100)),
    Column("provider", String(100)),
)