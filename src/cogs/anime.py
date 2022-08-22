import discord
from discord.ext import commands
import requests
import json
import random
import asyncio
from disputils import *
from download import get_episode_link
from gogoanimeapi import gogoanime
from jikanpy import jikan
from bs4 import BeautifulSoup

aki = jikan.Jikan()


class Example(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("anime is ready")

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.guild_only()
    async def anime(self, ctx, *, anime=""):
        async with ctx.typing():
            await asyncio.sleep(1)
        if anime == "":
            await ctx.send("Use `m.anime naruto` <a:heart3:879888752594530425>")
        else:
            asi = aki.search('anime', anime, page=1)

            name = (asi['results'][0]['title'])
            pic = (asi['results'][0]['image_url'])
            link = (asi['results'][0]['url'])
            info = (asi['results'][0]['synopsis'])
            epi = (asi['results'][0]['episodes'])
            score = (asi['results'][0]['score'])
            start = (asi['results'][0]['start_date'])
            end = (asi['results'][0]['end_date'])

            embed = discord.Embed(
                title=name,
                description=(f'[MyAnimeList🔗]({link})\n\n**SYNOPSIS**\n\n||{info}||\n'),
                colour=0x19198c
            )
            embed.set_thumbnail(
                url=pic)
            embed.set_footer(text=ctx.message.author.name,
                             icon_url=ctx.guild.icon_url)
            embed.add_field(name='EPISODES', value=epi, inline=True)
            embed.add_field(name='SCORE', value=score, inline=True)

            if end == None:
                embed.add_field(name='  AIRED', value=(f'FROM : {start[0: 9: 1]}\nTO : still airing'), inline=True)
            else:
                embed.add_field(name='  AIRED', value=(f'FROM : {start[0: 9: 1]}\nTO : {end[0: 9:1]}'), inline=True)
            try:
                rname = name.replace(" ", "-")

                anime_search = gogoanime.get_search_results(query=rname)
                for i in anime_search:
                    aid = i.get('animeid')
                    break
                asi = aki.search('anime', aid, page=1)
                pic = (asi['results'][0]['image_url'])
                anime_details = gogoanime.get_anime_details(animeid=aid)
                genreq = (anime_details['genre'])
                genre = genreq[1:-1]
                genre = genre.replace("'", "`")
                embed.add_field(name="GENRE", value=(genre), inline=True)

            except:
                pass
            await ctx.send(embed=embed)

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.guild_only()
    async def watch(self, ctx, *, name=""):
        if name == "":
            await ctx.send("Use `m.watch naruto #3` <a:heart3:879888752594530425>")
        else:
            x = name.split("#")
            y = (x[-1])
            z = x[0]
            rname = z.replace(" ", "-")

            try:
                anime_search = gogoanime.get_search_results(query=rname)
                for i in anime_search:
                    aid = i.get('animeid')
                    break
                response = requests.get(f'https://gogoanime.tv/{aid}-episode-{y}')
                url = response.url
                soup = BeautifulSoup(response.content, 'lxml')
                aki = soup.find('title')
                title = (aki.text.strip())
                aki = soup.find('div', class_="anime_muti_link")
                aku = aki.findAll('a')
                result = []
                for i in aku:
                    link_url = i["data-video"]
                    if not link_url.startswith("https:"):
                        link_url = "https:" + link_url
                    check = requests.get(link_url)
                    case = {'status': check.status_code, 'Domain': (i.text.strip().replace("Choose this server", "")),
                            'url': link_url}
                    result.append(case)
                p=""
                for i in result:
                    p=p+f"[{i['Domain']}]({i['url']}) - status {i['status']}\n"
                print(result)
                embed = discord.Embed(
                    title=(f'\t**{title}**'), url=url,
                    description=(
                        f'Click above to watch ** `{aid}` **episode **`{y}`** on gogoanime <:nezukopat_jess:878150040244338698>\n\n __**Other Domins**__\n{p}'),
                    colour=0x19198c
                )
                embed.set_thumbnail(
                    url='https://cdn.discordapp.com/attachments/424792877546340372/878663313611952148/80.png')
                embed.set_footer(text=ctx.message.author.name,
                                 icon_url=ctx.guild.icon_url)
                await ctx.send(embed=embed)
            except:
                embed = discord.Embed(title="Error",
                                      description=f"unable to find {name}\n ```example command m.watch naruto #1``` for naruto ep 1",
                                      colour=0x19198c)
                embed.set_footer(text=ctx.message.author.name,
                                 icon_url=ctx.guild.icon_url)
                await ctx.send(embed=embed)

    @commands.command(aliases=["download"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.guild_only()
    async def dload(self, ctx, *, name=""):
        if name == "":
            await ctx.send("Use `m.dload naruto #3` <a:heart3:879888752594530425>")
        else:
            x = name.split("#")
            y = (x[-1])
            z = (x[0])
            rname = z.replace(" ", "-")

            try:
                anime_search = gogoanime.get_search_results(query=rname)
                for i in anime_search:
                    aid = i.get('animeid')
                    break
                try:
                    response = requests.get(f'https://gogoanime.tv/{aid}-episode-{y}')
                    soup = BeautifulSoup(response.content, 'lxml')
                    aki = soup.find("li", class_="dowloads")
                    links = aki.find_all("a")
                    download_url = links[0]["href"]
                    aki = soup.find("meta", property="og:image")
                    pic = (aki["content"])
                    embed = discord.Embed(
                        title=f'Download `{aid}` Episode `{y}` on Gogoanime',
                        description=f'**[Download Here 🔗]({download_url})**\n`HDP-MP4, 1080-MP4, 720-MP4, 360P-MP4`',
                        colour=0x19198c)
                    embed.set_thumbnail(url=pic)
                    embed.set_footer(text=ctx.message.author.name,
                                     icon_url=ctx.guild.icon_url)
                    await ctx.send(embed=embed)
                except:

                    embed = discord.Embed(title="not available",
                                          description=f"download is not availabe in gogoanime try `m.watch {name}`",
                                          colour=0x19198c)
                    embed.set_thumbnail(url=pic)
                    embed.add_field(name="** **",
                                    value="only animes released b/w 2006 - 2021 are available for download",
                                    inline=True)
                    embed.set_footer(text=ctx.message.author.name,
                                     icon_url=ctx.guild.icon_url)
                    await ctx.send(embed=embed)
            except:

                embed = discord.Embed(title="Error",
                                      description=f"unable to find {name}, use m.help to get help",
                                      colour=0x19198c)
                embed.set_footer(text=ctx.message.author.name,
                                 icon_url=ctx.guild.icon_url)
                await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Example(client))
