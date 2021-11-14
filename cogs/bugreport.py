import discord
from discord.ext import commands
import datetime

class BRCog(commands.Cog, name="Bugreport Cog"):
    def __init__(self, bot):
        self.bot = bot
        global ownerid
        ownerid = [623984743914012712]
        global ratecheck
        ratecheck = {}


    #bugreport command
    @commands.command()
    async def bugreport(self, ctx, *, report: str = None):
        try:
            if report == None:
                embed = discord.Embed(title="Error", description="Please write something in your report!", color=discord.Color.dark_red())
                await ctx.send(embed=embed)
            else:
                try:
                    if ratecheck[str(ctx.author.id)]:
                        pass
                except:
                    ratecheck[str(ctx.author.id)] = None
                
                passflag = False
                if ratecheck[str(ctx.author.id)] == None:
                    passflag = True
                else:
                    dtn = datetime.datetime.now()
                    dif = dtn - ratecheck[str(ctx.author.id)]
                    difmin = int(dif.total_seconds()/60)
                    if difmin > 10:
                        passflag = True
                    else:
                        embed = discord.Embed(title="Cooldown", description=f"You can send another bug report in {str(difmin - 10)[1:]}min.", color=discord.Color.dark_red())
                        await ctx.send(embed=embed)

                if passflag == True:
                    ratecheck[str(ctx.author.id)] = datetime.datetime.now()
                    embed = discord.Embed(title="Success", description="Bug report sent!", color=discord.Color.green())
                    await ctx.send(embed=embed)
                    user = self.bot.get_user(623984743914012712)
                    embed = discord.Embed(title=f"Bug Report by {ctx.author.name}", description=report, color=discord.Color.dark_red())
                    msg = await user.send(embed = embed)
                    await msg.add_reaction("✅")

        except Exception as e:
            embed = discord.Embed(title="Error", description=f"Error running the command:\n```{e}```", color=discord.Color.dark_red())
            await ctx.send(embed=embed)


    #report command
    @commands.command()
    async def report(self, ctx, *, report: str = None):
        try:
            if report == None:
                embed = discord.Embed(title="Error", description="Please write something in your report!", color=discord.Color.dark_red())
                await ctx.send(embed=embed)
            else:
                try:
                    if ratecheck[str(ctx.author.id)]:
                        pass
                except:
                    ratecheck[str(ctx.author.id)] = None
                
                passflag = False
                if ratecheck[str(ctx.author.id)] == None:
                    passflag = True
                else:
                    dtn = datetime.datetime.now()
                    dif = dtn - ratecheck[str(ctx.author.id)]
                    difmin = int(dif.total_seconds()/60)
                    if difmin > 10:
                        passflag = True
                    else:
                        embed = discord.Embed(title="Cooldown", description=f"You can send another report in {str(difmin - 10)[1:]}min.", color=discord.Color.dark_red())
                        await ctx.send(embed=embed)

                if passflag == True:
                    ratecheck[str(ctx.author.id)] = datetime.datetime.now()
                    embed = discord.Embed(title="Success", description="Bug report sent!", color=discord.Color.green())
                    await ctx.send(embed=embed)
                    user = self.bot.get_user(623984743914012712)
                    embed = discord.Embed(title=f"Report {ctx.author.name}", description=report, color=discord.Color.dark_red())
                    msg = await user.send(embed = embed)
                    await msg.add_reaction("✅")

        except Exception as e:
            embed = discord.Embed(title="Error", description=f"Error running the command:\n```{e}```", color=discord.Color.dark_red())
            await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(BRCog(bot))