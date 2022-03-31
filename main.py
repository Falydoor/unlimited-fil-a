import browser_cookie3
import requests
import os
import logging
from bs4 import BeautifulSoup

logging.basicConfig(level=logging.INFO)
order_date = '03/30/2022'
order_number = 1
restaurant_number = '04161'
match_count = 0

# Set manual cookies here
asp_net_cookie = ''
crn_token = ''

# Use manual cookies or Chrome cookies if empty
if asp_net_cookie and crn_token:
    logging.info('Manual cookie')
    cookies = {
        '.AspNet.Cookies': asp_net_cookie,
        'Crn.TokenInformation': crn_token}
else:
    logging.info('Chrome cookie')
    cookie_jar = browser_cookie3.chrome(
        cookie_file=f"{os.getenv('HOME')}/Library/Application Support/Google/Chrome/Profile 1/Cookies",
        domain_name='.chick-fil-a.com')
    cookies = {'.AspNet.Cookies': cookie_jar._cookies['.chick-fil-a.com']['/']['.AspNet.Cookies'].value,
               'Crn.TokenInformation': cookie_jar._cookies['.chick-fil-a.com']['/']['Crn.TokenInformation'].value}

while True:
    logging.info('Checking order %i', order_number)

    # Fill form data
    data = {'RestaurantNumber': restaurant_number,
            'Date': order_date,
            'OrderNumber': order_number,
            'OrderTotal': 15.00}

    # Sends POST request and parse HTML response
    r = requests.post('https://www.chick-fil-a.com/missedtransaction', data=data, cookies=cookies)
    html = BeautifulSoup(r.text, 'html.parser')

    # with open("debug.html", "w") as f:
    #     f.write(r.text)

    if html.find_all('h3', string='Success!'):
        # Match found
        logging.info('Match found, points added!')
        match_count += 1
    elif 'missed' in html.find_all('p', attrs={'role': 'alert'})[0].text:
        # Quota reached
        logging.info('Quota reached!')
        logging.info('Matches total %i', match_count)
        break
    else:
        logging.info('No match found')

    # Increment order number
    order_number += 1
