import datetime
from sqlmodel import Field, SQLModel


class TransactionBase(SQLModel):
    amount: int
    category: str
    description: str | None = None
    date: datetime.date = Field(default_factory=datetime.date.today)

class TransactionCreate(TransactionBase):
    pass

class TransactionUpdate(SQLModel):
    amount: int | None = None
    category: str | None = None
    description: str | None = None
    date: datetime.date | None = None

class TransactionPublic(TransactionBase):
    id: int
        
class Transaction(TransactionBase, table=True):
    id: int | None = Field(default=None, primary_key=True)