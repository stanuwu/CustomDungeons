import discord
from discord.ext import commands

class HelpCog(commands.Cog, name="Help Cog"):
    def __init__(self, bot):
        self.bot = bot
        global ownerid
        ownerid = [623984743914012712]

    #help command
    @commands.command()
    async def help(self, ctx, menu: str = None):
        #start help
        if menu == "start":
            embed = discord.Embed(title="Everything you need to know:",description="""
**NOTE:** By typing `<start` you agree that your profile picture and user name can be shown on the bots leaderboards visible from any server.

When you first start a profile is created for you.
You can view it any time with `<stats`.
You can also view a compact version of your stats with `<stats brief`.
To see all the commands do `<help`.
The main goal of the game is to level up your dungeon (a server gets a dungeon) and get onto leaderboards.
You also want to improve your stats.

There is 3 ways to Improve stats:
            """, color=discord.Color.green())

            embed.set_thumbnail(url=self.bot.user.avatar_url)
            embed.set_footer(text=self.bot.description)
            await ctx.send(embed=embed)

            embed = discord.Embed(description="""
1) Gear
You have a weapon, a set of armor and an extra item.
You can rarely obtain better gear from writing in chat and clearing rooms(more on that later.)
You can also level your gear by fighting or infusing(see `<help items`)
You can only have 1 of every gear item at a time.
You can also purchase a storage to store a second set later on.
Some high rarity gears can only be obtained when your level is very high.
You can also obtain gear from level ups, boss fights, or drops purchased with coins.
            """, color=discord.Color.green())

            await ctx.send(embed=embed)

            embed = discord.Embed(description="""
2) Coins
You can use coins for many things like buying gear drops, buying gear from `<shop` and gambling.
Coins can be gained by opening doors, but you can also loose coins. You also get coins when you just chat in a channel the bot can see.
To get some bonus coins you can also do `<daily` every 24h. To reset the cooldown you can use `<vote` every 12h.
Daily coins depend on your level so if you are level 0 you will get 0 coins. Only use daily after you are at least level 1.
            """, color=discord.Color.green())

            await ctx.send(embed=embed)

            embed = discord.Embed(description="""
3) Classes
You can pick a class that can make different stats higher or lower(see `<help general`)

4) Leveling
As you level up by writing in chat, clearing rooms and fighting bosses. 
Your health and multiplier will rise.
The health stat is your total hp in a fight and the multiplier makes your damage and healing higher.
            """, color=discord.Color.green())

            await ctx.send(embed=embed)

            embed = discord.Embed(description="""
You can start a fight by writing `<door` to open a door.
A room will show up, where you either find coins, a trap or fight an enemy.
The fight history will be displayed.
If you lose you will lose coins but if you win you will get coins, xp and gear xp.
If you win the server you are in will also get doors and slowly level up.

Now you know everything you have to know to start out.
If you want more info look in `<help`.
To start your journey type `<start`.
            """, color=discord.Color.green())

            await ctx.send(embed=embed)
            embed.set_footer(text=self.bot.description)
            await ctx.send(embed=embed)

        #core help
        elif menu == "core":
            embed = discord.Embed(title="Core Commands:",description="""
__**Core commands are owner only**__
`<reload [module-name]`
Reload all cogs except listed below.

`<reload_game`
Reload game cog, saves and restart task.
            
`<reload_backup`
Reload backup cog and restart task.

`<eval [value]`
Get eval (for debug purposes).

`<servers`
Get a list of the servers the bot is in. aka. |guilds
            """, color=discord.Color.green())

            embed.set_thumbnail(url=self.bot.user.avatar_url)
            embed.set_footer(text=self.bot.description)
            await ctx.send(embed=embed)

        #admin help
        elif menu == "admin":
            embed = discord.Embed(title="Testing Commands:",description="""
__**Admin commands are owner only**__
`<setweapon [user-id] [xp] [weapon-name]`
Replaces targets weapon.

`<setarmor [user-id] [xp] [armor-name]`
Replaces targets armor.
            
`<setweapon [user-id] [xp] [extra-name]`
Replaces targets extra.

`<setxp [user-id] [xp]`
Sets targets xp stat.

`<setcoins [user-id] [coins]`
Sets targets coins.

`<rdc (user-id)`
Resets door cooldown.

`<rpc (user-id)`
Resets pvp cooldown.

`<rtc (user-id)`
Resets train cooldown.

`<rdcc (user-id)`
Resets daily cooldown.

`<rac (user-id)`
Resets the boss attack cooldown.

`<clear_boss`
Removes a dungeons boss.
            """, color=discord.Color.green())

            embed.set_thumbnail(url=self.bot.user.avatar_url)
            embed.set_footer(text=self.bot.description)
            await ctx.send(embed=embed)

        #general help
        elif menu == "general":
            embed = discord.Embed(title="General Commands:",description="""
`<start`
Creates a profile for you.

`<stats (brief|full) (uid)`
Shows your stats. Adding brief shows a compact version without gear.
Adding another players user id shows you their stats.
Note: If you want to see another players full stats you have to add full.

            
`<dungeon`
Shows info about the current dungeon.

`<rename [name]`
Change your characters name.

`<setclass [Class Name]`
Sets your class.
Classes:
Empty -> Normal
`Thief`
`Fighter`
`Tank`
`Mage`
`Dark Mage`
`Assassin`

`<classinfo [Class Name]`
Gives you the stats of the class.

`<lvltop`
Shows xp leaderboard.

`<get`
Get the link to add the bot to your server.

`<report id: 00000000000000000 (invite: discord.gg/something) (message: https://discordapp.com/channels/0000/0000000/000000000) then write your report`
This can be multiple lines (in one message).
Report a player for reasons like scam/botting/exploiting bugs.
Please ALLWAYS include the user id of a player in the report.
If you want to report someone also include a message link of a message when it happened and a server invite.
(screenshots are not proof as inspect element exists)

`<bugreport type your report like this`
This can be multiple lines (in one message).
Please report any bugs or unbalanced things and suggestions.
The older mosters are easy on the lower levels but higher levels should be hard.
            """, color=discord.Color.green())

            embed.set_thumbnail(url=self.bot.user.avatar_url)
            embed.set_footer(text=self.bot.description)
            await ctx.send(embed=embed)

        #item help
        elif menu == "items":
            embed = discord.Embed(title="Item Commands:",description="""
`<rename_weapon [name]`
Rename your weapon.

`<rename_armor [name]`
Rename your armor.

`<rename_extra [name]`
Rename your extra.

`<geartop`
See who has the best gear.

`<sell_drop`
Sells your last drop you got for its value.

`<infuse_drop`
Infuses your last drop into your gear giving it xp.

`<claim_drop`
Replaces a gear piece with your last drop. (WARNING: your current gear piece will be lost)

`<buy_drop [rarity]`
Buy a random drop of the given rarity.
Rarities and Prices:
common: 100
normal: 500
uncommon: 1000
rare: 10000
very rare: 20000
epic: 50000
unstable: 100000
corrupted: 200000

`<train`
Level up your gear on the side. (has a 5min cooldown)

`<weapon [Weapon Name]`
Gives you the stats of the weapon.

`<armor [Armor Name]`
Gives you the stats of the armor.

`<extra [Extra Name]`
Gives you the stats of the extra.

`<shop`
Shows you the shop.

`<shop_buy [item-name]`
Buy an item from the shop.

`<store [weapon|armor|extra]`
Swap this item with the one in your storage (if you have one).

`<view_storage`
See whats in your storage.

`<buy_storage`
Buy a storage. A storage can store 1 of every item slot.
Needs lvl 10 to buy and costs 10k coins.

`<trade [@user] [weapon|armor|extra]`
Send a user a trade request for an item type.

`<trade_accept`
Accept a trade request.

`<trade_decline`
Decline a trade request.
            """, color=discord.Color.green())

            embed.set_thumbnail(url=self.bot.user.avatar_url)
            embed.set_footer(text=self.bot.description)
            await ctx.send(embed=embed)

        #coins help
        elif menu == "coins":
            embed = discord.Embed(title="Coin Commands:",description="""
`<pay [@user] [ammount]`
Give a user coins.

`<coinflip [bet]`
Coinflip for coins.

`<slots [bet]`
Play a slot game.
If you get the 3 green hearts you win 25x.
If you get any other 3 icons you win 10x.

`<daily`
Claim daily coins every 24h.

`<vote`
Reset your daily cooldown.

`<coinstop`
Shows coin leaderboard.
            """, color=discord.Color.green())

            embed.set_thumbnail(url=self.bot.user.avatar_url)
            embed.set_footer(text=self.bot.description)
            await ctx.send(embed=embed)

        #fight help
        elif menu == "fight":
            embed = discord.Embed(title="Fighting Commands:",description="""
`<door`
Open a door to a new room in the dungeon.

`<monster [Monster Name]`
Gives you the stats of the monster.

`<pvp [@user] (wager)`
Send someone a request to pvp.
If wager is not given it will be 0.

`<pvp_accept`
Accept a request to pvp.

`<pvp_decline`
Decline a request to pvp.

`doorstop`
Top dungeon leaderboard.
            """, color=discord.Color.green())
            embed.set_thumbnail(url=self.bot.user.avatar_url)
            embed.set_footer(text=self.bot.description)
            await ctx.send(embed=embed)

        #boss help
        elif menu == "boss":
            embed = discord.Embed(title="Boss Commands:",description="""
**Info:**
Your dungeon has to be minimum LvL 3 to summon a boss.
Also please note that some boss drops are better than others but all of them have the same price/xp.

`<summon_boss [boss-name]`
Summon a new boss to the dungeon.
There can only be 1 boss at a time.

`<atk`
Attack a boss if there is one.
Has a 30 second cooldown.
When you attack the boss and the dmg of the boss kills you you lose coins and dont do damage.
If your boss dies the people with the most damage % will be most likely to get the drop.

`<boss`
See the current bosses health and stats.

`<bossinfo [boss-name]`
Here you can see stats and summoning requirements of a boss.

**Bosses:**
Gigagoblin
Hive Slayer
World Eater
Ancient Magic Caster
Life Collector
Devils Son
            """, color=discord.Color.green())

            embed.set_thumbnail(url=self.bot.user.avatar_url)
            embed.set_footer(text=self.bot.description)
            await ctx.send(embed=embed)

        #general help    
        else:
            embed = discord.Embed(title="CustomDungeons | help pages", color=discord.Color.green())
            embed.add_field(name="<help start", value="The Basics", inline=True)
            embed.add_field(name="<help items", value="All Item related Commands", inline=True)
            embed.add_field(name="<help coins", value="All Coin related Commands", inline=True)
            embed.add_field(name="<help fight", value="All Fight related Commands", inline=True)
            embed.add_field(name="<help boss", value="All Boss related Commands", inline=True)
            embed.add_field(name="<help general", value="All General Commands", inline=True)
            embed.add_field(name="<help admin", value="Bot Owner Testing Commands", inline=True)
            embed.add_field(name="<help core", value="Bot Owner Commands", inline=True)
            embed.add_field(name="<info", value="Info about CustomDungeons", inline=True)
            embed.set_thumbnail(url=self.bot.user.avatar_url)
            embed.set_footer(text=self.bot.description)
            await ctx.send(embed=embed)

    #info
    @commands.command()
    async def info(self, ctx):
        embed = discord.Embed(title="CustomDungeons | info",description=f"""
CustomDungeons is a Discord Bot that is made to play a chat based Dungeon Game.
This bot makes every server a dungeon, that has different monsters for different level players to fight.
It focuses on customisation and advantage by being on Discord a lot.

**Version**
{self.bot.description}
**Creator**
stan#0666
**Home**
https://discord.gg/K7EnebH
**Get CustomDungeons**
https://discordapp.com/oauth2/authorize?scope=bot&permissions=1144507456&client_id=717757487482273813
**Created with**
discord.py (ext)
            """, color=discord.Color.green())

        embed.set_thumbnail(url=self.bot.user.avatar_url)
        embed.set_footer(text=self.bot.description)
        await ctx.send(embed=embed)


    #get
    @commands.command()
    async def get(self, ctx):
        embed = discord.Embed(title="Get CustomDungeons",description=f"""
**Use this link to add CustomDungeons to your server.**
https://discordapp.com/oauth2/authorize?scope=bot&permissions=1144507456&client_id=717757487482273813
            """, color=discord.Color.green())

        embed.set_thumbnail(url=self.bot.user.avatar_url)
        embed.set_footer(text=self.bot.description)
        await ctx.send(embed=embed)


    #rules
    @commands.command()
    async def rules(self, ctx):
        embed = discord.Embed(title="CustomDungeons | rules",description="""
Not following these rules can and will lead to warnings, stat resets and/or being blacklisted from the bot completely.
I must also note that I am the only dev of the bot and will never ask for any money/items as i can just take/give them.
Also do NOT give money/items to anyone you don't trust and check someones stats before wagering money in a pvp match.

1) Stay friendly, its only a game.
2) Stay somewhat family friendly with item/character name. (warning / stat clear)
3) No links anywhere in the bot. (stat clear / blacklist)
4) Nothing illegal. This includes links to anything illegal. (stat clear / blacklist / report to authorities)
5) No Botting. Use of any selfbot / scripts to farm this bot will be detected by the anti-cheat. (stat clear / blacklist / report to discord for TOS Violation)
6) No scamming. If you got scammed look in `<help general` how to report someone. (stat clear / blacklist)
7) Using alts for any purpose. Just play one one account. (stat clear / blacklist)
8) Sharing an account is not allowed. (stat clear / blacklist)

If you see anyone breaking these rules report them! Its very easy and there is no excuse. If someone breaks the rules again, report them twice.
The person will not know who reported them.
Look in `<help general` for more info.
If you do not report someone breaking the rules you can face the same punishment as the rulebreaker.
If you think you have been falsely blacklisted please dm stan#0666 / join the CustomDungeons Dev discord to appeal.
            """, color=discord.Color.green())

        embed.set_thumbnail(url=self.bot.user.avatar_url)
        embed.set_footer(text=self.bot.description)
        await ctx.send(embed=embed)


    #vote help
    @commands.command()
    async def vote(self, ctx):
        embed = discord.Embed(title="Vote",description="""
Vote for CustomDungeons on Discord Bot List to reset your daily cooldown!
You can vote every 12h and it might take a few minutes for your vote to register.
Vote here:
https://top.gg/bot/717757487482273813
            """, color=discord.Color.green())
        await ctx.send(embed=embed)


    #on join
    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        try:
            general = discord.utils.find(lambda x: x.name == 'general',  guild.text_channels)
            embed = discord.Embed(title="Hello",description="""
Thanks for adding this bot.
To get started and use the bot do `<help`.
If you have any more questions or like the bot please join our official discord!
https://discord.gg/K7EnebH
You can also dm the creator *stan#0666* if something is urgent.
If you enjoy using this bot please share it with your friends.
**NOTE:** By typing `<start` you agree that your profile picture and user name can be shown on the bots leaderboards visible from any server.
            """, color=discord.Color.green())
            if general:
                try:
                    await general.send(embed=embed)
                except: pass
            else:
                try:
                    await guild.text_channels[0].send(embed=embed)
                except:
                    for x in guild.text_channels:
                        try:
                            await x.send(embed=embed)
                            break
                        except: pass
        except Exception as e:
            print(e)


def setup(bot):
    bot.add_cog(HelpCog(bot))