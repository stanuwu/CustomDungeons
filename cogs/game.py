import discord
from discord.ext import commands, tasks
import json
import asyncio
import datetime
import random
import math
import dbl

import gamedata

class GameCog(commands.Cog, name="Game Cog"):
    def __init__(self, bot):
        self.bot = bot
        global ownerid
        ownerid = [623984743914012712]
        global datadict

        #stuff for dbl
        self.token = "DBL TOKEN"
        self.dblpy = dbl.DBLClient(self.bot, self.token, webhook_path='/dblwebhook', webhook_auth='DBL PASS', webhook_port=5000)

        #check to see if data is there, if it is not create data
        print("----------")
        print("Loading Save Data")
        try:
            savedata = open("data/mainsave.json", "x")
            savedata.close()
            print("-No Save Found - Creating")
            savedata = open("data/mainsave.json", "w")
            tempdata = {}
            json.dump(tempdata, savedata)
            savedata.close()
        except:
            print("-Save Found")
            print("-Loaded")
        print("Ready")
        print("----------")
        savedata = open("data/mainsave.json", "r")
        datadict = json.load(savedata)
        savedata.close()

        #task to save data every x seconds
        async def data_save():
            saveinterval = 30 #saves every saveinterval seconds
            await bot.wait_until_ready()
            while not bot.is_closed():
                await asyncio.sleep(saveinterval)
                try:
                    print("----------")
                    print(f"Attempting Save @{datetime.datetime.now().time()}")
                    savedata = open("data/mainsave.json", "w")
                    json.dump(datadict, savedata)
                    savedata.close()
                    print("Save Completed")
                except Exception as e:
                    print(f"Error saving \n{e}\n")

        #create the task
        self.savetask = bot.loop.create_task(data_save())


    #reload command -> saves and stops task first
    @commands.command()
    async def reload_game(self, ctx):
        if ctx.author.id in ownerid:
            try:
                print("----------")
                print(f"Attempting Forced Save @{datetime.datetime.now().time()}")
                savedata = open("data/mainsave.json", "w")
                json.dump(datadict, savedata)
                savedata.close()
                print("Forced Save Completed, Reloading")

                self.savetask.cancel()
                self.bot.reload_extension("cogs.game")
                embed = discord.Embed(title=f"{ctx.author.name} - Reload", description="Game module was reloaded!", color=discord.Color.green())
                await ctx.send(embed=embed)
            except Exception as e:
                embed = discord.Embed(title="Error", description=f"Game module could not be reloaded:\n```{e}```", color=discord.Color.dark_red())
                await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title="No Permission", description="You can't use this command!", color=discord.Color.dark_red())
            await ctx.send(embed=embed)

    
    #start game command
    @commands.command()
    async def start(self, ctx):
        try:
            uid = str(ctx.author.id)
            try:
                if datadict[uid]:
                    embed = discord.Embed(title="Error", description="You already started the game.", color=discord.Color.dark_red())
                    await ctx.send(embed=embed)
            except:
                datadict[uid] = {}
                datadict[uid]["reg"] = True
                datadict[uid]["name"] = ctx.author.name
                datadict[uid]["coins"] = 0
                datadict[uid]["xp"] = 0
                datadict[uid]["class"] = gamedata.CLASSLIST.NON
                datadict[uid]["weapon"] = {"type":gamedata.Weapons.STICK, "name":"Stick", "xp":0}
                datadict[uid]["armor"] = {"type":gamedata.Armor.NAKED, "name":"Naked", "xp":0}
                datadict[uid]["extra"] = {"type":gamedata.Extra.NOTHING, "name":"Nothing", "xp":0}
                datadict[uid]["hp"] = 100
                datadict[uid]["boost"] = 1 
                datadict[uid]["title"] = "Player"
                datadict[uid]["latestdrop"] = None
                datadict[uid]["lastdoor"] = None
                datadict[uid]["lastpvp"] = None
                datadict[uid]["pvpreq"] = None
                datadict[uid]["tradereq"] = None
                datadict[uid]["mosterslain"] = 0
                datadict[uid]["cheaterchanced"] = 0
                datadict[uid]["cheaterchancea"] = 0
                datadict[uid]["cheaterdifd"] = None
                datadict[uid]["cheaterdifa"] = None
                datadict[uid]["cheaterchancet"] = 0
                datadict[uid]["cheaterdift"] = None
                embed = discord.Embed(title="User Generated", description="You can now play the game.\nPlease read `<rules` before you play.\nFor commands do `<help`.", color=discord.Color.green())
                await ctx.send(embed=embed)
        except Exception as e:
            embed = discord.Embed(title="Error", description=f"```{e}```", color=discord.Color.dark_red())
            await ctx.send(embed=embed)

    
    #stats view command
    @commands.command()
    async def stats(self, ctx, briefq: str = None, uid: str = None):
        try:
            if uid == None:
                uid = str(ctx.author.id)
                xname = ctx.author.name
                avurl = ctx.author.avatar_url
                try:
                    regflag = False
                    if datadict[uid]:
                        regflag = True
                except:
                    embed = discord.Embed(title="No Data", description="Do `<start` to create a player.", color=discord.Color.dark_red())
                    await ctx.send(embed=embed)
            else:
                user = self.bot.get_user(int(uid))
                xname = user.name
                avurl = user.avatar_url
                regflag = False
                try:
                    if datadict[uid]:
                        regflag = True
                except:
                    embed = discord.Embed(title="No Data", description="This player has no data.", color=discord.Color.dark_red())
                    await ctx.send(embed=embed)

            if regflag == True:
                if briefq == None:
                    pass
                elif briefq == "-brief" or briefq == "brief":
                    statpart1 = f"""
**CHARACTER**
Name: {datadict[uid]["name"]}
Title: {datadict[uid]["title"]}
Money: {datadict[uid]["coins"]}
XP: {datadict[uid]["xp"]}
Level: {int(math.sqrt(datadict[uid]["xp"]/10))}
Class: {datadict[uid]["class"]["name"]}
HP: {datadict[uid]["hp"]}
Stat Multiplier: {round(datadict[uid]["boost"], 2)}
Monsters Slain: {datadict[uid]["mosterslain"]}
"""
                    embed = discord.Embed(title=f"{xname} - stats", description=statpart1, color=discord.Color.green())
                    embed.set_thumbnail(url=avurl)
                    await ctx.send(embed=embed)
                    return
                statpart1 = f"""
**CHARACTER**
Name: {datadict[uid]["name"]}
Title: {datadict[uid]["title"]}
Money: {datadict[uid]["coins"]}
XP: {datadict[uid]["xp"]}
Level: {int(math.sqrt(datadict[uid]["xp"]/10))}
Class: {datadict[uid]["class"]["name"]}
HP: {datadict[uid]["hp"]}
Stat Multiplier: {round(datadict[uid]["boost"], 2)}
Monsters Slain: {datadict[uid]["mosterslain"]}

**WEAPON**
Name: {datadict[uid]["weapon"]["name"]}
Type: {datadict[uid]["weapon"]["type"]["name"]}
Description: {datadict[uid]["weapon"]["type"]["desc"]}
Base Damage: {datadict[uid]["weapon"]["type"]["dmg"]}
Current Damage: {round(datadict[uid]["weapon"]["type"]["dmg"]*(((int(math.sqrt(datadict[uid]["weapon"]["xp"]/10))+1)/100)+1), 2)}
XP: {datadict[uid]["weapon"]["xp"]}
Level: {int(math.sqrt(datadict[uid]["weapon"]["xp"]/10))}
Rarity: {datadict[uid]["weapon"]["type"]["rarity"]}
                    """

                if datadict[uid]["weapon"]["type"]["perks"] != "none":
                    for perk in datadict[uid]["weapon"]["type"]["perks"]:
                        stringperk = perk["name"]
                        statpart1+=f"\nPerk: {stringperk}"
                statpart1+="\n"
                statpart1+=f"""
**ARMOR**
Name: {datadict[uid]["armor"]["name"]}
Type: {datadict[uid]["armor"]["type"]["name"]}
Description: {datadict[uid]["armor"]["type"]["desc"]}
Base Damage: {datadict[uid]["armor"]["type"]["dmg"]}
Current Damage: {round(datadict[uid]["armor"]["type"]["dmg"]*(((int(math.sqrt(datadict[uid]["armor"]["xp"]/10))+1)/100)+1), 2)}
Base Heal: {datadict[uid]["armor"]["type"]["heal"]}%
Current Heal: {round(datadict[uid]["armor"]["type"]["heal"]*(((int(math.sqrt(datadict[uid]["armor"]["xp"]/10))+1)/100)+1), 2)}%
Damage Taken: {datadict[uid]["armor"]["type"]["tank"]*100}%
XP: {datadict[uid]["armor"]["xp"]}
Level: {int(math.sqrt(datadict[uid]["armor"]["xp"]/10))}
Rarity: {datadict[uid]["armor"]["type"]["rarity"]}
                    """

                if datadict[uid]["armor"]["type"]["perks"] != "none":
                    for perk in datadict[uid]["armor"]["type"]["perks"]:
                        stringperk = perk["name"]
                        statpart1+=f"\nPerk: {stringperk}"
                statpart1+="\n"
                statpart1+=f"""
**EXTRA**
Name: {datadict[uid]["extra"]["name"]}
Type: {datadict[uid]["extra"]["type"]["name"]}
Description: {datadict[uid]["extra"]["type"]["desc"]}
Base Damage: x{datadict[uid]["extra"]["type"]["dmg"]}
Current Damage: {round(datadict[uid]["extra"]["type"]["dmg"]*(((int(math.sqrt(datadict[uid]["extra"]["xp"]/10))+1)/100)+1), 2)}
Base Heal: {datadict[uid]["extra"]["type"]["heal"]}%
Current Heal: {round(datadict[uid]["extra"]["type"]["heal"]*(((int(math.sqrt(datadict[uid]["extra"]["xp"]/10))+1)/100)+1), 2)}%
Damage Taken: x{datadict[uid]["extra"]["type"]["tank"]}
XP: {datadict[uid]["extra"]["xp"]}
Level: {int(math.sqrt(datadict[uid]["extra"]["xp"]/10))}
Rarity: {datadict[uid]["extra"]["type"]["rarity"]}
                    """

                embed = discord.Embed(title=f"{xname} - stats", description=statpart1, color=discord.Color.green())
                embed.set_thumbnail(url=avurl)
                await ctx.send(embed=embed)

        except Exception as e:
            embed = discord.Embed(title="Error", description=f"```{e}```", color=discord.Color.dark_red())
            await ctx.send(embed=embed)
            

    #dungeon stats command
    @commands.command()
    @commands.guild_only()
    async def dungeon(self, ctx):
        try:
            gid = str(ctx.guild.id)
            gregflag = False
            try:
                if datadict[gid]:
                    gregflag = True
            except:
                datadict[gid] = {}
                datadict[gid]["name"] = ctx.guild.name
                datadict[gid]["doors"] = 0
                datadict[gid]["lvl0m"] = []
                datadict[gid]["lvl5m"] = []
                datadict[gid]["lvl15m"] = []
                datadict[gid]["lvl25m"] = []
                datadict[gid]["lvl45m"] = []

                datadict[gid]["lvl0m"].append(random.choice(gamedata.RandomLists.LVL0))
                datadict[gid]["lvl0m"].append(random.choice(gamedata.RandomLists.LVL0))
                datadict[gid]["lvl0m"].append(random.choice(gamedata.RandomLists.LVL0))
                datadict[gid]["lvl0m"].append(random.choice(gamedata.RandomLists.LVL0))

                datadict[gid]["lvl5m"].append(random.choice(gamedata.RandomLists.LVL5))
                datadict[gid]["lvl5m"].append(random.choice(gamedata.RandomLists.LVL5))
                datadict[gid]["lvl5m"].append(random.choice(gamedata.RandomLists.LVL5))
                datadict[gid]["lvl5m"].append(random.choice(gamedata.RandomLists.LVL5))

                datadict[gid]["lvl15m"].append(random.choice(gamedata.RandomLists.LVL15))
                datadict[gid]["lvl15m"].append(random.choice(gamedata.RandomLists.LVL15))
                datadict[gid]["lvl15m"].append(random.choice(gamedata.RandomLists.LVL15))
                datadict[gid]["lvl15m"].append(random.choice(gamedata.RandomLists.LVL15))

                datadict[gid]["lvl25m"].append(random.choice(gamedata.RandomLists.LVL25))
                datadict[gid]["lvl25m"].append(random.choice(gamedata.RandomLists.LVL25))
                datadict[gid]["lvl25m"].append(random.choice(gamedata.RandomLists.LVL25))
                datadict[gid]["lvl25m"].append(random.choice(gamedata.RandomLists.LVL25))

                datadict[gid]["lvl45m"].append(random.choice(gamedata.RandomLists.LVL45))
                datadict[gid]["lvl45m"].append(random.choice(gamedata.RandomLists.LVL45))
                datadict[gid]["lvl45m"].append(random.choice(gamedata.RandomLists.LVL45))
                datadict[gid]["lvl45m"].append(random.choice(gamedata.RandomLists.LVL45))
            dn = datadict[gid]["name"]
            dinfo=f"""
Name: {dn}
Doors: {datadict[gid]["doors"]}
Level: {int(math.sqrt((datadict[gid]["doors"]+1)/10))}
            """
            dinfo+=f"\nLVL0 Monsters"
            for i in datadict[gid]["lvl0m"]:
                nm = i["name"]
                dinfo+=f"\n{nm}"
            dinfo+="\n"

            dinfo+=f"\nLVL5 Monsters"
            for i in datadict[gid]["lvl5m"]:
                nm = i["name"]
                dinfo+=f"\n{nm}"
            dinfo+="\n"

            dinfo+=f"\nLVL15 Monsters"
            for i in datadict[gid]["lvl15m"]:
                nm = i["name"]
                dinfo+=f"\n{nm}"
            dinfo+="\n"

            dinfo+=f"\nLVL25 Monsters"
            for i in datadict[gid]["lvl25m"]:
                nm = i["name"]
                dinfo+=f"\n{nm}"
            dinfo+="\n"

            dinfo+=f"\nLVL45 Monsters"
            for i in datadict[gid]["lvl45m"]:
                nm = i["name"]
                dinfo+=f"\n{nm}"
            dinfo+="\n"
            embed = discord.Embed(title=f"{dn} Dungeon",description=dinfo, color=discord.Color.green())
            embed.set_thumbnail(url=ctx.guild.icon_url)
            await ctx.send(embed=embed)
        
        except Exception as e:
            embed = discord.Embed(title="Error", description=f"```{e}```", color=discord.Color.dark_red())
            await ctx.send(embed=embed)


    #set class
    @commands.command()
    async def setclass(self, ctx, *, classto: str = None):
        try:
            uid = str(ctx.author.id)
            regflag = False
            try:
                if datadict[uid]:
                    regflag = True
            except:
                embed = discord.Embed(title="No Data", description="Do `<start` to create a player.", color=discord.Color.dark_red())
                await ctx.send(embed=embed)

            if regflag == True:
                if classto == None:
                    datadict[uid]["class"] = gamedata.CLASSLIST.NON
                    embed = discord.Embed(title="Success", description="Set Class to normal!", color=discord.Color.green())
                    await ctx.send(embed=embed)
                elif classto == "Fighter":
                    datadict[uid]["class"] = gamedata.CLASSLIST.FIGHTER
                    embed = discord.Embed(title="Success", description="Set Class to fighter!", color=discord.Color.green())
                    await ctx.send(embed=embed)
                elif classto == "Mage":
                    datadict[uid]["class"] = gamedata.CLASSLIST.MAGE
                    embed = discord.Embed(title="Success", description="Set Class to mage!", color=discord.Color.green())
                    await ctx.send(embed=embed)
                elif classto == "Thief":
                    datadict[uid]["class"] = gamedata.CLASSLIST.THIEF
                    embed = discord.Embed(title="Success", description="Set Class to thief!", color=discord.Color.green())
                    await ctx.send(embed=embed)
                elif classto == "Tank":
                    datadict[uid]["class"] = gamedata.CLASSLIST.TANK
                    embed = discord.Embed(title="Success", description="Set Class to tank!", color=discord.Color.green())
                    await ctx.send(embed=embed)
                elif classto == "Dark Mage":
                    datadict[uid]["class"] = gamedata.CLASSLIST.DARKMAGE
                    embed = discord.Embed(title="Success", description="Set Class to dark mage!", color=discord.Color.green())
                    await ctx.send(embed=embed)
                elif classto == "Assassin":
                    datadict[uid]["class"] = gamedata.CLASSLIST.ASSASSIN
                    embed = discord.Embed(title="Success", description="Set Class to assassin!", color=discord.Color.green())
                    await ctx.send(embed=embed) 
                else:
                    embed = discord.Embed(title="Error", description="Class Name not found!\nName is CaSe sEnSiTiVe", color=discord.Color.dark_red())
                    await ctx.send(embed=embed)
        except Exception as e:
            embed = discord.Embed(title="Error", description=f"```{e}```", color=discord.Color.dark_red())
            await ctx.send(embed=embed)


    #shop add command
    @commands.command()
    async def shopadd(self, ctx, price: int = None,typex: str = None, *, item:str = None):
        try:
            if ctx.author.id in ownerid:
                try:
                    if datadict["shop"]:
                        pass
                except:
                    datadict["shop"] = []

                if price == None:
                    embed = discord.Embed(title="Error", description="No Price Given", color=discord.Color.dark_red())
                    await ctx.send(embed=embed)

                elif typex == None:
                    embed = discord.Embed(title="Error", description="No Type Given", color=discord.Color.dark_red())
                    await ctx.send(embed=embed)

                elif item == None:
                    embed = discord.Embed(title="Error", description="No Item Given", color=discord.Color.dark_red())
                    await ctx.send(embed=embed)

                if typex == "weapon":
                    foundflag = False
                    for i in gamedata.Basics.SHOPWEAPONS:
                        if i["name"] == item:
                            itemx = i
                            foundflag = True
                    if foundflag == True:
                        shopitem = [itemx, price, typex]
                        datadict["shop"].append(shopitem)
                        embed = discord.Embed(title="Success", description=f"Added {item} for {price}.", color=discord.Color.green())
                        await ctx.send(embed=embed)
                    else:
                        embed = discord.Embed(title="Error", description="Weapon not found.", color=discord.Color.dark_red())
                        await ctx.send(embed=embed)

                elif typex == "armor":
                    foundflag = False
                    for i in gamedata.Basics.SHOPARMOR:
                        if i["name"] == item:
                            itemx = i
                            foundflag = True
                    if foundflag == True:
                        shopitem = [itemx, price, typex]
                        datadict["shop"].append(shopitem)
                        embed = discord.Embed(title="Success", description=f"Added {item} for {price}.", color=discord.Color.green())
                        await ctx.send(embed=embed)
                    else:
                        embed = discord.Embed(title="Error", description="Armor not found.", color=discord.Color.dark_red())
                        await ctx.send(embed=embed)

                elif typex == "extra":
                    foundflag = False
                    for i in gamedata.Basics.SHOPEXTRA:
                        if i["name"] == item:
                            itemx = i
                            foundflag = True
                    if foundflag == True:
                        shopitem = [itemx, price, typex]
                        datadict["shop"].append(shopitem)
                        embed = discord.Embed(title="Success", description=f"Added {item} for {price}.", color=discord.Color.green())
                        await ctx.send(embed=embed)
                    else:
                        embed = discord.Embed(title="Error", description="Extra not found.", color=discord.Color.dark_red())
                        await ctx.send(embed=embed)

            else:
                embed = discord.Embed(title="Error", description="You can't use this command!", color=discord.Color.dark_red())
                await ctx.send(embed=embed)

        except Exception as e:
            embed = discord.Embed(title="Error", description=f"```{e}```", color=discord.Color.dark_red())
            await ctx.send(embed=embed)


    #shop command
    @commands.command()
    async def shop(self, ctx):
        try:
            try:
                if datadict["shop"]:
                    pass
            except:
                datadict["shop"] = []

            if datadict["shop"] == []:
                embed = discord.Embed(title="Shop", description="The Shop is empty!", color=discord.Color.dark_red())
                await ctx.send(embed=embed)
            else:
                shopview="**Shop**"
                for i in datadict["shop"]:
                    shopview+=f"""

{i[0]["name"]}
Type: {i[2]}
Price: {i[1]}
Rarity: {i[0]["rarity"]}
WARNING: Buying this will replace your current {i[2]}!!!
                    """

                shopview+="\nBuy items with `<shop_buy [item-name]`"
                embed = discord.Embed(title="Shop", description=shopview, color=discord.Color.green())
                await ctx.send(embed=embed)

        except Exception as e:
            embed = discord.Embed(title="Error", description=f"```{e}```", color=discord.Color.dark_red())
            await ctx.send(embed=embed)


    #shop remove
    @commands.command()
    async def shoprem(self, ctx, *,item:str = None):
        try:
            if ctx.author.id in ownerid:
                try:
                    if datadict["shop"]:
                        pass
                except:
                    datadict["shop"] = []

                foundflag = False
                for i in datadict["shop"]:
                    if i[0]["name"] == item:
                        foundflag = True
                        datadict["shop"].remove(i)
                
                if foundflag == True:
                    embed = discord.Embed(title="Success", description="Removed Item from Shop.", color=discord.Color.green())
                    await ctx.send(embed=embed)

                else:
                    embed = discord.Embed(title="Error", description="Item not found.", color=discord.Color.dark_red())
                    await ctx.send(embed=embed)

            else:
                embed = discord.Embed(title="Error", description="You can't use this command!", color=discord.Color.dark_red())
                await ctx.send(embed=embed)

        except Exception as e:
            embed = discord.Embed(title="Error", description=f"```{e}```", color=discord.Color.dark_red())
            await ctx.send(embed=embed)


    #shop buy command
    @commands.command()
    async def shop_buy(self, ctx, *,item: str = None):
        try:
            uid = str(ctx.author.id)
            if uid in datadict["bl"]:
                return
            regflag = False
            try:
                if datadict[uid]:
                    regflag = True
            except:
                embed = discord.Embed(title="No Data", description="Do `<start` to create a player.", color=discord.Color.dark_red())
                await ctx.send(embed=embed)

            if regflag == True:
                try:
                    if datadict["shop"]:
                        pass
                except:
                    datadict["shop"] = []

                foundflag = False
                for i in datadict["shop"]:
                    if i[0]["name"] == item:
                        foundflag = True
                        xitem = i
                        break
                
                if foundflag == True:

                    if datadict[uid]["coins"] < xitem[1]:
                        embed = discord.Embed(title="Error", description="You can't afford this.", color=discord.Color.dark_red())
                        await ctx.send(embed=embed)
                        return
                    else:
                        datadict[uid]["coins"] -= xitem[1]

                    if xitem[2] == "weapon":
                        datadict[uid]["weapon"] = {"name":item, "type":xitem[0], "xp":0}
                    elif xitem[2] == "armor":
                        datadict[uid]["armor"] = {"name":item, "type":xitem[0], "xp":0}
                    elif xitem[2] == "extra":
                        datadict[uid]["extra"] = {"name":item, "type":xitem[0], "xp":0}
                    embed = discord.Embed(title="Success", description=f"Bought {item} for {xitem[1]}.", color=discord.Color.green())
                    await ctx.send(embed=embed)

                else:
                    embed = discord.Embed(title="Error", description="Item not found.", color=discord.Color.dark_red())
                    await ctx.send(embed=embed)
                
        except Exception as e:
            embed = discord.Embed(title="Error", description=f"```{e}```", color=discord.Color.dark_red())
            await ctx.send(embed=embed) 


    #coinflip
    @commands.command()
    async def coinflip(self, ctx, wager: int = None):
        try:
            uid = str(ctx.author.id)
            if uid in datadict["bl"]:
                return
            regflag = False
            try:
                if datadict[uid]:
                    regflag = True
            except:
                embed = discord.Embed(title="No Data", description="Do `<start` to create a player.", color=discord.Color.dark_red())
                await ctx.send(embed=embed)

            if regflag == True:
                if wager == None:
                    embed = discord.Embed(title="Error", description="Please place a bet.", color=discord.Color.dark_red())
                    await ctx.send(embed=embed)
                    return

                if datadict[uid]["coins"] < wager:
                    embed = discord.Embed(title="Error", description="You cant afford this.", color=discord.Color.dark_red())
                    await ctx.send(embed=embed)

                else:
                    wq = random.randint(1,3)
                    if wq == 1:
                        datadict[uid]["coins"] += wager
                        embed = discord.Embed(title=f"{ctx.author.name} - Coinflip", description=f"You win +{wager} coins.", color=discord.Color.green())
                        await ctx.send(embed=embed)
                    else:
                        datadict[uid]["coins"] -= wager
                        embed = discord.Embed(title=f"{ctx.author.name} - Coinflip", description=f"You lose -{wager} coins.", color=discord.Color.dark_red())
                        await ctx.send(embed=embed)

        except Exception as e:
            embed = discord.Embed(title="Error", description=f"```{e}```", color=discord.Color.dark_red())
            await ctx.send(embed=embed)


    #slots
    @commands.command()
    async def slots(self, ctx, wager: int = None):
        try:
            uid = str(ctx.author.id)
            if uid in datadict["bl"]:
                return
            regflag = False
            try:
                if datadict[uid]:
                    regflag = True
            except:
                embed = discord.Embed(title="No Data", description="Do `<start` to create a player.", color=discord.Color.dark_red())
                await ctx.send(embed=embed)

            if regflag == True:
                if wager == None:
                    embed = discord.Embed(title="Error", description="Please place a bet.", color=discord.Color.dark_red())
                    await ctx.send(embed=embed)
                    return

                if datadict[uid]["coins"] < wager:
                    embed = discord.Embed(title="Error", description="You cant afford this.", color=discord.Color.dark_red())
                    await ctx.send(embed=embed)

                else:
                    slotlist = ["🔪","🔪","🍇","🍇","🍒","🍒","💚"]
                    slotres = []
                    for i in range(3):
                        slotres.append(random.choice(slotlist))
                    if slotres[0] == slotres[1] == slotres[2]:
                        if slotres[0] == "💚":
                            win = 25
                        else:
                            win = 10
                    else:
                        win = -1
                    datadict[uid]["coins"]+=wager*win
                    smsg = await ctx.send("Rolling...")
                    await asyncio.sleep(.2)
                    for i in range(4):
                        if i == 3:
                            slotd = slotres
                            if win == -1:
                                stext = f"You lose -{wager}!"
                                color = discord.Color.dark_red()
                            else:
                                stext = f"You win +{wager*win}!"
                                color = discord.Color.green()
                        else:
                            slotd = []
                            for i in range(3):
                                slotd.append(random.choice(slotlist))
                            stext = "Rolling..."
                            color = color = discord.Color.orange()
                        embed = discord.Embed(title=f"{ctx.author.name} - Slots", description=f"""
{stext}

:diamonds::red_square::red_square::red_square::diamonds:
:red_square::small_red_triangle_down::small_red_triangle_down::small_red_triangle_down::red_square:
:red_square:{slotd[0]}{slotd[1]}{slotd[2]}:red_square:
:red_square::small_red_triangle::small_red_triangle::small_red_triangle::red_square:
:diamonds::red_square::red_square::red_square::diamonds:
                        """, color=color)
                        await smsg.edit(content = None, embed=embed)
                        await asyncio.sleep(.4)

        except Exception as e:
            embed = discord.Embed(title="Error", description=f"```{e}```", color=discord.Color.dark_red())
            await ctx.send(embed=embed)


    #train command
    @commands.command()
    async def train(self, ctx):
        try:
            uid = str(ctx.author.id)
            if uid in datadict["bl"]:
                return
            regflag = False
            try:
                if datadict[uid]:
                    regflag = True
            except:
                embed = discord.Embed(title="No Data", description="Do `<start` to create a player.", color=discord.Color.dark_red())
                await ctx.send(embed=embed)
            if regflag == True:
                regflag = False
                try:
                    if datadict[uid]["lasttrain"]:
                        regflag = True
                except:
                    regflag = False
                if regflag == False:
                    datadict[uid]["lasttrain"] = None

                if datadict[uid]["lasttrain"] != None:
                    if datadict[uid]["lasttrain"]:
                        timenow = datetime.datetime.now()
                        difference = timenow - datetime.datetime.strptime(datadict[uid]["lasttrain"], "%Y-%m-%d %H:%M:%S.%f")
                        dif = difference.total_seconds()
                        if int(difference.total_seconds()/60) < 5:
                            embed = discord.Embed(title="Cooldown", description=f"You can train again in {str(int(difference.total_seconds()/60)-5)[1:]}min", color=discord.Color.dark_red())
                            await ctx.send(embed=embed)
                            return
                else:
                    dif = None

                #anticheat code
                if dif != None:
                    if datadict[uid]["cheaterdift"] != None:
                        difmin = dif-3
                        difmax = dif+3
                        if datadict[uid]["cheaterdift"] > difmin and datadict[uid]["cheaterdift"] < difmax:
                            datadict[uid]["cheaterchancet"] += 1
                        else:
                            datadict[uid]["cheaterchancet"] = 0
                        if datadict[uid]["cheaterchancet"] > 20:
                            datadict["bl"].append(uid)

                    datadict[uid]["cheaterdift"] = dif
                
                datadict[uid]["lasttrain"] = str(datetime.datetime.now())
                xpg = 15
                datadict[uid]["weapon"]["xp"] += xpg
                datadict[uid]["armor"]["xp"] += xpg
                datadict[uid]["extra"]["xp"] += xpg
                embed = discord.Embed(title="Train", description=f"You train with your gear.\n+{xpg} weapon xp\n+{xpg} armor xp\n+{xpg} extra xp", color=discord.Color.green())
                await ctx.send(embed=embed)

        except Exception as e:
            embed = discord.Embed(title="Error", description=f"```{e}```", color=discord.Color.dark_red())
            await ctx.send(embed=embed)


    #reset train cooldown
    @commands.command()
    async def rtc(self, ctx, uid: str = None):
        try:
            if ctx.author.id in ownerid:
                if uid == None:
                    uid = str(ctx.author.id)
                datadict[uid]["lasttrain"] = None
                embed = discord.Embed(title="Success", description=f"Train cooldown reset!", color=discord.Color.green())
                await ctx.send(embed=embed)
            else:
                embed = discord.Embed(title="No Permission", description=f"You can't use this command!", color=discord.Color.dark_red())
                await ctx.send(embed=embed)
        except Exception as e:
            embed = discord.Embed(title="Error", description=f"```{e}```", color=discord.Color.dark_red())
            await ctx.send(embed=embed)


    #daily command
    @commands.command()
    async def daily(self, ctx):
        try:
            uid = str(ctx.author.id)
            if uid in datadict["bl"]:
                return
            regflag = False
            try:
                if datadict[uid]:
                    regflag = True
            except:
                embed = discord.Embed(title="No Data", description="Do `<start` to create a player.", color=discord.Color.dark_red())
                await ctx.send(embed=embed)
            if regflag == True:
                regflag = False
                try:
                    if datadict[uid]["lastdaily"]:
                        regflag = True
                except:
                    regflag = False
                if regflag == False:
                    datadict[uid]["lastdaily"] = None

                if datadict[uid]["lastdaily"] != None:
                    if datadict[uid]["lastdaily"]:
                        timenow = datetime.datetime.now()
                        difference = timenow - datetime.datetime.strptime(datadict[uid]["lastdaily"], "%Y-%m-%d %H:%M:%S.%f")
                        if int(difference.total_seconds()/3600) < 24:
                            embed = discord.Embed(title="Cooldown", description=f"You can get daily again in {str(int(difference.total_seconds()/3600)-24)[1:]}h\nReset you cooldown with `<vote`!", color=discord.Color.dark_red())
                            await ctx.send(embed=embed)
                            return
                
                datadict[uid]["lastdaily"] = str(datetime.datetime.now())
                cpg = 100 * int(math.sqrt(datadict[uid]["xp"]/10))
                datadict[uid]["coins"] += cpg
                embed = discord.Embed(title="Daily", description=f"+{cpg} coins!", color=discord.Color.green())
                await ctx.send(embed=embed)

        except Exception as e:
            embed = discord.Embed(title="Error", description=f"```{e}```", color=discord.Color.dark_red())
            await ctx.send(embed=embed)


    #reset daily cooldown
    @commands.command()
    async def rdcc(self, ctx, uid: str = None):
        try:
            if ctx.author.id in ownerid:
                if uid == None:
                    uid = str(ctx.author.id)
                datadict[uid]["lastdaily"] = None
                embed = discord.Embed(title="Success", description=f"Daily cooldown reset!", color=discord.Color.green())
                await ctx.send(embed=embed)
            else:
                embed = discord.Embed(title="No Permission", description=f"You can't use this command!", color=discord.Color.dark_red())
                await ctx.send(embed=embed)
        except Exception as e:
            embed = discord.Embed(title="Error", description=f"```{e}```", color=discord.Color.dark_red())
            await ctx.send(embed=embed)


    #storage buy
    @commands.command()
    async def buy_storage(self, ctx):
        try:
            uid = str(ctx.author.id)
            if uid in datadict["bl"]:
                return
            regflag = False
            try:
                if datadict[uid]["hasstorage"]:
                    regflag = True
                    embed = discord.Embed(title="Error", description="You already have a storage.", color=discord.Color.dark_red())
                    await ctx.send(embed=embed)
            except: pass
            if regflag == False:
                if int(math.sqrt((datadict[uid]["xp"]+1)/10)) < 10:
                    embed = discord.Embed(title="Error", description="You need to be lvl 10 to buy a storage.", color=discord.Color.dark_red())
                    await ctx.send(embed=embed)
                else:
                    if datadict[uid]["coins"] < 10000:
                        embed = discord.Embed(title="Error", description="You can't afford this.", color=discord.Color.dark_red())
                        await ctx.send(embed=embed)
                    else:
                        datadict[uid]["storage"] = {}
                        datadict[uid]["coins"]-=10000
                        datadict[uid]["hasstorage"] = True
                        datadict[uid]["storage"]["weapon"] = {"type":gamedata.Weapons.STICK, "name":"Stick", "xp":0}
                        datadict[uid]["storage"]["armor"] = {"type":gamedata.Armor.NAKED, "name":"Naked", "xp":0}
                        datadict[uid]["storage"]["extra"] = {"type":gamedata.Extra.NOTHING, "name":"Nothing", "xp":0}
                        embed = discord.Embed(title="Storage", description="You now own a storage.", color=discord.Color.green())
                        await ctx.send(embed=embed)

        except Exception as e:
            embed = discord.Embed(title="Error", description=f"```{e}```", color=discord.Color.dark_red())
            await ctx.send(embed=embed)


    #store command
    @commands.command()
    async def store(self, ctx, typex: str = None):
        try:
            uid = str(ctx.author.id)
            if uid in datadict["bl"]:
                return
            regflag = False
            try:
                if datadict[uid]["hasstorage"]:
                    regflag = True
            except:
                embed = discord.Embed(title="No Storage", description="You can buy one with `<buy_storage` for 10k coins.", color=discord.Color.dark_red())
                await ctx.send(embed=embed)
            
            if regflag == True:
                if typex != "armor" and typex != "weapon" and typex != "extra":
                    embed = discord.Embed(title="Error", description="Enter item to store(weapon|armor|extra).", color=discord.Color.dark_red())
                    await ctx.send(embed=embed)
                else:
                    tostore = datadict[uid][typex]
                    toget = datadict[uid]["storage"][typex]
                    storename = tostore["name"]
                    getname = toget["name"]
                    datadict[uid][typex] = toget
                    datadict[uid]["storage"][typex] = tostore
                    embed = discord.Embed(title="Storage", description=f"Took your {getname}, and stored your {storename}.", color=discord.Color.green())
                    await ctx.send(embed=embed)

        except Exception as e:
            embed = discord.Embed(title="Error", description=f"```{e}```", color=discord.Color.dark_red())
            await ctx.send(embed=embed)


    #view storage command
    @commands.command()
    async def view_storage(self, ctx):
        try:
            uid = str(ctx.author.id)
            regflag = False
            try:
                if datadict[uid]["hasstorage"]:
                    regflag = True
            except:
                embed = discord.Embed(title="No Storage", description="You can buy one with `<buy_storage` for 10k coins.", color=discord.Color.dark_red())
                await ctx.send(embed=embed)
            
            if regflag == True:
                    embed = discord.Embed(title=f"Storage - {ctx.author.name}", description=f"""
**WEAPON**
Name: {datadict[uid]["storage"]["weapon"]["name"]}
Type: {datadict[uid]["storage"]["weapon"]["type"]["name"]}
XP: {datadict[uid]["storage"]["weapon"]["xp"]}
Level: {int(math.sqrt(datadict[uid]["storage"]["weapon"]["xp"]/10))}
Rarity: {datadict[uid]["storage"]["weapon"]["type"]["rarity"]}

**ARMOR**
Name: {datadict[uid]["storage"]["armor"]["name"]}
Type: {datadict[uid]["storage"]["armor"]["type"]["name"]}
XP: {datadict[uid]["storage"]["armor"]["xp"]}
Level: {int(math.sqrt(datadict[uid]["storage"]["armor"]["xp"]/10))}
Rarity: {datadict[uid]["storage"]["armor"]["type"]["rarity"]}

**EXTRA**
Name: {datadict[uid]["storage"]["extra"]["name"]}
Type: {datadict[uid]["storage"]["extra"]["type"]["name"]}
XP: {datadict[uid]["storage"]["extra"]["xp"]}
Level: {int(math.sqrt(datadict[uid]["storage"]["armor"]["xp"]/10))}
Rarity: {datadict[uid]["storage"]["extra"]["type"]["rarity"]}
                    """, color=discord.Color.green())
                    await ctx.send(embed=embed)

        except Exception as e:
            embed = discord.Embed(title="Error", description=f"```{e}```", color=discord.Color.dark_red())
            await ctx.send(embed=embed)


    #item trading
    @commands.command()
    async def trade(self, ctx, uxvc: str = None, item: str = None):
        try:
            uid = str(ctx.author.id)
            if uid in datadict["bl"]:
                return
            regflag = False
            try:
                if datadict[uid]:
                    regflag = True
            except:
                embed = discord.Embed(title="No Data", description="Do `<start` to create a player.", color=discord.Color.dark_red())
                await ctx.send(embed=embed)

            if regflag == True:
                if uxvc == None:
                    embed = discord.Embed(title="Error", description="No user mentioned.", color=discord.Color.dark_red())
                    await ctx.send(embed=embed)
                    return
                if item == None:
                    embed = discord.Embed(title="Error", description="No item type given.", color=discord.Color.dark_red())
                    await ctx.send(embed=embed)
                    return
                try:
                    opp = ctx.message.mentions[0]
                except:
                    embed = discord.Embed(title="Error", description="No user mentioned.", color=discord.Color.dark_red())
                    await ctx.send(embed=embed)
                    return
                oid = str(opp.id)
                if oid == uid:
                    embed = discord.Embed(title="Error", description="You can't trade yourself.", color=discord.Color.dark_red())
                    await ctx.send(embed=embed)
                    return

                regflag2 = False
                try:
                    if datadict[oid]:
                        regflag2 = True
                except:
                    embed = discord.Embed(title="No Data", description="The user you mentioned does not have a Profile.", color=discord.Color.dark_red())
                    await ctx.send(embed=embed)

                if regflag2 == True:
                    if item == "weapon" or item == "armor" or item == "extra":
                        datadict[oid]["tradereq"] = [ctx.author.id, item]
                        pname = datadict[uid][item]["type"]["name"]
                        oname = datadict[oid][item]["type"]["name"]
                        embed = discord.Embed(title="Trade", description=f"Asked {opp.name} for trade:\nHis **{pname}** for Your **{oname}**.", color=discord.Color.green())
                        await ctx.send(embed=embed)
                    else:
                        embed = discord.Embed(title="Error", description="Not a valit item type (weapon|armor|extra).", color=discord.Color.dark_red())
                        await ctx.send(embed=embed)

        except Exception as e:
            embed = discord.Embed(title="Error", description=f"```{e}```", color=discord.Color.dark_red())
            await ctx.send(embed=embed) 


    #trade decline command
    @commands.command()
    async def trade_decline(self, ctx):
        try:
            uid = str(ctx.author.id)
            regflag = False
            try:
                if datadict[uid]:
                    regflag = True
            except:
                embed = discord.Embed(title="No Data", description="Do `<start` to create a player.", color=discord.Color.dark_red())
                await ctx.send(embed=embed)

            if regflag == True:
                if datadict[uid]["tradereq"] == None:
                    embed = discord.Embed(title="Error", description="You don't have a trade request.", color=discord.Color.dark_red())
                    await ctx.send(embed=embed)
                else:
                    uname = self.bot.get_user(datadict[uid]["tradereq"][0]).name
                    embed = discord.Embed(title="Trade", description=f"You declines the request from {uname}.", color=discord.Color.green())
                    await ctx.send(embed=embed)
                    datadict[uid]["tradereq"] = None
        
        except Exception as e:
            embed = discord.Embed(title="Error", description=f"```{e}```", color=discord.Color.dark_red())
            await ctx.send(embed=embed)


    #trade accept
    @commands.command()
    async def trade_accept(self, ctx):
        try:
            uid = str(ctx.author.id)
            if uid in datadict["bl"]:
                return
            regflag = False
            try:
                if datadict[uid]:
                    regflag = True
            except:
                embed = discord.Embed(title="No Data", description="Do `<start` to create a player.", color=discord.Color.dark_red())
                await ctx.send(embed=embed)

            if regflag == True:
                if datadict[uid]["tradereq"] == None:
                    embed = discord.Embed(title="Error", description="You don't have a trade request.", color=discord.Color.dark_red())
                    await ctx.send(embed=embed)
                else:
                    opp = self.bot.get_user(datadict[uid]["tradereq"][0])
                    oid = str(opp.id)
                    oppitem = datadict[oid][datadict[uid]["tradereq"][1]]
                    pitem = datadict[uid][datadict[uid]["tradereq"][1]]
                    datadict[uid][datadict[uid]["tradereq"][1]] = oppitem
                    datadict[oid][datadict[uid]["tradereq"][1]] = pitem
                    piname = pitem["type"]["name"]
                    opiname = oppitem["type"]["name"]
                    embed = discord.Embed(title="Trade", description=f"You trade your {piname} for {opp.name}s {opiname}.", color=discord.Color.green())
                    await ctx.send(embed=embed)
                    datadict[uid]["tradereq"] = None
        
        except Exception as e:
            embed = discord.Embed(title="Error", description=f"```{e}```", color=discord.Color.dark_red())
            await ctx.send(embed=embed)


    #pvp offer
    @commands.command()
    async def pvp(self, ctx, uxvc: str = None, wager: int = None):
        try:
            uid = str(ctx.author.id)
            if uid in datadict["bl"]:
                return
            regflag = False
            try:
                if datadict[uid]:
                    regflag = True
            except:
                embed = discord.Embed(title="No Data", description="Do `<start` to create a player.", color=discord.Color.dark_red())
                await ctx.send(embed=embed)

            if regflag == True:
                if uxvc == None:
                    embed = discord.Embed(title="Error", description="No user mentioned.", color=discord.Color.dark_red())
                    await ctx.send(embed=embed)
                    return
                if wager == None:
                    wager = 0
                try:
                    opp = ctx.message.mentions[0]
                except:
                    embed = discord.Embed(title="Error", description="No user mentioned.", color=discord.Color.dark_red())
                    await ctx.send(embed=embed)
                    return
                oid = str(opp.id)
                if oid == uid:
                    embed = discord.Embed(title="Error", description="You can't fight yourself.", color=discord.Color.dark_red())
                    await ctx.send(embed=embed)
                    return

                regflag2 = False
                try:
                    if datadict[oid]:
                        regflag2 = True
                except:
                    embed = discord.Embed(title="No Data", description="Opponent does not have a Profile.", color=discord.Color.dark_red())
                    await ctx.send(embed=embed)

                if regflag2 == True:
                    datadict[oid]["pvpreq"] = [ctx.author.id, wager]
                    embed = discord.Embed(title="PvP", description=f"{ctx.author.name} asks <@{opp.id}> for a pvp match!\nWager: {wager}", color=discord.Color.green())
                    await ctx.send(embed=embed)

        except Exception as e:
            embed = discord.Embed(title="Error", description=f"```{e}```", color=discord.Color.dark_red())
            await ctx.send(embed=embed)


    #pvp decline command
    @commands.command()
    async def pvp_decline(self, ctx):
        try:
            uid = str(ctx.author.id)
            regflag = False
            try:
                if datadict[uid]:
                    regflag = True
            except:
                embed = discord.Embed(title="No Data", description="Do `<start` to create a player.", color=discord.Color.dark_red())
                await ctx.send(embed=embed)

            if regflag == True:
                if datadict[uid]["pvpreq"] == None:
                    embed = discord.Embed(title="Error", description="You don't have a pvp request.", color=discord.Color.dark_red())
                    await ctx.send(embed=embed)
                else:
                    uname = self.bot.get_user(datadict[uid]["pvpreq"][0]).name
                    embed = discord.Embed(title="PvP", description=f"You declines the request from {uname}.", color=discord.Color.green())
                    await ctx.send(embed=embed)
                    datadict[uid]["pvpreq"] = None
        
        except Exception as e:
            embed = discord.Embed(title="Error", description=f"```{e}```", color=discord.Color.dark_red())
            await ctx.send(embed=embed)


    #pvp command
    @commands.command()
    async def pvp_accept(self, ctx):
        try:
            uid = str(ctx.author.id)
            if uid in datadict["bl"]:
                return
            regflag = False
            try:
                if datadict[uid]:
                    regflag = True
            except:
                embed = discord.Embed(title="No Data", description="Do `<start` to create a player.", color=discord.Color.dark_red())
                await ctx.send(embed=embed)

            if regflag == False:
                return

            uid = str(ctx.author.id)
            if datadict[uid]["pvpreq"] == None:
                embed = discord.Embed(title="Error", description="You don't have a pvp request.", color=discord.Color.dark_red())
                await ctx.send(embed=embed)
            else:
                opp = self.bot.get_user(datadict[uid]["pvpreq"][0])
                oid = str(opp.id)

                if datadict[uid]["coins"] <  datadict[uid]["pvpreq"][1]:
                    embed = discord.Embed(title="Error", description=f"You can't afford the wager.", color=discord.Color.dark_red())
                    await ctx.send(embed=embed)
                    return
                elif datadict[oid]["coins"] <  datadict[uid]["pvpreq"][1]:
                    embed = discord.Embed(title="Error", description=f"Your opponent can't afford the wager.", color=discord.Color.dark_red())
                    await ctx.send(embed=embed)
                    return

                if datadict[uid]["lastpvp"] == None:
                    pass
                else:
                    timenow = datetime.datetime.now()
                    difference = timenow - datetime.datetime.strptime(datadict[uid]["lastpvp"], "%Y-%m-%d %H:%M:%S.%f")
                    if int(difference.total_seconds()/60) < 5:
                        embed = discord.Embed(title="Cooldown", description=f"You can pvp again in {str(int(difference.total_seconds()/60)-5)[1:]}min", color=discord.Color.dark_red())
                        await ctx.send(embed=embed)
                        return
                if datadict[oid]["lastpvp"] == None:
                    pass
                else:
                    timenow = datetime.datetime.now()
                    difference = timenow - datetime.datetime.strptime(datadict[oid]["lastpvp"], "%Y-%m-%d %H:%M:%S.%f")
                    if int(difference.total_seconds()/60) < 5:
                        embed = discord.Embed(title="Cooldown", description=f"Your opponent can pvp again in {str(int(difference.total_seconds()/60)-5)[1:]}min", color=discord.Color.dark_red())
                        await ctx.send(embed=embed)
                        return
                datadict[uid]["lastpvp"] = str(datetime.datetime.now())
                datadict[oid]["lastpvp"] = str(datetime.datetime.now())

                #player1 stat building
                #weapon
                php = datadict[uid]["hp"]
                dmg = datadict[uid]["weapon"]["type"]["dmg"]
                shieldbreak = 0
                heal = 0
                sbc = 0
                if datadict[uid]["weapon"]["type"]["perks"] != "none":
                    for i in datadict[uid]["weapon"]["type"]["perks"]:
                        dmg += i["dmg"] 
                        dmg += i["sharp"]
                        sbc += i["shieldbreak"]
                        heal += i["heal"]
                        if sbc > 100:
                            sbc = 100
                    shieldbreak = dmg*(sbc/100)
                    dmg-=shieldbreak

                #armor
                dmg+=datadict[uid]["armor"]["type"]["dmg"]
                heal+=datadict[uid]["armor"]["type"]["heal"]
                tank = datadict[uid]["armor"]["type"]["tank"]
                negatechance = 0
                returndmg = 0

                if datadict[uid]["armor"]["type"]["perks"] != "none":
                    for i in datadict[uid]["armor"]["type"]["perks"]:
                        dmg+=i["dmg"]
                        heal+=i["heal"]
                        tank*=i["tank"]
                        negatechance+=i["negatechance"]
                        returndmg+=i["returndmg"]

                #extra
                dmg*=datadict[uid]["extra"]["type"]["dmg"]
                heal+=datadict[uid]["extra"]["type"]["heal"]
                tank*=datadict[uid]["extra"]["type"]["tank"]

                #boost
                dmg*=datadict[uid]["boost"]
                heal*=datadict[uid]["boost"]

                #class
                dmg*=datadict[uid]["class"]["dmgm"]
                heal+=datadict[uid]["class"]["heal"]
                tank*=datadict[uid]["class"]["tanks"]
                if datadict[uid]["class"]["perks"] != "none":
                    for i in datadict[uid]["class"]["perks"]:
                        dmg*=i["dmg"]
                        heal+=i["heal"]
                        negatechance+=i["negatechance"]


                #player2 stat building
                #weapon
                ohp = datadict[oid]["hp"]
                odmg = datadict[oid]["weapon"]["type"]["dmg"]
                oshieldbreak = 0
                oheal = 0
                sbc = 0
                if datadict[oid]["weapon"]["type"]["perks"] != "none":
                    for i in datadict[oid]["weapon"]["type"]["perks"]:
                        odmg += i["dmg"] 
                        odmg += i["sharp"]
                        sbc += i["shieldbreak"]
                        oheal += i["heal"]
                        if sbc > 100:
                            sbc = 100
                    oshieldbreak = odmg*(sbc/100)
                    odmg-=shieldbreak

                #armor
                odmg+=datadict[oid]["armor"]["type"]["dmg"]
                oheal+=datadict[oid]["armor"]["type"]["heal"]
                otank = datadict[oid]["armor"]["type"]["tank"]
                onegatechance = 0
                oreturndmg = 0

                if datadict[oid]["armor"]["type"]["perks"] != "none":
                    for i in datadict[oid]["armor"]["type"]["perks"]:
                        odmg+=i["dmg"]
                        oheal+=i["heal"]
                        otank*=i["tank"]
                        onegatechance+=i["negatechance"]
                        oreturndmg+=i["returndmg"]

                #extra
                odmg*=datadict[oid]["extra"]["type"]["dmg"]
                oheal+=datadict[oid]["extra"]["type"]["heal"]
                otank*=datadict[oid]["extra"]["type"]["tank"]

                #boost
                odmg*=datadict[oid]["boost"]
                oheal*=datadict[oid]["boost"]

                #class
                odmg*=datadict[oid]["class"]["dmgm"]
                oheal+=datadict[oid]["class"]["heal"]
                otank*=datadict[oid]["class"]["tanks"]
                if datadict[oid]["class"]["perks"] != "none":
                    for i in datadict[oid]["class"]["perks"]:
                        odmg*=i["dmg"]
                        oheal+=i["heal"]
                        onegatechance+=i["negatechance"]
                

                counter = 0
                pname = datadict[uid]["name"]
                oname = datadict[oid]["name"]
                eventlog = f"**{pname} vs. {oname}**\n"
                omaxhp = ohp
                pmaxhp = php
                while php > 0 and ohp > 0:
                    counter+=1
                    eventlog+=(f"\n**Round {counter}:**")
                    #player1 hits opponent
                    negate = random.randint(0, 100)
                    if negate < onegatechance:
                        eventlog+=(f"\n{oname} Dodges")
                    else:
                        ohp-=(dmg*otank)+shieldbreak
                        eventlog+=(f"\n{pname} deals {round((dmg*otank)+shieldbreak, 2)}dmg")

                    if ohp <= 0:
                        break
                    if php <= 0:
                        break

                    php-=((dmg*tank)+shieldbreak)*(oreturndmg/100)
                    eventlog+=(f"\n{pname} takes {round(((dmg*tank)+shieldbreak)*(oreturndmg/100), 2)}dmg from attack.")

                    if ohp <= 0:
                        break
                    if php <= 0:
                        break

                    ohp+=omaxhp*(oheal/100)
                    if ohp > omaxhp:
                        ohp = omaxhp
                    eventlog+=(f"\n{oname} heals!")
                    eventlog+=(f"\n{oname} is at {round(ohp, 2)}/{omaxhp}hp!")
                    eventlog+=("\n")

                    #player2 hits opponent
                    negate = random.randint(0, 100)
                    if negate < negatechance:
                        eventlog+=(f"\n{pname} Dodges")
                    else:
                        php-=(odmg*tank)+oshieldbreak
                        eventlog+=(f"\n{oname} deals {round((odmg*tank)+oshieldbreak, 2)}dmg")

                    if ohp <= 0:
                        break
                    if php <= 0:
                        break

                    ohp-=((odmg*tank)+oshieldbreak)*(returndmg/100)
                    eventlog+=(f"\n{oname} takes {round(((odmg*tank)+oshieldbreak)*(returndmg/100), 2)}dmg from attack.")

                    if ohp <= 0:
                        break
                    if php <= 0:
                        break

                    php+=pmaxhp*(heal/100)
                    if php > pmaxhp:
                        php = pmaxhp
                    eventlog+=(f"\n{pname} heals!")
                    eventlog+=(f"\n{pname} is at {round(php, 2)}/{pmaxhp}hp!")
                    eventlog+=("\n")

                    eventlog+=("**Round End**")
                    eventlog+=(f"\n{pname} is at {round(php, 2)}/{pmaxhp}hp!")
                    eventlog+=(f"\n{oname} is at {round(ohp, 2)}/{omaxhp}hp!\n\n")
                    ovrflag = False
                    if counter > 30:
                        ovrflag = True
                        break
                    if len(eventlog) > 1500:
                        embed = discord.Embed(title="PVP", description=eventlog, color=discord.Color.orange())
                        await ctx.send(embed=embed)
                        eventlog = ""

                eventlog+=("\n\n**Match End**")
                eventlog+=(f"\n{pname} is at {round(php, 2)}/{pmaxhp}hp!")
                eventlog+=(f"\n{oname} is at {round(ohp, 2)}/{omaxhp}hp!\n\n")
                if php <= 0:
                    owin = True
                    eventlog+=(f"\n\n**{oname} Wins!**")
                elif ohp <= 0:
                    owin = False
                    eventlog+=(f"\n\n**{pname} Wins!**")
                elif ovrflag == True:
                    eventlog+=(f"\n\n**Nobody Wins!**")
                    owin = None

                if owin == False:
                    cw = datadict[uid]["pvpreq"][1]
                    eventlog+=f"\n\n{pname} wins {cw} coins.\n{oname} loses {cw} coins."
                    datadict[oid]["coins"] -= cw
                    datadict[uid]["coins"] += cw

                elif owin == True:
                    cw = datadict[uid]["pvpreq"][1]
                    eventlog+=f"\n\n{oname} wins {cw} coins.\n{pname} loses {cw} coins."
                    datadict[oid]["coins"] += cw
                    datadict[uid]["coins"] -= cw
                elif owin == None:
                    eventlog+=f"\nToo many rounds. Nobody wins."
                
                datadict[uid]["pvpreq"] = None
                embed = discord.Embed(title="PVP", description=eventlog, color=discord.Color.orange())
                await ctx.send(embed=embed)
        
        except Exception as e:
            embed = discord.Embed(title="Error", description=f"```{e}```", color=discord.Color.dark_red())
            await ctx.send(embed=embed)


    #reset pvp cooldown
    @commands.command()
    async def rpc(self, ctx, uid: str = None):
        try:
            if ctx.author.id in ownerid:
                if uid == None:
                    uid = str(ctx.author.id)
                datadict[uid]["lastpvp"] = None
                embed = discord.Embed(title="Success", description=f"Door cooldown reset!", color=discord.Color.green())
                await ctx.send(embed=embed)
            else:
                embed = discord.Embed(title="No Permission", description=f"You can't use this command!", color=discord.Color.dark_red())
                await ctx.send(embed=embed)
        except Exception as e:
            embed = discord.Embed(title="Error", description=f"```{e}```", color=discord.Color.dark_red())
            await ctx.send(embed=embed)


    #door command
    @commands.command()
    @commands.guild_only()
    async def door(self, ctx):
        try:
            gid = str(ctx.guild.id)
            uid = str(ctx.author.id)
            if uid in datadict["bl"]:
                return
            regflag = False
            try:
                if datadict[uid]:
                    regflag = True
            except:
                embed = discord.Embed(title="No Data", description="Do `<start` to create a player.", color=discord.Color.dark_red())
                await ctx.send(embed=embed)
                return

            if regflag == True:
                if datadict[uid]["lastdoor"] == None:
                    dif = None
                    pass
                else:
                    timenow = datetime.datetime.now()
                    difference = timenow - datetime.datetime.strptime(datadict[uid]["lastdoor"], "%Y-%m-%d %H:%M:%S.%f")
                    dif = difference.total_seconds()
                    if int(difference.total_seconds()/60) < 15:
                        embed = discord.Embed(title="Cooldown", description=f"You can open another door in {str(int(difference.total_seconds()/60)-15)[1:]}min", color=discord.Color.dark_red())
                        await ctx.send(embed=embed)
                        return
                datadict[uid]["lastdoor"] = str(datetime.datetime.now())
                gregflag = False
                try:
                    if datadict[gid]:
                        gregflag = True
                except:
                    datadict[gid] = {}
                    datadict[gid]["name"] = ctx.guild.name
                    datadict[gid]["doors"] = 0
                    datadict[gid]["lvl0m"] = []
                    datadict[gid]["lvl5m"] = []
                    datadict[gid]["lvl15m"] = []
                    datadict[gid]["lvl25m"] = []
                    datadict[gid]["lvl45m"] = []

                    datadict[gid]["lvl0m"].append(random.choice(gamedata.RandomLists.LVL0))
                    datadict[gid]["lvl0m"].append(random.choice(gamedata.RandomLists.LVL0))
                    datadict[gid]["lvl0m"].append(random.choice(gamedata.RandomLists.LVL0))
                    datadict[gid]["lvl0m"].append(random.choice(gamedata.RandomLists.LVL0))

                    datadict[gid]["lvl5m"].append(random.choice(gamedata.RandomLists.LVL5))
                    datadict[gid]["lvl5m"].append(random.choice(gamedata.RandomLists.LVL5))
                    datadict[gid]["lvl5m"].append(random.choice(gamedata.RandomLists.LVL5))
                    datadict[gid]["lvl5m"].append(random.choice(gamedata.RandomLists.LVL5))

                    datadict[gid]["lvl15m"].append(random.choice(gamedata.RandomLists.LVL15))
                    datadict[gid]["lvl15m"].append(random.choice(gamedata.RandomLists.LVL15))
                    datadict[gid]["lvl15m"].append(random.choice(gamedata.RandomLists.LVL15))
                    datadict[gid]["lvl15m"].append(random.choice(gamedata.RandomLists.LVL15))

                    datadict[gid]["lvl25m"].append(random.choice(gamedata.RandomLists.LVL25))
                    datadict[gid]["lvl25m"].append(random.choice(gamedata.RandomLists.LVL25))
                    datadict[gid]["lvl25m"].append(random.choice(gamedata.RandomLists.LVL25))
                    datadict[gid]["lvl25m"].append(random.choice(gamedata.RandomLists.LVL25))

                    datadict[gid]["lvl45m"].append(random.choice(gamedata.RandomLists.LVL45))
                    datadict[gid]["lvl45m"].append(random.choice(gamedata.RandomLists.LVL45))
                    datadict[gid]["lvl45m"].append(random.choice(gamedata.RandomLists.LVL45))
                    datadict[gid]["lvl45m"].append(random.choice(gamedata.RandomLists.LVL45))

            #anticheat code
            if dif != None:
                if datadict[uid]["cheaterdifd"] != None:
                    difmin = dif-3
                    difmax = dif+3
                    if datadict[uid]["cheaterdifd"] > difmin and datadict[uid]["cheaterdifd"] < difmax:
                        datadict[uid]["cheaterchanced"] += 1
                    else:
                        datadict[uid]["cheaterchanced"] = 0
                    if datadict[uid]["cheaterchanced"] > 10:
                        datadict["bl"].append(uid)

                datadict[uid]["cheaterdifd"] = dif

            fight = random.randint(0,100)
            if fight < 75:
                if int(math.sqrt(datadict[uid]["xp"]/10)) < 5:
                    mopponent = random.choice(datadict[gid]["lvl0m"])
                elif int(math.sqrt(datadict[uid]["xp"]/10)) < 15:
                    mopponent = random.choice(datadict[gid]["lvl0m"]+datadict[gid]["lvl5m"])
                elif int(math.sqrt(datadict[uid]["xp"]/10)) < 25:
                    mopponent = random.choice(datadict[gid]["lvl0m"]+datadict[gid]["lvl5m"]+datadict[gid]["lvl15m"])
                elif int(math.sqrt(datadict[uid]["xp"]/10)) < 45:
                    mopponent = random.choice(datadict[gid]["lvl0m"]+datadict[gid]["lvl5m"]+datadict[gid]["lvl15m"]+datadict[gid]["lvl25m"])
                else:
                    mopponent = random.choice(datadict[gid]["lvl0m"]+datadict[gid]["lvl5m"]+datadict[gid]["lvl15m"]+datadict[gid]["lvl25m"]+datadict[gid]["lvl45m"])

                #opponent stat building
                mxp = datadict[uid]["xp"] - 100 + random.randint(0, 200)
                if mxp < 1:
                    mxp = 1
                mlvl = int(math.sqrt(mxp/10))+1
                mboost = mlvl/50 + 1
                mhp = round(mopponent["hp"] * mboost, 2)
                mheal = mopponent["heal"] * mboost
                mdmg = mopponent["dmg"] * mboost
                mtank = mopponent["tank"]
                mnegatechance = 0
                mreturndmg = 0

                if mopponent["perks"] != "none":
                    for i in mopponent["perks"]:
                        mdmg+=i["dmg"]
                        mheal+=i["heal"]
                        mtank*=i["tank"]
                        mnegatechance+=i["negatechance"]
                        mreturndmg+=i["returndmg"]


                #player stat building
                #weapon
                php = datadict[uid]["hp"]
                dmg = datadict[uid]["weapon"]["type"]["dmg"]
                shieldbreak = 0
                heal = 0
                sbc = 0
                if datadict[uid]["weapon"]["type"]["perks"] != "none":
                    for i in datadict[uid]["weapon"]["type"]["perks"]:
                        dmg += i["dmg"] 
                        dmg += i["sharp"]
                        sbc += i["shieldbreak"]
                        heal += i["heal"]
                        if sbc > 100:
                            sbc = 100
                    shieldbreak = dmg*(sbc/100)
                    dmg-=shieldbreak

                #armor
                dmg+=datadict[uid]["armor"]["type"]["dmg"]
                heal+=datadict[uid]["armor"]["type"]["heal"]
                tank = datadict[uid]["armor"]["type"]["tank"]
                negatechance = 0
                returndmg = 0

                if datadict[uid]["armor"]["type"]["perks"] != "none":
                    for i in datadict[uid]["armor"]["type"]["perks"]:
                        dmg+=i["dmg"]
                        heal+=i["heal"]
                        tank*=i["tank"]
                        negatechance+=i["negatechance"]
                        returndmg+=i["returndmg"]

                #extra
                dmg*=datadict[uid]["extra"]["type"]["dmg"]
                heal+=datadict[uid]["extra"]["type"]["heal"]
                tank*=datadict[uid]["extra"]["type"]["tank"]

                #boost
                dmg*=datadict[uid]["boost"]
                heal*=datadict[uid]["boost"]

                #class
                dmg*=datadict[uid]["class"]["dmgm"]
                heal+=datadict[uid]["class"]["heal"]
                tank*=datadict[uid]["class"]["tanks"]
                if datadict[uid]["class"]["perks"] != "none":
                    for i in datadict[uid]["class"]["perks"]:
                        dmg*=i["dmg"]
                        heal+=i["heal"]
                        negatechance+=i["negatechance"]

                counter = 0
                pname = datadict[uid]["name"]
                mname = mopponent["name"]
                eventlog = f"You open a door...\n\n**{pname} vs. Lvl[{mlvl}] {mname}**\n"
                mmaxhp = mhp
                pmaxhp = php
                while php > 0 and mhp > 0:
                    counter+=1
                    eventlog+=(f"\nRound {counter}:")
                    #player hits opponent
                    negate = random.randint(0, 100)
                    if negate < mnegatechance:
                        eventlog+=(f"\n{mname} Dodges")
                    else:
                        mhp-=(dmg*mtank)+shieldbreak
                        eventlog+=(f"\n{pname} deals {round((dmg*mtank)+shieldbreak, 2)}dmg")
                    php-=((dmg*tank)+shieldbreak)*(mreturndmg/100)
                    eventlog+=(f"\n{pname} takes {round(((dmg*tank)+shieldbreak)*(mreturndmg/100), 2)}dmg from attack.")
                    mhp+=mmaxhp*(mheal/100)
                    if mhp > mmaxhp:
                        mhp = mmaxhp
                    eventlog+=(f"\n{mname} heals!")
                    eventlog+=(f"\n{mname} is at {round(mhp, 2)}/{mmaxhp}hp!")
                    eventlog+=("\n")

                    #opponent hits player
                    negate = random.randint(0, 100)
                    if negate < negatechance:
                        eventlog+=(f"\n{pname} Dodges")
                    else:
                        php-=(mdmg*tank)
                        eventlog+=(f"\n{mname} deals {round((mdmg*tank), 2)}dmg")
                    mhp-=(mdmg*tank)*(returndmg/100)
                    eventlog+=(f"\n{mname} takes {round((mdmg*tank)*(returndmg/100), 2)}dmg from attack.")
                    php+=pmaxhp*(heal/100)
                    if php > pmaxhp:
                        php = pmaxhp
                    eventlog+=(f"\n{pname} heals!\n")
                    eventlog+=("**Round End**")
                    eventlog+=(f"\n{pname} is at {round(php, 2)}/{pmaxhp}hp!")
                    eventlog+=(f"\n{mname} is at {round(mhp, 2)}/{mmaxhp}hp!\n\n")
                    if counter > 30:
                        ovrflag = True
                        break
                    if len(eventlog) > 1500:
                        embed = discord.Embed(title="Room", description=eventlog, color=discord.Color.orange())
                        await ctx.send(embed=embed)
                        eventlog = ""

                eventlog+=("**Round End**")
                eventlog+=(f"\n{pname} is at {round(php, 2)}/{pmaxhp}hp!")
                eventlog+=(f"\n{mname} is at {round(mhp, 2)}/{mmaxhp}hp!\n\n")
                if php < 1:
                    win = False
                    eventlog+=("\n\n**You Lose**")
                    winclr = discord.Color.dark_red()
                elif mhp < 1:
                    win = True
                    eventlog+=("\n\n**You Win**")
                    winclr = discord.Color.green()
                elif ovrflag == True:
                    win = None
                    eventlog+=("\n\n**Nobody Wins**")
                    winclr = discord.Color.orange()
                coins = int(mboost*250*(1+(int(math.sqrt((datadict[gid]["doors"]+1)/10))+1)))

                if win == False:
                    eventlog+=(f"\nYou lose {int(coins/4)} coins.")
                    datadict[uid]["coins"]-=int(coins/4)
                    if datadict[uid]["coins"] < 0:
                        datadict[uid]["coins"] = 0

                elif win == None:
                    eventlog+=(f"\nToo many rounds, nobody wins.")

                elif win == True:
                    txp = int(coins/48)
                    rxp = int(coins/32)
                    eventlog+=(f"\nYou win {int(coins/4)} coins.\nYou gain {rxp}xp.\nThis Dungeon gains +1 doors.\n+{txp} Weapon XP\n+{txp} Armor XP\n+{txp} Extra XP")
                    datadict[uid]["coins"]+=int(coins/4)
                    datadict[gid]["doors"]+=1
                    datadict[uid]["mosterslain"]+=1
                    datadict[uid]["weapon"]["xp"]+=txp
                    datadict[uid]["armor"]["xp"]+=txp
                    datadict[uid]["extra"]["xp"]+=txp
                    oldlvl = int(math.sqrt(datadict[uid]["xp"]/10))
                    datadict[uid]["xp"]+=rxp
                    newlvl = int(math.sqrt(datadict[uid]["xp"]/10))
                    number = random.randint(0, 75)
                    if oldlvl < newlvl:
                        number = 75
                        embed = discord.Embed(title=f"{ctx.author.name} - Levelup", description=f"You are now level {newlvl}!\n+5hp\n+1% Stats", color=discord.Color.green())
                        datadict[uid]["hp"]+=5
                        datadict[uid]["boost"]+=0.01
                        embed.set_thumbnail(url=ctx.author.avatar_url)
                        await ctx.channel.send(embed=embed)
                
                embed = discord.Embed(title="Room", description=eventlog, color=winclr)
                await ctx.send(embed=embed)

                if win == True:
                    if number == 75:
                        if int(math.sqrt(datadict[uid]["xp"]/10)) > 25:
                            x = 10000
                        elif int(math.sqrt(datadict[uid]["xp"]/10)) > 15:
                            x = 9950
                        else:
                            x = 9900
                        number = random.randint(1, x)
                        number2 = random.randint(1,3)
                        if number < 6500:
                            coinsworth = gamedata.Basics.WORTH["common"]
                            if number2 == 1:
                                drop = [random.choice(gamedata.RandomLists.WEAPON_COMMON),"weapon"]
                            elif number2 == 2:
                                drop = [random.choice(gamedata.RandomLists.ARMOR_COMMON),"armor"]
                            elif number2 == 3:
                                drop = [random.choice(gamedata.RandomLists.EXTRA_COMMON),"extra"]

                        elif number < 8000:
                            coinsworth = gamedata.Basics.WORTH["normal"]
                            if number2 == 1:
                                drop = [random.choice(gamedata.RandomLists.WEAPON_NORMAL),"weapon"]
                            elif number2 == 2:
                                drop = [random.choice(gamedata.RandomLists.ARMOR_NORMAL),"armor"]
                            elif number2 == 3:
                                drop = [random.choice(gamedata.RandomLists.EXTRA_NORMAL),"extra"]

                        elif number < 9000:
                            coinsworth = gamedata.Basics.WORTH["uncommon"]
                            if number2 == 1:
                                drop = [random.choice(gamedata.RandomLists.WEAPON_UNCOMMON),"weapon"]
                            elif number2 == 2:
                                drop = [random.choice(gamedata.RandomLists.ARMOR_UNCOMMON),"armor"]
                            elif number2 == 3:
                                drop = [random.choice(gamedata.RandomLists.EXTRA_UNCOMMON),"extra"]

                        elif number < 9500:
                            coinsworth = gamedata.Basics.WORTH["rare"]
                            if number2 == 1:
                                drop = [random.choice(gamedata.RandomLists.WEAPON_RARE),"weapon"]
                            elif number2 == 2:
                                drop = [random.choice(gamedata.RandomLists.ARMOR_RARE),"armor"]
                            elif number2 == 3:
                                drop = [random.choice(gamedata.RandomLists.EXTRA_RARE),"extra"]

                        elif number < 9800:
                            coinsworth = gamedata.Basics.WORTH["very rare"]
                            if number2 == 1:
                                drop = [random.choice(gamedata.RandomLists.WEAPON_VERYRARE),"weapon"]
                            elif number2 == 2:
                                drop = [random.choice(gamedata.RandomLists.ARMOR_VERYRARE),"armor"]
                            elif number2 == 3:
                                drop = [random.choice(gamedata.RandomLists.EXTRA_VERYRARE),"extra"]

                        elif number < 9900:
                            coinsworth = gamedata.Basics.WORTH["epic"]
                            if number2 == 1:
                                drop = [random.choice(gamedata.RandomLists.WEAPON_EPIC),"weapon"]
                            elif number2 == 2:
                                drop = [random.choice(gamedata.RandomLists.ARMOR_EPIC),"armor"]
                            elif number2 == 3:
                                drop = [random.choice(gamedata.RandomLists.EXTRA_EPIC),"extra"]

                        elif number < 9950:
                            coinsworth = gamedata.Basics.WORTH["unstable"]
                            if number2 == 1:
                                drop = [random.choice(gamedata.RandomLists.WEAPON_UNSTABLE),"weapon"]
                            elif number2 == 2:
                                drop = [random.choice(gamedata.RandomLists.ARMOR_UNSTABLE),"armor"]
                            elif number2 == 3:
                                drop = [random.choice(gamedata.RandomLists.EXTRA_UNSTABLE),"extra"]

                        elif number < 10001:
                            coinsworth = gamedata.Basics.WORTH["corrupted"]
                            if number2 == 1:
                                drop = [random.choice(gamedata.RandomLists.WEAPON_CORRUPTED),"weapon"]
                            elif number2 == 2:
                                drop = [random.choice(gamedata.RandomLists.ARMOR_CORRUPTED),"armor"]
                            elif number2 == 3:
                                drop = [random.choice(gamedata.RandomLists.EXTRA_CORRUPTED),"extra"]
                        drop.append(coinsworth)
                        embed = discord.Embed(title=f"{ctx.author.name} - Drop!", description=f"""
**Congrats! You got a {drop[0]["name"]}**
Rarity: {drop[0]["rarity"]}
Worth: {drop[2]}

Type `<sell_drop` to claim the money.
Type `<infuse_drop` to infuse {int(drop[2]/4)}xp into your current {drop[1]}.
Type `<claim_drop` to replace your {datadict[uid][drop[1]]["name"]} (it will be lost).

This drop will expire when you get another drop.
                        """, color=discord.Color.green())
                        embed.set_thumbnail(url=ctx.author.avatar_url)
                        datadict[uid]["latestdrop"] = drop
                        await ctx.send(embed=embed)

                    else:
                        for x in list(gamedata.Basics.RAREDROPS.values()):
                            if x[0] == mopponent:
                                rd = random.randint(1, 500)
                                if rd == 500:
                                    xdrop = x
                                    drop = [xdrop[1], xdrop[2], gamedata.Basics.WORTH[xdrop[1]["rarity"]]]
                                    embed = discord.Embed(title=f"{ctx.author.name} - Drop!", description=f"""
    **Congrats! You got a RARE drop: {drop[0]["name"]}**
    Rarity: {drop[0]["rarity"]}
    Worth: {drop[2]}

    Type `<sell_drop` to claim the money.
    Type `<infuse_drop` to infuse {int(drop[2]/4)}xp into your current {drop[1]}.
    Type `<claim_drop` to replace your {datadict[uid][drop[1]]["name"]} (it will be lost).

    This drop will expire when you get another drop.
                            """, color=discord.Color.green())
                                    embed.set_thumbnail(url=ctx.author.avatar_url)
                                    datadict[uid]["latestdrop"] = drop
                                    await ctx.send(embed=embed)

            else:
                chance = random.randint(1,100)
                if chance < 3:
                    coins = 5000
                elif chance < 75:
                    coins = int(150*(1+(int(math.sqrt((datadict[gid]["doors"]+1)/100))+1)))
                else:
                    coins = -int((150*(1+(int(math.sqrt((datadict[gid]["doors"]+1)/100))+1)))/2)
                    embed = discord.Embed(title="Room", description=f"You open a door...\n\nAaaaaa its a trap! {coins} coins!", color=discord.Color.dark_red())
                    await ctx.send(embed=embed)
                    datadict[uid]["coins"]-=coins
                    if datadict[uid]["coins"] < 0:
                        datadict[uid]["coins"] = 0
                    return
                embed = discord.Embed(title="Room", description=f"You open a door...\n\nYay +{coins} coins!", color=discord.Color.green())
                await ctx.send(embed=embed)
                datadict[uid]["coins"]+=coins
        
        except Exception as e:
            embed = discord.Embed(title="Error", description=f"```{e}```", color=discord.Color.dark_red())
            await ctx.send(embed=embed)


    #reset door cooldown
    @commands.command()
    async def rdc(self, ctx, uid: str = None):
        try:
            if ctx.author.id in ownerid:
                if uid == None:
                    uid = str(ctx.author.id)
                datadict[uid]["lastdoor"] = None
                embed = discord.Embed(title="Success", description=f"Door cooldown reset!", color=discord.Color.green())
                await ctx.send(embed=embed)
            else:
                embed = discord.Embed(title="No Permission", description=f"You can't use this command!", color=discord.Color.dark_red())
                await ctx.send(embed=embed)
        except Exception as e:
            embed = discord.Embed(title="Error", description=f"```{e}```", color=discord.Color.dark_red())
            await ctx.send(embed=embed)


    #blacklist command
    @commands.command()
    async def blacklist(self, ctx, uid: str = None):
        try:
            if ctx.author.id in ownerid:
                if uid == None:
                    embed = discord.Embed(title="Error", description="No User Given.", color=discord.Color.dark_red())
                    await ctx.send(embed=embed)
                else:
                    try:
                        if datadict["bl"]: pass
                    except:
                        datadict["bl"] = []
                    datadict["bl"].append(uid)
                    embed = discord.Embed(title="Success", description="User Blacklisted!", color=discord.Color.green())
                    await ctx.send(embed=embed)

        except Exception as e:
            embed = discord.Embed(title="Error", description=f"```{e}```", color=discord.Color.dark_red())
            await ctx.send(embed=embed)


    #unblacklist command
    @commands.command()
    async def unblacklist(self, ctx, uid: str = None):
        try:
            if ctx.author.id in ownerid:
                if uid == None:
                    embed = discord.Embed(title="Error", description="No User Given.", color=discord.Color.dark_red())
                    await ctx.send(embed=embed)
                else:
                    try:
                        if datadict["bl"]: pass
                    except:
                        datadict["bl"] = []
                    try:
                        datadict["bl"].remove(uid)
                        datadict[uid]["cheaterchancet"] = 0
                        datadict[uid]["cheaterdift"] = None
                        datadict[uid]["cheaterchanced"] = 0
                        datadict[uid]["cheaterdifd"] = None
                        datadict[uid]["cheaterchancea"] = 0
                        datadict[uid]["cheaterdifa"] = None
                        embed = discord.Embed(title="Success", description="User Removed from Blacklist!", color=discord.Color.green())
                        await ctx.send(embed=embed)
                    except:
                        embed = discord.Embed(title="Error", description="User is not blacklisted!", color=discord.Color.dark_red())
                        await ctx.send(embed=embed)

        except Exception as e:
            embed = discord.Embed(title="Error", description=f"```{e}```", color=discord.Color.dark_red())
            await ctx.send(embed=embed)


    #set item commands
    @commands.command()
    async def setweapon(self, ctx, uid: str = None, xpx: int = None, *, weaponx: str = None):
        try:
            if ctx.author.id in ownerid:
                if uid == None:
                    uid = str(ctx.author.id)
                if xpx == None:
                    xpx = 0
                if weaponx == None:
                    embed = discord.Embed(title="Error", description="No Weapon Given", color=discord.Color.dark_red())
                    await ctx.send(embed=embed)
                else:
                    foundflag = False
                    for i in gamedata.RandomLists.WEAPON_COMMON + gamedata.RandomLists.WEAPON_NORMAL + gamedata.RandomLists.WEAPON_UNCOMMON + gamedata.RandomLists.WEAPON_RARE + gamedata.RandomLists.WEAPON_VERYRARE + gamedata.RandomLists.WEAPON_EPIC + gamedata.RandomLists.WEAPON_UNSTABLE + gamedata.RandomLists.WEAPON_CORRUPTED + gamedata.RandomLists.WEAPON_LIMITED + gamedata.RandomLists.WEAPON_UNIQUE:
                        if i["name"] == weaponx:
                            datadict[uid]["weapon"] = {"type":i, "name":i["name"], "xp":xpx}
                            foundflag = True
                            embed = discord.Embed(title="Success", description="Weapon set.", color=discord.Color.green())
                            await ctx.send(embed=embed)
                    if foundflag == False:
                        embed = discord.Embed(title="Error", description="Weapon not found.", color=discord.Color.dark_red())
                        await ctx.send(embed=embed)
            else:
                embed = discord.Embed(title="No Permission", description=f"You can't use this command!", color=discord.Color.dark_red())
                await ctx.send(embed=embed)
        except Exception as e:
            embed = discord.Embed(title="Error", description=f"```{e}```", color=discord.Color.dark_red())
            await ctx.send(embed=embed)


    @commands.command()
    async def setarmor(self, ctx, uid: str = None, xpx: int = None, *, armorx: str = None):
        try:
            if ctx.author.id in ownerid:
                if uid == None:
                    uid = str(ctx.author.id)
                if xpx == None:
                    xpx = 0
                if armorx == None:
                    embed = discord.Embed(title="Error", description="No Armor Given", color=discord.Color.dark_red())
                    await ctx.send(embed=embed)
                else:
                    foundflag = False
                    for i in gamedata.RandomLists.ARMOR_COMMON + gamedata.RandomLists.ARMOR_NORMAL + gamedata.RandomLists.ARMOR_UNCOMMON + gamedata.RandomLists.ARMOR_RARE + gamedata.RandomLists.ARMOR_VERYRARE + gamedata.RandomLists.ARMOR_EPIC + gamedata.RandomLists.ARMOR_UNSTABLE + gamedata.RandomLists.ARMOR_CORRUPTED + gamedata.RandomLists.ARMOR_LIMITED + gamedata.RandomLists.ARMOR_UNIQUE:
                        if i["name"] == armorx:
                            datadict[uid]["armor"] = {"type":i, "name":i["name"], "xp":xpx}
                            foundflag = True
                            embed = discord.Embed(title="Success", description="Armor set.", color=discord.Color.green())
                            await ctx.send(embed=embed)
                    if foundflag == False:
                        embed = discord.Embed(title="Error", description="Armor not found.", color=discord.Color.dark_red())
                        await ctx.send(embed=embed)
            else:
                embed = discord.Embed(title="No Permission", description=f"You can't use this command!", color=discord.Color.dark_red())
                await ctx.send(embed=embed)
        except Exception as e:
            embed = discord.Embed(title="Error", description=f"```{e}```", color=discord.Color.dark_red())
            await ctx.send(embed=embed)


    @commands.command()
    async def setextra(self, ctx, uid: str = None, xpx: int = None, *, extrax: str = None):
        try:
            if ctx.author.id in ownerid:
                if uid == None:
                    uid = str(ctx.author.id)
                if xpx == None:
                    xpx = 0
                if extrax == None:
                    embed = discord.Embed(title="Error", description="No Extra Given", color=discord.Color.dark_red())
                    await ctx.send(embed=embed)
                else:
                    foundflag = False
                    for i in gamedata.RandomLists.EXTRA_COMMON + gamedata.RandomLists.EXTRA_NORMAL + gamedata.RandomLists.EXTRA_UNCOMMON + gamedata.RandomLists.EXTRA_RARE + gamedata.RandomLists.EXTRA_VERYRARE + gamedata.RandomLists.EXTRA_EPIC + gamedata.RandomLists.EXTRA_UNSTABLE + gamedata.RandomLists.EXTRA_CORRUPTED + gamedata.RandomLists.EXTRA_LIMITED + gamedata.RandomLists.EXTRA_UNIQUE:
                        if i["name"] == extrax:
                            datadict[uid]["extra"] = {"type":i, "name":i["name"], "xp":xpx}
                            foundflag = True
                            embed = discord.Embed(title="Success", description="Extra set.", color=discord.Color.green())
                            await ctx.send(embed=embed)
                    if foundflag == False:
                        embed = discord.Embed(title="Error", description="Extra not found.", color=discord.Color.dark_red())
                        await ctx.send(embed=embed)
            else:
                embed = discord.Embed(title="No Permission", description=f"You can't use this command!", color=discord.Color.dark_red())
                await ctx.send(embed=embed)
        except Exception as e:
            embed = discord.Embed(title="Error", description=f"```{e}```", color=discord.Color.dark_red())
            await ctx.send(embed=embed)


    #set xp
    @commands.command()
    async def setxp(self, ctx, uid: str = None, *, xp: int = None):
        try:
            if ctx.author.id in ownerid:
                if uid == None:
                    uid = str(ctx.author.id)
                if xp == None:
                    embed = discord.Embed(title="Error", description="No XP Given", color=discord.Color.dark_red())
                    await ctx.send(embed=embed)
                else:
                    datadict[uid]["xp"] = xp
                    embed = discord.Embed(title="Success", description="XP Set", color=discord.Color.green())
                    await ctx.send(embed=embed)
            else:
                embed = discord.Embed(title="No Permission", description=f"You can't use this command!", color=discord.Color.dark_red())
                await ctx.send(embed=embed)
        except Exception as e:
            embed = discord.Embed(title="Error", description=f"```{e}```", color=discord.Color.dark_red())
            await ctx.send(embed=embed)


    #set coins
    @commands.command()
    async def setcoins(self, ctx, uid: str = None, *, coins: int = None):
        try:
            if ctx.author.id in ownerid:
                if uid == None:
                    uid = str(ctx.author.id)
                if coins == None:
                    embed = discord.Embed(title="Error", description="No Coins Given", color=discord.Color.dark_red())
                    await ctx.send(embed=embed)
                else:
                    datadict[uid]["coins"] = coins
                    embed = discord.Embed(title="Success", description="Coins Set", color=discord.Color.green())
                    await ctx.send(embed=embed)
            else:
                embed = discord.Embed(title="No Permission", description=f"You can't use this command!", color=discord.Color.dark_red())
                await ctx.send(embed=embed)
        except Exception as e:
            embed = discord.Embed(title="Error", description=f"```{e}```", color=discord.Color.dark_red())
            await ctx.send(embed=embed)


    #sell drop
    @commands.command()
    async def sell_drop(self, ctx):
        try:
            uid = str(ctx.author.id)
            if uid in datadict["bl"]:
                return
            regflag = False
            try:
                if datadict[uid]:
                    regflag = True
            except:
                embed = discord.Embed(title="No Data", description="Do `<start` to create a player.", color=discord.Color.dark_red())
                await ctx.send(embed=embed)

            if regflag == True:
                if datadict[uid]["latestdrop"] == None:
                    embed = discord.Embed(title="No Drop", description="You have no drop to sell.", color=discord.Color.dark_red())
                    await ctx.send(embed=embed)
                else:
                    datadict[uid]["coins"]+=datadict[uid]["latestdrop"][2]
                    moneygained = datadict[uid]["latestdrop"][2]
                    datadict[uid]["latestdrop"] = None
                    embed = discord.Embed(title="Sold Drop", description=f"+{moneygained} coins.", color=discord.Color.green())
                    await ctx.send(embed=embed)

        except Exception as e:
            embed = discord.Embed(title="Error", description=f"```{e}```", color=discord.Color.dark_red())
            await ctx.send(embed=embed)

    
    #infuse drop
    @commands.command()
    async def infuse_drop(self, ctx):
        try:
            uid = str(ctx.author.id)
            if uid in datadict["bl"]:
                return
            regflag = False
            try:
                if datadict[uid]:
                    regflag = True
            except:
                embed = discord.Embed(title="No Data", description="Do `<start` to create a player.", color=discord.Color.dark_red())
                await ctx.send(embed=embed)

            if regflag == True:
                if datadict[uid]["latestdrop"] == None:
                    embed = discord.Embed(title="No Drop", description="You have no drop to infuse.", color=discord.Color.dark_red())
                    await ctx.send(embed=embed)
                else:
                    whatsthis = str(datadict[uid]["latestdrop"][1])
                    datadict[uid][whatsthis]["xp"]+=int(datadict[uid]["latestdrop"][2]/4)
                    iteminfused = datadict[uid][whatsthis]["name"]
                    xpgained = int(datadict[uid]["latestdrop"][2]/4)
                    datadict[uid]["latestdrop"] = None
                    embed = discord.Embed(title="Infused Drop", description=f"Your {iteminfused} gains +{xpgained}xp.", color=discord.Color.green())
                    await ctx.send(embed=embed)

        except Exception as e:
            embed = discord.Embed(title="Error", description=f"```{e}```", color=discord.Color.dark_red())
            await ctx.send(embed=embed)


    #claim drop
    @commands.command()
    async def claim_drop(self, ctx):
        try:
            uid = str(ctx.author.id)
            if uid in datadict["bl"]:
                return
            regflag = False
            try:
                if datadict[uid]:
                    regflag = True
            except:
                embed = discord.Embed(title="No Data", description="Do `<start` to create a player.", color=discord.Color.dark_red())
                await ctx.send(embed=embed)

            if regflag == True:
                if datadict[uid]["latestdrop"] == None:
                    embed = discord.Embed(title="No Drop", description="You have no drop to claim.", color=discord.Color.dark_red())
                    await ctx.send(embed=embed)
                else:
                    datadict[uid][datadict[uid]["latestdrop"][1]] = {"type":datadict[uid]["latestdrop"][0], "name":datadict[uid]["latestdrop"][0]["name"], "xp":0}
                    itemreplaced = datadict[uid]["latestdrop"][1]
                    itemnow = datadict[uid]["latestdrop"][0]["name"]
                    datadict[uid]["latestdrop"] = None
                    embed = discord.Embed(title="Claimed Drop", description=f"Your {itemreplaced} is now a {itemnow}.", color=discord.Color.green())
                    await ctx.send(embed=embed)

        except Exception as e:
            embed = discord.Embed(title="Error", description=f"```{e}```", color=discord.Color.dark_red())
            await ctx.send(embed=embed)


    #rename
    @commands.command()
    async def rename(self, ctx, *, selname: str = None):
        try:
            uid = str(ctx.author.id)
            regflag = False
            try:
                if datadict[uid]:
                    regflag = True
            except:
                embed = discord.Embed(title="No Data", description="Do `<start` to create a player.", color=discord.Color.dark_red())
                await ctx.send(embed=embed)

            if regflag == True:
                if selname == None:
                    embed = discord.Embed(title="Error", description="No name given.", color=discord.Color.dark_red())
                    await ctx.send(embed=embed)
                elif len(selname) > 32:
                    embed = discord.Embed(title="Error", description="Name can't be over 32 characters.", color=discord.Color.dark_red())
                    await ctx.send(embed=embed)
                else:
                    datadict[uid]["name"] = selname
                    embed = discord.Embed(title="Success", description=f"Name changed to {selname}.", color=discord.Color.green())
                    await ctx.send(embed=embed)
        except Exception as e:
            embed = discord.Embed(title="Error", description=f"```{e}```", color=discord.Color.dark_red())
            await ctx.send(embed=embed)


    #rename weapon
    @commands.command()
    async def rename_weapon(self, ctx, *, selname: str = None):
        try:
            uid = str(ctx.author.id)
            regflag = False
            try:
                if datadict[uid]:
                    regflag = True
            except:
                embed = discord.Embed(title="No Data", description="Do `<start` to create a player.", color=discord.Color.dark_red())
                await ctx.send(embed=embed)

            if regflag == True:
                if selname == None:
                    embed = discord.Embed(title="Error", description="No name given.", color=discord.Color.dark_red())
                    await ctx.send(embed=embed)
                elif len(selname) > 32:
                    embed = discord.Embed(title="Error", description="Name can't be over 32 characters.", color=discord.Color.dark_red())
                    await ctx.send(embed=embed)
                else:
                    datadict[uid]["weapon"]["name"] = selname
                    embed = discord.Embed(title="Success", description=f"Name changed to {selname}.", color=discord.Color.green())
                    await ctx.send(embed=embed)
        except Exception as e:
            embed = discord.Embed(title="Error", description=f"```{e}```", color=discord.Color.dark_red())
            await ctx.send(embed=embed)


    #rename armor
    @commands.command()
    async def rename_armor(self, ctx, *, selname: str = None):
        try:
            uid = str(ctx.author.id)
            regflag = False
            try:
                if datadict[uid]:
                    regflag = True
            except:
                embed = discord.Embed(title="No Data", description="Do `<start` to create a player.", color=discord.Color.dark_red())
                await ctx.send(embed=embed)

            if regflag == True:
                if selname == None:
                    embed = discord.Embed(title="Error", description="No name given.", color=discord.Color.dark_red())
                    await ctx.send(embed=embed)
                elif len(selname) > 32:
                    embed = discord.Embed(title="Error", description="Name can't be over 32 characters.", color=discord.Color.dark_red())
                    await ctx.send(embed=embed)
                else:
                    datadict[uid]["armor"]["name"] = selname
                    embed = discord.Embed(title="Success", description=f"Name changed to {selname}.", color=discord.Color.green())
                    await ctx.send(embed=embed)
        except Exception as e:
            embed = discord.Embed(title="Error", description=f"```{e}```", color=discord.Color.dark_red())
            await ctx.send(embed=embed)


    #rename weapon
    @commands.command()
    async def rename_extra(self, ctx, *, selname: str = None):
        try:
            uid = str(ctx.author.id)
            regflag = False
            try:
                if datadict[uid]:
                    regflag = True
            except:
                embed = discord.Embed(title="No Data", description="Do `<start` to create a player.", color=discord.Color.dark_red())
                await ctx.send(embed=embed)

            if regflag == True:
                if selname == None:
                    embed = discord.Embed(title="Error", description="No name given.", color=discord.Color.dark_red())
                    await ctx.send(embed=embed)
                elif len(selname) > 32:
                    embed = discord.Embed(title="Error", description="Name can't be over 32 characters.", color=discord.Color.dark_red())
                    await ctx.send(embed=embed)
                else:
                    datadict[uid]["extra"]["name"] = selname
                    embed = discord.Embed(title="Success", description=f"Name changed to {selname}.", color=discord.Color.green())
                    await ctx.send(embed=embed)
        except Exception as e:
            embed = discord.Embed(title="Error", description=f"```{e}```", color=discord.Color.dark_red())
            await ctx.send(embed=embed)


    #weapon stats
    @commands.command()
    async def weapon(self, ctx, *, weaponx: str = None):
        try:
            if weaponx == None:
                embed = discord.Embed(title="Error", description="No Weapon Given", color=discord.Color.dark_red())
                await ctx.send(embed=embed)
            else:
                foundflag = False
                for i in gamedata.RandomLists.WEAPON_COMMON + gamedata.RandomLists.WEAPON_NORMAL + gamedata.RandomLists.WEAPON_UNCOMMON + gamedata.RandomLists.WEAPON_RARE + gamedata.RandomLists.WEAPON_VERYRARE + gamedata.RandomLists.WEAPON_EPIC + gamedata.RandomLists.WEAPON_UNSTABLE + gamedata.RandomLists.WEAPON_CORRUPTED + gamedata.RandomLists.WEAPON_LIMITED + gamedata.RandomLists.WEAPON_UNIQUE:
                    if i["name"] == weaponx:
                        foundflag = True
                        wpd = f"""
**Name: {i["name"]}**
Description: {i["desc"]}
Base Damage: {i["dmg"]}
Rarity: {i["rarity"]}
                        """
                        if i["perks"] != "none":
                            for x in i["perks"]:
                                wpd+=f"""

**Perk: {x["name"]}**
Description: {x["desc"]}
Damage: {x["dmg"]}
Sharpness: {x["sharp"]}
Shieldbreak: {x["shieldbreak"]}
Heal: {x["heal"]}
                                """
                        embed = discord.Embed(title=i["name"], description=wpd, color=discord.Color.green())
                        await ctx.send(embed=embed)
                if foundflag == False:
                    embed = discord.Embed(title="Error", description="Weapon not found.", color=discord.Color.dark_red())
                    await ctx.send(embed=embed)
        except Exception as e:
            embed = discord.Embed(title="Error", description=f"```{e}```", color=discord.Color.dark_red())
            await ctx.send(embed=embed)


    #armor stats
    @commands.command()
    async def armor(self, ctx, *, armorx: str = None):
        try:
            if armorx == None:
                embed = discord.Embed(title="Error", description="No Armor Given", color=discord.Color.dark_red())
                await ctx.send(embed=embed)
            else:
                foundflag = False
                for i in gamedata.RandomLists.ARMOR_COMMON + gamedata.RandomLists.ARMOR_NORMAL + gamedata.RandomLists.ARMOR_UNCOMMON + gamedata.RandomLists.ARMOR_RARE + gamedata.RandomLists.ARMOR_VERYRARE + gamedata.RandomLists.ARMOR_EPIC + gamedata.RandomLists.ARMOR_UNSTABLE + gamedata.RandomLists.ARMOR_CORRUPTED + gamedata.RandomLists.ARMOR_LIMITED + gamedata.RandomLists.ARMOR_UNIQUE:
                    if i["name"] == armorx:
                        foundflag = True
                        wpd = f"""
**Name: {i["name"]}**
Description: {i["desc"]}
Base Damage: {i["dmg"]}
Base Heal: {i["heal"]}
Tank: {i["tank"]}
Rarity: {i["rarity"]}
                        """
                        if i["perks"] != "none":
                            for x in i["perks"]:
                                wpd+=f"""

**Perk: {x["name"]}**
Description: {x["desc"]}
Damage: {x["dmg"]}
Heal: {x["heal"]}
Tank: {x["tank"]}
Dodge Chance: {x["negatechance"]}%
Return Damage: {x["returndmg"]}%
                                """
                        embed = discord.Embed(title=i["name"], description=wpd, color=discord.Color.green())
                        await ctx.send(embed=embed)
                if foundflag == False:
                    embed = discord.Embed(title="Error", description="Armor not found.", color=discord.Color.dark_red())
                    await ctx.send(embed=embed)
        except Exception as e:
            embed = discord.Embed(title="Error", description=f"```{e}```", color=discord.Color.dark_red())
            await ctx.send(embed=embed)


    #extra stats
    @commands.command()
    async def extra(self, ctx, *, extrax: str = None):
        try:
            if extrax == None:
                embed = discord.Embed(title="Error", description="No Extra Given", color=discord.Color.dark_red())
                await ctx.send(embed=embed)
            else:
                foundflag = False
                for i in gamedata.RandomLists.EXTRA_COMMON + gamedata.RandomLists.EXTRA_NORMAL + gamedata.RandomLists.EXTRA_UNCOMMON + gamedata.RandomLists.EXTRA_RARE + gamedata.RandomLists.EXTRA_VERYRARE + gamedata.RandomLists.EXTRA_EPIC + gamedata.RandomLists.EXTRA_UNSTABLE + gamedata.RandomLists.EXTRA_CORRUPTED + gamedata.RandomLists.EXTRA_LIMITED + gamedata.RandomLists.EXTRA_UNIQUE:
                    if i["name"] == extrax:
                        foundflag = True
                        wpd = f"""
**Name: {i["name"]}**
Description: {i["desc"]}
Base Damage: {i["dmg"]}
Base Heal: {i["heal"]}
Tank: {i["tank"]}
Rarity: {i["rarity"]}
                        """
                        embed = discord.Embed(title=i["name"], description=wpd, color=discord.Color.green())
                        await ctx.send(embed=embed)
                if foundflag == False:
                    embed = discord.Embed(title="Error", description="Extra not found.", color=discord.Color.dark_red())
                    await ctx.send(embed=embed)
        except Exception as e:
            embed = discord.Embed(title="Error", description=f"```{e}```", color=discord.Color.dark_red())
            await ctx.send(embed=embed)


    #monster stats
    @commands.command()
    async def monster(self, ctx, *, mx: str = None):
        try:
            if mx == None:
                embed = discord.Embed(title="Error", description="No Monster Given", color=discord.Color.dark_red())
                await ctx.send(embed=embed)
            else:
                foundflag = False
                for i in gamedata.RandomLists.LVL0 + gamedata.RandomLists.LVL5 + gamedata.RandomLists.LVL15 + gamedata.RandomLists.LVL25 + gamedata.RandomLists.LVL45:
                    if i["name"] == mx:
                        foundflag = True
                        wpd = f"""
**Name: {i["name"]}**
Description: {i["desc"]}
Base Damage: {i["dmg"]}
Base Heal: {i["heal"]}
Base HP: {i["hp"]}
Tank: {i["tank"]}
Lowest level: {i["minlvl"]}
                        """
                        if i["perks"] != "none":
                            for x in i["perks"]:
                                wpd+=f"""

**Perk: {x["name"]}**
Description: {x["desc"]}
Damage: {x["dmg"]}
Heal: {x["heal"]}
Tank: {x["tank"]}
Dodge Chance: {x["negatechance"]}%
Return Damage: {x["returndmg"]}%
                                """
                        embed = discord.Embed(title=i["name"], description=wpd, color=discord.Color.green())
                        await ctx.send(embed=embed)
                if foundflag == False:
                    embed = discord.Embed(title="Error", description="Monster not found.", color=discord.Color.dark_red())
                    await ctx.send(embed=embed)
        except Exception as e:
            embed = discord.Embed(title="Error", description=f"```{e}```", color=discord.Color.dark_red())
            await ctx.send(embed=embed)


    #boss stats
    @commands.command()
    async def bossinfo(self, ctx, *, mx: str = None):
        try:
            if mx == None:
                embed = discord.Embed(title="Error", description="No Boss Given", color=discord.Color.dark_red())
                await ctx.send(embed=embed)
            else:
                foundflag = False
                for i in gamedata.RandomLists.BOSSES:
                    if i["name"] == mx:
                        foundflag = True
                        wpd = f"""
**Name: {i["name"]}**
Description: {i["desc"]}
Minimum Dungeon Level: {i["minlvl"]}
Minimum Player Level: {i["plvl"]}
Damage: {i["returndmg"]}
Health: ???
Drop: {i["drop"]["name"]}
Summon Cost: {i["summoncost"]}
                        """
                        embed = discord.Embed(title=i["name"], description=wpd, color=discord.Color.green())
                        await ctx.send(embed=embed)
                if foundflag == False:
                    embed = discord.Embed(title="Error", description="Boss not found.", color=discord.Color.dark_red())
                    await ctx.send(embed=embed)
        except Exception as e:
            embed = discord.Embed(title="Error", description=f"```{e}```", color=discord.Color.dark_red())
            await ctx.send(embed=embed)


    #class stats
    @commands.command()
    async def classinfo(self, ctx, *, cx: str = None):
        try:
            if cx == None:
                embed = discord.Embed(title="Error", description="No Class Given", color=discord.Color.dark_red())
                await ctx.send(embed=embed)
            else:
                foundflag = False
                for i in [gamedata.CLASSLIST.NON, gamedata.CLASSLIST.FIGHTER, gamedata.CLASSLIST.MAGE, gamedata.CLASSLIST.THIEF, gamedata.CLASSLIST.TANK, gamedata.CLASSLIST.DARKMAGE, gamedata.CLASSLIST.ASSASSIN]:
                    if i["name"] == cx:
                        foundflag = True
                        wpd = f"""
**Name: {i["name"]}**
Description: {i["desc"]}
Damage: {i["dmgm"]}
Heal: {i["heal"]}
Tank: {i["tanks"]}
                        """
                        if i["perks"] != "none":
                            for x in i["perks"]:
                                wpd+=f"""

**Perk: {x["name"]}**
Description: {x["desc"]}
Damage: {x["dmg"]}
Heal: {x["heal"]}
Dodge Chance: {x["negatechance"]}%
                                """
                        embed = discord.Embed(title=i["name"], description=wpd, color=discord.Color.green())
                        await ctx.send(embed=embed)
                if foundflag == False:
                    embed = discord.Embed(title="Error", description="Class not found.", color=discord.Color.dark_red())
                    await ctx.send(embed=embed)
        except Exception as e:
            embed = discord.Embed(title="Error", description=f"```{e}```", color=discord.Color.dark_red())
            await ctx.send(embed=embed)

    
    #set title
    @commands.command()
    async def settitle(self, ctx, uid: str = None, *, seltitle: str = None):
        try:
            if ctx.author.id in ownerid:
                regflag = False
                try:
                    if datadict[uid]:
                        regflag = True
                except:
                    embed = discord.Embed(title="No Data", description="Do `<start` to create a player.", color=discord.Color.dark_red())
                    await ctx.send(embed=embed)

                if regflag == True:
                    if seltitle == None:
                        embed = discord.Embed(title="Error", description="No title given.", color=discord.Color.dark_red())
                        await ctx.send(embed=embed)
                    elif len(seltitle) > 32:
                        embed = discord.Embed(title="Error", description="Title can't be over 32 characters.", color=discord.Color.dark_red())
                        await ctx.send(embed=embed)
                    else:
                        datadict[uid]["title"] = seltitle
                        embed = discord.Embed(title="Success", description=f"Title changed to {seltitle}.", color=discord.Color.green())
                        await ctx.send(embed=embed)
        except Exception as e:
            embed = discord.Embed(title="Error", description=f"```{e}```", color=discord.Color.dark_red())
            await ctx.send(embed=embed)


    #pay people
    @commands.command()
    async def pay(self, ctx, goesto:str, ammount: int = None):
        try:
            uid = str(ctx.author.id)
            if uid in datadict["bl"]:
                return
            regflag = False
            try:
                if datadict[uid]:
                    regflag = True
            except:
                embed = discord.Embed(title="No Data", description="Do `<start` to create a player.", color=discord.Color.dark_red())
                await ctx.send(embed=embed)

            if ammount == None:
                embed = discord.Embed(title="Error", description="Pleas enter an ammount.", color=discord.Color.dark_red())
                await ctx.send(embed=embed)

            if regflag == True:
                if datadict[uid]["coins"] >= ammount:
                    datadict[uid]["coins"]-=ammount
                    datadict[str(ctx.message.mentions[0].id)]["coins"]+=ammount
                    embed = discord.Embed(title="Success", description=f"Sent {ammount} coins to {ctx.message.mentions[0].name}", color=discord.Color.green())
                    await ctx.send(embed=embed)
                else:
                    embed = discord.Embed(title="Error", description="You cant afford this.", color=discord.Color.dark_red())
                    await ctx.send(embed=embed)
        except Exception as e:
            embed = discord.Embed(title="Error", description=f"```{e}```", color=discord.Color.dark_red())
            await ctx.send(embed=embed)


    #buy drop
    @commands.command()
    async def buy_drop(self, ctx, *, rarity: str = None):
        try:
            uid = str(ctx.author.id)
            if uid in datadict["bl"]:
                return
            regflag = False
            try:
                if datadict[uid]:
                    regflag = True
            except:
                embed = discord.Embed(title="No Data", description="Do `<start` to create a player.", color=discord.Color.dark_red())
                await ctx.send(embed=embed)

            if regflag == True:
                canaffor = True
                if rarity == None:
                    embed = discord.Embed(title="Error", description="No rarity selected.", color=discord.Color.dark_red())
                    await ctx.send(embed=embed)
                    return

                number2 = random.randint(1,3)
                if rarity == "common":
                    price = 100
                    if datadict[uid]["coins"] < price:
                        canaffor = False
                    coinsworth = gamedata.Basics.WORTH["common"]
                    if number2 == 1:
                        drop = [random.choice(gamedata.RandomLists.WEAPON_COMMON),"weapon"]
                    elif number2 == 2:
                        drop = [random.choice(gamedata.RandomLists.ARMOR_COMMON),"armor"]
                    elif number2 == 3:
                        drop = [random.choice(gamedata.RandomLists.EXTRA_COMMON),"extra"]

                elif rarity == "normal":
                    price = 500
                    if datadict[uid]["coins"] < price:
                        canaffor = False
                    coinsworth = gamedata.Basics.WORTH["normal"]
                    if number2 == 1:
                        drop = [random.choice(gamedata.RandomLists.WEAPON_NORMAL),"weapon"]
                    elif number2 == 2:
                        drop = [random.choice(gamedata.RandomLists.ARMOR_NORMAL),"armor"]
                    elif number2 == 3:
                        drop = [random.choice(gamedata.RandomLists.EXTRA_NORMAL),"extra"]

                elif rarity == "uncommon":
                    price = 1000
                    if datadict[uid]["coins"] < price:
                        canaffor = False
                    coinsworth = gamedata.Basics.WORTH["uncommon"]
                    if number2 == 1:
                        drop = [random.choice(gamedata.RandomLists.WEAPON_UNCOMMON),"weapon"]
                    elif number2 == 2:
                        drop = [random.choice(gamedata.RandomLists.ARMOR_UNCOMMON),"armor"]
                    elif number2 == 3:
                        drop = [random.choice(gamedata.RandomLists.EXTRA_UNCOMMON),"extra"]

                elif rarity == "rare":
                    price = 10000
                    if datadict[uid]["coins"] < price:
                        canaffor = False
                    coinsworth = gamedata.Basics.WORTH["rare"]
                    if number2 == 1:
                        drop = [random.choice(gamedata.RandomLists.WEAPON_RARE),"weapon"]
                    elif number2 == 2:
                        drop = [random.choice(gamedata.RandomLists.ARMOR_RARE),"armor"]
                    elif number2 == 3:
                        drop = [random.choice(gamedata.RandomLists.EXTRA_RARE),"extra"]

                elif rarity == "very rare":
                    price = 20000
                    if datadict[uid]["coins"] < price:
                        canaffor = False
                    coinsworth = gamedata.Basics.WORTH["very rare"]
                    if number2 == 1:
                        drop = [random.choice(gamedata.RandomLists.WEAPON_VERYRARE),"weapon"]
                    elif number2 == 2:
                        drop = [random.choice(gamedata.RandomLists.ARMOR_VERYRARE),"armor"]
                    elif number2 == 3:
                        drop = [random.choice(gamedata.RandomLists.EXTRA_VERYRARE),"extra"]

                elif rarity == "epic":
                    price = 50000
                    if datadict[uid]["coins"] < price:
                        canaffor = False
                    coinsworth = gamedata.Basics.WORTH["epic"]
                    if number2 == 1:
                        drop = [random.choice(gamedata.RandomLists.WEAPON_EPIC),"weapon"]
                    elif number2 == 2:
                        drop = [random.choice(gamedata.RandomLists.ARMOR_EPIC),"armor"]
                    elif number2 == 3:
                        drop = [random.choice(gamedata.RandomLists.EXTRA_EPIC),"extra"]

                elif rarity == "unstable":
                    price = 100000
                    if datadict[uid]["coins"] < price:
                        canaffor = False
                    coinsworth = gamedata.Basics.WORTH["unstable"]
                    if number2 == 1:
                        drop = [random.choice(gamedata.RandomLists.WEAPON_UNSTABLE),"weapon"]
                    elif number2 == 2:
                        drop = [random.choice(gamedata.RandomLists.ARMOR_UNSTABLE),"armor"]
                    elif number2 == 3:
                        drop = [random.choice(gamedata.RandomLists.EXTRA_UNSTABLE),"extra"]

                elif rarity == "corrupted":
                    price = 200000
                    if datadict[uid]["coins"] < price:
                        canaffor = False
                    coinsworth = gamedata.Basics.WORTH["corrupted"]
                    if number2 == 1:
                        drop = [random.choice(gamedata.RandomLists.WEAPON_CORRUPTED),"weapon"]
                    elif number2 == 2:
                        drop = [random.choice(gamedata.RandomLists.ARMOR_CORRUPTED),"armor"]
                    elif number2 == 3:
                        drop = [random.choice(gamedata.RandomLists.EXTRA_CORRUPTED),"extra"]

                else:
                    embed = discord.Embed(title="Error", description="Rarity not found.", color=discord.Color.dark_red())
                    await ctx.send(embed=embed)
                    return

                datadict[uid]["coins"]-=price
                drop.append(coinsworth)

                if canaffor == False:
                    embed = discord.Embed(title="Error", description="You can't afford this.", color=discord.Color.dark_red())
                    await ctx.send(embed=embed)
                    return

                embed = discord.Embed(title=f"{ctx.author.name} - Drop!", description=f"""
**Congrats! You got a {drop[0]["name"]}**
Rarity: {drop[0]["rarity"]}
Worth: {drop[2]}

Type `<sell_drop` to claim the money.
Type `<infuse_drop` to infuse {int(drop[2]/4)}xp into your current {drop[1]}.
Type `<claim_drop` to replace your {datadict[uid][drop[1]]["name"]} (it will be lost).

This drop will expire when you get another drop.
                """, color=discord.Color.green())
                embed.set_thumbnail(url=ctx.author.avatar_url)
                datadict[uid]["latestdrop"] = drop
                await ctx.send(embed=embed)

        except Exception as e:
            embed = discord.Embed(title="Error", description=f"```{e}```", color=discord.Color.dark_red())
            await ctx.send(embed=embed)


    #lvl top
    @commands.command()
    async def lvltop(self, ctx):
        try:
            validlist = []
            for i in datadict.keys():
                try:
                    temp = datadict[i]["xp"]
                    validlist.append(i)
                except: pass

            top1 = [0, None]
            for i in validlist:
                if top1[0] < datadict[i]["xp"]:
                    top1 = [datadict[i]["xp"], i]
            validlist.remove(top1[1])
            if len(validlist) == 0:
                top2 = None
                top3 = None

            else:
                top2 = [0, None]
                for i in validlist:
                    if top2[0] < datadict[i]["xp"]:
                        top2 = [datadict[i]["xp"], i]
                validlist.remove(top2[1])
            if len(validlist) == 0:
                top3 = None
            
            else:
                top3 = [0, None]
                for i in validlist:
                    if top3[0] < datadict[i]["xp"]:
                        top3 = [datadict[i]["xp"], i]

            topview=f"""
**Top 1: {datadict[top1[1]]["name"]}**
XP: {datadict[top1[1]]["xp"]}
Level: {int(math.sqrt(datadict[top1[1]]["xp"]/10))}
Weapon: {datadict[top1[1]]["weapon"]["name"]}
Armor: {datadict[top1[1]]["armor"]["name"]}
Extra: {datadict[top1[1]]["extra"]["name"]}
            """

            if top2 != None:
                topview+=f"""

**Top 2: {datadict[top2[1]]["name"]}**
XP: {datadict[top2[1]]["xp"]}
Level: {int(math.sqrt(datadict[top2[1]]["xp"]/10))}
Weapon: {datadict[top2[1]]["weapon"]["name"]}
Armor: {datadict[top2[1]]["armor"]["name"]}
Extra: {datadict[top2[1]]["extra"]["name"]}
            """

            if top3 != None:
                topview+=f"""

**Top 3: {datadict[top3[1]]["name"]}**
XP: {datadict[top3[1]]["xp"]}
Level: {int(math.sqrt(datadict[top3[1]]["xp"]/10))}
Weapon: {datadict[top3[1]]["weapon"]["name"]}
Armor: {datadict[top3[1]]["armor"]["name"]}
Extra: {datadict[top3[1]]["extra"]["name"]}
            """

            embed = discord.Embed(title="Level Top", description=topview, color=discord.Color.green())
            embed.set_thumbnail(url=self.bot.get_user(int(top1[1])).avatar_url)
            await ctx.send(embed=embed)

        except Exception as e:
            embed = discord.Embed(title="Error", description=f"```{e}```", color=discord.Color.dark_red())
            await ctx.send(embed=embed)


    #coins top
    @commands.command()
    async def coinstop(self, ctx):
        try:
            validlist = []
            for i in datadict.keys():
                try:
                    temp = datadict[i]["coins"]
                    validlist.append(i)
                except: pass

            top1 = [0, None]
            for i in validlist:
                if top1[0] < datadict[i]["coins"]:
                    top1 = [datadict[i]["coins"], i]
            validlist.remove(top1[1])
            if len(validlist) == 0:
                top2 = None
                top3 = None

            else:
                top2 = [0, None]
                for i in validlist:
                    if top2[0] < datadict[i]["coins"]:
                        top2 = [datadict[i]["coins"], i]
                validlist.remove(top2[1])
            if len(validlist) == 0:
                top3 = None
            
            else:
                top3 = [0, None]
                for i in validlist:
                    if top3[0] < datadict[i]["coins"]:
                        top3 = [datadict[i]["coins"], i]

            topview=f"""
**Top 1: {datadict[top1[1]]["name"]}**
Coins: {datadict[top1[1]]["coins"]}
Weapon: {datadict[top1[1]]["weapon"]["name"]}
Armor: {datadict[top1[1]]["armor"]["name"]}
Extra: {datadict[top1[1]]["extra"]["name"]}
            """

            if top2 != None:
                topview+=f"""

**Top 2: {datadict[top2[1]]["name"]}**
Coins: {datadict[top2[1]]["coins"]}
Weapon: {datadict[top2[1]]["weapon"]["name"]}
Armor: {datadict[top2[1]]["armor"]["name"]}
Extra: {datadict[top2[1]]["extra"]["name"]}
            """

            if top3 != None:
                topview+=f"""

**Top 3: {datadict[top3[1]]["name"]}**
Coins: {datadict[top3[1]]["coins"]}
Weapon: {datadict[top3[1]]["weapon"]["name"]}
Armor: {datadict[top3[1]]["armor"]["name"]}
Extra: {datadict[top3[1]]["extra"]["name"]}
            """

            embed = discord.Embed(title="Coins Top", description=topview, color=discord.Color.green())
            embed.set_thumbnail(url=self.bot.get_user(int(top1[1])).avatar_url)
            await ctx.send(embed=embed)

        except Exception as e:
            embed = discord.Embed(title="Error", description=f"```{e}```", color=discord.Color.dark_red())
            await ctx.send(embed=embed)


    #gear top
    @commands.command()
    async def geartop(self, ctx):
        try:
            validlist = []
            for i in datadict.keys():
                try:
                    temp = datadict[i]["weapon"]
                    validlist.append(i)
                except: pass

            top1 = [0, None, None]
            for i in validlist:
                xv = datadict[i]["weapon"]["type"]["rarity"]
                yv = datadict[i]["armor"]["type"]["rarity"]
                zv = datadict[i]["extra"]["type"]["rarity"]
                iv = gamedata.Basics.WORTH[xv] + gamedata.Basics.WORTH[yv] + gamedata.Basics.WORTH[zv]
                if top1[0] < iv:
                    top1 = [iv, i, [xv, yv, zv]]
            validlist.remove(top1[1])
            if len(validlist) == 0:
                top2 = None
                top3 = None

            else:
                top2 = [0, None, None]
                for i in validlist:
                    xv = datadict[i]["weapon"]["type"]["rarity"]
                    yv = datadict[i]["armor"]["type"]["rarity"]
                    zv = datadict[i]["extra"]["type"]["rarity"]
                    iv = gamedata.Basics.WORTH[xv] + gamedata.Basics.WORTH[yv] + gamedata.Basics.WORTH[zv]
                    if top2[0] < iv:
                        top2 = [iv, i, [xv, yv, zv]]
                validlist.remove(top2[1])
            if len(validlist) == 0:
                top3 = None
            
            else:
                top3 = [0, None, None]
                for i in validlist:
                    xv = datadict[i]["weapon"]["type"]["rarity"]
                    yv = datadict[i]["armor"]["type"]["rarity"]
                    zv = datadict[i]["extra"]["type"]["rarity"]
                    iv = gamedata.Basics.WORTH[xv] + gamedata.Basics.WORTH[yv] + gamedata.Basics.WORTH[zv]
                    if top3[0] < iv:
                        top3 = [iv, i, [xv, yv, zv]]
                validlist.remove(top3[1])

            topview=f"""
**Top 1: {datadict[top1[1]]["name"]}**
Weapon: {datadict[top1[1]]["weapon"]["name"]}
Rarity: {top1[2][0]}
Armor: {datadict[top1[1]]["armor"]["name"]}
Rarity: {top1[2][1]}
Extra: {datadict[top1[1]]["extra"]["name"]}
Rarity: {top1[2][2]}
            """

            if top2 != None:
                topview+=f"""

**Top 2: {datadict[top2[1]]["name"]}**
Weapon: {datadict[top2[1]]["weapon"]["name"]}
Rarity: {top2[2][0]}
Armor: {datadict[top2[1]]["armor"]["name"]}
Rarity: {top2[2][1]}
Extra: {datadict[top2[1]]["extra"]["name"]}
Rarity: {top2[2][2]}
            """

            if top3 != None:
                topview+=f"""
                
**Top 3: {datadict[top3[1]]["name"]}**
Weapon: {datadict[top3[1]]["weapon"]["name"]}
Rarity: {top3[2][0]}
Armor: {datadict[top3[1]]["armor"]["name"]}
Rarity: {top3[2][1]}
Extra: {datadict[top3[1]]["extra"]["name"]}
Rarity: {top3[2][2]}
            """

            embed = discord.Embed(title="Gear Top", description=topview, color=discord.Color.green())
            embed.set_thumbnail(url=self.bot.get_user(int(top1[1])).avatar_url)
            await ctx.send(embed=embed)

        except Exception as e:
            embed = discord.Embed(title="Error", description=f"```{e}```", color=discord.Color.dark_red())
            await ctx.send(embed=embed)


    #door top
    @commands.command()
    async def doorstop(self, ctx):
        try:
            validlist = []
            for i in datadict.keys():
                try:
                    temp = datadict[i]["doors"]
                    validlist.append(i)
                except: pass

            top1 = [0, None]
            for i in validlist:
                if top1[0] < datadict[i]["doors"]:
                    top1 = [datadict[i]["doors"], i]
            validlist.remove(top1[1])
            if len(validlist) == 0:
                top2 = None
            else:
                top2 = [0, None]
                for i in validlist:
                    if top2[0] < datadict[i]["doors"]:
                        top2 = [datadict[i]["doors"], i]
                validlist.remove(top2[1])
                no2 = self.bot.get_guild(int(top2[1]))
            if len(validlist) == 0:
                top3 = None
            else:
                top3 = [0, None]
                for i in validlist:
                    if top3[0] < datadict[i]["doors"]:
                        top3 = [datadict[i]["doors"], i]
                no3 = self.bot.get_guild(int(top3[1]))
            no1 = self.bot.get_guild(int(top1[1]))
            topview=f"""
**Top 1: {no1.name}**
Doors: {datadict[top1[1]]["doors"]}
Level: {int(math.sqrt(datadict[top1[1]]["doors"]/10))}
            """

            if top2 != None:
                topview+=f"""

**Top 2: {no2.name}**
Doors: {datadict[top2[1]]["doors"]}
Level: {int(math.sqrt(datadict[top2[1]]["doors"]/10))}
            """

            if top3 != None:
                topview+=f"""

**Top 3: {no3.name}**
Doors: {datadict[top3[1]]["doors"]}
Level: {int(math.sqrt(datadict[top3[1]]["doors"]/10))}
            """

            embed = discord.Embed(title="Top Dungeons", description=topview, color=discord.Color.green())
            embed.set_thumbnail(url=no1.icon_url)
            await ctx.send(embed=embed)

        except Exception as e:
            embed = discord.Embed(title="Error", description=f"```{e}```", color=discord.Color.dark_red())
            await ctx.send(embed=embed)


    #buyboss 
    @commands.command()
    @commands.guild_only()
    async def summon_boss(self, ctx, *, bossname: str = None):
        try:
            uid = str(ctx.author.id)
            if uid in datadict["bl"]:
                return
            regflag = False
            try:
                if datadict[uid]:
                    regflag = True
            except:
                embed = discord.Embed(title="No Data", description="Do `<start` to create a player.", color=discord.Color.dark_red())
                await ctx.send(embed=embed)

            if regflag == True:
                gid = str(ctx.guild.id)
                gregflag = False
                try:
                    if datadict[gid]:
                        gregflag = True
                except:
                    embed = discord.Embed(title="Error", description="This Dungeon has to be lvl 3 or higher.", color=discord.Color.dark_red())
                    await ctx.send(embed=embed)
                    return
                if int(math.sqrt(datadict[gid]["doors"]/10)) < 3:
                    embed = discord.Embed(title="Error", description="This Dungeon has to be lvl 3 or higher.", color=discord.Color.dark_red())
                    await ctx.send(embed=embed)
                else:
                    try:
                        if datadict[gid]["currentboss"]:
                            temp = False
                    except:
                        datadict[gid]["currentboss"] = None
                    if bossname == None:
                        embed = discord.Embed(title="Error", description="No Boss Given", color=discord.Color.dark_red())
                        await ctx.send(embed=embed)
                    else:
                        foundflag = False
                        for i in gamedata.RandomLists.BOSSES:
                            if i["name"] == bossname:
                                foundflag = True
                                #checks if player can summon
                                if int(math.sqrt(datadict[uid]["xp"]/10)) < i["plvl"]:
                                    embed = discord.Embed(title="Error", description="Your level is too low to summon this boss.", color=discord.Color.dark_red())
                                    await ctx.send(embed=embed)
                                    return
                                if int(math.sqrt(datadict[gid]["doors"]/10)) < i["minlvl"]:
                                    embed = discord.Embed(title="Error", description="This dungeons level is too low to summon this boss.", color=discord.Color.dark_red())
                                    await ctx.send(embed=embed)
                                    return
                                if datadict[uid]["coins"] < i["summoncost"]:
                                    embed = discord.Embed(title="Error", description="You can't afford to summon this boss.", color=discord.Color.dark_red())
                                    await ctx.send(embed=embed)
                                    return
                                if datadict[gid]["currentboss"] != None:
                                    embed = discord.Embed(title="Error", description="This dungeon already has an active boss.", color=discord.Color.dark_red())
                                    await ctx.send(embed=embed)
                                    return
                                #boss hp calculation
                                validlist = []
                                for x in datadict.keys():
                                    serverm = ctx.guild.members
                                    try:
                                        temp = datadict[x]["xp"]
                                        useriq = self.bot.get_user(int(x))
                                        if useriq in serverm:
                                            if int(math.sqrt(datadict[x]["xp"]/10)) >= i["plvl"]:
                                                validlist.append(x)
                                    except: pass
                                if len(validlist) > 0:
                                    bhp = len(validlist)/2*3000
                                    datadict[gid]["currentboss"] = [i, bhp, round(bhp, 2), {}]
                                    bname = i["name"]
                                    datadict[uid]["coins"] -= i["summoncost"]
                                    embed = discord.Embed(title="Boss", description=f"You have summoned a {bname}!\nTo view the active boss use `<boss`.", color=discord.Color.green())
                                    await ctx.send(embed=embed)
                        if foundflag == False:
                            embed = discord.Embed(title="Error", description="Boss not found.", color=discord.Color.dark_red())
                            await ctx.send(embed=embed)

        except Exception as e:
            embed = discord.Embed(title="Error", description=f"```{e}```", color=discord.Color.dark_red())
            await ctx.send(embed=embed)


    #boss view command
    @commands.command()
    @commands.guild_only()
    async def boss(self, ctx):
        try:
            gid = str(ctx.guild.id)
            gregflag = False
            try:
                if datadict[gid]:
                    gregflag = True
            except:
                embed = discord.Embed(title="Error", description="This Dungeon does not have an active boss.", color=discord.Color.dark_red())
                await ctx.send(embed=embed)
                return
            try:
                if datadict[gid]["currentboss"]:
                    temp = False
            except:
                datadict[gid]["currentboss"] = None
            if datadict[gid]["currentboss"] == None:
                embed = discord.Embed(title="Error", description="This Dungeon does not have an active boss.", color=discord.Color.dark_red())
                await ctx.send(embed=embed)
            else:
                embed = discord.Embed(title="Boss", description=f"""
**Active Boss:**
Name: {datadict[gid]["currentboss"][0]["name"]}

Health: {int(datadict[gid]["currentboss"][1]/500) * "I"} - ({round(datadict[gid]["currentboss"][1], 2)}/{datadict[gid]["currentboss"][2]})

For more info do `<bossinfo {datadict[gid]["currentboss"][0]["name"]}`
                """, color=discord.Color.green())
                await ctx.send(embed=embed)

        except Exception as e:
            embed = discord.Embed(title="Error", description=f"```{e}```", color=discord.Color.dark_red())
            await ctx.send(embed=embed)


    @commands.command()
    @commands.guild_only()
    async def clear_boss(self, ctx):
        try:
            gid = str(ctx.guild.id)
            try:
                if datadict[gid]:
                    if ctx.author.id in ownerid:
                        datadict[gid]["currentboss"] = None
                        embed = discord.Embed(title="Success", description="Cleared current boss.", color=discord.Color.green())
                        await ctx.send(embed=embed)
                    else:
                        embed = discord.Embed(title="No Permission", description="You can't use this command.", color=discord.Color.dark_red())
                        await ctx.send(embed=embed)
            except: pass
            
        except Exception as e:
            embed = discord.Embed(title="Error", description=f"```{e}```", color=discord.Color.dark_red())
            await ctx.send(embed=embed)


    @commands.command()
    @commands.guild_only()
    async def atk(self, ctx):
        try:
            uid = str(ctx.author.id)
            if uid in datadict["bl"]:
                return
            regflag = False
            try:
                if datadict[uid]:
                    regflag = True
            except:
                embed = discord.Embed(title="No Data", description="Do `<start` to create a player.", color=discord.Color.dark_red())
                await ctx.send(embed=embed)

            if regflag == True:
                gid = str(ctx.guild.id)
                gregflag = False
                try:
                    if datadict[gid]:
                        gregflag = True
                except:
                    embed = discord.Embed(title="Error", description="This Dungeon does not have an active boss.", color=discord.Color.dark_red())
                    await ctx.send(embed=embed)
                    return
                try:
                    if datadict[gid]["currentboss"]:
                        temp = False
                except:
                    datadict[gid]["currentboss"] = None
                if datadict[gid]["currentboss"] == None:
                    embed = discord.Embed(title="Error", description="This Dungeon does not have an active boss.", color=discord.Color.dark_red())
                    await ctx.send(embed=embed)
                else:
                    #cooldown here
                    try:
                        if datadict[uid]["lastatk"]:
                            temp = False
                    except:
                        datadict[uid]["lastatk"] = None
                    cooldownflag = False
                    if datadict[uid]["lastatk"] == None:
                        dif = None
                        pass
                    else:
                        timenow = datetime.datetime.now()
                        difference = timenow - datetime.datetime.strptime(datadict[uid]["lastatk"], "%Y-%m-%d %H:%M:%S.%f")
                        dif = difference.total_seconds()
                        if difference.total_seconds() < 30:
                            cooldownflag = True
                    if cooldownflag == True:
                        embed = discord.Embed(title="Cooldown", description=f"You can attack again in {str(int(difference.total_seconds()-30))[1:]}sec", color=discord.Color.dark_red())
                        await ctx.send(embed=embed)
                        return
                    datadict[uid]["lastatk"] = str(datetime.datetime.now())

                    #anticheat code
                    if dif != None:
                        if datadict[uid]["cheaterdifa"] != None:
                            difmin = dif-1
                            difmax = dif+1
                            if datadict[uid]["cheaterdifa"] > difmin and datadict[uid]["cheaterdifa"] < difmax:
                                datadict[uid]["cheaterchancea"] += 1
                            else:
                                datadict[uid]["cheaterchancea"] = 0
                            if datadict[uid]["cheaterchancea"] > 25:
                                datadict["bl"].append(uid)

                        datadict[uid]["cheaterdif"] = dif

                    #player statbuilding
                    php = datadict[uid]["hp"]
                    dmg = datadict[uid]["weapon"]["type"]["dmg"]
                    if datadict[uid]["weapon"]["type"]["perks"] != "none":
                        for i in datadict[uid]["weapon"]["type"]["perks"]:
                            dmg += i["dmg"] 
                            dmg += i["sharp"]

                    #armor
                    dmg+=datadict[uid]["armor"]["type"]["dmg"]
                    tank = datadict[uid]["armor"]["type"]["tank"]

                    if datadict[uid]["armor"]["type"]["perks"] != "none":
                        for i in datadict[uid]["armor"]["type"]["perks"]:
                            dmg+=i["dmg"]
                            tank*=i["tank"]

                    #extra
                    dmg*=datadict[uid]["extra"]["type"]["dmg"]
                    tank*=datadict[uid]["extra"]["type"]["tank"]

                    #boost
                    dmg*=datadict[uid]["boost"]

                    #class
                    dmg*=datadict[uid]["class"]["dmgm"]
                    tank*=datadict[uid]["class"]["tanks"]
                    if datadict[uid]["class"]["perks"] != "none":
                        for i in datadict[uid]["class"]["perks"]:
                            dmg*=i["dmg"]
                    dmg = round(dmg, 2)
                    bossdmg = datadict[gid]["currentboss"][0]["returndmg"]
                    php -= bossdmg*tank
                    if php < 0:
                        embed = discord.Embed(title=f"{ctx.author.name}- Boss", description=f"The boss deals {bossdmg}dmg.\nYou lose 500 coins.", color=discord.Color.dark_red())
                        datadict[uid]["coins"] -= 500
                        if datadict[uid]["coins"] < 0:
                            datadict[uid]["coins"] = 0
                        await ctx.send(embed=embed)
                    else:
                        try:
                            datadict[gid]["currentboss"][3][uid] += dmg
                        except:
                            datadict[gid]["currentboss"][3][uid] = dmg
                        datadict[gid]["currentboss"][1] -= dmg
                        if datadict[gid]["currentboss"][1] < 0:
                            datadict[gid]["currentboss"][1] = 0
                            winstring = f"""
**Boss Cleared**
The {datadict[gid]["currentboss"][0]["name"]} has been defeated.
Everyone who dealt damage gets 500xp.

**Damage:**
                            """
                            for i in list(datadict[gid]["currentboss"][3].keys()):
                                datadict[i]["xp"] += 500
                                pname = datadict[i]["name"]
                                pdmg = datadict[gid]["currentboss"][3][i]
                                winstring+=f"{pname}: {round(pdmg, 2)}\n"
                            embed = discord.Embed(title=f"Boss", description=winstring, color=discord.Color.green())
                            await ctx.send(embed=embed)
                            #drops
                            for i in list(datadict[gid]["currentboss"][3].keys()):
                                winin100 = datadict[gid]["currentboss"][3][i] / datadict[gid]["currentboss"][2]
                                winin100 = int(winin100*100)
                                rndnum = random.randint(0, 100)
                                if rndnum < winin100:
                                    if datadict[gid]["currentboss"][0]["drop"] in gamedata.RandomLists.WEAPON_UNIQUE:
                                        typex = "weapon"
                                    if datadict[gid]["currentboss"][0]["drop"] in gamedata.RandomLists.ARMOR_UNIQUE:
                                        typex = "armor"
                                    if datadict[gid]["currentboss"][0]["drop"] in gamedata.RandomLists.EXTRA_UNIQUE:
                                        typex = "extra"
                                    drop = [datadict[gid]["currentboss"][0]["drop"], typex]
                                    drop.append(gamedata.Basics.WORTH["unique"])
                                    pname = datadict[i]["name"]
                                    embed = discord.Embed(title=f"{pname} - Drop!", description=f"""
                **Congrats! You got a {drop[0]["name"]}**
                Rarity: {drop[0]["rarity"]}
                Worth: {drop[2]}

                Type `<sell_drop` to claim the money.
                Type `<infuse_drop` to infuse {int(drop[2]/4)}xp into your current {drop[1]}.
                Type `<claim_drop` to replace your {datadict[i][drop[1]]["name"]} (it will be lost).

                This drop will expire when you get another drop.
                                    """, color=discord.Color.green())
                                    embed.set_thumbnail(url=ctx.author.avatar_url)
                                    datadict[i]["latestdrop"] = drop
                                    await ctx.send(embed=embed)

                            datadict[gid]["currentboss"] = None
                        
                        else:
                            bosshp = datadict[gid]["currentboss"][1]
                            bossmax = datadict[gid]["currentboss"][2]
                            embed = discord.Embed(title=f"{ctx.author.name} - Boss", description=f"You hit the boss for {dmg}dmg.\nThe boss is at {round(bosshp, 2)}/{bossmax}", color=discord.Color.orange())
                            await ctx.send(embed=embed)

        except Exception as e:
            embed = discord.Embed(title="Error", description=f"```{e}```", color=discord.Color.dark_red())
            await ctx.send(embed=embed)


    #reset atk cooldown
    @commands.command()
    async def rac(self, ctx, uid: str = None):
        try:
            if ctx.author.id in ownerid:
                if uid == None:
                    uid = str(ctx.author.id)
                datadict[uid]["lastatk"] = None
                embed = discord.Embed(title="Success", description=f"Attack cooldown reset!", color=discord.Color.green())
                await ctx.send(embed=embed)
            else:
                embed = discord.Embed(title="No Permission", description=f"You can't use this command!", color=discord.Color.dark_red())
                await ctx.send(embed=embed)
        except Exception as e:
            embed = discord.Embed(title="Error", description=f"```{e}```", color=discord.Color.dark_red())
            await ctx.send(embed=embed)


    #listener (leveling, coins and random drops)
    @commands.Cog.listener()
    async def on_message(self, message):
        try:
            if message.author == self.bot.user:
                return
            try:
                if datadict["bl"]: pass
            except:
                datadict["bl"] = []
            uid = str(message.author.id)
            if uid in datadict["bl"]:
                return
            regflag = False
            try:
                if datadict[uid]:
                    regflag = True
            except:
                return

            if regflag == True:
                number = random.randint(1, 250)
                if number < 100:
                    datadict[uid]["coins"]+=1
                elif number < 200:
                    oldlvl = int(math.sqrt(datadict[uid]["xp"]/10))
                    datadict[uid]["xp"]+=1
                    newlvl = int(math.sqrt(datadict[uid]["xp"]/10))
                    if oldlvl < newlvl:
                        embed = discord.Embed(title=f"{message.author.name} - Levelup", description=f"You are now level {newlvl}!\n+5hp\n+1% Stats", color=discord.Color.green())
                        datadict[uid]["hp"]+=5
                        datadict[uid]["boost"]+=0.01
                        embed.set_thumbnail(url=message.author.avatar_url)
                        await message.channel.send(embed=embed)
                        number=250
                if number == 250:
                    if message.content.startswith("<buy_drop"):
                        return
                    if int(math.sqrt(datadict[uid]["xp"]/10)) > 25:
                        x = 10000
                    elif int(math.sqrt(datadict[uid]["xp"]/10)) > 15:
                        x = 9950
                    else:
                        x = 9900
                    number = random.randint(1, x)
                    number2 = random.randint(1,3)
                    if number < 6500:
                        coinsworth = gamedata.Basics.WORTH["common"]
                        if number2 == 1:
                            drop = [random.choice(gamedata.RandomLists.WEAPON_COMMON),"weapon"]
                        elif number2 == 2:
                            drop = [random.choice(gamedata.RandomLists.ARMOR_COMMON),"armor"]
                        elif number2 == 3:
                            drop = [random.choice(gamedata.RandomLists.EXTRA_COMMON),"extra"]

                    elif number < 8000:
                        coinsworth = gamedata.Basics.WORTH["normal"]
                        if number2 == 1:
                            drop = [random.choice(gamedata.RandomLists.WEAPON_NORMAL),"weapon"]
                        elif number2 == 2:
                            drop = [random.choice(gamedata.RandomLists.ARMOR_NORMAL),"armor"]
                        elif number2 == 3:
                            drop = [random.choice(gamedata.RandomLists.EXTRA_NORMAL),"extra"]

                    elif number < 9000:
                        coinsworth = gamedata.Basics.WORTH["uncommon"]
                        if number2 == 1:
                            drop = [random.choice(gamedata.RandomLists.WEAPON_UNCOMMON),"weapon"]
                        elif number2 == 2:
                            drop = [random.choice(gamedata.RandomLists.ARMOR_UNCOMMON),"armor"]
                        elif number2 == 3:
                            drop = [random.choice(gamedata.RandomLists.EXTRA_UNCOMMON),"extra"]

                    elif number < 9500:
                        coinsworth = gamedata.Basics.WORTH["rare"]
                        if number2 == 1:
                            drop = [random.choice(gamedata.RandomLists.WEAPON_RARE),"weapon"]
                        elif number2 == 2:
                            drop = [random.choice(gamedata.RandomLists.ARMOR_RARE),"armor"]
                        elif number2 == 3:
                            drop = [random.choice(gamedata.RandomLists.EXTRA_RARE),"extra"]

                    elif number < 9800:
                        coinsworth = gamedata.Basics.WORTH["very rare"]
                        if number2 == 1:
                            drop = [random.choice(gamedata.RandomLists.WEAPON_VERYRARE),"weapon"]
                        elif number2 == 2:
                            drop = [random.choice(gamedata.RandomLists.ARMOR_VERYRARE),"armor"]
                        elif number2 == 3:
                            drop = [random.choice(gamedata.RandomLists.EXTRA_VERYRARE),"extra"]

                    elif number < 9900:
                        coinsworth = gamedata.Basics.WORTH["epic"]
                        if number2 == 1:
                            drop = [random.choice(gamedata.RandomLists.WEAPON_EPIC),"weapon"]
                        elif number2 == 2:
                            drop = [random.choice(gamedata.RandomLists.ARMOR_EPIC),"armor"]
                        elif number2 == 3:
                            drop = [random.choice(gamedata.RandomLists.EXTRA_EPIC),"extra"]

                    elif number < 9950:
                        coinsworth = gamedata.Basics.WORTH["unstable"]
                        if number2 == 1:
                            drop = [random.choice(gamedata.RandomLists.WEAPON_UNSTABLE),"weapon"]
                        elif number2 == 2:
                            drop = [random.choice(gamedata.RandomLists.ARMOR_UNSTABLE),"armor"]
                        elif number2 == 3:
                            drop = [random.choice(gamedata.RandomLists.EXTRA_UNSTABLE),"extra"]

                    elif number < 10001:
                        coinsworth = gamedata.Basics.WORTH["corrupted"]
                        if number2 == 1:
                            drop = [random.choice(gamedata.RandomLists.WEAPON_CORRUPTED),"weapon"]
                        elif number2 == 2:
                            drop = [random.choice(gamedata.RandomLists.ARMOR_CORRUPTED),"armor"]
                        elif number2 == 3:
                            drop = [random.choice(gamedata.RandomLists.EXTRA_CORRUPTED),"extra"]
                    drop.append(coinsworth)
                    embed = discord.Embed(title=f"{message.author.name} - Drop!", description=f"""
**Congrats! You got a {drop[0]["name"]}**
Rarity: {drop[0]["rarity"]}
Worth: {drop[2]}

Type `<sell_drop` to claim the money.
Type `<infuse_drop` to infuse {int(drop[2]/4)}xp into your current {drop[1]}.
Type `<claim_drop` to replace your {datadict[uid][drop[1]]["name"]} (it will be lost).

This drop will expire when you get another drop.
                    """, color=discord.Color.green())
                    embed.set_thumbnail(url=message.author.avatar_url)
                    datadict[uid]["latestdrop"] = drop
                    await message.channel.send(embed=embed)

        except Exception as e:
            embed = discord.Embed(title="Error", description=f"```{e}```", color=discord.Color.dark_red())
            await message.channel.send(embed=embed)


    #eval for owner
    @commands.command()
    async def eval(self, ctx, input_value):
        if ctx.author.id in ownerid:
            try:
                output_value = eval(input_value)
                embed = discord.Embed(title=f"{ctx.author.name} - Eval", description=f"{input_value} = {output_value}", color=discord.Color.green())
                await ctx.send(embed=embed)
            except Exception as e:
                embed = discord.Embed(title="Error", description=f"Error running the command:\n```{e}```", color=discord.Color.dark_red())
                await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title="No Permission", description=f"You can't use this command!", color=discord.Color.dark_red())
            await ctx.send(embed=embed)


    #dbl stuff
    @tasks.loop(minutes=30.0)
    async def update_stats(self):
        print("----------")
        print(f"Attempting Count Post @{datetime.datetime.now().time()}")
        try:
            await self.dblpy.post_guild_count()
            print(f"Posted Server Count @{datetime.datetime.now().time()}")
        except Exception as e:
            print(f"Error posting server count:\n{e}")

    @commands.command()
    async def manual_servercount_post(self, ctx):
        if ctx.author.id in ownerid:
            try:
                await self.dblpy.post_guild_count()
                print(f"Posted Server Count @{datetime.datetime.now().time()}")
                embed = discord.Embed(title="Manual Server Count Post", description="Post Completed!", color=discord.Color.green())
                await ctx.send(embed=embed)
            except Exception as e:
                embed = discord.Embed(title="Error", description=f"Error running the command:\n```{e}```", color=discord.Color.dark_red())
                await ctx.send(embed=embed)
                print(f"Error posting server count:\n{e}")
        else:
            embed = discord.Embed(title="No Permission", description=f"You can't use this command!", color=discord.Color.dark_red())
            await ctx.send(embed=embed)

    @commands.Cog.listener()
    async def on_dbl_vote(self, data):
        print("----------")
        uid = data["user"]
        print(f"VOTE FROM USER {uid}")
        datadict[uid]["lastdaily"] = None
        

    @commands.Cog.listener()
    async def on_dbl_test(self, data):
        print("----------")
        print("TEST")
        print(data)

def setup(bot):
    bot.add_cog(GameCog(bot))