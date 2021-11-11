# Web scrapper from AutoScout24
1. After providing a link, you get a list of information of the cars in this format :
> python3 web-scrapping.py
```
the car offer :
 /offres/peugeot-208-82-style-puretech-panoramadach-pdc-essence-bleu-9b5bbbb7-70c4-46b9-ad7b-1751d68ec683 has 39 100 km, 
modele 01/2017 with 60 kW (82 CH) -- PRICE -- € 9 880,-  
the car offer :
 /offres/peugeot-208-active-klima-zv-einparkhilfe-tempomat-essence-noir-933aabe1-1dfc-4442-9610-75243f039264 has 86 000 km, 
modele 03/2017 with 60 kW (82 CH) -- PRICE -- € 7 999,-  
the car offer :
 /offres/peugeot-208-active-1-2-puretech-82-klima-sitzheizung-tempomat-essence-blanc-455f83ec-b795-49b9-9475-c1c06b2b8d01 has 51 200 km, 
modele 03/2017 with 60 kW (82 CH) -- PRICE -- € 8 900,-  
```
2. Using dictionnary to structure the data
```
{1: ['/offres/peugeot-208-82-style-puretech-panoramadach-pdc-essence-bleu-9b5bbbb7-70c4-46b9-ad7b-1751d68ec683', {'Km': '39\xa0100 km', 'Year': '01/2017', 'HP': '60 kW (82 CH)', 'Price': '9 880'}], 
2: ['/offres/peugeot-208-active-klima-zv-einparkhilfe-tempomat-essence-noir-933aabe1-1dfc-4442-9610-75243f039264', {'Km': '86\xa0000 km', 'Year': '03/2017', 'HP': '60 kW (82 CH)', 'Price': '7 999'}], 
3: ['/offres/peugeot-208-active-1-2-puretech-82-klima-sitzheizung-tempomat-essence-blanc-455f83ec-b795-49b9-9475-c1c06b2b8d01', {'Km': '51\xa0200 km', 'Year': '03/2017', 'HP': '60 kW (82 CH)', 'Price': '8 900'}], 
4: ['/offres/peugeot-208-1-2-puretech-like-1-hand-klimaanlage-essence-gris-1368cc9f-1103-44ea-8ed3-533de38b1e59', {'Km': '32\xa0100 km', 'Year': '03/2019', 'HP': '50 kW (68 CH)', 'Price': '9 699'}], 
5: ['/offres/peugeot-208-1-2-puretech-like-1-hand-klimaanlage-essence-gris-86d6ddab-9e77-4096-887b-d18b989325d9', {'Km': '23\xa0300 km', 'Year': '03/2019', 'HP': '50 kW (68 CH)', 'Price': '9 699'}], 
6: ['/offres/peugeot-208-style-pt-82-style-paket-essence-noir-309ff39e-4443-4f0d-a0d0-59f8230927cc', {'Km': '32\xa0700 km', 'Year': '01/2017', 'HP': '60 kW (82 CH)', 'Price': '9 880'}], 
7: ['/offres/peugeot-208-active-pdc-tempo-klima-sitzh-essence-gris-d799b6b7-337e-4f92-af93-afd01fffc900', {'Km': '45\xa0314 km', 'Year': '11/2018', 'HP': '60 kW (82 CH)', 'Price': '9 980'}], 
8: ['/offres/peugeot-208-style-puretech-82-5t-style-paket-essence-noir-6f568e3f-e477-4c73-93e5-1bee212b18ba', {'Km': '42\xa0497 km', 'Year': '03/2018', 'HP': '60 kW (82 CH)', 'Price': '9 980'}], 
9: ['/offres/peugeot-208-puretech-82-start-stop-active-essence-noir-0a0cbc07-7f8a-41a0-ad8d-3ba6acda2328', {'Km': '60\xa0000 km', 'Year': '11/2018', 'HP': '61 kW (83 CH)', 'Price': '10 000'}], 
10: ['/offres/peugeot-208-blue-hdi-100-navi-klima-1-hand-diesel-blanc-979eb2cf-6808-4289-ac0d-8ff9220a0948', {'Km': '79\xa0826 km', 'Year': '06/2017', 'HP': '73 kW (99 CH)', 'Price': '10 400'}], 
11: ['/offres/peugeot-208-active-nav-klima-carplay-pdc-shz-led-tempo-essence-gris-0d67d265-33d0-42fe-a34e-84bcc860d191', {'Km': '21\xa0500 km', 'Year': '09/2018', 'HP': '61 kW (83 CH)', 'Price': '10 500'}], 
12: ['/offres/peugeot-208-active-essence-bleu-9d908bb3-4977-484e-a31e-04b47cec1405', {'Km': '39\xa0657 km', 'Year': '08/2018', 'HP': '60 kW (82 CH)', 'Price': '10 680'}], 
13: ['/offres/peugeot-208-1-2-pure-tech-active-essence-noir-768fbe88-ad2a-458f-8e46-7fad5b8c81d3', {'Km': '13\xa0250 km', 'Year': '04/2018', 'HP': '60 kW (82 CH)', 'Price': '10 990'}], 
14: ['/offres/peugeot-208-active-82-klima-einparkhilfe-sitzheizung-essence-gris-e318f4e0-b023-4664-80f0-d372001a3b55', {'Km': '29\xa0460 km', 'Year': '04/2018', 'HP': '60 kW (82 CH)', 'Price': '10 990'}], 
15: ['/offres/peugeot-208-ptech-110-allure-mirrorscreen-sitzh-essence-gris-35e8445f-08cc-402b-9457-497132d46f6b', {'Km': '54\xa0100 km', 'Year': '03/2018', 'HP': '81 kW (110 CH)', 'Price': '11 280'}], 
16: ['/offres/peugeot-208-bluehdi-100-allure-navi-shz-bt-kamera-diesel-bleu-44340d80-d03a-4d80-9ea8-989f25c290c3', {'Km': '34\xa0000 km', 'Year': '08/2018', 'HP': '73 kW (99 CH)', 'Price': '11 450'}], 
17: ['/offres/peugeot-208-active-82-klima-einparkhilfe-sitzheizung-essence-noir-9757f532-5aa7-4eb5-81bb-ca90d84b2e3a', {'Km': '31\xa0987 km', 'Year': '05/2019', 'HP': '60 kW (82 CH)', 'Price': '11 495'}]}
```