from django.shortcuts import render
import json
import pandas as pd
import os 
from django.db.models import Q

#posts=pd.read_json ('wscrp/jsonfile/jsonFile.json', orient='records')

with open('C:/Users/pc/PycharmProjects/Projet_Big-Data Web_Scraping/Week3_BigData/file0.json') as datafile:  
    posts = json.load(datafile)
retail = pd.DataFrame(posts)

with open('C:/Users/pc/PycharmProjects/Projet_Big-Data Web_Scraping/Week3_BigData/file1.json') as datafile1:
    posts1 = json.load(datafile1)
retail1 = pd.DataFrame(posts1)

with open('C:/Users/pc/PycharmProjects/Projet_Big-Data Web_Scraping/Week3_BigData/file2.json') as datafile2:
    posts2 = json.load(datafile2)
retail2 = pd.DataFrame(posts2)

with open('C:/Users/pc/PycharmProjects/Projet_Big-Data Web_Scraping/Week3_BigData/file3.json') as datafile3:
    posts3 = json.load(datafile3)
retail3 = pd.DataFrame(posts3)

with open('C:/Users/pc/PycharmProjects/Projet_Big-Data Web_Scraping/Week3_BigData/reflexion.json') as datafile4:
    posts4 = json.load(datafile4)
retail4 = pd.DataFrame(posts4)

with open('C:/Users/pc/PycharmProjects/Projet_Big-Data Web_Scraping/Week3_BigData/lnr_dz.json') as datafile5:
    posts5 = json.load(datafile5)
retail5 = pd.DataFrame(posts5)

with open('C:/Users/pc/PycharmProjects/Projet_Big-Data Web_Scraping/Week3_BigData/lesoirdalgerie.json') as datafile6:
    posts6 = json.load(datafile6)
retail6 = pd.DataFrame(posts6)

with open('C:/Users/pc/PycharmProjects/Projet_Big-Data Web_Scraping/Week3_BigData/lequotidien .json') as datafile7:
    posts7 = json.load(datafile7)
retail7 = pd.DataFrame(posts7)

with open('C:/Users/pc/PycharmProjects/Projet_Big-Data Web_Scraping/Week3_BigData/jeune.json') as datafile8:
    posts8 = json.load(datafile8)
retail8 = pd.DataFrame(posts8)

with open('C:/Users/pc/PycharmProjects/Projet_Big-Data Web_Scraping/Week3_BigData/elmoudjahid.json') as datafile9:
    posts9 = json.load(datafile9)
retail9 = pd.DataFrame(posts9)
with open('C:/Users/pc/PycharmProjects/Projet_Big-Data Web_Scraping/Week3_BigData/dzfoot.json') as datafile10:
    posts10 = json.load(datafile10)
retail10 = pd.DataFrame(posts10)

with open('C:/Users/pc/PycharmProjects/Projet_Big-Data Web_Scraping/Week3_BigData/competition.json') as datafile11:
    posts11 = json.load(datafile11)
retail11 = pd.DataFrame(posts11)

with open('C:/Users/pc/PycharmProjects/Projet_Big-Data Web_Scraping/Week3_BigData/capouest.json') as datafile12:
    posts12 = json.load(datafile12)
retail12 = pd.DataFrame(posts12)

with open('C:/Users/pc/PycharmProjects/Projet_Big-Data Web_Scraping/Week3_BigData/bejaia.json') as datafile13:
    posts13 = json.load(datafile13)
retail13 = pd.DataFrame(posts13) 

def home(request):
   
    context = {
        'title': "page d'accueil",
     }
    return render(request, 'wscrp/index.html', context)

def home1(request):
   
    contextt = {
        'title': "",
     }
    return render(request, 'wscrp/base.html', contextt)

def about(request):
    return render(request, 'wscrp/about.html', {'title': 'A propos de nous'})

def Liberte(request):
   
    context = {
        'title': "Liberté",
        'posts': posts,
     }
    return render(request, 'wscrp/Liberte.html', context)

def elwatan(request):
    context1 = {
        'title': "Elwatan",
        'posts1': posts1
     }
    return render(request, 'wscrp/Elwatan.html', context1)

def aps(request):
    context2 = {
        'title': "APS",
        'posts2': posts2
     }
    return render(request, 'wscrp/APS.html', context2)

def tsa(request):
    context3 = {
        'title': "TSA",
        'posts3': posts3
     }
    return render(request, 'wscrp/TSA.html', context3)

def reflexion(request):
    context4 = {
        'title': "Reflexion",
        'posts4': posts4
     }
    return render(request, 'wscrp/reflexion.html', context4)

def lnr_dz(request):
    context5 = {
        'title': "lnr_dz",
        'posts5': posts5
     }
    return render(request, 'wscrp/lnr_dz.html', context5)

def lesoirdalgerie(request):
    context6 = {
        'title': "lesoirdalgerie",
        'posts6': posts6
     }
    return render(request, 'wscrp/lnr_dz.html', context6)  

def lequotidien(request):
    context7 = {
        'title': "lesoirdalgerie",
        'posts7': posts7
     }
    return render(request, 'wscrp/lequotidien.html', context7)

def jeune(request):
    context8 = {
        'title': "jeune",
        'posts8': posts8
     }
    return render(request, 'wscrp/jeune.html', context8)

def elmoudjahid(request):
    context9 = {
        'title': "elmoudjahid",
        'posts9': posts9
     }
    return render(request, 'wscrp/elmoudjahid.html', context9)

def dzfoot(request):
    context10 = {
        'title': "dzfoot",
        'posts10': posts10
     }
    return render(request, 'wscrp/dzfoot.html', context10)


def competition(request):
    context11 = {
        'title': "competition",
        'posts11': posts11
     }
    return render(request, 'wscrp/competition.html', context11)


def capouest(request):
    context12 = {
        'title': "capouest",
        'posts12': posts12
     }
    return render(request, 'wscrp/capouest.html', context12)

def bejaia(request):
    context13 = {
        'title': "bejaia",
        'posts13': posts13
     }
    return render(request, 'wscrp/bejaia.html', context13)