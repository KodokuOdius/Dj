async def msg(title, content):
    users = DB.request("select user_id from tg_users;", "fetchall")

    for user in users:
        await dp.bot.send_message(
            chat_id=user,
            text=f"<h2><b>{title}</b></h2>\n\n{content}"
        )


    print("TG Done!")



from aiogram import Bot, types, executor, Dispatcher

from . import local_settings as ls
import simplePostgrConnector as Connector

DB = Connector.PostgrDB(
    database_name=ls.NAME,
    user=ls.USER,
    user_password=ls.PASSWORD,
    host=ls.HOST,
    port=ls.PORT
)


bot = Bot(
    token=ls.TG_TOKEN,
    parse_mode=types.ParseMode.HTML
)
dp = Dispatcher(bot=bot)


@dp.message_handler()
async def start(event: types.Message):
    res = DB.request(f"select * from tg_users where user_id = {event.from_user.id};", "result")

    if not res:
        DB.request(f"insert into tg_users (user_id) values ({event.from_user.id});")
    else:
        await event.answer("Привет")

    await event.answer(event.text)


if __name__ == "__main__":
    executor.start_polling(dp)





