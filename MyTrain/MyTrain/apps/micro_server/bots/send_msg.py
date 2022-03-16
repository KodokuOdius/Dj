

async def send_msg(data):
    title = "Админ Вещает!!!!!\n" + data["title"].upper()
    content = data["content"]
    select = str(data["select"])

    if select == "VK":
        from .vk.main import msg
        await msg(title, content)

    elif select == "Telegram":
        from .tg.main import msg
        await msg(title, content)

    elif select == "all":
        from .vk.main import msg
        await msg(title, content)

        from .tg.main import msg
        await msg(title, content)
    else:
        print("nope")

    return None