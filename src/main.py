# import os
# import discord
# import requests
# import json
# import random
# from discord.ext import commands, tasks
# from itertools import cycle
# from jikanpy import jikan
# from discord.utils import find
# from gogoanimeapi import gogoanime
# from discord.ext.commands import has_permissions, MissingPermissions
# from download import get_episode_link
# from discord.ext.commands import Bot
# from disputils import *
# import nekos
# from datetime import datetime
# import time
# from datetime import timedelta
# import asyncio
# from bs4 import BeautifulSoup
# import requests
# import lxml
# import validators
# import datetime

# aki = jikan.Jikan()
# # client = commands.Bot(command_prefix=["m.","M."], case_insensitive=True,strip_after_prefix=True)
# # intents = discord.Intents.default()
# # intents.members = True
# # intents = discord.Intents(messages=True, guilds=True, members=True, presences=True)
# client = commands.AutoShardedBot(command_prefix=["<@876139135507763280>","<@!876139135507763280>","m.","M."], case_insensitive=True, strip_after_prefix=True, shard_count=10)
# client.remove_command('help')


# @client.command()
# @commands.is_owner()
# async def load(ctx,extension):
#     client.load_extension(f'cogs.{extension}')
#     await ctx.send(f"Loaded {extension} <a:pepegun2:893754489457246208> ")


# @client.command()
# @commands.is_owner()
# async def unload(ctx,extension):
#     client.unload_extension(f'cogs.{extension}')
#     await ctx.send(f"Reloaded {extension} <a:pepegun2:893754489457246208> ")

# for filename in os.listdir('./cogs'):
#     if filename.endswith(".py"):
#         client.load_extension(f'cogs.{filename[:-3]}')

# @client.command()
# @commands.is_owner()
# async def file(ctx):
#     await ctx.send(file=discord.File("member.json"))
#     await ctx.send(file=discord.File("mainbank.json"))

# @tasks.loop(minutes=180)
# async def work():
#     channel = client.get_channel(988421322960928798)
#     uptime = str(timedelta(seconds=int(round(time.time()-startTime))))
#     await channel.send(f"> Current uptime : {uptime}")





# import topgg

# dbl_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6Ijg3NjEzOTEzNTUwNzc2MzI4MCIsImJvdCI6dHJ1ZSwiaWF0IjoxNjMzODA0NzYzfQ.xMREbcyBUSTyTAM_ygWaiAvT9a4SlmEGrVQjRCS_xjs"
# client.topgg = topgg.DBLClient(client, dbl_token, autopost=True, post_shard_count=True)
# status = cycle([
#     'm.help', 'm.invite', 'prefix: m.', 'm.wallpaper','m.quiz','m.vote'
# ])
# @tasks.loop(seconds=30)
# async def change_status():
#     ff = random.randint(1, 2)
# #     if (ff == 0):
# #         await client.change_presence(activity=discord.Game(name=next(status)))
#     if (ff == 1):
#         await client.change_presence( activity=discord.Activity(
#             type=discord.ActivityType.watching, name=next(status)))
#     else:
#         await client.change_presence(activity=discord.Activity(
#             type=discord.ActivityType.listening, name=next(status)))






# @client.event
# async def on_autopost_success():
#     print(
#         f"Posted server count ({client.topggpy.guild_count}), shard count ({client.shard_count})"
#     )


# # async def update_stats():
# #     try:
# #         await client.topgg.post_guild_count()
# #         print(f"Posted! server count ({client.topgg.guild_count} )")
# #     except Exception as e:
# #         print(f"Failed! \n{e.__class__.__name__}: {e}")

# @client.event
# async def on_guild_join(guild):
# #     channel = client.get_channel(858653930376265728)
# #     a=0
# #     for member in guild.members:
# #             if member.bot == True:
# #                 a=a+1
#     # await channel.send(f"joined a new server `{guild}` & `{guild.id}` with `{len(guild.members)-1}` member and {a} bots member \nnow there are `{len(client.guilds)}` servers now")
# #     await update_stats()
#     for channel in guild.text_channels:
#         if channel.permissions_for(guild.me).send_messages:
#             embed = discord.Embed (title = "use `M.help` to get help" ,description="Thx for adding me in <:02Love:881774327769481256> ",colour=0x39138b)
#             embed.set_footer(text=(guild.name),icon_url=guild.icon_url )
#             embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/424792877546340372/878194349920366632/Screenshot_2021-06-29_at_22.13.51.png")
#             embed.set_author(name = "Hello People",icon_url=client.user.avatar_url )

