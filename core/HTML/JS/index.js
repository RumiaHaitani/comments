// 1. Запускаем код после полной загрузки DOM
document.addEventListener('DOMContentLoaded', () => {
    // 2. Получаем ссылки на элементы интерфейса
    const logConsole = document.getElementById('log-console');
    const balanceAmount = document.getElementById('balance-amount');
    const paymentForm = document.getElementById('payment-form');
    // 3. Начальный баланс пользователя
    let currentBalance = 50000;

    // 4. Функция добавления сообщения в лог
    function addLog(message) {
        const timestamp = new Date().toLocaleTimeString();
        logConsole.innerHTML += `[${timestamp}] ${message}<br>`;
        logConsole.scrollTop = logConsole.scrollHeight;
    }

    // 5. Загрузка конфигурации сервера
    async function fetchServerConfig() {
        try {
            addLog("Запрос конфигурации с SERVER_api_SELECTEL...");
            const response = await fetch('/api/config');
            const config = await response.json();
            addLog(`Сервер подключен к: ${config.server_url} (Окружение: ${config.environment})`);
        } catch (e) {
            addLog("Использование локальной эмуляции конфигурации сервера.");
        }
    }

    // 6. Обновление данных о погоде
    async function updateWeather() {
        try {
            const response = await fetch('/api/weather');
            const data = await response.json();
            document.getElementById('weather-display').innerText = `Москва: ${data.temp}°C, ${data.condition}`;
            addLog("Данные Open_weather успешно обновлены.");
        } catch (e) {
            document.getElementById('weather-display').innerText = `Москва: +18°C, Облачно`;
        }
    }

    // 7. Обработка отправки формы платежа
    paymentForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        // 8. Считываем выбранный банк и сумму
        const bank = document.getElementById('bank-select').value;
        const amount = parseFloat(document.getElementById('amount-input').value);

        // 9. Проверяем, хватает ли средств
        if (amount > currentBalance) {
            addLog(`Ошибка: Недостаточно средств для списания ${amount} ₽`);
            return;
        }

        addLog(`Инициализация шлюза API_Payment для ${bank}...`);
        
        // 10. Отправляем платёж на сервер и обрабатываем ответ
        try {
            const response = await fetch('/api/pay', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({ bank, amount })
            });
            const result = await response.json();

            if (result.success) {
                currentBalance -= amount;
                balanceAmount.innerText = `${currentBalance.toLocaleString('ru-RU')}.00 ₽`;
                addLog(`Транзакция одобрена. ID: ${result.transaction_id}. Списано: ${amount} ₽ через ${result.gateway}`);
            } else {
                addLog(`Ошибка шлюза: ${result.message}`);
            }
        } catch (error) {
            currentBalance -= amount;
            balanceAmount.innerText = `${currentBalance.toLocaleString('ru-RU')}.00 ₽`;
            const mockId = Math.floor(Math.random() * 900000) + 100000;
            addLog(`[Эмуляция клиента] Успешный платеж через API_${bank}. ID: TX-${mockId}. Списано: ${amount} ₽`);
        }
        document.getElementById('amount-input').value = '';
    });

    fetchServerConfig();
    updateWeather();
});