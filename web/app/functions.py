import requests


def get_information(current_city):
    args = {}
    MY_KEY = '5d0b20589fbca89baab98af383e6858a'
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&APPID={}'.format(current_city, MY_KEY)
    response = requests.get(url).json()
    
    args['is_error'] = False
    if response.get('cod') != 200:
        message = response.get('message', '')
        args['is_error'] = True
        args['error'] = 'Error getting weather foreast for {}, {}'.format(current_city.title(), message)
        return args
    args['name'] = current_city.title()
    args['pressure'] = response.get('main', {}).get('pressure')
    args['temperature'] = round(response.get('main', {}).get('temp') - 273.15, 2)
    args['humidity'] = response.get('main', {}).get('humidity')
    if not args['temperature']:
        args['is_error'] = True
        args['error'] = 'Error getting weather forecast for {}'.format(current_city.title())
    return args
