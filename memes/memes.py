import datetime
import discord

from redbot.core import Config, commands
from redbot.core.bot import Red

BaseCog = getattr(commands, "Cog", object)

def role_check(ctx, roles):
    for n, role in enumerate(roles):
        role = ctx.guild.get_role(role)
        roles[n] = role
    return len(set(ctx.author.roles).intersection(set(roles))) > 0

class Memes(BaseCog):
    
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if role_check(ctx, [454262524955852800, 454268394464870401, 659513332218331155, 720221658501087312, 676408167063879715, 454262729620848641, 793163338007707679]):
            embed = None
            if message.content.lower() == "docflood":
                doc = message.guild.get_member(216316781483130880)
                embed = discord.Embed(description = f"**Con tal ironía de Italia**\n\n**EN HONOR A NUESTRO LÍDER ({doc.mention})**", timestamp = datetime.datetime.now(), color = discord.Colour.gold())
                embed.set_image(url = "https://cdn.glitch.com/ce23a52c-740e-4bfd-a0b2-8e7f838de4d2%2Fimage0.png?v=1589287037268")
                embed.set_footer(text = f"richiesto da {ctx.author}")
            if message.content.lower() == "theredheat":
                theredheat = message.guild.get_member(423572109684637708)
                if ctx.author == theredheat:
                    embed = discord.Embed(title = "Error 404: qualcosa non va...", description = "O mio supremo maestro!\nCi inchineremo tutti alla sua presenza.", timestamp = datetime.datetime.now(), color = discord.Colour.blue())
                    embed.set_footer(text = "Richiesto dal Maestro Supremo")
                else:
                    embed = discord.Embed(title = "Cane con Anguria sul Capo", description = f"**Autore:** {theredheat.mention}\n**Tecnica:** Olio su Discord\n**Collocazione:** Official Fortnite Italia", timestamp = datetime.datetime.now(), color = discord.Colour.green())
                    embed.set_image(url = "https://cdn.glitch.com/ce23a52c-740e-4bfd-a0b2-8e7f838de4d2%2Fimage0.jpg?v=1589229005745")
                    embed.set_footer(text = f"richiesto da {ctx.author}")
            if message.content.lower() == "mettiushyper":
                mettius = message.guild.get_member(707165674845241344)
                if ctx.author == mettius:
                    embed = discord.Embed(title = "Error 404: qualcosa non va...", description = "O mio supremo maestro!\nCi inchineremo tutti alla sua presenza.", timestamp = datetime.datetime.now(), color = discord.Colour.orange())
                    embed.set_footer(text = "Richiesto dal Maestro Supremo")
                else:
                    embed = discord.Embed(title = "La Meraviglia", description = f"**Autore:** {mettius.mention}\n**Stile:** Dolce Stil Veneto\n**Collocazione:** Official Fortnite Italia", timestamp = datetime.datetime.now(), color = discord.Colour.blue())
                    embed.set_image(url = "https://cdn.glitch.com/ce23a52c-740e-4bfd-a0b2-8e7f838de4d2%2F7bed4Gr.png?v=1589286696419")
                    embed.set_footer(text = f"richiesto da {ctx.author}")
            if embed != None:
                await message.delete()
                await ctx.send(embed = embed)
