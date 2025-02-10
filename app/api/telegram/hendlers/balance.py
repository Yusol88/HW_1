# app/api/telegram/handlers/balance.py
@dp.message_handler(commands=['balance'])
async def show_balance(message: Message):
    # Показ баланса пользователя