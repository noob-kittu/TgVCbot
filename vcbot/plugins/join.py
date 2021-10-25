from vcbot import app
from pytgcalls import GroupCallFactory
from telethon import events

group_call_factory = GroupCallFactory(app, GroupCallFactory.MTPROTO_CLIENT_TYPE.TELETHON)
group_call = group_call_factory.get_file_group_call('input.raw')


@app.on(events.NewMessage(outgoing=True, pattern=r'^/join$'))
async def join_handler(event):
    chat = await event.get_chat()
    await group_call.start(chat.id)