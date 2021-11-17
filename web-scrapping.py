# # TODO:
#     - Scrap link from website : autoscout ..
#     - Display the data using graphs after saving them on a file
# # FIXME:
    # - Leboncoin block request


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

# Saving a dictionnary to csv file
csv_file = "cars.csv"
csv_columns = ['link', 'No', 'Km', 'Year', 'HP', 'Price']


def search_cars(dict_car):
    # Erasing the file content before adding cars info 
    open(csv_file, 'w').close()
    for car in dict_car:
        CAR_NAME = dict_car[car]
        HTML_TEXT = requests.get(CAR_NAME).text
        soup = BeautifulSoup(HTML_TEXT, 'lxml')
        JOBS = soup.find_all("div", class_="cl-list-element cl-list-element-gap")

        NUM = 0
        DICT = {}
        for job in JOBS:
            # Scrapping data from the web page 
            price = job.find('div', class_='cldt-summary-payment').text
            car_details = job.find('div', class_='cldt-summary-vehicle-data').text
            info = job.ul.find_all('li')
            info_list = [str(li) for li in info]
            link_extraction = job.find('div', class_='cldt-summary-titles')
            link = link_extraction.a['href']

            km = info_list[0].splitlines()[1]
            year = info_list[1].splitlines()[1]
            hp = info_list[2].splitlines()[1]

            # removing unnecessary values from Price and Km
            price_digit = only_num(price)
            km_digit = only_num(km)

            # Adding values to a dictionanary 
            NUM = NUM + 1
            DICT[NUM] = [link, km_digit, year, hp, price_digit]

        data_to_csv(DICT,car)

def data_to_csv(DICT,car_name):
    try:
        with open(csv_file, 'a') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            writer.writeheader()
            writer.writerow({'link':car_name})
            for key in DICT:
                writer.writerow({'link':DICT[key][0],'No':key, 'Km':DICT[key][1], 'Year':DICT[key][2], 'HP':DICT[key][3], 'Price':DICT[key][4]})

    except IOError:
        print("I/O error")

def only_num(value):
    # "€ 9 699,-"" to "9 699" or "10 000 km" to "10000"
    Only_digit = re.findall(r'\d+', value)
    value_in_digit = ' '.join(Only_digit)

    return value_in_digit
    
search_cars(DICT_CARS)
