import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters import CommandStart, Command

from config import TOKEN
import weather

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(F.photo)
async def react_photo(message: Message):
    await message.answer('ИИ, или искусственный интеллект, — это область компьютерной науки, которая занимается созданием систем, способных выполнять задачи, требующие человеческого интеллекта. Эти задачи могут включать распознавание речи, понимание естественного языка, принятие решений, решение проблем, обучение и адаптацию на основе опыта.')

@dp.message(F.text == 'Что такое ИИ?')
async def aitext(message: Message):
    await message.answer('ИИ, или искусственный интеллект, — это область компьютерной науки, которая занимается созданием систем, способных выполнять задачи, требующие человеческого интеллекта. Эти задачи могут включать распознавание речи, понимание естественного языка, принятие решений, решение проблем, обучение и адаптацию на основе опыта.')

@dp.message(Command('help'))
async def help(message: Message):
    await message.answer('Бот выполняет /start /help')


@dp.message(CommandStart())
async def start(message : Message):
    city = F.text
    weather_text = weather.get_weather(city)
    await message.answer(f'Погода в {city}: {weather_text}')



async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
