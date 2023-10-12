import discord
from AntiScam import AntiScam

whitelist = [414913108654686209] 
logs_channel = 1077705264184168508 

intents = discord.Intents.default()
intents.message_content = True
bot = discord.Client(intents=intents)

@bot.event
async def on_message(message):
    await AntiScam(message, bot = bot, whitelist = whitelist, muted_role='Muted', verified_role='Verificado', logs_channel=logs_channel)
bot.run('MTA3NzgwOTA1NTg2NDczNzg0Mw.G4XNRJ.wWFxZ3WnWz4Bx6VrJnq8i4VnGjrgRwp1n734tA')