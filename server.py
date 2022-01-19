import logging
import os

from aiogram import Bot, Dispatcher, executor, types

from conv_voice import convert
from recogn_face import detect_face


API_TOKEN = os.getenv('API_TOKEN')

# Configure logging.
logging.basicConfig(level=logging.INFO)


# Initialize bot and dispatcher.
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


#
@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will called when user send '/start' or '/help' command
    """
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")


#
@dp.message_handler(content_types=["photo"])
async def download_photo(message: types.Message):
    file_name = f"data/{message.from_user.id}/image/img{message.message_id}.jpg"
    await message.photo[-1].download(destination_file=file_name)
    detect_face(file_name)


#
@dp.message_handler(content_types=["voice"])
async def download_voice(message: types.Message):    
    file_name = f"data/{message.from_user.id}/voice/audio_message_{message.message_id}.ogg"
    await message.voice.download(destination_file=file_name)
    #
    convert(file_name, message.message_id, message.from_user.id)
    
    

@dp.message_handler(content_types=["audio"])
async def download_audio(message: types.Message):
    await message.audio.download(destination_dir="temp_audio/")



@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
