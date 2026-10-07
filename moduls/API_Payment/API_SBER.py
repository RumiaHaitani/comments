# 1. Подключаем модуль random для генерации ID транзакции
import random

# 2. Класс платёжного шлюза Сбербанка
class SberPayGateway:
    # 3. Конструктор класса
    def __init__(self):
        # 4. Название и версия шлюза
        self.gateway_name = "SberBank API v2.4"

    # 5. Метод обработки платежа
    def process_payment(self, amount: float) -> dict:
        # 6. Проверка лимита для анонимного шлюза
        if amount > 100000:
            # 7. Возвращаем ошибку при превышении лимита
            return {"success": False, "message": "Limit exceeded for Sber anonymized gateway"}
        
        # 8. Генерируем уникальный ID транзакции
        tx_id = f"SBER-{random.randint(100000, 999999)}"
        # 9. Возвращаем успешный результат платежа
        return {
            "success": True,
            "transaction_id": tx_id,
            "gateway": self.gateway_name,
            "amount": amount
        }
# 10. Конец класса SberPayGateway