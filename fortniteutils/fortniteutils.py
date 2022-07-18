import re
import dislash
import discord
import fortnite_api

from redbot.core import Config, commands
from redbot.core.bot import Red
from dislash import *


def getNick(nick:str):
  form_nick = re.sub(r'\s+\[⚡\d+\]', '', nick)
  if form_nick:
    return form_nick
  else:
    return None

# Setup
max_level = 138
allowed_channel = 702576186185875546
fn_api_icon = "https://fortnite-api.com/assets/img/logo_small.png"


BaseCog = getattr(commands, "Cog", object)
 
class FortniteUtils(BaseCog):
  
  def __init__(self, bot, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.bot = bot
    self.fn_api = fortnite_api.FortniteAPI(api_key=((await bot.get_shared_api_tokens('FortniteAPI'))['api_key']), run_async=True)

  def cog_unload(self):
    self.bot.slash.teardown()
    

  #---------------------------# PowerLevel #---------------------------# 
  
  @dislash.guild_only()
  @slash_command(description="Gestisce il livello di Potenza STW all'interno del server")
  async def powerlevel(self, inter):
      pass
    
  @powerlevel.sub_command(
    description="Aggiunge il livello di Potenza STW al proprio nickname",
    options=[
        Option("level", "Inserisci il livello di Potenza STW", OptionType.INTEGER, required=True)
    ]
  )
  async def set(self, inter, level=None):
    if int(inter.channel.id) != int(allowed_channel):
      return await inter.reply(f"🤐 Spostati in <#{allowed_channel}> per usare questo comando!", ephemeral=True)
    # Vars
    index = int(level)
    member = inter.guild.get_member(inter.author.id)
    # Level Check
    if index < 1 or index > max_level:
      return await inter.reply(f"😕 Ops... qualcosa è andato storto: **livello non valido**!", ephemeral=True)
    # New Nickname
    new_nick = getNick(inter.author.display_name) + " [⚡" + str(index) + "]"
    if len(new_nick) > 32:
      return await inter.reply(f"😕 Ops... qualcosa è andato storto: **massimo dei caratteri superato**!", ephemeral=True)
    # Set Nickname
    try:
      await member.edit(nick=new_nick)
    except:
      return await inter.reply(f"😕 Ops... qualcosa è andato storto: **permessi insufficienti**!", ephemeral=True)
    await inter.reply(f"👉 Ho **aggiunto** il livello al tuo nickname!", ephemeral=True)
  
  @powerlevel.sub_command(description="Rimuove il livello di Potenza STW dal proprio nickname")
  async def reset(self, inter):
    if int(inter.channel.id) != int(allowed_channel):
      return await inter.reply(f"🤐 Spostati in <#{allowed_channel}> per usare questo comando!", ephemeral=True)
    member = inter.guild.get_member(inter.author.id)
    # New Nickname
    original_nick = getNick(inter.author.display_name)
    if original_nick is inter.author.display_name:
      return await inter.reply(f"😕 Sembra che non ci sia **nessun livello** nel tuo nickname!", ephemeral=True)
    # Reset Nickname
    try:
      await member.edit(nick=original_nick)
    except:
      return await inter.reply(f"😕 Ops... qualcosa è andato storto: **permessi insufficienti**!", ephemeral=True)
    await inter.reply(f"🙃 Ho **rimosso** il livello dal tuo nickname!", ephemeral=True)
    
    
  #---------------------------# Fortnite Map #---------------------------# 

  @dislash.guild_only()
  @slash_command(
    description="Restituisce la mappa attuale di Fortnite Battaglia Reale",
    options=[
        Option("pois", "Aggiunge o rimuove i punti di interesse sulla mappa", OptionType.BOOLEAN, required=False)
    ]
  )
  async def map(self, inter, pois=None):
    pois = pois or True
    if int(inter.channel.id) != int(allowed_channel):
      return await inter.reply(f"🤐 Spostati in <#{allowed_channel}> per usare questo comando!", ephemeral=True)
    # Getting Data
    try:
      map = await self.fn_api.map.fetch(language="it")
    except:
      return await inter.reply(f"😕 Ops... qualcosa è andato storto!", ephemeral=True)
    # Map URL
    if pois is True:
      url = map.data.images.pois
    else:
      url = map.data.images.blank
    if url is None:
      return await inter.reply(f"😕 Ops... qualcosa è andato storto!", ephemeral=True)
    # Response
    embed = discord.Embed(timestamp = datetime.datetime.utcnow())
    embed.set_image(url=url)
    embed.set_footer(text="Creato con ❤️ · Fortnite IT", icon_url=fn_api_icon)
    await inter.reply(embed=embed, ephemeral=False)
