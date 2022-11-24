from bs4 import BeautifulSoup
import requests
import pandas 

url="https://en.wikipedia.org/wiki/List_of_brown_dwarfs"

page=requests.get(url)
page_soup=BeautifulSoup(page.text,"html.parser")
star_table=page_soup.find_all("table", attrs={"class": "wikitable sortable"})
lista=[]
table_row=star_table[1].find_all("tr")
for x in table_row:
    td=x.find_all("td")
    row=[i.text.rstrip()for i in td]
    lista.append(row)
name=[]
radius=[]
mass=[]
distance=[]
for z in range(1,len(lista)):
    name.append(lista[z][0])
    radius.append(lista[z][8])
    mass.append(lista[z][7])
    distance.append(lista[z][5])
    
headers=["name","radius","mass","distance"]
new_planet_df_1 = pandas.DataFrame(list(zip(name,radius,mass,distance)),columns=headers)
new_planet_df_1.to_csv("pro128.csv")