#             message=await channel.send(embed=embed)
#             member_server=(message.guild.member_count)
#             break
#     channel = client.get_channel(858653930376265728)
#     try:
#         embed = discord.Embed(title=f"Joined `{guild}`",description = f"> Id :{message.guild.id}\n> members : {member_server}",colour=0x00ff00)
#         embed.set_footer(text=f"Now there are {len(client.guilds)} server",icon_url=guild.icon_url )
#         await channel.send(embed=embed)
#     except:
#         embed = discord.Embed(title=f"Joined `{guild}`",description = f"> Id :{guild.id}\n\n> members : n/a",colour=0x00ff00)
#         embed.set_footer(text=f"Now there are {len(client.guilds)} server",icon_url=guild.icon_url )
#         await channel.send(embed=embed)
#     # if (len(guild.members))<4:
#     #     guild=client.get_guild(guild.id)
#     #     for channel in guild.text_channels:
#     #         if channel.permissions_for(guild.me).send_messages:
#     #             embed = discord.Embed (title = "we have reaced 100 servers" ,description="but not verified yet so, we need to leave servers with less users or non active,so other servers with huge users can access,\n `you can add us back in this server also, but try adding us back in servers with atlest 10 active people with bot`",color=discord.Colour.red())
#     #             embed.set_footer(text=(guild.name),icon_url=guild.icon_url )
#     #             embed.set_author(name = "bye for now",icon_url=client.user.avatar_url )
#     #             embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/424792877546340372/880807833514410004/Screenshot_2021-03-28_at_11.39.01.png")
#     #             embed.add_field(name='** **',
#     #                 value="join SUPPORT [SERVER](https://discord.gg/cyKAjwcZdB) for more info • [INVITE BOT 🎀](https://discord.com/api/oauth2/authorize?client_id=876139135507763280&permissions=2684741712&scope=bot%20applications.commands) • [VOTE US](https://top.gg/bot/844046442046029824/vote)",
#     #                 inline=False)
#     #             await channel.send(embed=embed)
#     #             break
#     #     to_leave = client.get_guild(guild.id)
#     #     await to_leave.leave()
# import sys
# import os
# def restart_bot():
#   os.execv(sys.executable, ['python'] + sys.argv)

# @client.command(name= 'restart')
# @commands.is_owner()
# async def restart(ctx):
#   await ctx.send("Restarting bot...")
#   restart_bot()

# @client.event
# async def on_guild_remove(guild):

#     with open('member.json', 'r') as f:
#         users = json.load(f)
#     gg=[]
#     for i in users:
#         if users[i]["server"]==guild.id:
#             gg = gg + [i]
#     if gg!=[]:
#         for j in gg:
#             users.pop(j, None)
#         with open('member.json', 'w') as f:
#             json.dump(users, f,indent=4)
#         channel = client.get_channel(927454065737207818)
#         await channel.send(f'server removed `{guild.id}`  `{guild}`', file=discord.File("member.json"))
#     channel = client.get_channel(858653930376265728)
#     embed = discord.Embed(title=f"left `{guild}`",description = f"> Id :{guild.id}",colour=0xFF0000)
#     embed.set_footer(text=f"Now there are {len(client.guilds)} server",icon_url=guild.icon_url )
#     await channel.send(embed=embed)


# @client.command()
# @commands.is_owner()
# async def fclear(ctx, *, amount):
#     amt = int(amount)
#     await ctx.channel.purge(limit=amt)


# # PING
# @client.command()
# @commands.guild_only()
# async def ping(ctx):
#     await ctx.send(f'Bot ping is {round(client.latency * 1000)} ms <a:heart3:879888752594530425>')


# # anim


# #
# # # GENRE
# # @client.command()
# # @commands.guild_only()
# # async def genre(ctx, *, name):
# #     author = ctx.message.author
# #     pfp = author.avatar_url
# #     rname = name.replace(" ", "-")
# #
# #     try:
# #         anime_search = gogoanime.get_search_results(query=rname)
# #         for i in anime_search:
# #             aid = i.get('animeid')
# #             break
# #         asi = aki.search('anime', aid, page=1)
# #         pic = (asi['results'][0]['image_url'])
# #         anime_details = gogoanime.get_anime_details(animeid=aid)
# #         genre = (anime_details['genre'])
# #         embed = discord.Embed(
# #             title=aid,
# #             description=(f'**{genre}**'),
# #             colour=0x19198c
# #         )
# #         embed.set_thumbnail(url=pic)
# #         embed.set_footer(text="DM me m.invite for animequiz🎊 🎉  Every month",
# #                          icon_url=pfp)
# #         await ctx.send(embed=embed)
# #     except:
# #         embed = discord.Embed(title="Error",
# #                               description=f"unable to find {name}",
# #                               colour=0x19198c)
# #         embed.set_author(name=author, icon_url=pfp)
# #         embed.set_footer(text="DM me m.invite for animequiz🎊 🎉  Every month",
# #                          icon_url=author.avatar_url)
# #         await ctx.send(embed=embed)



