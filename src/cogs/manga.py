import discord
from discord.ext import commands
import requests
from jikanpy import jikan

aki = jikan.Jikan()
from bs4 import BeautifulSoup
from AnilistPython import Anilist
anilist_bot= Anilist()
import lxml
import asyncio
import validator
from disputils import *


class Example(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("manga is ready")

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.guild_only()
    async def manga(self, ctx, *, anime=""):
        if anime == "":
            await ctx.send("Use `m.manga naruto` <a:heart3:879888752594530425>"
                           )
        else:
            asi = aki.search('manga', anime, page=1)

            name = (asi['results'][0]['title'])
            pic = (asi['results'][0]['image_url'])
            link = (asi['results'][0]['url'])
            info = (asi['results'][0]['synopsis'])
            chapters = (asi['results'][0]['chapters'])
            volumes = (asi['results'][0]['volumes'])
            score = (asi['results'][0]['score'])
            start = (asi['results'][0]['start_date'])
            end = (asi['results'][0]['end_date'])

            embed = discord.Embed(
                title=name,
                description=(
                    f'[MyAnimeList🔗]({link})\n\n**SYNOPSIS**\n\n||{info}||\n'),
                colour=0x19198c)
            embed.set_thumbnail(url=pic)
            embed.set_footer(text=ctx.message.author.name,
                             icon_url=ctx.guild.icon_url)
            embed.add_field(name='CHAPTERS', value=chapters, inline=True)
            embed.add_field(name='VOLUME', value=volumes, inline=True)
            embed.add_field(name='SCORE', value=score, inline=True)
            if end == None:
                embed.add_field(
                    name='  AIRED',
                    value=(f'FROM : {start[0: 9: 1]}\nTO : still airing'),
                    inline=True)
            else:
                embed.add_field(
                    name='  AIRED',
                    value=(f'FROM : {start[0: 9: 1]}\nTO : {end[0: 9:1]}'),
                    inline=True)
            await ctx.send(embed=embed)

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.guild_only()
    async def character(self, ctx, *, anime=""):
        if anime == "":
            await ctx.send("Use `m.character naruto` <a:heart3:879888752594530425>"
                           )
        else:
            asi = aki.search('character', anime, page=1)
            author = ctx.message.author
            pfp = author.avatar_url
            result = anilist_bot.get_character(anime)
            # name = (asi['results'][0]['name'])
            name=result["first_name"] + " " + result["last_name"]
            link = (asi['results'][0]['url'])
            print(link)
            pic=result["image"]
            alternative_names = (asi['results'][0]['alternative_names'])
            a = " "
            for i in range(0, len(alternative_names)):
                if a==" ":
                    a=(alternative_names[i])
                else:
                    a = a + ", "+(alternative_names[i])
            embed = discord.Embed(
                    description=(f'[MyAnimeList]({link})\n\n**{a}**'),
                    colour=0x19198c)
            embed.set_author(name=name, icon_url=pfp)
            embed.set_footer(text=f"{author.name} spoiler : ✅ wrong : ❌", icon_url=ctx.guild.icon_url)
            embed.set_image(url=pic)
            message = await ctx.send(embed=embed)
            await message.add_reaction("<a:Yes:893317269973762138>")
            await message.add_reaction("<a:No:893318616479567873>")
            a1 = embed = discord.Embed(description=(
                    f'**[MyAnimeList]({link})**\n\n**{a}**\n\n{result["desc"]}'
                ),
                                           colour=0x19198c)
            embed.set_author(name=name, icon_url=pfp)
            embed.set_footer(text=f"{author.name}",
                             icon_url=ctx.guild.icon_url)
            embed.set_image(url=pic)

            a2 = embed = discord.Embed(
                    description=(f'**[MyAnimeList]({link})**\n\n**{a}**\n '),
                    colour=0x19198c)
            embed.set_author(name=name, icon_url=pfp)
            embed.set_footer(text=f"{author.name} Try with full name !!",
                             icon_url=ctx.guild.icon_url)
            embed.set_image(url=pic)

            def check(reaction, user):
                return user == ctx.author and str(reaction.emoji) in [
                    "<a:Yes:893317269973762138>", "<a:No:893318616479567873>"
                ] and message.id == reaction.message.id

            time = 45
            while True:
                try:
                    reaction, user = await self.client.wait_for("reaction_add",
                                                                timeout=time,
                                                                check=check)

                    if str(reaction.emoji) == "<a:Yes:893317269973762138>":
                        time = 45
                        await message.edit(embed=a1)
                        try:
                            await message.remove_reaction(reaction, user)
                        except:
                            pass
                    elif str(reaction.emoji) == "<a:No:893318616479567873>":
                        time = 45
                        await message.edit(embed=a2)
                        try:
                            await message.remove_reaction(reaction, user)
                        except:
                            pass
                    else:
                        try:
                            await message.remove_reaction(reaction, user)
                        except:
                            pass

                except asyncio.TimeoutError:
                    await message.clear_reactions()
                    return


def setup(client):
    client.add_cog(Example(client))
