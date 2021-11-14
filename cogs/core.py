import discord
from discord.ext import commands

class CoreCog(commands.Cog, name="Core Commands Cog"):
    def __init__(self, bot):
        self.bot = bot
        global ownerid
        ownerid = [623984743914012712]

    #reload any cog in cogs
    @commands.command()
    async def reload(self, ctx, to_reload: str):
        if ctx.author.id in ownerid:
            if to_reload == "game" or to_reload == "backup":
                embed = discord.Embed(title=f"{ctx.author.name} - Reload", description=f"Module \"{to_reload}\" has tasks! Use `<reload_{to_reload}`", color=discord.Color.dark_red())
                await ctx.send(embed=embed)
            else:
                try:
                    self.bot.reload_extension(f"cogs.{to_reload}")
                    embed = discord.Embed(title=f"{ctx.author.name} - Reload", description=f"Module \"{to_reload}\" was reloaded!", color=discord.Color.green())
                    await ctx.send(embed=embed)
                except Exception as e:
                    embed = discord.Embed(title="Error", description=f"Module \"{to_reload}\" could not be reloaded:\n```{e}```", color=discord.Color.dark_red())
                    await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title="No Permission", description=f"You can't use this command!", color=discord.Color.dark_red())
            await ctx.send(embed=embed)

    #server list
    @commands.command(aliases=["guilds"])
    async def servers(self, ctx):
        if ctx.author.id in ownerid:
            try:
                serverlist = ""
                for i in self.bot.guilds:
                    serverlist = serverlist + i.name + "\n"
                embed = discord.Embed(title=f"Guilds ({len(self.bot.guilds)})", description=serverlist, color=discord.Color.dark_red())
                await ctx.send(embed=embed)
            except Exception as e:
                embed = discord.Embed(title="Error", description=f"Error running the command:\n```{e}```", color=discord.Color.dark_red())
                await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title="No Permission", description=f"You can't use this command!", color=discord.Color.dark_red())
            await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(CoreCog(bot))