async def msg(title, content):
    users = DB.request("select user_id from vk_users;", "fetchall")

    for user in users:
        await bot.api.messages.send(
            user_id=user,
            message=f"{title}!\n\n{content}"
        )

    print("VK Done!")





from vkbottle import Bot
from vkbottle.bot import Message

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


@bot.on.private_message()
async def start(event: Message):
    res = DB.request(f"select * from vk_users where user_id = {event.from_id};", "result")
    

    if not res:
        DB.request(f"insert into vk_users (user_id) values ({event.from_id});")
    else:
        await event.answer("Привет")

    await event.answer(event.text)



if __name__ == "__main__":
    bot.run_forever()


