import asyncio, os


from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import (
    Message,
    CallbackQuery,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)


from class_schedule import get_schedule


load_dotenv()


BOT_TOKEN = os.getenv("BOT_TOKEN", "bot token")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: Message) -> None:
    text = f'Привет {message.from_user.full_name}!\nВыбери свою группу'
    markup = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text=f"IT{i}", callback_data=f"group_it{i}")]
            for i in range(1, 5)
        ])
    await message.answer(text=text, reply_markup=markup)


@dp.callback_query(lambda call: call.data.startswith("group_"))
async def select_day(call: CallbackQuery) -> None:
    group = call.data.split('_')[1]
    await call.answer()
    text = f"Выбери день недели\n"
    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Понедельник", callback_data=f"{group}_monday")],
        [InlineKeyboardButton(text="Вторник", callback_data=f"{group}_tuesday")],
        [InlineKeyboardButton(text="Среда", callback_data=f"{group}_wednesday")],
        [InlineKeyboardButton(text="Четверг", callback_data=f"{group}_thursday")],
        [InlineKeyboardButton(text="Пятница", callback_data=f"{group}_friday")],
        [InlineKeyboardButton(text="Суббота", callback_data=f"{group}_saturday")]
    ])
    await bot.send_message(call.message.chat.id, text=text, reply_markup=markup)


@dp.callback_query(lambda call: '_' in call.data)
async def return_schedule(call: CallbackQuery) -> None:
    group, day = call.data.split('_')
    schedule = get_schedule(group=group, day=day)
    await bot.send_message(call.message.chat.id, text=schedule)
   
 
async def main() -> None:
    await dp.start_polling(bot)


if __name__ == "__main__":
    print("Запуск бота...")
    asyncio.run(main())