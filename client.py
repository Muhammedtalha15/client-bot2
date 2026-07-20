import discord

#izinleri tanımla
intents=discord.Intents.default()
client=discord.Client(intents=intents)

@client.event
async def on_member_join(member)
#Bot giriş yaptığında çalışır
print('Bot başarıyla bağlandı')

@client.event
async def on_ready():
  #Sunucuya yeni biri katılırsa
  print(f'{member.name}sunucuya katıldı')

@client.event
async def on discommer!():
#bot bağls
print('bağlantı kesildi')
clien.run('Token')
