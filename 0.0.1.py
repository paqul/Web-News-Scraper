from bs4 import BeautifulSoup
import requests
import time


def time_start():
    time_start = time.clock()
    return time_start


def time_stop():
    time_stop = time.clock()
    return time_stop


def delta_time(time_start, time_stop):
    d_time = abs(time_stop - time_start)
    print(d_time)
    return d_time


def TVN():
    stronka_tvn = requests.get("https://www.tvn24.pl/")
    link_najnowsze = BeautifulSoup(stronka_tvn.content, 'html.parser')
    link_najnowsze = link_najnowsze.find(class_="item-najnowsze").a["href"]
    podstronka = requests.get(link_najnowsze)
    infoall_tvn = BeautifulSoup(podstronka.content, 'html.parser')
    infoall_tvn = (infoall_tvn.find(class_="mainRightColumn"))
    info = (infoall_tvn.find(class_="content"))
    info_zmienna = (info.find_all("a"))
    info_tvn = []
    for zmienna in range(0,15):
        print(info_zmienna[zmienna].get_text())
        info_tvn.append(info_zmienna[zmienna].get_text())
    print(info_tvn)


def Polsat():
    stronka_polsat = requests.get("http://www.polsatnews.pl/")
    infoall_polsat = BeautifulSoup(stronka_polsat.content, 'html.parser')
    info_zmienna = infoall_polsat.find(class_="tabs__content")
    info = list(info_zmienna.find_all("h2"))
    info_polsat=[]
    for zmienna in range(0,len(info)):
        print(info[zmienna].get_text())
        info_polsat.append(info[zmienna].get_text())
    print(info_polsat)


def TVP():
    stronka_tvp = requests.get("https://www.tvp.info/")
    infoall_tvp = BeautifulSoup(stronka_tvp.content, 'html.parser')
    info_zmienna = infoall_tvp.find(class_="news__container")
    info = info_zmienna.find_all("a")
    info_tvp=[]
    for zmienna in range(0,len(info)):
        print(info[zmienna].get_text())
        info_tvp.append(info[zmienna].get_text())
    print(info_tvp)

def WP():
    stronka_WP = requests.get("https://www.wp.pl/")
    infoall_WP = BeautifulSoup(stronka_WP.content, 'html.parser')

    print(infoall_WP)
    pass

def onet():
    pass

def interia():
    pass



first = time_start()
TVN()
Polsat()
TVP()
# WP()
# onet()
# interia()
second = time_stop()
wynik = delta_time(first, second)

plik = open("czasy_dzialania_programu.txt", "a+")
plik.write(str(wynik)+"\n")
plik.close()


