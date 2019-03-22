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
    tvn = "https://www.tvn24.pl"
    stronka_tvn = requests.get(tvn)
    link_najnowsze = BeautifulSoup(stronka_tvn.content, 'html.parser')
    link_najnowsze = link_najnowsze.find(class_="item-najnowsze").a["href"]
    podstronka = requests.get(link_najnowsze)
    infoall_tvn = BeautifulSoup(podstronka.content, 'html.parser')
    infoall_tvn = (infoall_tvn.find(class_="mainRightColumn"))
    info = (infoall_tvn.find(class_="content"))
    info_zmienna = (info.find_all("a"))
    info_tvn = []
    info_tvn_link = []
    for zmienna in range(0, 15):
        # print(info_zmienna[zmienna].get_text())
        info_tvn.append(info_zmienna[zmienna].get_text())
        # print(tvn+info_zmienna[zmienna].get('href'))
        http = info_zmienna[zmienna].get('href')
        http = http[0:4]
        if http != "http":
            info_tvn_link.append(tvn+info_zmienna[zmienna].get('href'))
        else:
            info_tvn_link.append(info_zmienna[zmienna].get('href'))
    print(info_tvn, info_tvn_link) # tu ma byc return


def Polsat():
    stronka_polsat = requests.get("http://www.polsatnews.pl/")
    infoall_polsat = BeautifulSoup(stronka_polsat.content, 'html.parser')
    info_zmienna = infoall_polsat.find(class_="tabs__content")
    info = list(info_zmienna.find_all("h2"))
    linki = list(info_zmienna.find_all("a"))
    info_polsat=[]
    info_polsat_link=[]
    for zmienna in range(0,len(info)):
        # print(info[zmienna].get_text())
        info_polsat.append(info[zmienna].get_text())
        # print(linki[zmienna].get('href'))
        info_polsat_link.append(linki[zmienna].get('href'))
    print(info_polsat, info_polsat_link) # tu ma byc return


def TVP():
    tvp = "https://www.tvp.info"
    stronka_tvp = requests.get(tvp)
    infoall_tvp = BeautifulSoup(stronka_tvp.content, 'html.parser')
    info_zmienna = infoall_tvp.find(class_="news__container")
    info = list(info_zmienna.find_all("a"))
    info_tvp=[]
    linki_tvp=[]
    for zmienna in range(0, len(info)):
        info_tvp.append(info[zmienna].get_text())
        http = info[zmienna].get('href')
        http = http[0:4]
        if http != "http":
            linki_tvp.append(tvp + info[zmienna].get('href'))
        else:
            linki_tvp.append(info[zmienna].get('href'))
    print(info_tvp, linki_tvp)

def WP():
    wp = "https://www.wp.pl/"
    stronka_WP = requests.get(wp)
    infoall_WP = BeautifulSoup(stronka_WP.content, 'html.parser')
    infoall_WP = infoall_WP.find("body")
    # infoall_WP = infoall_WP.find(id='root')
    # infoall_WP = infoall_WP.find(class_="rmnfvs-0 jfUSQI lpn5rg-1 jfyVeE")
    # infoall_WP = infoall_WP.find(class_="sc-1fu2hk8-0 jIlknD")
    infoall_text_0 = infoall_WP.find_all(class_="lclzf3-0 gxKMbd")
    infoall_linki_0 = infoall_WP.find_all(class_="sks72q-0 gsEIgT")
    infoall_text_1 = infoall_WP.find_all(class_="sc-135bwa8-3 jAavTs lclzf3-0 egPcYF")
    infoall_linki_1 = infoall_WP.find_all(class_="sks72q-0 desPEO")
    infoall_text = infoall_WP.find_all(class_="lclzf3-0 egPcYF")
    infoall_linki = infoall_WP.find_all(class_="sks72q-0 cqUubc")
    wp_text = [infoall_text_0[0].get_text(), infoall_text_1[0].get_text()]
    wp_linki = [infoall_linki_0[0].get('href'), infoall_linki_1[0].get('href')]
    for x, zmienna in enumerate(range(0, 7)):
        print(x, infoall_text[zmienna].get_text())
        wp_text.append(infoall_text[zmienna].get_text())
        print(x, infoall_linki[zmienna].get('href'))
        wp_linki.append(infoall_linki[zmienna].get('href'))
    infoall_linki_3 = infoall_WP.find_all(class_="sks72q-0 WvEyB")
    info_linki_3 = infoall_linki_3[0]
    info_text_3 = info_linki_3.find_all(class_="lclzf3-0 egPcYF")
    wp_text.append(info_text_3[0].get_text())
    wp_linki.append(infoall_linki_3[0].get('href'))

    print(wp_text, wp_linki)

def onet():
    pass

def interia():
    pass



first = time_start()
TVN()
Polsat()
TVP()
WP()
# onet()
# interia()
second = time_stop()
wynik = delta_time(first, second)

plik = open("czasy_dzialania_programu.txt", "a+")
plik.write(str(wynik)+"\n")
plik.close()


