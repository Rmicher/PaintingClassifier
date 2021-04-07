import pandas as pd
import requests
from bs4 import BeautifulSoup
import urllib.request
import re
from pprint import pprint

def getdata(url):
    r = requests.get(url)
    return r.text


artist_full = pd.read_csv('artists_fulllist.csv', header=0)
print (artist_full)

#paths=['https://www.wikiart.org/en/salvador-dali', 'https://www.wikiart.org/en/ivan-aivazovsky']


artists_df = pd.DataFrame(columns=['artist_name','born','died','active_years', 'Nationality', 'Art_movement','Genre', 'Influenced_by_list', 'Influenced_on_list', 'Pupils_list', 'Art_institution', 'Friends_list'])
for each in artist_full.iterrows():

        path = each[1]['link']
        request = requests.get(path)
        htmldata = getdata(path)
        soup = BeautifulSoup(htmldata, 'html.parser')

        #name
        artist_name = soup.findAll('h3')
        for name in artist_name:
            artist_name=name.text.strip()
        print(artist_name)

        # Born
        row = soup.findAll('s', string='Born:')
        if len(row) > 0:
                for r in row:
                        nextSib = r.nextSibling.nextSibling
                        born = nextSib.text
        else:
                born = None
        print (born)

        # Died

        row = soup.findAll('s', string='Died:')
        if len(row) > 0:
                for r in row:
                        nextSib = r.nextSibling.nextSibling
                        died = nextSib.text
        else:
                died = None
        print(died)

        #Active Years

        row = soup.findAll('s', string='Active Years:')
        if len(row)>0:
                for r in row:
                        nextSib = r.nextSibling
                        active_years=nextSib.strip()

        else:
                active_years=None



        #Nationality
        try:
                Nationality = []
                r = soup.findAll('s', string='Nationality:')[0]
                links_list = r.__dict__['parent'].find_all('a')
                for each in links_list:
                        Nationality.append(each.text)
                print(Nationality)
        except:
                Nationality=None


        #Art Movement
        try:
                Art_movement = []
                r = soup.findAll('s', string='Art Movement:')[0]
                links_list = r.__dict__['parent'].find_all('a')
                for each in links_list:
                        Art_movement.append(each.text)
                print(Art_movement)
        except:
                Art_movement=None

        #Genre
        try:
                Genre = []
                r = soup.findAll('s', string='Genre:')[0]
                links_list = r.__dict__['parent'].find_all('a')
                for each in links_list:
                        Genre.append(each.text)
                print(Genre)
        except:
                Genre=None
        #Influenced by
        try:
                Influenced_by_list=[]
                r=soup.findAll('s',string='Influenced by:')[0]
                links_list=r.__dict__['parent'].find_all('a')
                for each in links_list:
                        if "artists" not in str(each):
                                Influenced_by_list.append(each.text)
                print (Influenced_by_list)
        except:
                Influenced_by_list=None

        #Influenced on
        try:
                Influenced_on_list=[]
                r=soup.findAll('s',string='Influenced on:')[0]
                links_list=r.__dict__['parent'].find_all('a')
                for each in links_list:
                        if "artists" not in str(each):
                                Influenced_on_list.append(each.text)
                print (Influenced_on_list)
        except:
                Influenced_on_list=None

        #Pupils
        try:
                Pupils_list=[]
                r=soup.findAll('s',string='Pupils:')[0]
                links_list=r.__dict__['parent'].find_all('a')
                for each in links_list:
                        if "artists" not in str(each):
                                Pupils_list.append(each.text)
                print (Pupils_list)
        except:
                Pupils_list=None

        #Art institution
        try:
                Art_institution = []
                r = soup.findAll('s', string='Art institution:')[0]
                links_list = r.__dict__['parent'].find_all('a')
                for each in links_list:
                        Art_institution.append(each.text)
                print(Art_institution)
        except:
                Art_institution=None

        #Friends and Co-workers
        try:
                Friends_list=[]
                r=soup.findAll('s',string='Friends and Co-workers:')[0]
                links_list=r.__dict__['parent'].find_all('a')
                for each in links_list:
                        Friends_list.append(each.text)
                print (Friends_list)
        except:
                Friends_list=None

        artist_df = pd.DataFrame([[artist_name, born, died, active_years, Nationality, Art_movement, Genre, Influenced_by_list, Influenced_on_list, Pupils_list, Art_institution, Friends_list]],
                                  columns=['artist_name','born','died','active_years', 'Nationality', 'Art_movement','Genre', 'Influenced_by_list', 'Influenced_on_list', 'Pupils_list', 'Art_institution', 'Friends_list'])

        artists_df = artists_df.append(artist_df, ignore_index=True)

print (artists_df)
artists_df.to_csv(f"artists_all_data.csv", encoding='utf-8')