import json
import requests
import discord
import os


client = discord.Client()
 
@client.event
async def on_ready():
   print('We have logged in as {0.user}'.format(client))


# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key




@client.event
async def on_message(message):
   if message.author == client.user:
       return
 
   if message.content.startswith('jinping!'):
       await message.channel.send('亲爱的同志，你的 ping 是t')
       
   elif message.content.startswith('stockbock!'):
       url = 'https://www.alphavantage.co/query?function=OVERVIEW&symbol=IBM&apikey=L54G7GZI4H7CLIAC'
       r = requests.get(url)
       data = r.json()
       await message.channel.send(data)
   elif 'vad hände på himmelska fridens torg' in message.content:
       await message.channel.send('我拥护中华人民共和国, 没有什么')
   #elif 'Vad är meningen med livet?' in message.content:
       #await message.channel.send('我拥wekf中华人民共和国,四十二')

client.run('OTM4MDI0MDIyMDE1MzczMzcy.YfkQ8g.gZLTwqVq2oiVQd-zEkWaFNHq1HA')
