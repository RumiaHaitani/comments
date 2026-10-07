# 1. Подключаем модуль random для генерации ID транзакции
import random

# 2. Класс платёжного шлюза Т-Банка
class TBankPayGateway:
    # 3. Конструктор класса
    def __init__(self):
        # 4. Название и версия шлюза
        self.gateway_name = "T-Bank OpenAPI"

    # 5. Метод обработки платежа
    def process_payment(self, amount: float) -> dict:
        # 6. Генерируем уникальный ID транзакции
        tx_id = f"T-BANK-{random.randint(100000, 999999)}"
        # 7. Формируем успешный ответ
        return {
            # 8. Признак успешности операции
            "success": True,
            # 9. ID транзакции и название шлюза
            "transaction_id": tx_id,
            "gateway": self.gateway_name,
            # 10. Сумма платежа
            "amount": amount
        }