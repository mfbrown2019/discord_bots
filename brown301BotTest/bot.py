import discord
from discord.ext import commands
import random

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print('Bot is ready')
    
@bot.event
async def on_message(message):
    person = ['!merlin'.lower(), '!nick', '!matt']
    
    if message.content.lower() in person:
        channel = message.channel
        await channel.send('Bitch!')
        
    elif message.content == '$CoolGuySherm':
        with open('coolsherm.png', 'rb') as f:
            picture = discord.File(f)
            channel = message.channel
            await channel.send(file=picture)




bot.run('MTE4MDcxOTczMjg0MDczODgyNg.GhAZAL.a3cSW80Y11_HPOt83HgMeuqIFPo5A4XGl_seAE')


