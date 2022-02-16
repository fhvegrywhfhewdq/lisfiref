from telethon import TelegramClient
api_id = 13644867
api_hash = "252c5628ed52c1d091dcdd894c4ccd9d"
bot = TelegramClient('uba', api_id, api_hash)
@register(outgoing=True, pattern="^[.]plane$")
async def idu(event):
await client.send_message(event.chat_id, "[{event.sender.first_name}](tg://user?id={event.sender_id})")
bot.start()
bot.connect()
bot.run_until_disconnected()