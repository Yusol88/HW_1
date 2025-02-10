# app/core/entities/user.py
class User(Base):
    _id: int
    _username: str
    _email: str
    _balance: float
    _role: UserRole
    
    # Методы управления балансом и транзакциями