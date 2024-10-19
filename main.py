import discord
from discord.ext import commands
import json

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot("#", intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command
async def Which_garbage_goes_where(ctx, trash:str = "Cam"):
    with open("Trash.json", "r", encoding="utf-8") as file:
        await ctx.send(json.loads(file)["Atiklar"][trash])

bot.run("!!!You must paste your token!!!")