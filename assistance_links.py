import discord
from discord.ext import commands

'''General commands to use for 3DS assistance.'''



class AssistanceLinks:

    def __init__(self, bot):
        self.bot = bot

        async def simple_embed(self, text, title="", color=discord.Color.default()):
            embed = discord.Embed(title=title, color=color)
            embed.description = text
            await ctx.send(embed=embed)
		
    @commands.command(aliases=['pinfo'], pass_context=True)
    async def information(self, ctx):
        """About this cog"""
        await ctx.message.delete()
        embed = discord.Embed(title= "What is this cog for?")
        embed.set_author(name="PhazonicRidley")
        embed.description = "The purpose of this cog is to quickly provide useful links on the 3DS Homebrew discord server."
        embed.add_field(name="Where can I download this?", value="You can download it from the github [here](https://github.com/PhazonicRidley/Assistance-Links).")
        await ctx.send(embed=embed)
        
    @commands.command(pass_context=True)
    async def ub9s(self, ctx):
        """boot9strap updating guide link"""
        await ctx.message.delete()
        embed = discord.Embed(title="How to update boot9strap", color=1710847)
        embed.description = "You can use [this](https://3ds.guide/updating-b9s) guide to update boot9strap to the latest version."
        embed.set_author(name="Plailect")
        embed.set_thumbnail(url="https://avatars3.githubusercontent.com/u/16979510?v=48&s=500")
        await ctx.send(embed=embed)
        
    @commands.command(pass_context=True)
    async def ua9lh(self, ctx):
        """arm9loaderhax to boot9strap update guide"""
        await ctx.message.delete()
        embed = discord.Embed(title="How to update from arm9loaderhax to boot9strap", color=16718362)
        embed.description = "You can use [this](https://3ds.guide/a9lh-to-b9s) guide to update from A9LH to B9S."
        embed.set_author(name="Plailect")
        embed.set_thumbnail(url="https://avatars3.githubusercontent.com/u/16979510?v=48&s=500")
        await ctx.send(embed=embed)
        
    @commands.command(pass_context=True)
    async def region(self, ctx):
        """Guide for region changing the 3DS"""
        await ctx.message.delete()
        embed = discord.Embed(title="How to region change the 3DS", color=16750848)
        embed.description = "You can use [this](https://3ds.guide/region-changing) guide to region change your 3DS."
        embed.set_thumbnail(url="https://avatars3.githubusercontent.com/u/16979510?v=48&s=500")
        embed.set_author(name="Plailect")
        await ctx.send(embed=embed)
        
    @commands.group(pass_context=True)
    async def luma(self, ctx):
        """Links to Luma3DS versions 7.0.5, 7.1, and 8.1.1"""
        if ctx.invoked_subcommand is None:
            await ctx.message.delete()
            embed = discord.Embed(title="Luma3DS download links", color=65535)
            embed.description = "You can get luma 7.0.5, 7.1, and/or 8.1.1 below"
            embed.set_author(name="Aurora Wright")
            embed.set_thumbnail(url="https://gbatemp.net/attachments/Luma3DSalt-png.46691/")
            embed.add_field(name="Luma3DS 7.0.5", value="You can download Luma3DS 7.0.5 [here](https://github.com/AuroraWright/Luma3DS/releases/tag/v7.0.5). Please keep in mind that this version will only work for A9LH.")
            embed.add_field(name="Luma3DS 7.1", value="You can download Luma3DS 7.1 [here](https://github.com/AuroraWright/Luma3DS/releases/tag/v7.1). Please keep in mind this version will only work for B9S 1.0.")
            embed.add_field(name="Luma3DS 8.1.1", value="You can download the latest Luma3DS version [here](https://github.com/AuroraWright/Luma3DS/releases/tag/v8.1.1). Please keep in mind this version will only work for B9S 1.2.")
            embed.add_field(name="Latest Luma", value="You can always get the absolute latest version of Luma3DS [here](https://github.com/AuroraWright/Luma3DS/releases/latest). Please keep in mind you will need the latest version of B9S to be able to use it.")
            await ctx.send(embed=embed)
        
    @luma.command(pass_context=True)
    async def a9lh(self, ctx):
        """Links to Luma3DS version 7.0.5"""
        await ctx.message.delete()
        embed = discord.Embed(title="Luma3DS 7.0.5", color=65535)
        embed.description = "You can download Luma3DS 7.0.5 [here](https://github.com/AuroraWright/releases/tag/v7.0.5). Please keep in mind this version will only work for A9LH."
        embed.set_thumbnail(url="https://gbatemp.net/attachments/Luma3DSalt-png.46691/")
        embed.set_author(name="Aurora Wright")
        await ctx.send(embed=embed)
        
    @luma.command(pass_context=True)
    async def b9s10(self, ctx):
        """Links to Luma3DS version 7.1"""
        await ctx.message.delete()
        embed = discord.Embed(title="Luma3DS 7.1", color=65535)
        embed.description = "You can download Luma3DS 7.1 [here](https://github.com/AuroraWright/Luma3DS/releases/tag/v7.1). Please keep in mind this version will only work for B9S 1.0."
        embed.set_thumbnail(url="https://gbatemp.net/attachments/Luma3DSalt-png.46691/")
        embed.set_author(name="Aurora Wright")
        await ctx.send(embed=embed)
        
    @luma.command(pass_context=True)
    async def b9s12(self, ctx):
        """Links to Luma3DS version 8.1.1"""
        await ctx.message.delete()
        embed = discord.Embed(title="Luma3DS 8.1.1", color=65535)
        embed.description = "You can download Luma3DS 8.1.1 [here](https://github.com/AuroraWright/Luma3DS/releases/tag/v8.1.1). Please keep in mind this version will only work for B9S 1.2."
        embed.set_thumbnail(url="https://gbatemp.net/attachments/Luma3DSalt-png.46691/")
        embed.set_author(name="Aurora Wright")
        await ctx.send(embed=embed)
        
    @luma.command(aliases=['hourly'], pass_context=True)
    async def hourlies(self, ctx):
        """Links to the Luma3DS hourly site"""
        await ctx.message.delete()
        embed = discord.Embed(title="Luma3DS Hourlies", color=65535)
        embed.description = "You can get the Luma3DS hourlies [here](https://astronautlevel2.github.io/Luma3DS). Please keep in mind these are not always stable, and you use these at your own risk."
        embed.set_thumbnail(url="https://gbatemp.net/attachments/Luma3DSalt-png.46691/")
        embed.set_author(name="Aurora Wright")
        await ctx.send(embed=embed)
        
    @commands.command(pass_context=True)
    async def terms(self,ctx):
        """Link to Zeta's website; the information tab"""
        await ctx.message.delete()
        embed = discord.Embed(title="3DS Hacking Terms", color=52224)
        embed.description ="You can read [here](https://zetadesigns.github.io/info.html) for information about 3DS hacking."
        embed.set_author(name="Zeta")
        embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/186474714124910592/6c0bd4dc9c043fe35c4b5f08dcdfaa80.webp?width=250&height=250")
        await ctx.send(embed=embed)
        
    @commands.group(pass_context=True)
    async def randomize(self,ctx):
        """Pokemon randomizing guides"""
        if ctx.invoked_subcommand is None:
            await ctx.message.delete()
            embed = discord.Embed(title="How to Randomize Pokemon Games", color=10079487)
            embed.description = "These guides will help you randomize your pokemon game."
            embed.set_author(name="Slade and Zeta")
            embed.add_field(name="Randomizing a Pokemon game (CIA)",value="Use [this](https://zetadesigns.github.io/randomizing-cia.html) guide if you want to randomize a pokemon game then install it.")
            embed.add_field(name="Randomizing a Pokemon game (LayeredFS)", value="Use [this](https://zetadesigns.github.io/randomizing-layeredfs.html) guide if want to randomize a pokemon game without reinstalling it.")
            embed.set_thumbnail(url="http://i.imgur.com/eJfVxZv.png")
            await ctx.send(embed=embed)
            
    @randomize.command(pass_context=True)
    async def cia(self, ctx):
        """Randomize a Pokemon game via CIA"""
        await ctx.message.delete()
        embed = discord.Embed(title="How to Randomize A Pokemon Game as a CIA", color=10079487)
        embed.set_author(name="Slade and Zeta")
        embed.description = "Use [this](https://zetadesigns.github.io/randomizing-cia.html) guide if you want to randomize a pokemon game then install it."
        embed.set_thumbnail(url="http://i.imgur.com/eJfVxZv.png")
        await ctx.send(embed=embed)
        
    @randomize.command(pass_context=True)
    async def lfs(self, ctx):
        """Randomize a Pokemon game via CIA"""
        await ctx.message.delete()
        embed = discord.Embed(title="How to Randomize A Pokemon Game Using LayeredFS", color=10079487)
        embed.set_author(name="Slade and Zeta")
        embed.description = "Use [this](https://zetadesigns.github.io/randomizing-layeredfs.html) guide if want to randomize a pokemon game without reinstalling it."
        embed.set_thumbnail(url="http://i.imgur.com/eJfVxZv.png")
        await ctx.send(embed=embed)
        
    @commands.command(pass_context=True)
    async def prism(self, ctx):
        """How to inject Pokemon Prism saves"""
        await ctx.message.delete()
        embed = discord.Embed(title="How to Inject Pokemon Prism Saves", color=10079487)
        embed.description = "You can use [this](https://zetadesigns.github.io/injecting_prism.html) guide to inject pokemon prism saves."
        embed.set_thumbnail(url="http://i.imgur.com/eJfVxZv.png")
        await ctx.send(embed=embed)
        
    @commands.command(pass_context=True)
    async def ct(self,ctx):
        """"Cthulhu/Cashe Tool guide and download link"""
        await ctx.message.delete()
        embed = discord.Embed(title="What is Cthulhu/CacheTool?", color=993399)
        embed.description = "Cthulhu is a multipurpose tool for home menu and activity log manipulation."
        embed.add_field(name="Where can I download Cthulhu/CacheTool?", value="You can download Cthulhu/CacheTool [here](https://github.com/Ryuzaki-MrL/CacheTool/releases/tag/1.3.2). You can also download it from \nFBI > TitleDB, where it is listed simply as \"Cthulhu\".")
        embed.add_field(name="How do I use it?", value="You can use [this](https://zetadesigns.github.io/cthulhu-usage.html) guide for basic use of Cthulhu/CacheTool.")
        embed.set_author(name="Slade and Zeta (guide), Lázaro Vieira (Cthulhu)")
        await ctx.send(embed=embed)
        
    @commands.command(aliases=['fcp'], pass_context=True)
    async def flashcartpic(self,ctx):
        """Compatibility list for what flashcarts do and do not work for ntrboot"""
        await ctx.message.delete()
        embed = discord.Embed(title="Compatibility List for NTRBoot")
        embed.description = "Only the flashcarts on the left can currently be used for NTRBoot. If your flashcart does not look exactly like one of those, it can not currently be used for NTRBoot."
        embed.set_image(url="https://cdn.discordapp.com/attachments/346830960668573697/350842296075419648/ntrboot_checklist.png")
        embed.set_author(name="EdTheNerd,Jisagi")
        await ctx.send(embed=embed)
        
    @commands.command(aliases=['gm9'], pass_context=True)
    async def godmode9(self,ctx):
        """Godmod9 download link"""
        await ctx.message.delete()
        embed = discord.Embed(title="GodMode9 Download Link", color=13395711)
        embed.description = "Click [here](https://github.com/d0k3/GodMode9/releases) for the latest release of GodMode9"
        embed.set_author(name="d0k3")
        embed.set_thumbnail(url="https://avatars2.githubusercontent.com/u/12467483?v=4&s=460")
        await ctx.send(embed=embed)
        
    @commands.command(pass_context=True)
    async def fbi(self,ctx):
        """FBI download link"""
        await ctx.message.delete()
        embed = discord.Embed(title="FBI Download Link", color=16777215)
        embed.description = "Click [here](https://github.com/Steveice10/FBI/releases) for the latest version of FBI."
        embed.set_author(name="Steveice10")
        embed.set_thumbnail(url="https://avatars2.githubusercontent.com/u/1269164?v=4&s=460")
        await ctx.send(embed=embed)
        
    @commands.command(aliases=['db9s'], pass_context=True)
    async def boot9strap(self, ctx):
        """Boot9strap"""
        await ctx.message.delete()
        embed = discord.Embed(title="Boot9strap Download Link", color=59110)
        embed.description = "Click [here](https://github.com/SciresM/boot9strap/releases/download/1.2/boot9strap-1.2.zip) for a direct link for the normal version of boot9strap."
        embed.set_author(name="SciresM")
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(AssistanceLinks(bot))
