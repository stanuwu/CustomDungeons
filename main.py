import discord
from discord.ext import commands
import asyncio

print("""
 ▄████████ ███    █▄     ▄████████     ███      ▄██████▄    ▄▄▄▄███▄▄▄▄   ████████▄  ███    █▄  ███▄▄▄▄      ▄██████▄     ▄████████  ▄██████▄  ███▄▄▄▄      ▄████████ 
███    ███ ███    ███   ███    ███ ▀█████████▄ ███    ███ ▄██▀▀▀███▀▀▀██▄ ███   ▀███ ███    ███ ███▀▀▀██▄   ███    ███   ███    ███ ███    ███ ███▀▀▀██▄   ███    ███ 
███    █▀  ███    ███   ███    █▀     ▀███▀▀██ ███    ███ ███   ███   ███ ███    ███ ███    ███ ███   ███   ███    █▀    ███    █▀  ███    ███ ███   ███   ███    █▀  
███        ███    ███   ███            ███   ▀ ███    ███ ███   ███   ███ ███    ███ ███    ███ ███   ███  ▄███         ▄███▄▄▄     ███    ███ ███   ███   ███        
███        ███    ███ ▀███████████     ███     ███    ███ ███   ███   ███ ███    ███ ███    ███ ███   ███ ▀▀███ ████▄  ▀▀███▀▀▀     ███    ███ ███   ███ ▀███████████ 
███    █▄  ███    ███          ███     ███     ███    ███ ███   ███   ███ ███    ███ ███    ███ ███   ███   ███    ███   ███    █▄  ███    ███ ███   ███          ███ 
███    ███ ███    ███    ▄█    ███     ███     ███    ███ ███   ███   ███ ███   ▄███ ███    ███ ███   ███   ███    ███   ███    ███ ███    ███ ███   ███    ▄█    ███ 
████████▀  ████████▀   ▄████████▀     ▄████▀    ▀██████▀   ▀█   ███   █▀  ████████▀  ████████▀   ▀█   █▀    ████████▀    ██████████  ▀██████▀   ▀█   █▀   ▄████████▀  
""")

global version
version = "1.1"
client = commands.Bot(command_prefix="<", description=f"CustomDungeons {version} | Release")
client.remove_command("help")

TOKEN = "TOKEN HERE"

startup_extensions = ["help","bugreport","game","core","backup"]

if __name__ == '__main__':
    for cog in startup_extensions:
        client.load_extension(f"cogs.{cog}")
        print(f"Loaded extention: {cog}")


@client.event
async def on_ready():
    print(f"-\nRunning {client.description}\nUser: {client.user.name} | ID: {client.user.id}")
    print(f"Boot completed!\n-")
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name=f"<help | CustomDungeons {version}"))

client.run(TOKEN, bot=True, reconnect=True)