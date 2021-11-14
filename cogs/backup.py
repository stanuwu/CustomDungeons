import discord
from discord.ext import commands
import datetime
import asyncio
import json

class BackupCog(commands.Cog, name="Backup Cog"):
    def __init__(self, bot):
        self.bot = bot
        global ownerid
        ownerid = [623984743914012712]
        global datadict


        #task to create backup data every x seconds
        async def data_backup():
            saveinterval = 21600 #saves every saveinterval seconds
            await bot.wait_until_ready()
            while not bot.is_closed():
                await asyncio.sleep(saveinterval)
                try:
                    savedata = open("data/mainsave.json", "r")
                    datadict = json.load(savedata)
                    savedata.close()

                    print("----------")
                    print(f"Attempting Backup @{datetime.datetime.now().time()}")
                    filename = f"backups/mainsave{datetime.datetime.now()}.json".replace(":", "-")
                    savedata = open(filename, "w")
                    json.dump(datadict, savedata)
                    savedata.close()
                    print("Backup Completed")
                except Exception as e:
                    print(f"Error with backup \n{e}\n")

        #create the task
        self.backuptask = bot.loop.create_task(data_backup())


        #reload command -> stops task first
    @commands.command()
    async def reload_backup(self, ctx):
        if ctx.author.id in ownerid:
            try:
                print("----------")
                print("Reloading Backup Module")

                self.backuptask.cancel()
                self.bot.reload_extension("cogs.backup")
                embed = discord.Embed(title=f"{ctx.author.name} - Reload", description="Backup module was reloaded!", color=discord.Color.green())
                await ctx.send(embed=embed)
            except Exception as e:
                embed = discord.Embed(title="Error", description=f"Backup module could not be reloaded:\n```{e}```", color=discord.Color.dark_red())
                await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title="No Permission", description="You can't use this command!", color=discord.Color.dark_red())
            await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(BackupCog(bot))