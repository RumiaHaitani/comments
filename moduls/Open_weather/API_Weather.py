# 1. Подключаем модуль random для генерации погоды
import random

# 2. Класс монитора погоды
class WeatherMonitor:
    # 3. Конструктор класса
    def __init__(self):
        # 4. Город по умолчанию
        self.city = "Moscow"

    # 5. Метод получения текущей погоды
    def get_current_weather(self) -> dict:
        # 6. Список возможных погодных условий
        conditions = ["Clear", "Cloudy", "Rainy", "Snowing"]
        # 7. Возвращаем словарь с погодой
        return {
            # 8. Название города
            "city": self.city,
            # 9. Случайная температура
            "temp": random.randint(-5, 25),
            # 10. Случайное погодное условие
            "condition": random.choice(conditions)
        }