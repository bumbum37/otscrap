import requests
from bs4 import BeautifulSoup
from os import system
import re 
print('''        
            ╔═╗╔╦╗  ╔═╗╔═╗╦═╗╔═╗╔═╗
            ║ ║ ║   ╚═╗║  ╠╦╝╠═╣╠═╝
            ╚═╝ ╩   ╚═╝╚═╝╩╚═╩ ╩╩  
                               v1.0
''')
nama_anime = str(input('Masukan Nama Anime: '))

#REQUESTS KE WEB
r = requests.get('https://otakudesu.moe/?s={}&post_type=anime'.format(nama_anime)).text


#MENCARI ANIME
soup = BeautifulSoup(r, 'html.parser')
listNamaAnime = []
for index,nama_element in enumerate(soup.find_all('h2'),start=1):
    print(index,':',nama_element.text.replace('Subtitle Indonesia',' '))
    for link in nama_element.find_all('a'):
        listNamaAnime.append(link.get('href'))


#PILIH ANIME
episode = int(input('\nPilih: '))
pil = listNamaAnime[episode-1]
if pil:
    system('clear')
    
    anime = requests.get(pil).text
    animenya = BeautifulSoup(anime,'html.parser')
    for var1 in animenya.find('div', class_="infozingle"):
        print(var1.text)
    sinopsis = animenya.find('div', class_='sinopc');print('Sinopsis: '+sinopsis.text)


#PILIH BATCH

    for batch in animenya.find('div', class_="episodelist"):
        for url in batch.find_all('a'):
            sk = requests.get(url.get('href')).text
            kip = BeautifulSoup(sk,'html.parser')
            print('\n\nDownload Batch:')
            for div in kip.find('div',class_='download'):
                #print(div.prettify())
                
                #MENAMPILKAN UKURAN ANIME DAN KUALITAS
                siz = []
                for size in div.find_all('i'):
                    siz.append(size.text)
                NA = []
                for nama in div.find_all('strong'):
                    NA.append(nama.text)

                #DISINI MENAMPILKAN SEMUANYA




                for i,e in enumerate(zip(NA,siz),start=1):
                    print(i ,':', ' ->> '.join(e))
                
                #MENYAMBUT KEBAGIAN URL
                urlkos=[]
                for kos in div.find_all('li'):
                    for x in kos.find_all('a'):
                        data = x.get('href')
                        
                        pola = re.compile(r'http://desudrive.com/otakudrive/\?id=\w+')
                        cocok = pola.findall(str(data))
                        for x in cocok:
                            urlkos.append(x)
                pilihsize = int(input('Pilih: '))
                res = urlkos[pilihsize-1]
                if res:
                    print('\nResult:\n'+res+'\n\n')
                    system(f'xdg-open {res}')
