from aiogram import Router, types
from aiogram.enums import ChatType
from aiogram.filters.command import Command
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

class CRouter:
    def __init__(self, b_class):
        self.b_class = b_class
        self.t_router = Router(name=__name__)

        self.t_router.message(Command("start"))(self.start_command)
        self.t_router.message()(self.handle_message)

    async def start_command(self, message: types.Message):
        lnk_btn = InlineKeyboardButton(text = 'add to chat',
                                       url='https://t.me/mitu_totenkompfsammler_bot?startgroup=true')
        kbr_d = InlineKeyboardMarkup(inline_keyboard=[[lnk_btn]])
        await message.answer("Hello nigga, add me to chat", reply_markup=kbr_d)

    async def handle_message(self, message: types.Message):
        # Check if the message is from a private chat
        if message.chat.type == ChatType.PRIVATE:
            await message.answer(f"{message.text} - that says gay nigga before die")
        elif message.chat.type in [ChatType.GROUP, ChatType.SUPERGROUP]:
            await message.reply("Hello gay nigger")