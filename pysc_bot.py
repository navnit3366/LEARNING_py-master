import config
import logging

from aiogram import Bot, Dispatcher, executor, types

#log level
logging.basicCinfig(level=logging.INFO)

# bot init
bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)

# ban command
@dp.message_handler(is_admin=True,commands=["ban"],commands_prefix="!/")
async def cmd_ban(message: types.Message):
    if not message.reply_to_message:
        await message.reply("Answer")
        return

    await message.bot.delete_message(chat_id=config.GROUP_ID)
    await message.bot.kick_chat_member(chat_id=config.GROUP_ID,user_id=message.reply_to_message.from_user.id)

#echo
@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)

# run long-polling
if __name__ == "__main__":
    executor.start_polling(dp,skip_updates=True)

import telebot

bot = telebot.TeleBot("5546044871:AAFALv3hDv66e5MAoUXIkl0mB-dEw7iVLZY")
@bot.message_handler(content_types=['text'])
def send_echo(message):
    # bot.reply_to(message, message.text)
    bot.send_message(message.chat.id, message.text)
bot.polling(none_stop=True)
