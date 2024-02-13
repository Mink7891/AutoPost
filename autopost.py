import os
import asyncio
from telegram import Bot, InputMediaPhoto, InlineKeyboardButton, InlineKeyboardMarkup

TOKEN = '...'
CHANNEL_ID = '...'
PHOTO_FOLDER = '...'

async def send_photo_with_button(photo_path, button_url, caption=""):
    bot = Bot(token=TOKEN)
    
    photo = open(photo_path, 'rb')
    
    keyboard = [[InlineKeyboardButton("Посетить сайт", url=button_url)]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await bot.send_photo(chat_id=CHANNEL_ID, photo=photo, caption=caption, reply_markup=reply_markup)


async def send_photos():
    for filename in sorted(os.listdir(PHOTO_FOLDER)):
        if filename.endswith('.jpg'):
            photo_path = os.path.join(PHOTO_FOLDER, filename)
            button_url = 'https://vk.com/'
            
            await send_photo_with_button(photo_path, button_url, caption="")
            await asyncio.sleep(3)
            os.remove(photo_path)

if __name__ == "__main__":
    asyncio.run(send_photos())
