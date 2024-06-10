import nextcord
from nextcord.ext import commands
import os
from dotenv import load_dotenv
import logging
load_dotenv()

logging.basicConfig(level=logging.INFO)

TESTING_GUILD_ID = 978006345619996722


logger = logging.getLogger('nextcord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='nextcord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

bot = commands.Bot()

@bot.event

async def on_ready():
   print(f'WE have logged in as {bot.user}')

@bot.slash_command(description='My first Slash command', guild_ids=[TESTING_GUILD_ID])
async def hello(interaction: nextcord.Interaction):
    await interaction.send("Hello!")

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
bot.run(DISCORD_TOKEN)