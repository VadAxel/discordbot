from data_API_func import data_API_func
from url_func import url_func
from response_func import response_func
from term_list import term_list
#hanterar input och anropar url_func, data_API_func samt response_func.
async def bot_summon_func(message):
    request = message.content
    request_list, url = url_func(request)
    jsonData_response = data_API_func(url)
    await response_func(message, term_list, request_list, jsonData_response)
