from aiogram import Bot, Dispatcher
import asyncio
from c_router import *

async def main():
    t_bot = Bot(token="")
    t_dp = Dispatcher()
    router_class = CRouter(t_bot)
    t_dp.include_router(router_class.t_router)
    await t_dp.start_polling(t_bot)

if __name__ == "__main__":
    asyncio.run(main())