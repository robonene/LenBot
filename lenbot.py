import discord, ssl
from discord.ext import commands

TOKEN = "**Token Goes Here**"
GUILD = "gnat's server"
intents = discord.Intents.all()
intents.members = True
bot = commands.Bot(command_prefix='!', intents=intents)
bot.remove_command('help')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.event
async def on_message(message):
    await message.channel.send("hi!")

bot.run(TOKEN)
