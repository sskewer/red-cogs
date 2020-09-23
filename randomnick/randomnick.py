import asyncio
import random

from contextlib import suppress
import discord
from redbot.core import commands

randomArray = ["Pescesecco", "Aura", "Cuorenero", "Ibrido", "Bananita", "Lusso", "Trog", "Calzamaglia", "Yonder", "Fiaba", "Belladonna", "Cacciatrice", "Alla Deriva", "Linea Rossa", "Soccorso in Corsa", "Mazza", "Ragnarok", "Carburo", "Teknica", "Zoey", "Valore", "Omega", "Visitatore", "Specialista di Missioni", "Signore della Ruggine", "Camminatore Lunare", "Viaggiatore Oscuro", "Agente Élite", "Mietitore", "Cavaliere Blu", "Cavaliere Reale", "Cavaliere Nero", "Milite Assalto Aereo", "Incursore Rinnegato", "Coniglio Mastino", "Coniglio Incursore", "Segugio da Guerra", "Trifoglio Verde", "Wukong", "Difensore Scarlatto", "Ranger dell’Amore", "Schiaccianoci", "Saccheggiatore Felice", "Artigliere allo Zenzero", "Milite Ghoul", "Agente Ribelle", "Percussore Sommitale", "Asso", "Bombardiere Reale", "Percussore Blu", "Havoc", "Pioniere", "Subcomandante", "Galassia", "Doppia Elica", "Frostbite", "Riflesso"];

BaseCog = getattr(commands, "Cog", object)

class RandomNick(BaseCog):
    """Pick a random nickname and set it for the user"""
    def __init__(self, bot):
        self.bot = bot

    @commands.guild_only()
    @commands.command(aliases=["random"])
    @commands.has_permissions(manage_nicknames=True)
    async def randomnick(self, ctx: Context, user: discord.Member):
        randomnick = random.choice(randomArray)
        try:
            await user.edit(nick=randomnick)
            await ctx.send(f":crayon: Il nuovo nome generato casualmente per **{user.name}** è **{randomnick}**.")
        except:
            await ctx.send(f":crayon: Non riesco a generare casualmente un soprannome per **{user.name}**.")
