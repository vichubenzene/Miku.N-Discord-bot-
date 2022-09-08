import discord
from discord.ext import commands
import random
from datetime import datetime
import time
from datetime import timedelta
import json
import requests
from jikanpy import jikan
aki = jikan.Jikan()
import topgg
dbl_token = "####" #token

with open('sfw_json/topic.json', 'r') as f:
    src_topic=json.load(f)
class Example(commands.Cog):
    def __init__(self,client):
        self.client=client
    
    @commands.Cog.listener()
    async def on_ready(self):
        global startTime 
        startTime = time.time()
        print("Utility is ready")


    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.guild_only()
    async def avatar(self,ctx, member: discord.Member = None):
        if not member:
            member = ctx.message.author
        embed = discord.Embed(description=f"{member.mention} Avatar <:02Cozy:878167184705204225>",timestamp=(ctx.message.created_at),colour=0x39138b)
        embed.set_image(url=member.avatar_url)
        await ctx.send(embed=embed)


    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.guild_only()
    async def banner(self,ctx, member: discord.Member = None):
        if not member:
                member = ctx.message.author
        req = await self.client.http.request(discord.http.Route("GET", f"/users/{member.id}"))
        banner_id = req["banner"]
        if banner_id:
            banner_url = f"https://cdn.discordapp.com/banners/{member.id}/{banner_id}?size=1024"

            embed = discord.Embed(description=f"{member.mention} Banner <:MikuThanks:879900458603393094>", colour=0x39138b)
            embed.set_footer(text=f"{ctx.message.author.name}",icon_url=self.client.user.avatar_url)
            embed.set_image(url=banner_url)
            await ctx.send(embed=embed)




    @commands.command(aliases=["guildinfo","server","serverinfo"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.guild_only()
    async def doxserver(self,ctx):
        now = datetime.now()
        mem_join = ctx.guild.created_at
        join_days = (now-mem_join).days
        date_format = "%a, %d %b %Y %I:%M %p"


        embed = discord.Embed(title=f"{ctx.guild.name}",

                            timestamp=(ctx.message.created_at), color=0x39138b)
        embed.add_field(name="Server created at", value=f"{ctx.guild.created_at.strftime(date_format)}\n`Created {(join_days)} days ago`",inline=False)

        embed.add_field(name='Created before', value=f"{(join_days)} days",inline=False)
        owner=ctx.guild.owner_id
        embed.add_field(name="Server Owner", value=f"> {await self.client.fetch_user(owner)}",inline=False)
        # embed.add_field(name="Server Region", value=f"{ctx.guild.region}",inline=False)
        embed.add_field(name="Server ID", value=f"{ctx.guild.id}",inline=False)
        roles = [role for role in ctx.guild.roles]
        roles.reverse()
        rolee=''.join([role.mention for role in roles])
        embed.add_field(name="Server with",value=f"> {(ctx.message.guild.member_count)} Members\n > {len(ctx.guild.roles)} Roles\n> {len(ctx.guild.text_channels)} Text-Channels\n> {len(ctx.guild.voice_channels)} Voice-Channels\n> {len(ctx.guild.categories)} Categories")
        embed.set_thumbnail(url=f"{ctx.guild.icon_url}")
        if len(rolee)<1000:
            embed.add_field(name='Roles:', value=(''.join([role.mention for role in roles])),inline=False)
        else:
            embed.add_field(name='Roles:', value="use `m.roles`",inline=False)

        embed.set_footer(text='Miku.N development',icon_url=ctx.message.author.avatar_url)
        await ctx.send(embed=embed)



    @commands.command(aliases=['whois','userinfo',"user"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.guild_only()
    async def info(self,ctx, member: discord.Member = None):

        if not member:
            member = ctx.message.author
        roles = [role for role in member.roles]
        embed = discord.Embed(colour=0x39138b, timestamp=(ctx.message.created_at),
                            title=f"{member}")
        embed.set_thumbnail(url=(member.avatar_url))
        embed.set_footer(text='Miku.N development',icon_url=ctx.message.author.avatar_url)
        embed.add_field(name='ID:', value=(member.id))
        embed.add_field(name='Display Name:', value=(member.display_name),inline=False)
        # s=str(member.status)
        # s=s.replace("dnd", "**Do Not Disturb** <:dnd:880701480196263986>")
        # s=s.replace("online", "**Online** <:status_online:880701632738889788>")
        # s=s.replace("idle", "**Idle** <:idle:880708125009772554>")
        # s=s.replace("offline", "**Offline**")
        # try:
        #     embed.add_field(name="**Status**", value=f'{s} - {member.activities[0].name}', inline=True)
        # except:
        #     embed.add_field(name="**Status**", value=s, inline=True)
        # embed.set_thumbnail(url=f"{member.avatar_url}")
        now = datetime.now()
        print(now)
        crt_join = (now-member.created_at).days
        embed.add_field(name='Created Account On:', value=f"{(member.created_at.strftime('%a, %#d %B %Y, %I:%M %p UTC'))}\n `created {crt_join} days ago`",inline=False)
        mem_join = member.joined_at

        join_days = (now-mem_join).days
        embed.add_field(name='Joined Server On:', value=(f"{(mem_join.strftime('%a, %#d %B %Y, %I:%M %p UTC'))}\n`Joined {join_days} days ago`"),inline=False)

        rolee=''.join([role.mention for role in roles])
        embed.add_field(name='Highest Role:', value=(member.top_role.mention))
        if len(rolee)<1000:
            print("helloe")
            embed.add_field(name='Roles:', value=rolee,inline=False)
        else:
            embed.add_field(name='Roles:', value="use `m.roles @user`",inline=False)
        embed.set_author(name="Miku.N" ,icon_url=self.client.user.avatar_url)
        await ctx.send(embed=embed)


    @commands.command(aliases=["role"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.guild_only()
    async def roles(self,ctx, member: discord.Member = None):
            if not member:
                roles = [role for role in ctx.guild.roles]
            else:
                roles = [role for role in member.roles]
            rolee=''.join([role.mention for role in roles])
            embed = discord.Embed(title=f"Roles",description=f"{rolee}",timestamp=(ctx.message.created_at), color=0x39138b)
            embed.set_footer(text='😎',icon_url=ctx.message.author.avatar_url)
            await ctx.send(embed=embed)
    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.guild_only()
    async def topic(self,ctx):
        ltopic=random.choice(src_topic)
        await ctx.send(ltopic)
        
     
    @commands.command(aliases=["trash"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.guild_only()
    async def toxic(self,ctx, member: discord.Member = None):
        url = 'https://evilinsult.com/generate_insult.php?lang=en&type=json'
        response = requests.get(url)
        x = response.json()
        if not member:
            await ctx.send(f"{x['insult']}")
        else:
          await ctx.send(f"`{str(member)}` {x['insult']}")
    # await ctx.send(x['insult'], delete_after=120)
    # await ctx.message.delete(delay=120)
    # if await client.topgg.get_user_vote(user_id=ctx.author.id):
    #     ctx.command.reset_cooldown(ctx)

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.guild_only()
    @commands.has_permissions(manage_messages=True)
    async def clear(self,ctx, *, amount):
        amt = int(amount)
        if ((amt < 25) and (amt > 0)):
            await ctx.channel.purge(limit=amt)
        else:
            await ctx.send("`enter less than 25`",delete_after=10)


    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.guild_only()
    @commands.has_permissions(manage_messages=True)
    async def purge(self,ctx, limit=10, member: discord.Member=None):
        msg = []
        try:
            limit = int(limit)
        except:
            return await ctx.send("Please pass in an integer as limit")
        if not member:
            await ctx.channel.purge(limit=limit)
            return await ctx.send(f"Purged {limit} messages", delete_after=3)
        async for m in ctx.channel.history():
            if len(msg) == limit:
                break
            if m.author == member:
                msg.append(m)
        await ctx.channel.delete_messages(msg)
        await ctx.send(f"Purged {limit} messages of {member.mention}", delete_after=3)



    @commands.command(aliases=["botstats","botstat"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.guild_only()
    async def botinfo(self,ctx):
        shard_id = ctx.guild.shard_id
        shard = self.client.get_shard(shard_id)
        shard_ping = shard.latency
        print(shard_id)
        shard_servers = len([guild for guild in self.client.guilds if guild.shard_id == shard_id])
        owner=await self.client.fetch_user(557578041908396033)
        uptime = str(timedelta(seconds=int(round(time.time()-startTime))))
        guilds = self.client.guilds
        members=0
        for guild in guilds:
            members += len(guild.members)
        print(members)
        embed = discord.Embed(title=f"Owner : {owner}  <:benzenehappy:865643379530792981> \n\n Bot : Miku.N||sfw||#0211 <a:shy:895708817789157448>",description=f"> language : `D.py` <:APY:895722825409781812>\n> Guilds :** `{len(self.client.guilds)}` **\n> members : 41k avrg \n> shards :** `10` **\n> server shard : {shard_id}\n> shard servers : {shard_servers}\n> uptime : `{uptime}`\n> ping : `{round(self.client.latency * 1000)}`\n\n[Server](https://discord.gg/cyKAjwcZdB) •  [Github](https://github.com/vichubenzene/Miku.N-Discord-bot-/blob/main/README.md)",colour = 0x19198c)
        embed.set_thumbnail(url=self.client.user.avatar_url)
        embed.set_footer(icon_url=self.client.user.avatar_url,
                         text=f"Solo Owner of Miku.N with 💖.. M.donate for support")
        await ctx.send(embed=embed)

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.guild_only()
    async def owner(self,ctx):
        owner=await self.client.fetch_user(557578041908396033)
        embed = discord.Embed(title=f"\t{owner}  <:benzenehappy:865643379530792981>\n\t<:tx18plus:894297424523325470>\t♂️\t<:hetero_flag:897586113923919872>\t🇮🇳",description="> • Just intrested in creating bots that brings Otaku vibes to users\n> • An introvert searching for an Dandere girl\n> • Noob at making friends\n> • Simp : dandere waifu's\n> • First anime : Death Note on 10/2018\n> • Fav anime : Naruto\n> • First sauce : 177013\n> • Thought of creating this bot on `25/2/2021 6:00 PM IST` in the mindset of personel use for doujin recommendation\n> • Then thats it ig... nothing more <:c6h6tq:878149821955989545>\n\n contact: [Server](https://discord.gg/cyKAjwcZdB) • [Github](https://github.com/vichubenzene/vichubenzene)",colour = 0x19198c)
        embed.set_thumbnail(url=owner.avatar_url)
        embed.set_image(url="https://cdn.discordapp.com/attachments/858653930376265728/993865959867691068/ezgif-3-ed26c922ada2.gif")
        embed.set_footer(icon_url=self.client.user.avatar_url,text=f"Solo Owner of Miku.N with 💖.. M.donate for support")
        await ctx.send(embed=embed)

    @commands.command(aliases=["donate"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.guild_only()
    async def donation(self, ctx):
        owner = await self.client.fetch_user(557578041908396033)
        author = ctx.message.author
        print(author)
        embed = discord.Embed(
            description=f"> ** Miku.n Runs on a free host now... `For {len(self.client.guilds)} servers with {round(self.client.latency * 1000)} ms ping` **\n> Your donations will be help full to make some progress\n\n > Right now accepting all type of **`Crypto`** <a:btc:978980488360374302> & **`indian`** paymets..\n\n **__Other Supports__**\n> Gift nitro to `{owner}` <a:nitro:895330869479362640> \n> Boost the [Support Server](https://discord.gg/cyKAjwcZdB) <a:plz_boost:895330700104990790>\n\nJoin [Server](https://discord.gg/cyKAjwcZdB) for info abount patreon\n\n> *Help my master get a ~~coffee~~ Body Pillow*\n> Thank you in Advance {author.mention} <:nekoheart:898116154973888544>",
            colour=0x19198c)
        embed.set_thumbnail(url=owner.avatar_url)
        embed.set_footer(icon_url=author.avatar_url)
        await ctx.send(embed=embed)

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.guild_only()
    async def vote(self,ctx):
        author = ctx.message.author
        embed = discord.Embed( title="Vote Here",url="https://top.gg/bot/876139135507763280/vote",description="You can vote every 12 hrs, to unlock few cool options of the bot",colour=0x19198c)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/424792877546340372/895114005687963658/Screenshot_2021-05-24_at_23.56.34.png")
        if await self.client.topgg.get_user_vote(user_id=ctx.author.id):
            embed.set_footer(icon_url=author.avatar_url,text=f"{author.name} You have voted ✅")
        else:
            embed.set_footer(icon_url=author.avatar_url,text=f"{author.name} you need to vote ❌")
        await ctx.send(embed=embed)
    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.guild_only()
    async def invite(self,ctx):
        author = ctx.message.author

        embed = discord.Embed(
                title=("__Invite This Bot__"),
                url='https://discord.com/oauth2/authorize?client_id=876139135507763280&permissions=2684741712&scope=bot%20applications.commands',
                description=(
                    "```1.FOR GOGOANIME LINK🔗📺 ON DISCORD\n\n2.ANIME & MANGA🤩 info from MYANIMELIST\n\n3.ANIME QUIZ WITH GLOBAL POINT SYSTEM\n\n4.ANIME QUOTES,WALLPAPER🎊 🎉\n\n6.120 language translator with pronounciation ```"),
                colour=0x19198c)
        
            
        embed.add_field(name=("**EVENTS**"), value=("`every month anime quiz 🎊 giveaway\n for table toppers in support server`"), inline=True)
        embed.set_thumbnail(
                url='https://cdn.discordapp.com/attachments/424792877546340372/878663313611952148/80.png')
        embed.set_footer(text="click above to add me",
                            icon_url=self.client.user.avatar_url)
        embed1=discord.Embed(
                title=("INVITE LINK 🎀"),
                url='https://discord.com/oauth2/authorize?client_id=876139135507763280&permissions=2684741712&scope=bot%20applications.commands', 
                description=("click above to add this Miku.N bot"),colour=0x19198c)
        await author.send(embed=embed)
        await ctx.send(f"check your DM for all features of this bot{author.mention} ", embed=embed1)

# @client.command()
# async def privacy(ctx):
#     await ctx.send(
#         "```**we dont save any of your data**\n FOR QUIZ WE STORE U R USER ID ALONE IF U WANT TO DELETE IT USE m.delete\n  What information is saved temporary\n\nYour userid is stored if you have any command. Your userid may be stored multiple times for each command.\nYour userid is stored if you are blacklisted.\nIf you send a message that channel id saved.\n\n Why we store the information and how we use it.\nto mention you for the output\n to send the mmsg to crt server or channel\n\nWho gets this data?\n no data is publically available. All datas is only available to bot Administrators.\n Third Party Data Sharing\n\n we dont share anything with third party apps we use only api for search results\nHow to Remove your data.\n\n we store any to remove..\nNote: We reserve the right to change this without notifying our users.\n\n\nThis policy was last updated April 6th, 2021.```")

    #create a command in the cog


    @commands.command(name='Uptime')
    async def _uptime(self,ctx):
        uptime = str(timedelta(seconds=int(round(time.time()-startTime))))
        await ctx.send(uptime)
def setup(client):
    client.add_cog(Example(client))