# # server list
# # @client.command(aliases=["botmembers","botservers"])
# # async def botservers(ctx):
# #     user = ctx.message.author
# #     if user.id == 557578041908396033:
# #         msg = len(client.guilds)
# #         await ctx.send(msg)
# #     else:
# #         await ctx.send("classified content pa thambi")

# # @client.command(aliases=["botmembers","botservers"])
# # @commands.is_owner()
# # async def bm(ctx):
# #         msg = len(client.guilds)
# #         members = 0
# #         guilds = client.guilds
# #         for guild in guilds:
# #             members += len(guild.members)
# #         members_set = set( )
# #         for guild in guilds:
# #             for member in guild.members:
# #                 members_set.add(member)
# #         members2 = len(members_set)
# #         await ctx.send(f'channel:{msg},members:{members},true members:{members2}')

# #         def filterOnlyBots(member):
# #             return member.bot

# #         botsInServerCount=0
# #         usersInServerCount=0

# #         for guild in guilds:
# #             membersInServer = guild.members
# #             botsInServer = list(filter(filterOnlyBots, membersInServer))
# #             botsInServerCount += len(botsInServer)
# #             # (Total Member count - bot count) = Total user count
# #             usersInServerCount += len(guild.members) - botsInServerCount
# #         print(botsInServerCount)
# #         print(usersInServerCount)
# @client.command()
# @commands.is_owner()
# async def fleave(ctx,*,id):
#     print(id)
#     id = int(id)
#     guild=client.get_guild(id)
#     for channel in guild.text_channels:
#             if channel.permissions_for(guild.me).send_messages:
#                 embed = discord.Embed (title = "Suspicious abuse of bot has been detected <:KillerZeroTwo_:881783524410138644>" ,description="Join support server for more Info,\n `you can add us back in this server also, but try adding us back in servers with atlest 10 active people with bot`",colour=0x19198c)
#                 embed.set_footer(text=(guild.name),icon_url=guild.icon_url )
#                 embed.set_author(name = "bye for now",icon_url=client.user.avatar_url )
#                 embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/424792877546340372/880807833514410004/Screenshot_2021-03-28_at_11.39.01.png")
#                 embed.add_field(name='** **',
#                     value="Join support [server](https://discord.gg/cyKAjwcZdB) for more info • [invite bot 🎀](https://discord.com/api/oauth2/authorize?client_id=876139135507763280&permissions=2684741712&scope=bot%20applications.commands) • [vote](https://top.gg/bot/844046442046029824/vote)",
#                     inline=False)
#                 await channel.send(embed=embed)
#                 break

#     to_leave = client.get_guild(id)
#     await to_leave.leave()




# @client.command()
# @commands.is_owner()
# async def leave(ctx):
#     guilds = client.guilds
#     for guild in guilds:
#         a=0
#         for member in guild.members:
#             if member.bot == True:
#                 a=a+1
#         print(f"{len(guild.members)},  {a}  ,\t{guild},\t{guild.id}")




#     # user = ctx.message.author
#     # if user.id == 557578041908396033:
#     #     guilds = client.guilds
#     #     i=1
#     #     for guild in guilds:
#     #         if len(guild.members) < 6:
#     #             print(i)
#     #             i = i+1
#     #             print(f"{len(guild.members)},\t{guild},\t{guild.id}")


# # @client.command()
# # @commands.has_permissions(manage_messages=True)
# # @commands.guild_only()
# # async def blocknsfw(ctx):
# #     a=0
# #     with open('nsfw.json','r') as f:
# #         users = json.load(f)
# #         print(len(users))
# #     for i in range(0,len(users)):
# #         if ctx.guild.id == users[i]:
# #             await ctx.send(f"> `NSFW` Contents Already `Blocked` for {ctx.guild}")
# #             a=1
# #     with open('nsfw.json','r') as f:
# #         users = json.load(f)
# #     if a==0:
# #         await ctx.send(f"> `NSFW` Contents are `Blocked` for {ctx.guild}")
# #         a=[ctx.guild.id]
# #         users=users+a
# #         with open('nsfw.json', 'w') as f:
# #             json.dump(users, f)



