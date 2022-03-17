from email import message
from vkbottle import Bot
from vkbottle.bot import Message

from vkbottle.tools import Keyboard, EMPTY_KEYBOARD, KeyboardButtonColor, Text

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
    token=ls.VK_TOKEN
)

UnSubKey = (
    Keyboard(one_time=False, inline=False)
    .add(Text("Отписаться 😥"), color=KeyboardButtonColor.NEGATIVE)
    .get_json()
)

SubKey = (
    Keyboard(one_time=False, inline=False)
    .add(Text("Подписаться 😆"), color=KeyboardButtonColor.POSITIVE)
    .get_json()
)


@bot.on.private_message(text="Отписаться 😥")
async def unsub(event: Message):
    DB.request(f"update vk_users set sub = false where user_id = {event.from_id}")

    await event.answer(
        message="Вы успешно отписались от рассылки!",
        keyboard=SubKey
    )

@bot.on.private_message(text="Подписаться 😆")
async def sub(event: Message):
    DB.request(f"update vk_users set sub = true where user_id = {event.from_id}")

    await event.answer(
        message="Вы успешно подписались на рассылку!",
        keyboard=UnSubKey
    )



@bot.on.private_message()
async def start(event: Message):
    res = DB.request(f"select * from vk_users where user_id = {event.from_id};", "result")
    

    if not res:
        DB.request(f"insert into vk_users (user_id) values ({event.from_id});")
        await event.answer(
            message="Я бот для рассылки новостей с помощью сайта на Django, в любой момент ты можешь отписаться ил подписаться",
            keyboard=SubKey
    )
    else:
        await event.answer("Я тебя помню")
        await event.answer(event.text)




if __name__ == "__main__":
    bot.run_forever()


async def msg(title, content):
    users = DB.request("select user_id from vk_users where sub = true;", "fetchall")

    for user in users:
        await bot.api.messages.send(
            user_id=int(user[0]),
            message=f"{title}!\n\n{content}",
            random_id=0
        )

    print("VK Done!")