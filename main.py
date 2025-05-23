from aiogram import Bot, Dispatcher, types, executor
import asyncio, json
from config import BOT_TOKEN, KASPI_CARD

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

with open("quiz_data.json", "r", encoding="utf-8") as f:
    quiz_data = json.load(f)

@dp.message_handler(commands=["start"])
async def start_cmd(message: types.Message):
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add("📋 Начать викторину", "💳 Поддержать проект")
    await message.answer("Привет! Это ВикторинаPRO 🎓
Выбирай действие:", reply_markup=kb)

@dp.message_handler(lambda message: message.text == "📋 Начать викторину")
async def start_quiz(message: types.Message):
    question = quiz_data[0]
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for option in question["options"]:
        markup.add(option)
    await message.answer(question["question"], reply_markup=markup)

@dp.message_handler(lambda message: message.text == "💳 Поддержать проект")
async def support(message: types.Message):
    await message.answer(f"Если хочешь поддержать проект, вот номер Kaspi Gold:

🔗 {KASPI_CARD}")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)