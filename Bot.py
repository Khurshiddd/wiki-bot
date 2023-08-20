import logging
import wikipedia
from aiogram import Bot, Dispatcher, executor, types
wikipedia.set_lang('uz')
TOKEN = '5551095031:AAHv7FPM78_PUAdEXYrD66pxzNpoy80wPzc'  # Replace with your actual bot token
logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Assalomu alaykum, \nXush kelibsiz!")

@dp.message_handler()
async def sendWiki(message: types.Message):
    try:
        respond = wikipedia.summary(message.text)
        await message.answer(respond)
    except:
        await message.answer("Bu mavzuga oid maqola topilmadi")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)


