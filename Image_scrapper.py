import pandas as pd
import requests
from bs4 import BeautifulSoup
import urllib.request
import re
from pprint import pprint


def getdata(url):
    r = requests.get(url)
    return r.text

artists_fullname={"claude-monet": "Claude Monet",
                  "amedeo-modigliani":"Amedeo Modigliani",
                 "wassily-kandinsky":"Wassily Kandinskiy",
                 "diego-rivera":"Diego Rivera",
                 "rene-magritte":"Rene Magritte",
                 "salvador-dali":"Salvador Dali",
                 "edouard-manet":"Edouard Manet",
                 "andrei-rublev":"Andrei Rublev",
                 "vincent-van-gogh":"Vincent van Gogh",
                 "gustav-klimt":"Gustav Klimt",
                 "hieronymus-bosch":"Hieronymus Bosch",
                 "kazimir-malevich":"Kazimir Malevich",
                 "mikhail-vrubel":"Mikhail Vrubel",
                 "pablo-picasso":"Pablo Picasso",
                 "peter-paul-rubens":"Peter Paul Rubens",
                 "pierre-auguste-renoir":"Pierre-Auguste Renoir",
                 "francisco-goya":"Francisco Goya",
                 "frida-kahlo":"Frida Kahlo",
                 "el-greco":"El Greco",
                 "albrecht-durer":"Albrecht Durer",
                 "alfred-sisley":"Alfred Sisley",
                 "pieter-bruegel-the-elder":"Pieter Bruegel",
                 "marc-chagall":"Marc Chagall",
                 "giotto-di-bondone":"Giotto di Bondone",
                 "sandro-botticelli":"Sandro Botticelli",
                 "caravaggio":"Caravaggio",
                 "leonardo-da-vinci":"Leonardo da Vinci",
                 "diego-velazquez":"Diego Velazquez",
                 "henri-matisse":"Henri Matisse",
                 "jan-van-eyck":"Jan van Eyck",
                 "edgar-degas":"Edgar Degas",
                 "rembrandt":"Rembrandt",
                 "titian":"Titian",
                 "henri-de-toulouse-lautrec":"Henri de Toulouse-Lautrec",
                 "gustave-courbet":"Gustave Courbet",
                 "camille-pissarro":"Camille Pissarro",
                 "william-turner":"William Turner",
                 "edvard-munch":"Edvard Munch",
                 "paul-cezanne":"Paul Cezanne",
                 "eugene-delacroix":"Eugene Delacroix",
                 "henri-rousseau":"Henri Rousseau",
                 "georges-seurat": "Georges Seurat",
                 "paul-klee":"Paul Klee",
                 "piet-mondrian":"Piet Mondrian",
                 "joan-miro":"Joan Miro",
                 "andy-warhol":"Andy Warhol",
                 "paul-gauguin":"Paul Gauguin",
                 "raphael":"Raphael",
                 "michelangelo":"Michelangelo",
                 "jackson-pollock":"Jackson Pollock"}
artists=list(artists_fullname.keys())[:1]
print (artists)

artists=['frida-kahlo']

for artist in artists:
    artwork_qty=0
    path = f'{artist}/artworks_all.csv'

    artist_works = pd.read_csv(path, header=0)
    print (artists_fullname[artist])
    #print (artist_works)

    #artist_works=artist_works.replace(' ', '-', regex=True)
    #artist_works=artist_works.replace('(', '', regex=True)
    #artist_works=artist_works.replace(')', '', regex=True)

    #artist_works = artist_works.applymap(lambda s:s.lower() if type(s) == str else s)
    artist_works.drop_duplicates(subset=None, keep='first', inplace=True)
    artist_works['date'] = artist_works['date'].fillna(0).astype(int)
    artist_works['date'] = artist_works['date'].astype(str)
    #print (artist_works)
    artworks_dict={}
    artworks_df = pd.DataFrame(columns=['artist','folder', 'artwork', 'date','style','genre', 'link', 'path'])
    for artwork_all in artist_works.iterrows():
        artwork=artwork_all[1]['artwork']
        #print ("artwork", artwork)
        artwork_date = artwork_all[1]['date']
        #print("artwork_date", artwork_date)

        path=artwork_all[1]['link']
        #print("path", date)
        try:
            request = requests.get(path)

            htmldata = getdata(path)
            soup = BeautifulSoup(htmldata, 'html.parser')


            for item in soup.find_all('img'):
                #print(item['src'])
                if "jpg" in item['src']:
                    path= item['src']
                    #print (path)

            style=soup.findAll('a', href=re.compile('/en/paintings-by-style/'))
            for tag in style:
                artwork_style=tag.text
            genre=soup.findAll('a', href=re.compile('/en/paintings-by-genre/'))
            #print (genre)
            for tag in genre:
                artwork_genre=tag.text
        #print (artwork_genre)
        except:
            continue

        try:
            #path=f"https://uploads0.wikiart.org/images/{artist}/{artwork}.jpg"
            #print (path)
            path = path.replace('ó', '%C3%B3')
            artwork_name=artwork.replace(' ', '-')

            artwork_name=artwork_name.lower()
            print (artwork_name)
            urllib.request.urlretrieve(path, f"{artist}/artworks/{artwork_name}.jpg")
            #print('2',path)
            artwork_qty=artwork_qty+1

            artwork_df=pd.DataFrame([[artists_fullname[artist], artist, artwork, artwork_date, artwork_style,artwork_genre, path,f"{artist}/artworks/{artwork_name}.jpg"]], columns=['artist','folder', 'artwork','date','style', 'genre','link', 'path'])
            #print (artwork_df)

            artworks_df=artworks_df.append(artwork_df, ignore_index=True)

        except:
            continue
    print (artwork_qty)
    artworks_df.drop_duplicates('path', inplace=True)
    artworks_df.reset_index(drop=True, inplace=True)
    artworks_df.to_csv(f"{artist}/artworks.csv")