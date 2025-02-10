# app/core/services/finance.py
class BalanceService:
    def deposit(self, user: User, amount: float) -> Transaction:
        # Логика пополнения баланса