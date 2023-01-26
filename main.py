from telethon import TelegramClient, events

# брать с сайта телеграмма https://my.telegram.org/auth
api_id = ''
api_hash = ''

client = TelegramClient('mirror', api_id, api_hash)

client.start()

client.start()

#Id чата криптотаверны
@client.on(events.NewMessage(-1001244789214))
async def main1(event):
    if "WTS" in event.message.upper() and "WL" in event.message.upper():
        #Id чата куда присылать сообщения
        await client.send_message(-1111111111111, event.message)


client.run_until_disconnected()
