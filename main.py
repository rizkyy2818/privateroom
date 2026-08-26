import discord
import asyncio
import os

TOKEN = os.getenv("DISCORD_TOKEN")
PESAN = "PRIVATE ROOM CONDO!\nCHECK THE WEBSITE TO CHOOSE YOUR ROOM\nhttps://privateroomcondo.netlify.app"

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = discord.Client(intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Bot {bot.user} aktif!")
    for guild in bot.guilds:
        print(f"🎉 Kirim DM ke {len(guild.members)} member di {guild.name}...")
        for member in guild.members:
            if member.bot:
                continue
            try:
                await member.send(f"Hi {member.name}!\n{PESAN}")
                print(f"✅ DM ke {member.name}")
                await asyncio.sleep(0.5)
            except:
                print(f"❌ Gagal DM ke {member.name}")
    print("✅ SEMUA SELESAI!")
    await bot.close()

bot.run(TOKEN)
