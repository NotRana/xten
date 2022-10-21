import discord 
from discord import Interaction, app_commands
from discord.ext import commands
import json
import os


bot = commands.Bot(command_prefix="&", intents = discord.Intents.all())

with open("./config.json", "r") as configjsonFile:
    configdata = json.load(configjsonFile)
    TOKEN = configdata["token"]

@bot.event
async def on_ready():
    print("i am ready here")
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="Under Development."))
    try:
        synced = await bot.tree.sync()
        print(f"synced {len(synced)} slash commands")
    except Exception as e:
        print(e)

@bot.tree.command(name="hallo", description="say hallo!")
async def hallo(interaction: discord.Interaction):
    await interaction.response.send_message(f"hey {interaction.user.mention}!",ephemeral=True)
    

@bot.tree.command(name="say", description="say something!")
@app_commands.describe(thing_to_say="what should i say")
async def say(interaction: discord.Interaction, thing_to_say: str):
    await interaction.response.send_message(f"{interaction.user.mention} say that `{thing_to_say}`")

@bot.command()
async def hi(ctx):
    await ctx.reply("hi")




bot.run(TOKEN)