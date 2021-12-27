# # TODO:
#     - send email
# # FIXME:
    # - 


from bs4 import BeautifulSoup
import requests
import urllib3
import re
import csv
import sys

DICT_CARS = {
    "yaris":"https://www.autoscout24.fr/lst/toyota/yaris/60311-innenstadt-(frankfurt-am-main)?sort=standard&desc=0&offer=D%2CJ%2CO%2CU&fuel=2&ustate=N%2CU&size=20&page=1&lon=8.6790758&lat=50.1129&zip=60311%20Innenstadt%20(Frankfurt%20am%20Main)&zipr=100&cy=D&priceto=12500&kmto=90000&fregfrom=2016&atype=C&fc=14&qry=&",
    "peugeot_diesel":"https://www.autoscout24.fr/lst/peugeot/208/60311-innenstadt-(frankfurt-am-main)?sort=standard&desc=0&offer=D%2CJ%2CO%2CU&fuel=D&ustate=N%2CU&size=20&page=1&lon=8.6790758&lat=50.1129&zip=60311%20Innenstadt%20(Frankfurt%20am%20Main)&zipr=100&cy=D&priceto=12500&kmto=90000&fregfrom=2015&atype=C&fc=18&qry=&",
    "clio":"https://www.autoscout24.fr/lst/renault/clio/60311-innenstadt-(frankfurt-am-main)?sort=standard&desc=0&offer=D%2CJ%2CO%2CU&fuel=D&ustate=N%2CU&size=20&page=1&lon=8.6790758&lat=50.1129&zip=60311%20Innenstadt%20(Frankfurt%20am%20Main)&zipr=100&cy=D&priceto=12500&kmto=90000&fregfrom=2015&atype=C&fc=34&qry=&",
    "polo_diesel":"https://www.autoscout24.fr/lst/volkswagen/polo-(tous)/60311-innenstadt-(frankfurt-am-main)?sort=standard&desc=0&offer=D%2CJ%2CO%2CU&fuel=D&ustate=N%2CU&size=20&page=1&lon=8.6790758&lat=50.1129&zip=60311%20Innenstadt%20(Frankfurt%20am%20Main)&zipr=100&cy=D&priceto=12500&kmto=80000&fregfrom=2015&atype=C&fc=33&qry=&",
    "polo_essence":"https://www.autoscout24.fr/lst/volkswagen/polo-(tous)/60311-innenstadt-(frankfurt-am-main)?sort=standard&desc=0&offer=D%2CJ%2CO%2CU&fuel=B&ustate=N%2CU&size=20&page=1&lon=8.6790758&lat=50.1129&zip=60311%20Innenstadt%20(Frankfurt%20am%20Main)&zipr=100&cy=D&priceto=12500&kmto=80000&fregfrom=2015&atype=C&fc=35&qry=&",
    "peugeot_essence":"https://www.autoscout24.fr/lst/peugeot/208/60311-innenstadt-(frankfurt-am-main)?sort=standard&desc=0&offer=D%2CJ%2CO%2CU&fuel=B&ustate=N%2CU&size=20&page=1&lon=8.6790758&lat=50.1129&zip=60311%20Innenstadt%20(Frankfurt%20am%20Main)&zipr=100&cy=D&priceto=12500&kmto=90000&fregfrom=2015&atype=C&fc=20&qry=&",
}
CARS_NUM = {'yaris': '2', 'peugeot_diesel': '4', 'clio': '16', 'polo_diesel': '5', 'polo_essence': '54', 'peugeot_essence': '51'}
SEND_EMAIL = False
CARS_LIST = []

def search_cars(dict_car):
    for car in dict_car:
        CAR_NAME = dict_car[car]
        HTML_TEXT = requests.get(CAR_NAME).text
        soup = BeautifulSoup(HTML_TEXT, 'lxml')

        # 2 Offres
        car_available = soup.find('span', class_="sc-font-bold cl-filters-summary-counter").text
        car_available_num = only_num(car_available)

        if CARS_NUM[car] < car_available_num : 
            SEND_EMAIL = True
            # Add cars number available 
            CARS_LIST.append(car)
            CARS_NUM[car] = car_available_num

    print(CARS_NUM)
    # Send the email 
    # send_email(SEND_EMAIL, CARS_LIST)
    
def only_num(value):
    # "2 Offres" to "2"
    Only_digit = re.findall(r'\d+', value)
    value_in_digit = ' '.join(Only_digit)

    return value_in_digit

# def send_email(send, cars_list):
#     if send:
#         return 0

        
search_cars(DICT_CARS)

