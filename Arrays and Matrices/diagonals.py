import discord
import random
import asyncio
import datetime

TOKEN = "MTM2NDExOTk1MTU3NjY2MjAyNg.GUxRm_.n8459cp3F14GNvRbYwifo4Q-tK8Sbe7oMmn9gY"
CHANNEL_ID = 123456789012345678 # Замени с ID на канала, където искаш да праща

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

quotes = [
"Действай, дори когато не ти се иска. В това е силата.",
"Всеки ден е нов шанс да започнеш отначало.",
"Ти си по-силен, отколкото мислиш.",
"Мечтите ти заслужават усилията ти.",
"Бъди промяната, която искаш да видиш в света."
]

async def send_daily_quote():
    await client.wait_until_ready()
    channel = client.get_channel(CHANNEL_ID)
    while not client.is_closed():
        now = datetime.datetime.now()
        next_run = now.replace(hour=8, minute=0, second=0, microsecond=0)
        if now > next_run:
            next_run = next_run + datetime.timedelta(days=1)
            wait_time = (next_run - now).total_seconds()
            await asyncio.sleep(wait_time)
            quote = random.choice(quotes)
            await channel.send(quote)

@client.event
async def on_ready():
    print(f'Влязох като {client.user}')
    client.loop.create_task(send_daily_quote())

client.run(TOKEN)