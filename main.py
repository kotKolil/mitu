from aiogram import Bot, Dispatcher
import asyncio
from c_router import *
import json
from ai_rqst import *

async def main():
    with open('config.json', 'r') as file:
        data = json.load(file)
        print(data["bot_token"])

    t_ai_rqst = AiRqst(data["api_token"])
    t_bot = Bot(token=data["bot_token"])
    t_dp = Dispatcher()
    router_class = CRouter(t_bot, t_ai_rqst)
    t_dp.include_router(router_class.t_router)
    await t_dp.start_polling(t_bot)

if __name__ == "__main__":
    asyncio.run(main())