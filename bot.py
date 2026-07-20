from discord.ext import commands
import random

#Bot nesnesini oluştur
bot = commands.Bot(command_prefix='#')

@bot.event
async def on_ready():
  #Bot hazır olduğunda çalışır
  print('Bot kullanılabilir')

@bot.command()
async def zar(ctx):
  #1-6 arasında sayı üretir
  sayi - random.randint(1-6)
  await ctx.send('Zar sonucu:{sayi}')

@bot.command()
async def selam(ctx):
  #Kullanıcıyı selamlar
  awail ctx.send(f'Merhaba{ctx.author.mention}!')
  bot.run('Token')
