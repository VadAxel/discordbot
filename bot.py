import json
import discord
import urllib.request

client = discord.Client()

#lista över informationstermer som jämförs mot user request. Om de inte matchar startar 'if' satsen i response_func.
term_list = ['AssetType', 'Name', 'Description', 'Exchange', 'Currency', 'Country', 'Sector', 'Industry', 'PEGRatio', 'PERatio', 'ReturnOnEquityTTM', 'PriceToSalesRatioTTM', '52WeekHigh', '52WeekLow', '50DayMovingAverage']

#meddelande om inloggning terminal
@client.event
async def on_ready():
   print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    #kollar tillkallelse av bot och kör kod
    if 'stockbot!' in message.content:
        request = message.content
        request_list, url = url_func(request)
        jsonData_response = data_API_func(url)
        await response_func(message, term_list, request_list, jsonData_response) 

        #slutmeddelande "Over and out!" genererat i Brainf*ck. Markerar slutet på output.
        await message.channel.send('++++++++++[>+>+++>+++++++>++++++++++<<<<-]>>>+++++++++.>++++++++++++++++++.-----------------.+++++++++++++.<<++.>>-----------------.+++++++++++++.----------.<<.>>+++++++++++.++++++.-.<<+.')
    
    #--help - kommando för att ge syntax
    elif message.content.startswith('stockhelp!'):
        await message.channel.send('Syntax: Företagssymbol Informationsterm Informationsterm Informationsterm ...' + '\n\n' + 'Informationstermer: \nAssetType \nName \nDescription \nExchange \nCurrency \nCountry \nSector \nIndustry \nPEGRatio \nPERatio \nReturnOnEquityTTM \nPriceToSalesRatioTTM \n52WeekHigh \n52WeekLow \n50DayMovingAverage')
    

#API tillkallas
def data_API_func(url):
    url_response = urllib.request.urlopen(url)
    data_response = url_response.read() 
    jsonData_response = json.loads(data_response)
    return jsonData_response

#user request delas upp i en lista, [1] i lista lägs in i URL för API, resterande skickas vidare. 
def url_func(request):
    request_list = list(request.split(' '))
    url = ('https://www.alphavantage.co/query?function=OVERVIEW&symbol=' + request_list[1] + '&apikey=L54G7GZI4H7CLIAC')
    return request_list,url

#request jämförs mot möjliga efterfrågningar, om efterfrågan inte överenstämmer ges N/A.
async def response_func(message, term_list, request_list, jsonData_response):
    for i in range(len(request_list)-2):
        if request_list[i+2] not in term_list:
            await message.channel.send(request_list[i+2] + ': N/A' + '\n---------------------------------------------')
        else:
            response = jsonData_response[request_list[i+2]]
            await message.channel.send(request_list[i+2] + ': ' + response + '\n---------------------------------------------')
            #await message.channel.send(char_length_func(response))
""""
async def char_length_func(response):
    for i in range(len(response)):
        chars = []
        chars.append('-')
        i = i + 1
    return chars
"""

#personlig bot-nyckel
client.run('OTM4MDI0MDIyMDE1MzczMzcy.YfkQ8g.gZLTwqVq2oiVQd-zEkWaFNHq1HA')

