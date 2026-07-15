import os
import disnake
from disnake.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

intents = disnake.Intents.default()
intents.message_content = True

bot = commands.Bot(
    command_prefix="!", 
    intents=intents,
    activity=disnake.Activity(type=disnake.ActivityType.watching, name="nekos time! | /help"),
    status=disnake.Status.online
)

for filename in os.listdir("./cogs"):
    if filename.endswith(".py") and not filename.startswith("__"):
        try:
            bot.load_extension(f"cogs.{filename[:-3]}")
            print(f"✅ Успешно импортирован модуль: {filename}")
        except Exception as e:
            print(f"❌ Ошибка при загрузке модуля {filename}:")
            print(e)

@bot.event
async def on_ready():
    print(f'Login successful as {bot.user.name} ({bot.user.id})')
    print('--- LOG STARTING ---')

bot.run(TOKEN)