import discord
import os
from dotenv import load_dotenv
load_dotenv()

from discord.ext import commands



print("lancement du bot")
bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("Le bot est allumé !")
    #synchonisation des commandes
    try:
        synced = await bot.tree.sync()
        print(f"Commandes slash synchronisées : {len(synced)}")
    except Exception as e:
        print(e)

@bot.event
async def on_message(message: discord.Message):
    if message.author.bot:
        return
    if message.content.lower() == "bonjour":
        channel = message.channel
        await channel.send("Bonjour ! Comment ça va ?")
    if message.content.lower() == "bienvenue":
        suivi_channel = bot.get_channel(1331184527208484884)
        await suivi_channel.send(f"Bienvenue {message.author.mention} ! N'oublie pas de lire les règles et de te présenter !")

@bot.tree.command(name="karim", description="TANA!")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message("TANA!")

@bot.tree.command(name="warn", description="Met un warn a un utilisateur")
async def warn(interaction: discord.Interaction, user: discord.Member, *, reason: str = "Aucune raison fournie"):
    if interaction.user.guild_permissions.manage_messages:
        embed = discord.Embed(title="Avertissement", description=f"{user.mention} a été averti.", color=discord.Color.red())
        embed.add_field(name="Raison", value=reason, inline=False)
        await interaction.response.send_message(embed=embed)
        await user.send(f"Vous avez été averti dans le serveur {interaction.guild.name} pour la raison suivante : {reason}")
    else:
        await interaction.response.send_message("Vous n'avez pas la permission de gérer les messages.", ephemeral=True)

@bot.tree.command(name="ban", description="Banni un utilisateur")
async def ban(interaction: discord.Interaction, user: discord.Member, *, reason: str = "Aucune raison fournie"):
    if interaction.user.guild_permissions.ban_members:
        await user.ban(reason=reason)
        embed = discord.Embed(title="Bannissement", description=f"{user.mention} a été banni.", color=discord.Color.red())
        embed.add_field(name="Raison", value=reason, inline=False)
        await interaction.response.send_message(embed=embed)
    else:
        await interaction.response.send_message("Vous n'avez pas la permission de bannir des membres.", ephemeral=True)

@bot.tree.command(name="kick", description="Expulse un utilisateur")
async def kick(interaction: discord.Interaction, user: discord.Member, *, reason: str = "Aucune raison fournie"):
    if interaction.user.guild_permissions.kick_members:
        await user.kick(reason=reason)
        embed = discord.Embed(title="Expulsion", description=f"{user.mention} a été expulsé.", color=discord.Color.red())
        embed.add_field(name="Raison", value=reason, inline=False)
        await interaction.response.send_message(embed=embed)
    else:
        await interaction.response.send_message("Vous n'avez pas la permission d'expulser des membres.", ephemeral=True)

@bot.tree.command(name="test", description="Test des embeds")
async def test(interaction: discord.Interaction):
    embed = discord.Embed(title="Test d'Embed", description="Ceci est un test d'embed.", color=discord.Color.blue())
    embed.add_field(name="Apprendre a faire un embeds", value="Ceci est le contenu du champ 1", inline=False)
    embed.add_field(name="Champ 2", value="Ceci est le contenu du champ 2.", inline=False)
    await interaction.response.send_message(embed=embed)





bot.run(os.getenv("DISCORD_TOKEN"))