# # @client.command()
# # @commands.has_permissions(manage_messages=True)
# # @commands.guild_only()
# # async def addnsfw(ctx):
# #     with open('nsfw.json','r') as f:
# #         users = json.load(f)
# #     for i in range(0,len(users)):
# #         print(i)
# #         if ctx.guild.id == users[i]:
# #             print(i)
# #             users.pop(i)
# #             with open('nsfw.json', 'w') as f:
# #                 json.dump(users, f)
# #             await ctx.send(f"> `NSFW` Contents are `Added` for {ctx.guild}")




# # @client.command()
# # async def listservers(ctx):
# #     user = ctx.message.author
# #     if user.id == 557578041908396033:
# #         a = len(client.guilds)
# #         for i in range(0, a):
# #             await ctx.send(client.guilds[i])
# #     else:
# #         await ctx.send("classified content pa thambi")



# async def god(cat):
#        url = f"https://api.waifu.pics/sfw/{cat}"
#        r = requests.get(url)
#        link = json.loads(r.text)
#        crtlink = link["url"]
#        return crtlink


# @client.command()
# @commands.cooldown(1, 3, commands.BucketType.user)
# @commands.guild_only()
# async def shinobu(ctx):
#     cat = "shinobu"
#     crtlink=await god(cat)
#     embed = discord.Embed(colour=0x39138b)
#     embed.set_image(url=crtlink)
#     await ctx.send(embed=embed)


# @client.command()
# @commands.cooldown(1, 3, commands.BucketType.user)
# @commands.guild_only()
# async def kanna(ctx):
#             url = "https://nekobot.xyz/api/image?type=kanna"
#             r = requests.get(url)
#             link = json.loads(r.text)
#             crtlink = link["message"]
#             embed = discord.Embed(colour=0x39138b)
#             embed.set_image(url=crtlink)
#             await ctx.send(embed=embed)

# @client.command()
# @commands.cooldown(1, 3, commands.BucketType.user)
# @commands.guild_only()
# async def megumin(ctx):
#     cat = "megumin"
#     crtlink=await god(cat)
#     embed = discord.Embed(colour=0x39138b)
#     embed.set_image(url=crtlink)
#     await ctx.send(embed=embed)



# @client.event
# async def on_ready():
#         channel = client.get_channel(988421322960928798)
#         await channel.send("Restarted <@!557578041908396033>")
#         global startTime
#         startTime = time.time()
#         work.start()
#         change_status.start()
#         channel = client.get_channel(927454065737207818)
#         async for m in channel.history():

#             if m.author.id == 876139135507763280:
#                 try:
#                     attachment = m.attachments[0]
#                     response = requests.get(attachment.url)
#                     file = open(f"member.json", "wb")
#                     file.write(response.content)
#                     file.close()
#                     print("ok")
#                     break
#                 except:
#                     pass
#         channel = client.get_channel(988420077177171998)
#         async for m in channel.history():
#             if m.author.id == 876139135507763280:
#                 try:
#                     attachment = m.attachments[0]
#                     response = requests.get(attachment.url)
#                     file = open(f"mainbank.json", "wb")
#                     file.write(response.content)
#                     file.close()
#                     print("ok")
#                     break
#                 except:
#                     pass
#         try:
#             with open('member.json', 'r') as f:
#                 users = json.load(f)
#             gg=[]
#             for i in users:
#                 channel=client.get_channel(int(i))
#                 if channel.is_nsfw():
#                     pass
#                 else:
#                     await channel.send("> Channel removed from __AutoNsfw__ change channel settings to nsfw and try adding again <:large:898116452886933504>")
#                     gg = gg + [str(i)]
#             if gg!=[]:
#                 for j in gg:
#                     users.pop(j, None)
#                 with open('member.json', 'w') as f:
#                     json.dump(users, f,indent=4)
#                 channel = client.get_channel(927454065737207818)
#                 await channel.send(f'channel removed `{channel.guild.id}`  `{channel.guild}`', file=discord.File("member.json"))
#         except:
#             pass
        
# client.run("###") #token


import json
with open("src/sfw_json/wallpaper.json",'r') as f:
    users = json.load(f)

with open("src/sfw_json/wallpaper.json", 'w') as f:
        json.dump(users, f, indent=4)
