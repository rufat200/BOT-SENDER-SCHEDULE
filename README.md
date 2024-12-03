# Telegram Bot: Расписание для групп

## Описание проекта
Этот Telegram-бот предназначен для предоставления расписания занятий. Бот позволяет любому пользователю из различных групп получать расписание на конкретный день недели. 

### Основные функции:
- **Выбор группы:** Пользователь может выбрать свою группу (например, группа №1 или №3).
- **Запрос расписания:** После выбора группы можно указать день недели (например, вторник или четверг), чтобы получить актуальное расписание.

### Используемые технологии:
- Python
- Библиотека [aiogram](https://docs.aiogram.dev/en/latest/) для взаимодействия с Telegram API
- Файл `.env` для хранения конфиденциальной информации (например, токенов) 
- нужно создать свой файл 
```.env ``` и добавить в ```BOT_TOKEN``` токен вашего бота.
- `asyncio` для работы с асинхронными операциями

### Установка
1. Склонируйте репозиторий:
   ```bash
   git clone https://github.com/rufat200/BOT-SENDER-SCHEDULE.git
   cd BOT-SENDER-SCHEDULE
2. Создайтке виртуальное окружение:
   Для Windows:
   ```bash
   python -m venv venv
   venv/Scripts/activate
   ```
   Для macOS/Linux:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Установка библиотек:
   Для Windows:
   ```bash
   pip install -r requirements.txt
   ```
   Для macOS/Linux:
   ```bash
   pip3 install -r requirements.txt
   ```

### Запуск бота
   Для Windows:
   ```bash
   python main.py
   ```
   Для macOS/Linux:
   ```bash
   python3 main.py
   ```