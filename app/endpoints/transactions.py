from fastapi import HTTPException, APIRouter
from models.transaction import Transaction, TransactionCreate, TransactionPublic, TransactionUpdate
from database import SessionDep
from sqlmodel import select

router = APIRouter()

@router.post('/transactions', response_model = TransactionPublic)
def create_transaction(transaction: TransactionCreate, session: SessionDep) -> TransactionPublic:
    db_transaction = Transaction.model_validate(transaction)
    session.add(db_transaction)
    session.commit()
    session.refresh(db_transaction)
    return db_transaction

@router.get('/transactions', response_model = list[TransactionPublic])
def read_transactions(session: SessionDep) -> list[TransactionPublic]:
    transactions = session.exec(select(Transaction)).all()
    return transactions

@router.get('/transactions/{id}', response_model = TransactionPublic)
def read_transaction(id: int, session: SessionDep) -> TransactionPublic:
    transaction = session.get(Transaction, id)
    if not transaction:
        raise HTTPException(status_code=404, detail='Transaction not found')
    return transaction

@router.delete('/transactions/{id}')
def delete_transaction(id: int, session: SessionDep):
    transaction = session.get(Transaction, id)
    if not transaction:
            raise HTTPException(status_code=404, detail='Transaction not found')
    session.delete(transaction)
    session.commit()
    return {'Delete transaction': True}

@router.patch('/transactions/{id}', response_model = TransactionPublic)
def update_transaction(id: int, transaction_update: TransactionUpdate, session: SessionDep) -> TransactionPublic:
    transaction = session.get(Transaction, id)
    if not transaction:
        raise HTTPException(status_code=404, detail='Transaction not found')
    transaction_data = transaction_update.model_dump(exclude_unset=True)
    transaction.sqlmodel_update(transaction_data)
    session.add(transaction)
    session.commit()
    session.refresh(transaction)
    return transaction