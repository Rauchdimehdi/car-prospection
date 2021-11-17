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

3. Saving data to a csv file 
```
link,No,Km,Year,HP,Price
yaris,,,,,
/offres/toyota-yaris-yaris-hybrid-1-5-vvt-i-electrique-essence-bronze-515ddcee-3454-47e1-96ce-6d26c9d2b3d0,1,22 850,03/2017,74 kW (101 CH),13 795
/offres/toyota-yaris-hybrid-1-5-vvt-i-style-electrique-essence-blanc-172606dc-f118-494f-b8f6-d49e2b3666cd,2,42 000,11/2017,55 kW (75 CH),11 700
/offres/toyota-yaris-hybrid-1-5-vvt-i-lounge-electrique-essence-noir-361f919f-1966-4bc9-8c9a-275997dbb800,3,43 000,10/2017,55 kW (75 CH),13 100
/offres/toyota-yaris-hybrid-1-5-vvt-i-electrique-essence-rouge-53f341aa-f021-4e42-8fda-66060b1db308,4,43 500,05/2017,55 kW (75 CH),13 200
/offres/toyota-yaris-hybrid-1-5-vvt-i-style-selection-electrique-essence-bleu-9571b2d4-74c0-46fd-9137-d33913ad3e84,5,35 000,10/2017,55 kW (75 CH),13 500
/offres/toyota-yaris-hybrid-1-5-vvt-i-team-deutschland-electrique-essence-blanc-ff4b0bbf-0cc3-4c8c-bf9a-f90e9ad6cada,6,34 750,09/2018,55 kW (75 CH),13 800
/offres/toyota-yaris-1-5-hybrid-bi-tone-e-cvt-electrique-essence-gris-48645ac5-c230-ab5b-e053-0100007f410b,7,43 500,08/2017,74 kW (101 CH),13 900
/offres/toyota-yaris-yaris-hybrid-1-5-vvt-i-comfort-mit-design-paket-electrique-essence-gris-2cce4383-50bd-4198-8d48-495e102f7f80,8,49 619,07/2017,74 kW (101 CH),14 260
/offres/toyota-yaris-hybrid-1-5-vvt-i-edition-s-electrique-essence-blanc-8386cb8c-bea1-4d44-b635-dc9a840d9ca6,9,19 371,06/2016,55 kW (75 CH),14 500
/offres/toyota-yaris-hybrid-1-5-vvt-i-comfort-mit-design-paket-electrique-essence-bleu-cc093008-e66a-4b47-90d1-0084c10afcb7,10,41 400,08/2018,55 kW (75 CH),14 750
/offres/toyota-yaris-yaris-hybrid-1-5-vvt-i-comfort-mit-design-paket-electrique-essence-gris-c4a2ccf3-13bf-490c-b854-d210cbe6b19c,11,40 000,11/2017,74 kW (101 CH),14 940
link,No,Km,Year,HP,Price
peugeot,,,,,
/offres/peugeot-208-blue-hdi-100-navi-klima-1-hand-diesel-blanc-979eb2cf-6808-4289-ac0d-8ff9220a0948,1,79 826,06/2017,73 kW (99 CH),10 400
/offres/peugeot-208-bluehdi-100-allure-navi-shz-bt-kamera-diesel-bleu-44340d80-d03a-4d80-9ea8-989f25c290c3,2,34 000,08/2018,73 kW (99 CH),11 450
/offres/peugeot-208-active-bluehdi-100-diesel-blanc-6e1369d9-de02-4515-ab73-e39e1eada696,3,84 300,01/2018,73 kW (99 CH),11 490
link,No,Km,Year,HP,Price
clio,,,,,
/offres/renault-clio-iv-grandtour-limited-dci-90-klima-pdc-diesel-gris-abba7c79-b919-4036-ace2-8a9b010d14b5,1,72 688,04/2018,66 kW (90 CH),9 990
/offres/renault-clio-iv-grandtour-limited-dci-90-klima-shz-diesel-gris-c1256a00-fa1e-4adc-8d83-c79a1b5ce135,2,66 451,05/2018,66 kW (90 CH),10 290
/offres/renault-clio-iv-grandtour-limited-dci-90-klima-diesel-argent-97d0f37c-3194-4d1a-9dc3-cb614c2f7094,3,46 733,04/2018,66 kW (90 CH),10 390
/offres/renault-clio-energy-dci-90-intens-diesel-blanc-1038cf3e-2ba2-43ea-ba83-b76c2082f8c1,4,47 000,01/2017,66 kW (90 CH),11 950
/offres/renault-clio-grandtour-energy-dci-110-start-stop-intens-diesel-noir-f701f679-0c22-4b93-8e66-40dc9efa0042,5,76 000,05/2017,81 kW (110 CH),11 400
/offres/renault-clio-iv-cargo-extra-diesel-gris-e680abb0-49df-452b-b4c3-b791f6b902d1,6,69 000,05/2016,55 kW (75 CH),8 650
/offres/renault-clio-energy-dci-75-life-diesel-noir-727aac31-5fd4-44d6-b500-c6fdbc80467c,7,66 000,03/2017,55 kW (75 CH),8 750
/offres/renault-clio-grandtour-dci-75-stop-navi-pdc-klima-euro-6-diesel-blanc-6e23a418-8eef-4ae3-9687-ff413fedfe80,8,72 250,12/2016,55 kW (75 CH),8 750
/offres/renault-clio-cargo-1-5-dci-klimaaut-pdc-navi-e6-2-sitz-lkw-zul-diesel-gris-fd091c7f-3cf9-4a3d-beb7-353b11e92fd0,9,43 000,12/2016,55 kW (75 CH),8 995
/offres/renault-clio-1-5-dci-klimaaut-pdc-navi-eu6-temp-2-sitze-lkw-zul-diesel-blanc-46cbae02-1283-40f2-bf1f-3820117b506e,10,49 800,11/2016,55 kW (75 CH),8 995
/offres/renault-clio-1-5-dci-cargo-2-sitze-klima-navi-euro-6-diesel-gris-f5609f22-16f3-4205-9831-99db622c2415,11,47 555,04/2017,55 kW (75 CH),9 000
/offres/renault-clio-grandtour-limited-dci-90-klima-diesel-blanc-734a1d28-afa8-4357-8a74-3937685fc990,12,46 650,01/2017,66 kW (90 CH),9 490
/offres/renault-clio-dynamique-dci-90-energy-start-stop-navi-bt-alu-diesel-noir-5aa2bb2e-1912-4183-aac6-ed5941fe0aac,13,48 200,08/2015,66 kW (90 CH),9 890
/offres/renault-clio-energy-dci-90-edc-limited-navi-pdc-klima-diesel-blanc-cf403fcc-6141-4cf9-91f0-c07dfd670003,14,71 200,02/2018,66 kW (90 CH),9 990
/offres/renault-clio-intens-iv-grandtour-diesel-gris-330cbc60-669b-4e56-8c53-2c764774e2af,15,73 000,10/2016,81 kW (110 CH),10 000
/offres/renault-clio-iv-grandtour-limited-dci-90-navi-klima-diesel-argent-ac9940e6-c13a-485e-9bac-9d68bc8f5d48,16,65 817,04/2018,66 kW (90 CH),10 490
/offres/renault-clio-dci-90-limited-navi-tempo-klima-pdc-1-hand-diesel-gris-d7db363f-4563-4979-a42d-c54403f819aa,17,61 000,06/2018,66 kW (90 CH),10 590
/offres/renault-clio-iv-grandtour-limited-dci-90-klima-diesel-argent-8449a72d-bcf5-4ba9-9da5-06327b52918e,18,57 354,04/2018,66 kW (90 CH),10 790
/offres/renault-clio-energy-dci90-limited-pdcsitzhklima1hand-eu6-diesel-blanc-f34200d6-eeee-4358-b511-dfc400bacf58,19,52 249,09/2017,66 kW (90 CH),10 880
/offres/renault-clio-iv-life-1-5-dci-75-eco-klima-bluetooth-diesel-blanc-71d4f265-1165-45d2-9a02-8c4e4639e8a4,20,33 365,01/2018,55 kW (75 CH),10 990
link,No,Km,Year,HP,Price
polo,,,,,
/offres/volkswagen-polo-1-4-tdi-blue-motion-technology-comfortline-diesel-gris-8cdb10c0-1a93-457d-ae58-37bb2894da2d,1,65 500,06/2015,66 kW (90 CH),8 490
/offres/volkswagen-polo-1-4-tdi-blue-motion-technology-lounge-diesel-bleu-6e918e9d-bf3b-4058-83b4-c0350d964df9,2,60 000,12/2015,66 kW (90 CH),9 800
/offres/volkswagen-polo-comfortline-bmt-start-stopp-v-6c1-euro6-sr-wr-diesel-noir-c0eaa88e-5b9c-4b91-86e1-b86ea627fbb5,3,76 250,11/2015,55 kW (75 CH),9 990
/offres/volkswagen-polo-1-4tdi-klima-sitzh-tempo-radio-diesel-noir-96853b2e-3376-441d-a798-2d027ced658e,4,69 250,02/2017,55 kW (75 CH),10 990
/offres/volkswagen-polo-1-4-tdi-voll-sheft-klima-1-hand-tempo-aux-diesel-blanc-fa8dea0e-f2c0-4c4b-bbf6-ab06b27067f2,5,24 713,05/2017,55 kW (75 CH),11 450
/offres/volkswagen-polo-comfortline-1-4-tdi-comfortline-navi-alu-sitzheiz-diesel-bleu-4f41efca-7f96-4614-a6cf-74fe45b7c9ad,6,64 500,07/2016,55 kW (75 CH),11 600
/offres/volkswagen-polo-1-4-tdi-highline-klima-shz-alu-diesel-bleu-c5da1054-4269-4a65-98a5-ff32d766d387,7,42 234,11/2015,77 kW (105 CH),12 390
/offres/volkswagen-polo-1-4-tdi-sound-bmt-usb-klima-pdc-shz-diesel-argent-ec59b280-cf47-4fcc-a905-f3cce0395209,8,29 900,08/2017,55 kW (75 CH),12 490
/offres/volkswagen-polo-1-4-tdi-blue-motion-technology-sound-diesel-noir-fc0f4838-3e79-4e80-81d5-31a3d8d87c51,9,65 000,08/2017,66 kW (90 CH),12 500

```
4. Using Excel, we can import the data scrapped as below 
```
Data -> Get External Data -> From text -> cars.csv
```
![Screenshot 2021-11-17 at 20 48 14 (2)](https://user-images.githubusercontent.com/40724965/142272006-b2a6e7f4-a05a-4494-85ab-7765174a06cb.png)
