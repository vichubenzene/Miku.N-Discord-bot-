import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions
from jikanpy import jikan
aki = jikan.Jikan()
class Example(commands.Cog):
    def __init__(self,client):
        self.client=client
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("error handler is ready")

    @commands.Cog.listener()
    async def on_command_error(self,ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            em = discord.Embed(title='please enter correct `Aruguments`',
                            description="You can get help by using `m.help` command", colour=0x19198c)
            em.set_footer(text=(ctx.message.author),
                        icon_url=ctx.message.author.avatar_url)
            await ctx.send(embed=em, delete_after=7.5)
        # if isinstance(error, commands.CommandNotFound):
        #     em = discord.Embed(title='please enter correct `Command`',
        #                        description="You can get help by using `m.help` command", colour=0x19198c)
        #     em.set_footer(text=(ctx.message.author),
        #                   icon_url=ctx.message.author.avatar_url)
        #     await ctx.send(embed=em)
        if isinstance(error, commands.errors.NSFWChannelRequired):
            user=ctx.message.author
            em = discord.Embed(title='This is a `NFSW COMMAND` use it in nsfw channel <a:chikasmack_jess:878677310428053596>',
                            description="Click here to [INVITE](https://discord.com/api/oauth2/authorize?client_id=876139135507763280&permissions=2684741712&scope=bot%20applications.commands) BOT", colour=0x19198c)
            em.set_footer(text=(user),
                        icon_url=user.avatar_url)

            em.set_footer(text=(user),
                        icon_url=user.avatar_url)
            await ctx.send(embed=em, delete_after=7.5)
            return;

        if isinstance(error, commands.CommandOnCooldown):
            user=ctx.message.author
            em = discord.Embed(
                title = "Slow it down <a:demontime:878161676183150612>",
                description=f"\nsry its limited commands for a user\nRetry after `{error.retry_after:.2f} S`\n**[INVITE BOT](https://discord.com/api/oauth2/authorize?client_id=876139135507763280&permissions=2684741712&scope=bot%20applications.commands)**" ,
                colour=0x19198c)
            em.set_footer(text=(user),
                        icon_url=user.avatar_url)
            await ctx.reply(embed=em, delete_after=10)
        
        if isinstance(error, MissingPermissions):
            user=ctx.message.author
            em = discord.Embed(title="You don't have permission to do that!",
                            description="only users with `manage messages permission` can use this command \n\n [INVITE](https://discord.com/api/oauth2/authorize?client_id=876139135507763280&permissions=2684741712&scope=bot%20applications.commands) BOT",
                            colour=0x19198c)
            em.set_footer(text=(user),
                        icon_url=user.avatar_url)
            await ctx.send(embed=em)

        if isinstance(error, commands.NoPrivateMessage):
            await ctx.send("you dont have permission to use it here, for privacy add me to ur sperate server")
            embed = discord.Embed(
                title=("Click here to invite  <:MikuThanks:879980177982103572>"),
                url='https://discord.com/api/oauth2/authorize?client_id=876139135507763280&permissions=2684741712&scope=bot%20applications.commands',
                description=(
                    "```1.FOR GOGOANIME LINK🔗📺 ON DISCORD\n\n2.ANIME & MANGA🤩 info from MYANIMELIST\n\n3.ANIME QUIZ WITH GLOBAL POINT SYSTEM\n\n4.ANIME QUOTES,WALLPAPER🎊 🎉\n\n7.120 language translator with pronounciation \n \n6.Rule34 ,HENTAI, read DOUJIN🔞```"),
                colour=0x19198c
            )
            embed.add_field(name=("**EVENTS**"), value=("`every month anime quiz  🎊 🎉`"), inline=True)
            embed.set_thumbnail(
                url='https://cdn.discordapp.com/attachments/424792877546340372/878663313611952148/80.png')
            embed.set_footer(text="click above to add me",
                            icon_url="https://cdn.discordapp.com/avatars/557578041908396033/a_55298feb73b577438c099d5a30f6c7f5.gif?size=1024")
            await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Example(client))