from aiogram import Bot, types, executor, Dispatcher
from aiogram.types import (KeyboardButton, ReplyKeyboardMarkup,
                           ReplyKeyboardRemove)

if __name__ != "__main__":
    from . import local_settings as ls
    from . import simplePostgrConnector as Connector
else:
    import local_settings as ls
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




UnSubKey = (
    ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
    .add(KeyboardButton("Отписаться 😥"))
)

SubKey = (
    ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
    .add(KeyboardButton("Подписаться 😆"))
)


@dp.message_handler(text="Отписаться 😥")
async def unsub(event: types.Message):
    DB.request(f"update tg_users set sub = false where user_id = {event.from_user.id}")

    await event.answer(
        text="Вы успешно отписались от рассылки!",
        reply_markup=SubKey
    )

@dp.message_handler(text="Подписаться 😆")
async def sub(event: types.Message):
    DB.request(f"update tg_users set sub = true where user_id = {event.from_user.id}")

    await event.answer(
        text="Вы успешно подписались на рассылку!",
        reply_markup=UnSubKey
    )




@dp.message_handler()
async def start(event: types.Message):
    res = DB.request(f"select * from tg_users where user_id = {event.from_user.id};", "result")

    if not res:
        DB.request(f"insert into tg_users (user_id) values ({event.from_user.id});")
        await event.answer(
            text="Я бот для рассылки новостей с помощью сайта на Django, в любой момент ты можешь отписаться ил подписаться",
            reply_markup=SubKey
    )
    else:
        await event.answer("Я тебя помню")
        await event.answer(event.text)


if __name__ == "__main__":
    executor.start_polling(dp)



async def msg(title, content):
    users = DB.request("select user_id from tg_users where sub = true;", "fetchall")

    for user in users:
        await dp.bot.send_message(
            chat_id=int(user[0]),
            text=f"<b>{title}</b>\n\n{content}"
        )

    print("TG Done!")