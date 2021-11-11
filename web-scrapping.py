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

yaris = "https://www.autoscout24.fr/lst/toyota/yaris/60311-innenstadt-(frankfurt-am-main)?sort=standard&desc=0&offer=D%2CJ%2CO%2CU&fuel=2&ustate=N%2CU&size=20&page=1&lon=8.6790758&lat=50.1129&zip=60311%20Innenstadt%20(Frankfurt%20am%20Main)&zipr=50&cy=D&priceto=15000&fregfrom=2016&atype=C&fc=6&qry=&"
peugeot = "https://www.autoscout24.fr/lst/peugeot/208/60311-innenstadt-(frankfurt-am-main)?sort=standard&desc=0&offer=D%2CJ%2CO%2CU&ustate=N%2CU&size=20&page=1&lon=8.6790758&lat=50.1129&zip=60311%20Innenstadt%20(Frankfurt%20am%20Main)&zipr=50&cy=D&priceto=12500&kmto=90000&fregfrom=2017&atype=C&fc=3&qry=&"
clio = "https://www.autoscout24.fr/lst/renault/clio/60311-innenstadt-(frankfurt-am-main)?sort=standard&desc=0&offer=D%2CJ%2CO%2CU&fuel=D&ustate=N%2CU&size=20&page=1&lon=8.6790758&lat=50.1129&zip=60311%20Innenstadt%20(Frankfurt%20am%20Main)&zipr=150&cy=D&priceto=12500&kmto=100000&fregfrom=2015&atype=C&fc=31&qry=&"
ds3 = ""
polo = "https://www.autoscout24.fr/lst/volkswagen/polo-(tous)/60311-innenstadt-(frankfurt-am-main)?sort=standard&desc=0&offer=D%2CJ%2CO%2CU&fuel=D&ustate=N%2CU&size=20&page=1&lon=8.6790758&lat=50.1129&zip=60311%20Innenstadt%20(Frankfurt%20am%20Main)&zipr=150&cy=D&priceto=12500&kmto=100000&fregfrom=2015&atype=C&fc=27&qry=&"

HTML_TEXT = requests.get(peugeot).text
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

    # print(f'the car offer :\n{link} has {km}, \nmodele {year} with {hp} -- PRICE -- {price.strip()}  ')
    # "€ 9 699,-"" to "9 699"
    Only_digit = re.findall(r'\d+', price)
    price_digit = ' '.join(Only_digit)

    # Adding values to a dictionanary 
    NUM = NUM + 1
    DICT[NUM] = [link, {'Km':km, 'Year':year, 'HP':hp, 'Price':price_digit}]

# print(DICT)

# Saving a dictionnary to csv file
csv_file = "cars.csv"
csv_columns = ['link', 'No', 'Km', 'Year', 'HP', 'Price']

def data_to_csv(dict: DICT):
    try:
        with open(csv_file, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            writer.writeheader()
            for key in DICT:
                writer.writerow({'link':DICT[key][0],'No':key})
                print(DICT[key][1])
            
    except IOError:
        print("I/O error")

data_to_csv(DICT)
