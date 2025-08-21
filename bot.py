import discord
from discord.ext import commands
from config import token

# Car sınıfı - son ödevden
class Car:
    def __init__(self, color, brand, year=2025):
        self.color = color
        self.brand = brand
        self.year = year

    def info(self):
        return f"🚘 {self.year} model {self.color} renkli {self.brand}!"

# Bot ayarları
intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix='/', intents=intents)

@client.event
async def on_ready():
    print(f'Giriş yaptı:  {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(client.command_prefix):
        await client.process_commands(message)
    else:
        await message.channel.send(message.content)

@client.command()
async def about(ctx):
    await ctx.send('Bu discord.py kütüphanesi ile oluşturulmuş echo-bot!')

# Yeni handler: /car renk marka
@client.command()
async def car(ctx, color: str, brand: str):
    new_car = Car(color, brand)   # sınıf örneği oluştur
    await ctx.send(new_car.info())  # metod sonucunu kanala gönder

client.run(token)
