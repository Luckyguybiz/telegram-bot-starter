import logging
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '7186402403:AAGaIpUQDIeNwaXtKqC95oba1QYzHimZJl8'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.answer("Привет! Я Алина. Хочешь моё фото? Напиши /photo")

@dp.message_handler(commands=['photo'])
async def send_photo(message: types.Message):
    with open("girl.jpg", "rb") as photo:
        await message.reply_photo(photo, caption="Только для тебя 😉")

@dp.message_handler(commands=['voice'])
async def send_voice(message: types.Message):
    with open("voice.ogg", "rb") as voice:
        await message.reply_voice(voice, caption="Скучала по тебе...")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
