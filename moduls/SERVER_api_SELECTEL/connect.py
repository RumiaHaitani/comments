# 1. Импорт модуля json для чтения конфигурации
import json
# 2. Импорт модуля os для работы с путями
import os

# 3. Класс коннектора к серверу Selectel
class SelectelServerConnector:
    # 4. Конструктор класса
    def __init__(self):
        # 5. Определяем папку текущего файла
        current_dir = os.path.dirname(os.path.abspath(__file__))
        # 6. Формируем путь к config.json
        self.config_path = os.path.join(current_dir, 'config.json')

    # 7. Метод загрузки конфигурации
    def load_configuration(self) -> dict:
        # 8. Пытаемся прочитать JSON-файл
        try:
            # 9. Открываем файл и возвращаем словарь
            with open(self.config_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        # 10. Если файл недоступен, возвращаем настройки разработки
        except Exception:
            return {"server_url": "localhost", "environment": "development"}