#user request delas upp i en lista, [1] i lista läggs in i URL för API, resterande skickas vidare. 
def url_func(request):
    request_list = list(request.split(' '))
    url = ('https://www.alphavantage.co/query?function=OVERVIEW&symbol=' + request_list[1] + '&apikey=L54G7GZI4H7CLIAC')
    return request_list,url