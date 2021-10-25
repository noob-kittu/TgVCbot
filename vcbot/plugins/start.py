from vcbot import app
from telethon import events
from telethon.tl.functions.phone import CreateGroupCallRequest as startvc
from telethon.tl.functions.phone import DiscardGroupCallRequest as stopvc
from telethon.tl.functions.phone import GetGroupCallRequest as getvc
from telethon.tl.functions.channels import GetFullChannelRequest as getchat




async def get_call(event):
    mm = await event.client(getchat(event.chat_id))
    xx = await event.client(getvc(mm.full_chat.call))
    return xx.call



@app.on(events.NewMessage(outgoing=True, pattern=r'^/startvc$'))
async def _(e):
    try:
        await e.client(startvc(e.chat_id))
        await e.reply("`Starting voice chat...")
    except Exception as ex:
        await e.reply(f"`{ex}`")


@app.on(events.NewMessage(outgoing=True, pattern=r'^/stopvc$'))
async def _(e):
    try:
        await e.client(stopvc(await get_call(e)))
        await e.reply("`Stopping Voice chat...`")
    except Exception as ex:
        await e.reply(f"`{ex}`")