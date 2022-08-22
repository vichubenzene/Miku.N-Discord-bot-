import discord
from discord.ext import commands
import asyncio
from discord_components import DiscordComponents, ComponentsBot, Button, Select, SelectOption
from discord.ext.commands import has_permissions, MissingPermissions


class Example(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        DiscordComponents(self.client)
        print("help is ready")

    @commands.command()
    @commands.cooldown(1, 7, commands.BucketType.user)
    async def help(self, ctx):
        author = ctx.message.author
        pfp = ctx.author.avatar_url
        a1 = embed = discord.Embed(title=("ANIME <a:MikuJam:879895048437784617>"), colour=0x19198c)
        embed.add_field(name="`m.anime <anime name>`",
                        value='anime info from myanimelist (synopsis,total_epi,score,aired,pic)', inline=True)
        embed.add_field(name='` dload `', value='download anime (HDP)(360P)(480P)(720P)(1080P)', inline=True)
        embed.add_field(name="`m.watch <anime #ep>`", value='gogoanime episode link', inline=True)
        embed.add_field(name='** **',
                        value="**KINDLY OMIT '  <  '||'  >  '**\nSUPPORT [SERVER](https://discord.gg/cyKAjwcZdB) • [INVITE BOT](https://discord.com/oauth2/authorize?client_id=876139135507763280&permissions=2684741712&scope=bot%20applications.commands) • [VOTE](https://top.gg/bot/876139135507763280/vote)",
                        inline=False)
        embed.set_footer(text=author.name, icon_url=pfp)

        a12 = embed = discord.Embed(title=("MANGA <a:blushy:898116757775069244>"), colour=0x19198c)
        embed.add_field(name='`m.manga <manga name>`',
                        value='manga info from myanimelist\n(synopsis,chapters,volumes,score,pic)', inline=False)
        embed.add_field(name='Character <:MikuThanks:879900458603393094>',
                        value='** **', inline=False)
        embed.add_field(name='`m.character <character name>`',
                        value='character picture and info from myanimelist\n', inline=False)
        embed.add_field(name='** **',
                        value="**KINDLY OMIT '  <  '||'  >  '**\nSUPPORT [SERVER](https://discord.gg/cyKAjwcZdB) • [INVITE BOT](https://discord.com/oauth2/authorize?client_id=876139135507763280&permissions=2684741712&scope=bot%20applications.commands) • [VOTE](https://top.gg/bot/876139135507763280/vote)",
                        inline=False)
        embed.set_footer(text=author.name, icon_url=pfp)

        a2 = embed = discord.Embed(
            title=("TRANSLATOR <:ShinobuSHeart_:878676427178921994>"),
            description=("**PREFIX : `m.` **"),
            colour=0x19198c)
        embed.add_field(name='`m.lcode`',
                        value='universal language codes', inline=True)
        embed.add_field(name='`m.meaning`',
                        value='Gives the meaning of the words', inline=True)
        embed.add_field(name='`m.trans <lcode> content`',
                        value='Transtlates words & sentence\n```Example command\n1."m.trans ta Hello" This Translates hello to Tamil\n2."m.trans en வணக்கம்" This Translates வணக்கம் to English``` ',
                        inline=False)
        embed.add_field(name='** **',
                        value="**KINDLY OMIT '  <  '||'  >  '**\n[support server](https://discord.gg/cyKAjwcZdB) • [invite bot](https://discord.com/oauth2/authorize?client_id=876139135507763280&permissions=2684741712&scope=bot%20applications.commands) • [vote](https://top.gg/bot/876139135507763280/vote)",
                        inline=False)
        embed.set_footer(text=author.name, icon_url=pfp)

        a6 = embed = discord.Embed(
            title=('QUOTES <:MikuAraAra:879901712696082443>'),
            colour=0x19198c)
        embed.add_field(name='`m.quote`', value='randam anime Quote', inline=True)
        embed.add_field(name='`m.aquote <anime>`', value='  Quote from Anime', inline=True)
        embed.add_field(name='`m.cquote <character>`', value='Quote from Character', inline=True)
        embed.add_field(name='`m.inspire`', value='normie quotes', inline=True)
        embed.add_field(name='** **',
                        value="**KINDLY OMIT '  <  '||'  >  '**\nSUPPORT [SERVER](https://discord.gg/cyKAjwcZdB) • [INVITE BOT](https://discord.com/oauth2/authorize?client_id=876139135507763280&permissions=2684741712&scope=bot%20applications.commands) • [VOTE](https://top.gg/bot/876139135507763280/vote)",
                        inline=False)
        embed.set_footer(text=author.name, icon_url=pfp)

        a13 = embed = discord.Embed(
            title=('QUIZ <:MikuConfused:879903705548337192>'),
            colour=0x19198c)
        embed.add_field(name='`m.quiz`', value='`Anime quiz`', inline=True)
        # embed.add_field(name='`m.privacy`', value='`Anime quiz privacy policy`', inline=True)
        embed.add_field(name='`m.quotequiz <anime>`', value='`Quotes quiz on the anime`', inline=True)
        embed.add_field(name='`m.points`', value='`view points`', inline=True)
        embed.add_field(name='`m.lb`', value='`leader board`', inline=True)
#         embed.add_field(name='`m.slb`', value='`server leader board`', inline=True)
        embed.set_footer(text=author.name, icon_url=pfp)
        embed.add_field(name='** **',
                        value="**KINDLY OMIT '  <  '||'  >  '**\nSUPPORT [SERVER](https://discord.gg/cyKAjwcZdB) • [INVITE BOT](https://discord.com/oauth2/authorize?client_id=876139135507763280&permissions=2684741712&scope=bot%20applications.commands) • [VOTE](https://top.gg/bot/876139135507763280/vote)",
                        inline=False)

        a7 = embed = discord.Embed(
            title=('WALLPAPER <:8046_ZeroWow:879902918067753011>'),
            colour=0x19198c)
        embed.add_field(name="`m.waifu`", value="waifu pic", inline=True)
        embed.add_field(name='`m.wallpaper <tag>`', value='anime wallpaper on tags', inline=True)
        embed.add_field(name="`m.wallpaper`", value="random anime wallpaper", inline=True)
        embed.add_field(name='`m.pfp`', value='anime avatar ', inline=True)
        embed.add_field(name='`m.holo`', value='holo pic', inline=True)
        embed.add_field(name='`m.sfwkemo`', value='kemonomimi pic', inline=True)
        embed.add_field(name='`m.neko`', value='cat girls', inline=True)
        embed.add_field(name='`m.foxgirl`', value='fox girl', inline=True)
        embed.add_field(name='`m.nekogif`', value='nekogif', inline=True)
        embed.set_footer(text=author.name, icon_url=pfp)


        a11 = embed = discord.Embed(
            title=('ANIME / SAUCE FINDER <:kanna_inspect:878150112457687040>'),description="Anime Scene Seach Engine that can trace back the scene where an anime **screenshots / vedio clip** is taken from.\n It tells you which anime, which episode, and the exact moment this scene appears."
            ,colour=0x19198c)
        embed.add_field(name="`m.sauce <link>`", value="image link", inline=True)
        embed.add_field(name="`m.sauce <upload file>`", value="local screenshot", inline=True)
        embed.add_field(name="`m.sauce`", value="gets the last image or vedio, in the chat", inline=True)
        embed.add_field(name="** **", value="Below commands has low accuracy, But provides some Result, __use these if above commands didn't work__", inline=False)
        embed.add_field(name="`m.find <link>`", value="image link", inline=True)
        embed.add_field(name="`m.find <upload file>`", value="local screenshot", inline=True)
        embed.add_field(name='** **',
                        value="\n[support server](https://discord.gg/cyKAjwcZdB) • [invite bot](https://discord.com/oauth2/authorize?client_id=876139135507763280&permissions=2684741712&scope=bot%20applications.commands) • [vote](https://top.gg/bot/876139135507763280/vote)",
                        inline=False)

        a8 = embed = discord.Embed(
            title='UTILITY <:KillerZeroTwo_:881783524410138644>',
            description=("**PREFIX : `m.` **"),
            colour=0x19198c)
        embed.add_field(
            name='`avatar, banner, user, server, topic, insult, toxic,`||`pickupline @user` <:tx18plus:894297424523325470>,|| `roles, roles @user, clear <n>, purge @user <n>`',
            value='** ** \n`m.invite`, `m.botinfo`, `m.owner`, `m.donate`, `m.vote`, `m.ping`', inline=True)
        embed.add_field(name='Tag people if u want',
                        value="\n[support server](https://discord.gg/cyKAjwcZdB) • [invite bot](https://discord.com/oauth2/authorize?client_id=876139135507763280&permissions=2684741712&scope=bot%20applications.commands) • [vote](https://top.gg/bot/876139135507763280/vote)",
                        inline=False)

        a9 = embed = discord.Embed(
            title=('ROLE PLAY <:02Cozy:878167184705204225>'),
            description=("**PREFIX : `m.` **"),
            colour=0x19198c)
        embed.add_field(name='FUN 😁', value='**```m.kiss, m.blush, m.cuddle, m.hug, m.lick,m.bite, m.tickle``` **',
                        inline=False)
        embed.add_field(name='Anger 💢',
                        value='**```m.bonk, m.kill, m.slap, m.yeet, m.bully, m.kick, m.baka, m.jojo ```**',
                        inline=False)

        embed.add_field(name='Reaction ❤️',
                        value='**```m.happy, m.pat, m.smile, m.cry, m.highfive, m.wave, m.handhold, m.feed```   **',
                        inline=False)

        embed.add_field(name='Action ✌️', value='**```m.wink, m.dance, m.poke, m.smug, m.cringe, m.nom```**',
                        inline=False)
        embed.add_field(name='Tag people if u want',
                        value="\n[support server](https://discord.gg/cyKAjwcZdB) • [invite bot](https://discord.com/oauth2/authorize?client_id=876139135507763280&permissions=2684741712&scope=bot%20applications.commands) • [vote](https://top.gg/bot/876139135507763280/vote)",
                        inline=False)
        embed.set_footer(text=author.name, icon_url=pfp)

        an = embed = discord.Embed(
            title='NSFW <:MikuNyan:879902354193936394>',
            description=("**PREFIX : `m.` **"),
            colour=0x19198c)
        embed.add_field(name='`m.dhelp`', value='doujin info,\n\tRead full doujin in **(DM)**', inline=True)
        embed.add_field(name='`m.2dhelp`', value='2D nsfw, rule34, gif', inline=False)
        embed.add_field(name='`m.3dhelp`', value='porn, 3D nsfw', inline=True)
        embed.add_field(name='`🆕 m.fhelp`', value='futanari, furry', inline=False)
        embed.add_field(name='`🆕 m.ahelp`', value='autopost nsfw webhooks 3d & 2d', inline=False)

        a0 = embed = discord.Embed(
            title=("HELP <a:happyheart_jess:878675557452234803>"),
            description=("**PREFIX : `m.` **"), timestamp=(ctx.message.created_at),
            colour=0x19198c)
        embed.set_author(name=author, icon_url=pfp)
        embed.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/424792877546340372/879953807361048666/image7.png")
        embed.add_field(name="1️⃣ ANIME",
                        value='**\n**', inline=True)
        embed.add_field(name="2️⃣ MANGA",
                        value='**\n**', inline=True)
        embed.add_field(name="3️⃣ TRANSLATOR",
                        value='**\n**', inline=True)
        embed.add_field(name="4️⃣ QUOTES",
                        value='**\n**', inline=True)
        embed.add_field(name="5️⃣ QUIZ",
                        value='**\n**', inline=True)
        embed.add_field(name="6️⃣ WALLPAPER",
                        value='**\n**', inline=True)
        embed.add_field(name="7️⃣ SAUCE FINDER",
                        value='**\n**', inline=True)
        embed.add_field(name="8️⃣ REACTION",
                        value='**\n**', inline=True)
        embed.add_field(name="9️⃣ UTILITY",
                        value='**\n**', inline=True)
        embed.add_field(name='** **',
                        value="|| <a:heartarrow:879888953170346034> `m.nsfw` - NSFW <:tx18plus:894297424523325470>|| \n[support server](https://discord.gg/cyKAjwcZdB) • [invite bot](https://discord.com/oauth2/authorize?client_id=876139135507763280&permissions=2684741712&scope=bot%20applications.commands) • [vote](https://top.gg/bot/876139135507763280/vote)",
                        inline=False)
        embed.set_footer(text="react what u want", icon_url=self.client.user.avatar_url)

        message = await ctx.send(embed=embed, components=[
            Select(
                placeholder="Select something! 🍷",
                options=[
                    SelectOption(label="Anime", value="a"),
                    SelectOption(label="Manga", value="h"),
                    SelectOption(label="Translator", value="b"),
                    SelectOption(label="Quotes", value="c"),
                    SelectOption(label="Quiz", value="i"),
                    SelectOption(label="Wallpaper", value="d"),
                    SelectOption(label="Sauce Finder", value="j"),
                    SelectOption(label="Reaction", value="e"),
                    SelectOption(label="Utility", value="f"),
                    SelectOption(label="Nsfw", value="g"),
                    SelectOption(label="Main", value="m")])])

        while True:
            try:
                interaction = await self.client.wait_for("select_option", timeout=60)

                gg = f"{interaction.values[0]}"
                if gg == "a":
                    await interaction.edit_origin(embed=a1)
                elif gg=="j":
                    await interaction.edit_origin(embed=a11)
                elif gg=="h":
                    await interaction.edit_origin(embed=a12)
                elif gg=="i":
                    await interaction.edit_origin(embed=a13)
                elif gg == "b":
                    await interaction.edit_origin(embed=a2)
                elif gg == "c":
                    await interaction.edit_origin(embed=a6)
                elif gg == "d":
                    await interaction.edit_origin(embed=a7)
                elif gg == "e":
                    await interaction.edit_origin(embed=a9)
                elif gg == "f":
                    await interaction.edit_origin(embed=a8)
                elif gg == "m":
                    await interaction.edit_origin(embed=a0)
                elif gg == "g":
                    if ctx.channel.is_nsfw():
                        await interaction.edit_origin(embed=an)
                    else:
                        user = ctx.message.author
                        em = discord.Embed(
                            title='This is a `NFSW COMMAND` use it in nsfw channel <a:chikasmack_jess:878677310428053596>',
                            description="Click here to [INVITE](https://discord.com/api/oauth2/authorize?client_id=876139135507763280&permissions=2684741712&scope=bot%20applications.commands) BOT",
                            colour=0x19198c)
                        em.set_footer(text=(user),
                                      icon_url=user.avatar_url)

                        em.set_footer(text=(user),
                                      icon_url=user.avatar_url)
                        await interaction.send(embed=em)
            except asyncio.TimeoutError:
                await message.edit(content='> **Timed out!**', embed=em)
                return

    @commands.command(aliases=["3dhelp", "dhelp3"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.is_nsfw()
    @commands.guild_only()
    async def d3help(self, ctx):
        embed = discord.Embed(
            title=('3D nsfw 🔞'),
            description=("**PREFIX : `m.` **"),
            colour=0x39138b)
        embed.add_field(name="** **", value="```m.rass, m.rboobs, m.rpussy, m.rthigh, m.rlesbian```")
        embed.add_field(name="** **",
                        value="```m.ranal, m.rblowjob, m.porn, m.rbdsm, m.rcum, m.collared, m.dp (double penetration)``` ")
        embed.add_field(name="** **", value="```m.cosplay, m.wild, m.4k, m.nude```", inline=True)
        embed.add_field(name='** **', value="```m.rlesbiangif, m.rbdsmgif, m.rpussygif, m.rcumgif, m.blowjobgif, ranalgif, m.dpgif ```\n ` -> rpussygif is not recommened & gif has low content's try normal tags`", inline=True)
        embed.add_field(name='*voted users can get max 15 post per request\nex: `m.ass 15`*',
                        value="SUPPORT [SERVER](https://discord.gg/cyKAjwcZdB) • [INVITE BOT](https://discord.com/oauth2/authorize?client_id=876139135507763280&permissions=2684741712&scope=bot%20applications.commands) • [VOTE](https://top.gg/bot/876139135507763280/vote)",
                        inline=False)
        embed.set_footer(text='vote and join server for loop access', icon_url=ctx.message.author.avatar_url)
        await ctx.send(embed=embed)

    @commands.command(aliases=["2dhelp", "dhelp2"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.is_nsfw()
    @commands.guild_only()
    async def d2help(self, ctx):
        embed = discord.Embed(
            title=('DOUJIN (nsfw)🔞'),
            description=("**PREFIX : `m.` **"),
            colour=0x39138b)
        embed.add_field(name='website', value="```m.rule34 <name>, m.gelb <name>, m.random34```", inline=False)
        embed.add_field(name='Boobs', value="```m.boobs,  m.cleavage, m.midriff, m.boobjob, m.boobsgrab```",
                        inline=True)
        embed.add_field(name='Pussy', value="```m.pussy, m.panti, m.pantsu, m.pantyhose, m.bush, m.creampie, m.mast(mastrubation), m.cum```",
                        inline=True)
        embed.add_field(name='Ass', value="```m.ass, m.anal, m.thigh, m.assgrab, m.thicc, m.stock(stockings)```", inline=True)
        embed.add_field(name='Culture',
                        value="```m.hose, m.1girl, m.cosplay, m.swimsuit, m.bunny, m.milf, m.maid, m.lingerie, m.uniform,  m.armpit,  m.glasses,  m.ecchi, m.blowjob, m.trap, m.tentacle, m.public, m.wet, m.feetjob, m.feet, ```",
                        inline=True)
        embed.add_field(name='Dominance',
                        value="```m.bdsm, m.femdom, m.finger, m.ahegao, m.sucu(succubus), m.dark(skin), m.solo, m.spank, m.handjob, m.fit, m.mgirl(monstergirl) m.yuri, m.yaoi, m.fuck, m.cuckhold, m.gangbang, m.incest, m.orgy```",
                        inline=True)
        embed.add_field(name='Ero, Lewd, Nsfw',
                        value="```m.genshin, m.quint(quintuplets), m.hentai, m.elves, m.nsfwneko, m.nwaifu, m.ero, m.kemo, m.lewdneko```",
                        inline=True)
        embed.add_field(name='Gif',
                        value="```hentaigif, m.boobgif, m.yurigif, m.pussygif, m.blowjobgif, m.cumgif, m.analgif, m.mastgif(mastrubation)```\n\n```Join suport server for suggestion in addition of tags```",
                        inline=True)
        embed.add_field(name='*voted users can get max 15 post per request\nex: `m.ass 10`*',
                        value="SUPPORT [SERVER](https://discord.gg/cyKAjwcZdB) • [INVITE BOT](https://discord.com/oauth2/authorize?client_id=876139135507763280&permissions=2684741712&scope=bot%20applications.commands) • [VOTE](https://top.gg/bot/876139135507763280/vote)",
                        inline=False)
        embed.set_footer(text='vote and join server for loop access', icon_url=ctx.message.author.avatar_url)
        await ctx.send(embed=embed)

    @commands.command(aliases=["nhelp", "nsfwhelp"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.is_nsfw()
    @commands.guild_only()
    async def nsfw(self, ctx):
        embed = discord.Embed(
            title='NSFW <:MikuNyan:879902354193936394>',
            description=("**PREFIX : `m.` **"),
            colour=0x19198c)
        embed.add_field(name='`m.dhelp`', value='doujin info,\n\tRead full doujin in **(DM)**', inline=True)
        embed.add_field(name='`m.2dhelp`', value='2D nsfw, rule34, gif', inline=False)
        embed.add_field(name='`m.3dhelp`', value='porn, 3D nsfw', inline=True)
        embed.add_field(name='`🆕 m.fhelp`', value='futanari, furry', inline=False)
        embed.add_field(name='`🆕 m.ahelp`', value='autopost nsfw webhooks 3d & 2d', inline=False)
        await ctx.send(embed=embed)

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.is_nsfw()
    @commands.guild_only()
    async def ahelp(self, ctx):
        embed = discord.Embed(
            title=("`🆕` Nsfw Autopost Webhooks `(beta)`"),
            description=("**PREFIX : `m.` **"),
            colour=0x39138b)
        embed.add_field(name='`tagadd < >`', value='To add tags')
        embed.add_field(name='`tagremove < >`', value='To remove tags')
        embed.add_field(name='`totaltags`', value='linked tages in the channel')
        embed.add_field(name='** **',
                        value='```Needs webhook access for bot and the user\nExample commands:\n m.tagadd ass\n m.tagremove ass```')
        embed.add_field(name='`beta version.. contact support for bugs`',
                        value="SUPPORT [SERVER](https://discord.gg/cyKAjwcZdB) • [INVITE BOT](https://discord.com/oauth2/authorize?client_id=876139135507763280&permissions=2684741712&scope=bot%20applications.commands) • [VOTE](https://top.gg/bot/876139135507763280/vote)",
                        inline=False)
        await ctx.send(embed=embed)

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.is_nsfw()
    @commands.guild_only()
    async def fhelp(self, ctx):
        embed = discord.Embed(
            title=("🆕 Futanari, Furry `(beta)`"),
            description=("**PREFIX : `m.` **"),
            colour=0x39138b)

        embed.add_field(name="** **",
                        value="```m.fboob, m.fboobjob, m.fass, m.flick, m.fpussy, m.fpussyeat, m.ffinger, m.fspank```")
        embed.add_field(name="** **",
                        value="```m.fride, m.fsuck, m.f69, m.fanal, m.ftoys, m.fcumflation, m.fdp, m.fgif, m.fpet``` ")
        embed.add_field(name="** **",
                        value="```m.fsolo, ffemale, m.fbi, m.ffuta, m.fmale, m.fdick, m.fgay, m.fpokemon m.ftentacles```",
                        inline=True)
        embed.add_field(name='*`beta`*',
                        value="SUPPORT [SERVER](https://discord.gg/cyKAjwcZdB) • [INVITE BOT](https://discord.com/oauth2/authorize?client_id=876139135507763280&permissions=2684741712&scope=bot%20applications.commands) • [VOTE](https://top.gg/bot/876139135507763280/vote)",
                        inline=False)
        embed.set_footer(text='vote and join server for loop access', icon_url=ctx.message.author.avatar_url)
        await ctx.send(embed=embed)

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.is_nsfw()
    @commands.guild_only()
    async def dhelp(self, ctx):
        embed = discord.Embed(
            title=('DOUJIN (nsfw)🔞'),
            description=("**PREFIX : `m.` **"),
            colour=0x39138b)

        embed.add_field(name='`m.doujin <id>`', value="doujin info\n", inline=True)
        embed.add_field(name='`m.tag <tag>`', value="related tag\n", inline=True)
        embed.add_field(name='`m.radoujin`', value="random doujin\n", inline=True)
        embed.add_field(name='`m.popdoujin`', value="currently popular doujin\n", inline=True)

        embed.add_field(name='**Read doujin **', value="Full story in **DM** `cooldown=30 m/1 cmd`", inline=False)
        embed.add_field(name='`m.read <id>`', value="read doujin using id ", inline=True)
        embed.add_field(name='`m.reradoujin`', value="read random doujin", inline=True)
        embed.add_field(name='** **',
                        value="```diff\n-API error\nTry once.. if bot does not respond try later```\n**KINDLY OMIT '  <  '||'  >  '**\n[support server](https://discord.gg/cyKAjwcZdB) • [invite bot](https://discord.com/oauth2/authorize?client_id=876139135507763280&permissions=2684741712&scope=bot%20applications.commands) • [vote](https://top.gg/bot/876139135507763280/vote)",
                        inline=False)
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Example(client))

# import discord
# from discord.ext import commands
# import asyncio
# from discord.ext.commands import has_permissions, MissingPermissions
# class Example(commands.Cog):
#     def __init__(self,client):
#         self.client=client

#     @commands.Cog.listener()
#     async def on_ready(self):
#         print("help is ready")

#     @commands.command()
#     @commands.cooldown(1, 7, commands.BucketType.user)
#     async def help(self,ctx):
#         author = ctx.message.author
#         pfp = ctx.author.avatar_url
#         a1 = embed = discord.Embed(title=("ANIME <a:MikuJam:879895048437784617>"),colour=0x19198c)
#         embed.add_field(name="`m.anime <anime name>`",
#                         value='anime info from myanimelist (synopsis,total_epi,score,aired,pic)', inline=True)
#         embed.add_field(name='`m.dload <anime #ep>`', value='download anime (HDP)(360P)(480P)(720P)(1080P)', inline=True)
#         embed.add_field(name="`m.watch <anime #ep>`", value='gogoanime episode link', inline=True)
#         embed.add_field(name='MANGA <a:zzy_NezukoBlanket_2:879901247254171658>',
#                         value='** **', inline=False)
#         embed.add_field(name='`m.manga <manga name>`',
#                         value='manga info from myanimelist\n(synopsis,chapters,volumes,score,pic)', inline=False)
#         embed.add_field(name='Character <:MikuThanks:879900458603393094>',
#                         value='** **', inline=False)
#         embed.add_field(name='`m.character <character name>`',
#                         value='character picture and info from myanimelist\n', inline=False)
#         embed.add_field(name='** **',
#                         value="**KINDLY OMIT '  <  '||'  >  '**\nSUPPORT [SERVER](https://discord.gg/cyKAjwcZdB) • [INVITE BOT](https://discord.com/oauth2/authorize?client_id=876139135507763280&permissions=2684741712&scope=bot%20applications.commands) • [VOTE](https://top.gg/bot/876139135507763280/vote)",
#                         inline=False)
#         embed.set_footer(text=author.name, icon_url=pfp)

#         a2 = embed = discord.Embed(
#             title=("TRANSLATOR <:ShinobuSHeart_:878676427178921994>"),
#             description=("**PREFIX : `m.` **"),
#             colour=0x19198c)

#         embed.add_field(name='TRANSLATOR 🎀',
#                         value='** **', inline=False)
#         embed.add_field(name='`m.lcode`',
#                         value='universal language codes', inline=True)
#         embed.add_field(name='`m.meaning`',
#                         value='Gives the meaning of the words', inline=True)
#         embed.add_field(name='`m.trans <lcode> content`',
#                         value='Transtlates words & sentence\n```Example command\n1."m.trans ta Hello" This Translates hello to Tamil\n2."m.trans en வணக்கம்" This Translates வணக்கம் to English``` ', inline=False)
#         embed.add_field(name='** **',
#                         value="**KINDLY OMIT '  <  '||'  >  '**\n[support server](https://discord.gg/cyKAjwcZdB) • [invite bot](https://discord.com/oauth2/authorize?client_id=876139135507763280&permissions=2684741712&scope=bot%20applications.commands) • [vote](https://top.gg/bot/876139135507763280/vote)",
#                         inline=False)
#         embed.set_footer(text=author.name, icon_url=pfp)


#         a6 = embed = discord.Embed(
#             title=('QUOTES <:MikuAraAra:879901712696082443>'),
#             colour=0x19198c)
#         embed.add_field(name='`m.quote`', value='randam anime Quote', inline=True)
#         embed.add_field(name='`m.aquote <anime>`', value='  Quote from Anime', inline=True)
#         embed.add_field(name='`m.cquote <character>`', value='Quote from Character', inline=True)
#         # embed.add_field(name='`m.fiquote <num>`', value='num of anime quote', inline=True)
#         embed.add_field(name='`m.inspire`', value='normie quotes', inline=True)
#         embed.add_field(name='QUIZ <:MikuConfused:879903705548337192>', value='** **', inline=False)
#         embed.add_field(name='`m.quiz`', value='Anime quiz', inline=True)
#         embed.add_field(name='`m.quotequiz <anime>`', value='Quotes quiz on the anime', inline=True)
#         embed.add_field(name='`m.points`', value='`view points`', inline=True)
#         embed.add_field(name='`m.lb`', value='`leader board`', inline=True)
#         embed.set_footer(text=author.name, icon_url=pfp)

#         embed.add_field(name='** **',
#                         value="**KINDLY OMIT '  <  '||'  >  '**\nSUPPORT [SERVER](https://discord.gg/cyKAjwcZdB) • [INVITE BOT](https://discord.com/oauth2/authorize?client_id=876139135507763280&permissions=2684741712&scope=bot%20applications.commands) • [VOTE](https://top.gg/bot/876139135507763280/vote)",
#                         inline=False)
#         embed.set_footer(text=author.name, icon_url=pfp)

#         a7 = embed = discord.Embed(
#             title=('WALLPAPER <:8046_ZeroWow:879902918067753011>'),
#             colour=0x19198c)
#         embed.add_field(name="`m.waifu`",value="waifu pic",inline=True)
#         embed.add_field(name='`m.wallpaper <name>`', value='anime wallpaper ', inline=True)
#         embed.add_field(name='`m.pfp`', value='anime avatar ', inline=True)
#         embed.add_field(name='`m.holo`', value='holo pic', inline=True)
#         embed.add_field(name='`m.kemo`', value='kemonomimi pic', inline=True)
#         embed.add_field(name='`m.neko`', value='cat girls', inline=True)
#         embed.add_field(name='`m.foxgirl`', value='fox girl', inline=True)
#         embed.add_field(name='`m.nekogif`', value='nekogif', inline=True)
#         embed.add_field(name="`m.wallpaper`",value="random anime wallpaper",inline=True)
#         embed.add_field(name='`m.megumin`', value='megumin', inline=True)
#         embed.add_field(name='`m.kanna`', value='kanna', inline=True)
#         embed.add_field(name='`m.shinobu`', value='shinobu', inline=True)

#         embed.add_field(name='** **',
#                         value="\n[support server](https://discord.gg/cyKAjwcZdB) • [invite bot](https://discord.com/oauth2/authorize?client_id=876139135507763280&permissions=2684741712&scope=bot%20applications.commands) • [vote](https://top.gg/bot/876139135507763280/vote)",
#                         inline=False)
#         embed.set_footer(text=author.name, icon_url=pfp)

#         a8 = embed = discord.Embed(
#             title='UTILITY <:KillerZeroTwo_:881783524410138644>',
#         description=("**PREFIX : `m.` **"),
#             colour=0x19198c)
#         embed.add_field(name='```avatar, banner, user, server, topic, insult, toxic, roles, roles @user, clear <n>, purge @user <n>```', value='** ** \n`m.invite`, `m.botinfo`, `m.owner`, `m.donate`, `m.vote`, `m.ping`', inline=True)
#         embed.add_field(name='Tag people if u want',
#                         value="\n[support server](https://discord.gg/cyKAjwcZdB) • [invite bot](https://discord.com/oauth2/authorize?client_id=876139135507763280&permissions=2684741712&scope=bot%20applications.commands) • [vote](https://top.gg/bot/876139135507763280/vote)",
#                         inline=False)


#         a9 = embed = discord.Embed(
#             title=('ROLE PLAY <:02Cozy:878167184705204225>'),
#             description=("**PREFIX : `m.` **"),
#             colour=0x19198c)
#         embed.add_field(name='FUN 😁', value='**```m.kiss, m.blush, m.cuddle, m.hug, m.lick,m.bite, m.tickle``` **', inline=False)
#         embed.add_field(name='Anger 💢', value='**```m.bonk, m.kill, m.slap, m.yeet, m.bully, m.kick, m.baka, m.jojo ```**', inline=False)

#         embed.add_field(name='Reaction ❤️', value='**```m.happy, m.pat, m.smile, m.cry, m.highfive, m.wave, m.handhold, m.feed```   **', inline=False)

#         embed.add_field(name='Action ✌️', value='**```m.wink, m.dance, m.poke, m.smug, m.cringe, m.nom```**', inline=False)
#         embed.add_field(name='Tag people if u want',
#                         value="\n[support server](https://discord.gg/cyKAjwcZdB) • [invite bot](https://discord.com/oauth2/authorize?client_id=876139135507763280&permissions=2684741712&scope=bot%20applications.commands) • [vote](https://top.gg/bot/876139135507763280/vote)",
#                         inline=False)
#         embed.set_footer(text=author.name, icon_url=pfp)


#         a0 = embed = discord.Embed(
#             title=("HELP <a:happyheart_jess:878675557452234803>"),
#             description=("**PREFIX : `m.` **"),timestamp=(ctx.message.created_at),
#             colour=0x19198c)
#         embed.set_author(name=author, icon_url=pfp)
#         embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/424792877546340372/879953807361048666/image7.png")
#         embed.add_field(name="1️⃣ ANIME\nMANGA",
#                         value='** **', inline=True)
#                         #
#         embed.add_field(name="2️⃣TRANSLATOR",
#                         value='** **', inline=True)
#         embed.add_field(name="3️⃣ QUOTES\nQUIZ",
#                         value='** **', inline=True)
#         embed.add_field(name="4️⃣WALLPAPER",
#                         value='** **', inline=True)
#         embed.add_field(name="5️⃣REACTION",
#                         value='** **', inline=True)
#         embed.add_field(name="6️⃣ UTILITY",
#                         value='** **', inline=True)
#         embed.add_field(name='** **',
#                         value="`m.nsfw` <:tx18plus:894297424523325470>\n[support server](https://discord.gg/cyKAjwcZdB) • [invite bot](https://discord.com/oauth2/authorize?client_id=876139135507763280&permissions=2684741712&scope=bot%20applications.commands) • [vote](https://top.gg/bot/876139135507763280/vote)",
#                         inline=False)
#         # embed.add_field(name='`NSFW commands` - \n\n**Bonus: command **<:ShinobuSHeart_:878676427178921994>',
#         #                 value="`m.avatar`, `m.banner`, `m.userinfo`, `m.server` `m.topic`, `m.insult`\n[support server](https://discord.gg/cyKAjwcZdB) • [invite bot](https://discord.com/oauth2/authorize?client_id=876139135507763280&permissions=2684741712&scope=bot%20applications.commands) • [vote](https://top.gg/bot/876139135507763280/vote)",
#         #                 inline=False)
#         embed.set_footer(text="react what u want", icon_url=self.client.user.avatar_url)

#         message = await ctx.send(embed=embed)

#         await message.add_reaction("◀️")
#         await message.add_reaction("1️⃣")
#         await message.add_reaction("2️⃣")
#         await message.add_reaction("3️⃣")
#         await message.add_reaction("4️⃣")
#         await message.add_reaction("5️⃣")
#         await message.add_reaction("6️⃣")


#         def check(reaction, user):
#             return user == ctx.author and str(reaction.emoji) in ["◀️", "1️⃣", "2️⃣", "3️⃣",
#                                                                 "4️⃣", "5️⃣", "6️⃣"] and message.id == reaction.message.id
#             # This makes sure nobody except the command sender can interact with the "menu"

#         time = 45
#         while True:
#             try:
#                 reaction, user = await self.client.wait_for("reaction_add", timeout=time, check=check)

#                 if str(reaction.emoji) == "1️⃣":
#                     time = 45
#                     await message.edit(embed=a1)
#                     try:
#                         await message.remove_reaction(reaction, user)
#                     except:
#                         print("hi")
#                 elif str(reaction.emoji) == "2️⃣":
#                     time = 45
#                     await message.edit(embed=a2)
#                     try:
#                         await message.remove_reaction(reaction, user)
#                     except:
#                         print("hi")
#                 elif str(reaction.emoji) == "3️⃣":
#                     time = 45
#                     await message.edit(embed=a6)
#                     try:
#                         await message.remove_reaction(reaction, user)
#                     except:
#                         print("hi")
#                 elif str(reaction.emoji) == "4️⃣":
#                     time = 45
#                     await message.edit(embed=a7)
#                     try:
#                         await message.remove_reaction(reaction, user)
#                     except:
#                         print("hi")
#                 elif str(reaction.emoji) == "◀️":
#                     time = 45
#                     await message.edit(embed=a0)
#                     try:
#                         await message.remove_reaction(reaction, user)
#                     except:
#                         print("hi")
#                 elif str(reaction.emoji) == "6️⃣":
#                     await message.edit(embed=a8)
#                     try:
#                         await message.remove_reaction(reaction, user)
#                     except:
#                         print("hi")
#                 elif str(reaction.emoji) == "5️⃣":
#                     time = 45
#                     await message.edit(embed=a9)
#                     try:
#                         await message.remove_reaction(reaction, user)
#                     except:
#                         print("hi")
#                 else:
#                     try:
#                         await message.remove_reaction(reaction, user)
#                     except:
#                         print("hi")

#                         # removes reactions if the user tries to go forward on the last page or
#                     # backwards on the first page
#             except asyncio .TimeoutError:
#                 await message.clear_reactions()
#                 return


#     @commands.command(aliases = ["3dhelp","dhelp3"])
#     @commands.cooldown(1, 5, commands.BucketType.user)
#     @commands.is_nsfw()
#     @commands.guild_only()
#     async def d3help(self,ctx):
#         embed = discord.Embed(
#             title=('3D nsfw 🔞'),
#             description=("**PREFIX : `m.` **"),
#         colour=0x39138b)
#         embed.add_field(name="**s-1**",value="```m.rass, m.rboobs, m.rpussy, m.rthigh```")
#         embed.add_field(name="**s-2**",value="```m.ranal, m.rblowjob, m.porn, m.bdsm, m.rlesbian, m.rcum, m.collared, m.dp (double penetration)``` ")
#         embed.add_field(name="**s-3**", value="```m.cosplay, m.wild, m.4k, m.nude```", inline=True)
#         # embed.add_field(name='`m.3drandom`', value="** **", inline=True)
#         embed.add_field(name='*voted users can get max 10 post per request\nex: `m.ass 10`*',
#                         value="SUPPORT [SERVER](https://discord.gg/cyKAjwcZdB) • [INVITE BOT](https://discord.com/oauth2/authorize?client_id=876139135507763280&permissions=2684741712&scope=bot%20applications.commands) • [VOTE](https://top.gg/bot/876139135507763280/vote)",
#                         inline=False)
#         embed.set_footer(text='vote and join server for loop access',icon_url=ctx.message.author.avatar_url)
#         await ctx.send(embed=embed)


#     @commands.command(aliases = ["2dhelp","dhelp2"])
#     @commands.cooldown(1, 5, commands.BucketType.user)
#     @commands.is_nsfw()
#     @commands.guild_only()
#     async def d2help(self,ctx):
#         embed = discord.Embed(
#             title=('DOUJIN (nsfw)🔞'),
#             description=("**PREFIX : `m.` **"),
#             colour=0x39138b)
#         embed.add_field(name='website', value="```m.rule34 <name>, m.gelb <name>, m.random34```", inline=False)
#         embed.add_field(name='Boobs', value="```m.boobs, m.boobsgif, m.midriff, m.tits, m.boobjob m.boobsgrab```", inline=True)
#         embed.add_field(name='Pussy', value="```m.pussy, m.pussysgif, m.finger, m.kuni (lick) , m.panti```", inline=True)
#         embed.add_field(name='Ass', value="```m.ass, m.anal, m.thigh, m.spank, m.assgrab```", inline=True)
#         embed.add_field(name='Culture', value="```m.cosplay, m.swimsuit, m.hentai, m.blowjob, m.classic, m.trap, m.tentacle, m.cum, m.feet ```", inline=True)
#         embed.add_field(name='Dominance', value="```m.femdom, m.lesbian, m.solo, m.yuri, m.yaoi , m.futanari, m.fuck```", inline=True)
#         embed.add_field(name='Ero, Lewd, Nsfw', value="```m.nsfwneko, m.nwaifu, m.nsfwavatar\nm.lewdneko, m.lewdholo, m.lewdk(kitsune)\nm.ero, m.eroneko, m.eroyuri```", inline=True)
#         embed.add_field(name='Gif', value="```m.hentaigif, m.pussysgif, m.boobsgif, m.sologif, m.yurigif, m.blowjobgif, m.feetgif m.cumgif, m.nsfwnekogif```", inline=True)
#         embed.add_field(name='*voted users can get max 10 post per request\nex: `m.ass 10`*',
#                         value="SUPPORT [SERVER](https://discord.gg/cyKAjwcZdB) • [INVITE BOT](https://discord.com/oauth2/authorize?client_id=876139135507763280&permissions=2684741712&scope=bot%20applications.commands) • [VOTE](https://top.gg/bot/876139135507763280/vote)",
#                         inline=False)
#         embed.set_footer(text='vote and join server for loop access',icon_url=ctx.message.author.avatar_url)
#         await ctx.send(embed=embed)

#     @commands.command(aliases = ["nhelp","nsfwhelp"])
#     @commands.cooldown(1, 5, commands.BucketType.user)
#     @commands.is_nsfw()
#     @commands.guild_only()
#     async def nsfw(self,ctx):
#         embed = discord.Embed(
#             title='NSFW <:MikuNyan:879902354193936394>',
#         description=("**PREFIX : `m.` **"),
#             colour=0x19198c)
#         embed.add_field(name='`m.dhelp`', value='doujin info,\n\tRead full doujin in **(DM)**', inline=True)
#         embed.add_field(name='`m.2dhelp`', value='2D nsfw, rule34, gif',inline=False)
#         embed.add_field(name='`m.3dhelp`', value='porn, 3D nsfw', inline=True)
#         embed.add_field(name='`m.fhelp`', value='futanari nsfw under maintanance (28 cmds)', inline=False)
#         await ctx.send(embed=embed)


#     @commands.command()
#     @commands.cooldown(1, 5, commands.BucketType.user)
#     @commands.is_nsfw()
#     @commands.guild_only()
#     async def dhelp(self,ctx):
#         embed = discord.Embed(
#             title=('DOUJIN (nsfw)🔞'),
#             description=("**PREFIX : `m.` **"),
#             colour=0x39138b)

#         embed.add_field(name='`m.doujin <id>`', value="doujin info\n", inline=True)
#         embed.add_field(name='`m.tag <tag>`', value="related tag\n", inline=True)
#         embed.add_field(name='`m.radoujin`', value="random doujin\n", inline=True)
#         embed.add_field(name='`m.popdoujin`', value="currently popular doujin\n", inline=True)

#         embed.add_field(name='**Read doujin **', value="Full story in **DM** `cooldown=30 m/1 cmd`", inline=False)
#         embed.add_field(name='`m.read <id>`', value="read doujin using id ", inline=True)
#         embed.add_field(name='`m.reradoujin`', value="read random doujin", inline=True)
#         embed.add_field(name='** **',
#                         value="**KINDLY OMIT '  <  '||'  >  '**\n[support server](https://discord.gg/cyKAjwcZdB) • [invite bot](https://discord.com/oauth2/authorize?client_id=876139135507763280&permissions=2684741712&scope=bot%20applications.commands) • [vote](https://top.gg/bot/876139135507763280/vote)",
#                         inline=False)
#         await ctx.send(embed=embed)

# def setup(client):
#     client.add_cog(Example(client))
