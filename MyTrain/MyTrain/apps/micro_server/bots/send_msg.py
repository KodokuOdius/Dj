

async def send_msg(data):

    title = data["title"]
    content = data["content"]
    select = str(data["select"])

    if select == "VK":
        print(1)
        import vk.main as vk
        await vk.msg(title, content)

    elif select == "Telegram":
        print(2)
        import tg.main as tg
        await tg.msg(title, content)

    elif select == "all":
        print(3)
        from .vk.main import msg
        await msg(title, content)

        from .tg.main import msg
        await msg(title, content)
    else:
        print("nope")
    return None