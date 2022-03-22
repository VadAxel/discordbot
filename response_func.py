
#request jämförs mot möjliga efterfrågningar, om efterfrågan inte överenstämmer ges N/A.
async def response_func(message, term_list, request_list, jsonData_response):
    for i in range(len(request_list)-2):
        if request_list[i+2] not in term_list:
            dash_chars = na_dash_func(request_list, i)
            await message.channel.send(request_list[i+2] + ': N/A' + '\n' + dash_chars)
        else:
            response = jsonData_response[request_list[i+2]]
            dash_chars = dash_func(request_list, i, response)
            await message.channel.send(request_list[i+2] + ': ' + response + '\n' + dash_chars)

#genererar '-' baserat på längden av genererat svar då svaret inte erhålls av termlistan.
def na_dash_func(request_list, i):
    dash_chars = len(request_list[i]) * '----'
    if len(dash_chars) > 200:
        dash_chars = 200 * '-'
    return dash_chars

#genererar '-' baserat på längden av genererat svar.
def dash_func(request_list, i, response):
    dash_chars = len(response) * '--' + len(request_list[i]) * '--'
    if len(dash_chars) > 200:
        dash_chars = 200 * '-'
    return dash_chars
