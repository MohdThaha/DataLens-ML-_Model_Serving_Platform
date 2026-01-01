from pydantic import BaseModel

class TransactionInput(BaseModel):
    price: float
    quantity: int
    discount_pct: float
    category: str
    region: str
    sales_channel: str
    customer_type: str
    is_weekend: int

class AnomalyInput(BaseModel):
    price: float
    quantity: int
    discount_pct: float
    profit: float
    is_weekend: int
