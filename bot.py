from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from random import choice as rnd


from config import TOKEN




bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

random_answer = ('Чего хочешь зайка? :3', 'Чего желаете?', 'Повелитель, вся моя жизнь в служении!', 'Три икс в кубе плюс константа. Ну что там?')



@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply(str(rnd(random_answer)))


@dp.message_handler(commands=['start', 'help'])


@dp.message_handler(commands=['help'])
async def proccess_help_command(message: types.Message):
    await message.reply("Напиши мне что-нибудь, и я отправлю этот текст тебе в ответ!")


@dp.message_handler()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, msg.text)
 



if __name__ == '__main__':
    executor.start_polling(dp)
