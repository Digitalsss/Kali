#!/bin/python3

import sys, argparse
import re
import requests
from bs4 import BeautifulSoup


generalindex = 1

def vpar(url):
    file = open('liste', 'a')
    ferr = open('ferr', 'a')
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    full = re.split('<.*?>',str(soup))

    while '' in full:
        full.remove('')

    while '\n' in full:
        full.remove('\n')

    while '.' in full:
        full.remove('.')

    base = full.index('z')
    verb = full[base+1]
    base = full.index('Konj 2 1.Sg.')
    perf = full[base+2] # check if its not beisiele or strukturen
    pret = full[base+1] # same for this

    struk = full.index('Strukturen')
    strk = struk + 1
    strukturen = []

    while not full[strk]=='Beispiele':
        strukturen.append(full[strk])
        strk = strk + 1

    if not ( perf == 'Beispiele' or perf == verb or perf =='Strukturen' or pret == 'Beispiele' or pret == verb or pret =='Strukturen'):
        global generalindex
        file.write('!SEPARATOR!\n')
        file.write(verb+'\n\n')
        file.write(perf+'\n')
        file.write(pret+'\n\n')
        for item in strukturen:
            file.write('%s\n' % item)
        file.write('\n')
        print(str(generalindex).zfill(4) +' ' +verb)
        generalindex = generalindex + 1

    else :
        ferr.write(verb+'\n')


liste = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','z'] 
for a in liste:
    link = "http://www.d-seite.de/vis/vis.php?buchstabe="+a
    pages = requests.get(link)
    sp = BeautifulSoup(pages.content, 'html.parser')
    links = [a['href'] for a in sp.find_all('a', href=True)]
    index = links.index('vis.php?buchstabe=z') + 1
    links = links[index:]
    for verb in links:
        vpar("http://www.d-seite.de/vis/"+verb)



