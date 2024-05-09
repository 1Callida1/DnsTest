
import aiogram
import asyncio, logging
from config_reader import config
from helper import generate_inline_kb, generate_kb

logging.basicConfig(level=logging.INFO)
bot = aiogram.Bot(token=config.bot_token.get_secret_value())
dp = aiogram.Dispatcher()

@dp.message(aiogram.filters.Command("start"))
async def cmd_start(message: aiogram.types.Message):
    await bot.send_photo(message.chat.id, photo=aiogram.types.FSInputFile('photo_1.jpg'), caption="<i><b>Выберите интересущий вас пункт</b></i>", reply_markup=generate_inline_kb("start"), parse_mode=aiogram.enums.ParseMode.HTML) 

@dp.callback_query()
async def display_btn(call):
    if(call.data == 'call_display'):
        await bot.send_photo(call.message.chat.id, photo=aiogram.types.FSInputFile('photo_2.jpg'), caption="<i><b>Выберите SIS</b></i>", reply_markup=generate_inline_kb("regulations"), parse_mode=aiogram.enums.ParseMode.HTML)
        # await bot.edit_message_reply_markup(call.message.chat.id, msg.message_id, reply_markup=generate_inline_kb("regulations"))
    elif(call.data == 'call_regulations'):
        await bot.send_photo(call.message.chat.id, photo=aiogram.types.FSInputFile('photo_3.jpg'), caption="<i><b>Выберите интересущий вас регламент</b></i>", reply_markup=generate_inline_kb("display"), parse_mode=aiogram.enums.ParseMode.HTML)
        # await bot.edit_message_reply_markup(call.message.chat.id, msg.message_id, reply_markup=generate_inline_kb("display"))
    elif(call.data == 'call_distributions'):
        await bot.send_photo(call.message.chat.id, photo=aiogram.types.FSInputFile('photo_4.jpg'))

@dp.message(aiogram.filters.Command("Назад"))
async def cmd_back(message: aiogram.types.Message):
    await bot.send_photo(message.chat.id, photo=aiogram.types.FSInputFile('photo_1.jpg'), caption="<i><b>Выберите интересущий вас пункт</b></i>", reply_markup=generate_inline_kb("start"), parse_mode=aiogram.enums.ParseMode.HTML) 

@dp.message(aiogram.filters.Command("К началу"))
async def cmd_to_start(message: aiogram.types.Message):
    await bot.send_photo(message.chat.id, photo=aiogram.types.FSInputFile('photo_1.jpg'), caption="<i><b>Выберите интересущий вас пункт</b></i>", reply_markup=generate_inline_kb("start"), parse_mode=aiogram.enums.ParseMode.HTML) 

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
