from asyncio import sleep

from aiohttp import ClientSession, ClientTimeout

from bot import config_dict, LOGGER
from bot.helper.ext_utils.bot_utils import new_task


@new_task
async def ping_server():
    attempt = 1
    while attempt < 5:
        try:
            async with ClientSession(timeout=ClientTimeout(total=10)) as session, session.get(config_dict['BASE_URL'], ssl=False) as res:
                if (respon := res.status) != 200:
                    raise ValueError(f'ERROR, got respons {respon}. Retrying in 10 seconds ({attempt}/5).')
            await sleep(600)
        except Exception as e:
            LOGGER.error(e)
            await sleep(10)
            attempt += 1
