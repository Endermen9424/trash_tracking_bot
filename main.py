import discord
from discord.ext import commands
import json
from Bot_command import *

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot("#", intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command
async def Which_garbage_goes_where(ctx, trash:str = "Cam"):
    with open("Trash.json", "r", encoding="utf-8") as file:
        await ctx.send(json.loads(file.read)["Atiklar"][trash])

@bot.command
async def Add_garbage(ctx, Time:int = 1, count = 1):
    Garbage_by_time[Time - 1] = count
    await ctx.send("Başarı ile eklendi!")

@bot.command
async def How_is_garbage(ctx):
    await ctx.send(mean_garbage)

bot.run("!!!You must paste your token!!!")