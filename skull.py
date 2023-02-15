import discord, os, random
from discord.ext import commands
from datetime import datetime

with open(".token", 'r') as f: token = str(f.readline())

bot = commands.Bot(intents=discord.Intents.all(), description="Coded by DeadSkajp#5906", help_command=None)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

@bot.event
async def on_ready(): clear(); await bot.change_presence(status=discord.Status.online, activity=discord.Game("by DeadSkajp#5906")); print(f'\n\n|> {bot.user}({bot.user.id}) is now running!\n|> Use "/skull"')

@bot.slash_command(name="skull", description="💀")
async def ip(interaction: discord.Interaction):
    skulllist = ['https://media.tenor.com/aTljWQ18YeUAAAAd/rotating-skull.gif', 'https://media.tenor.com/epwlmzlBnAUAAAAC/skull.gif', 'https://media.tenor.com/ieXO0Ui-EoMAAAAC/skull-explode.gif', 'https://media.tenor.com/XmEgf6XjPRQAAAAd/skull.gif', 'https://media.tenor.com/g1bZgt4-tL4AAAAC/skull.gif', 'https://media.tenor.com/7_ZjV-cIL9YAAAAd/skull-grin.gif']
    selgif = random.randrange(len(skulllist))
    embed = discord.Embed(title="💀", timestamp=datetime.utcnow()).set_image(url=skulllist[selgif]).set_footer(text="By DeadSkajp#5906")
    await interaction.response.send_message(embed=embed, ephemeral=True)

bot.run(token)