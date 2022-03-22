import discord
import PySimpleGUI as sg

#importerar funktioner från filer
from data_API_func import data_API_func
from url_func import url_func
from response_func import response_func
from term_list import term_list

client = discord.Client()

#meddelande om inloggning terminal.
@client.event
async def on_ready():
   print('We have logged in as {0.user}'.format(client))

#bekräftar uppkoppling mot discord (termial)
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    #kollar tillkallelse av bot anropar bot_summon_func.
    if 'stockbot!' in message.content:
        await bot_summon_func(message)

        #slutmeddelande "Over and out!" genererat i Brainf*ck. Markerar slutet på output.
        await message.channel.send('++++++++++[>+>+++>+++++++>++++++++++<<<<-]>>>+++++++++.>++++++++++++++++++.-----------------.+++++++++++++.<<++.>>-----------------.+++++++++++++.----------.<<.>>+++++++++++.++++++.-.<<+.')
    
    #--help - kommando för att ge syntax
    elif message.content.startswith('stockhelp!'):
        await message.channel.send('Syntax: Företagssymbol Informationsterm Informationsterm Informationsterm ...' + '\n\n' + 'Informationstermer: \nAssetType \nName \nDescription \nExchange \nCurrency \nCountry \nSector \nIndustry \nPEGRatio \nPERatio \nReturnOnEquityTTM \nPriceToSalesRatioTTM \n52WeekHigh \n52WeekLow \n50DayMovingAverage')

#hanterar input och anropar url_func, data_API_func samt response_func.
async def bot_summon_func(message):
    request = message.content
    request_list, url = url_func(request)
    jsonData_response = data_API_func(url)
    await response_func(message, term_list, request_list, jsonData_response)
    
#personlig bot-nyckel.
client.run('OTM4MDI0MDIyMDE1MzczMzcy.YfkQ8g.gZLTwqVq2oiVQd-zEkWaFNHq1HA')

