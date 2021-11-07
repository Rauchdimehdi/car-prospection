# # TODO:
#     - Scrap link from website : autoscout ..
#     - Dssiplay the data using graphs 
# # FIXME:
    # - Leboncoin block request


from bs4 import BeautifulSoup
import requests
import urllib3
import re

url = "https://www.autoscout24.fr/lst/toyota/yaris/60311-innenstadt-(frankfurt-am-main)?sort=standard&desc=0&offer=D%2CJ%2CO%2CU&fuel=2&ustate=N%2CU&size=20&page=1&lon=8.6790758&lat=50.1129&zip=60311%20Innenstadt%20(Frankfurt%20am%20Main)&zipr=50&cy=D&priceto=15000&fregfrom=2016&atype=C&fc=6&qry=&"

html_text = requests.get(url).text
soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find_all("div", class_="cl-list-element cl-list-element-gap")
for job in jobs:
    price = job.find('div', class_='cldt-summary-payment').text
    car_details = job.find('div', class_='cldt-summary-vehicle-data').text
    info = job.ul.find_all('li')
    info_list = [str(li) for li in info]
    km = info_list[0].splitlines()[1]
    year = info_list[1].splitlines()[1]
    hp = info_list[2].splitlines()[1]
    print(f'the car has {km}, modele {year} with {hp} -- PRICE -- {price.strip()}  ')

