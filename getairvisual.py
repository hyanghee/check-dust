#!/usr/bin/python
# -*- coding: utf-8 -*-

#from /home/pi/.local/lib/python2.7/site-packages/BeautifulSoup import BeautifulSoup
#import sys
import json
import urllib2
import requests
import random
import time
from BeautifulSoup import BeautifulSoup
#from bs4 import BeautifulSoup

URL = 'http://cleanair.seoul.go.kr/air_city.htm?method=measure'
thingurl_pm="https://api.thingspeak.com/update?api_key=JYQPWHB0ENBYQ3TP&field5="
PM10="&field6="
GUNAME="송파구"

def GetInfo(gu):
    response = requests.get(URL)
    html_doc = response.text
    soup = BeautifulSoup(html_doc)
    tables = soup.findAll('table');
    dataTable = tables[2]
    trs = dataTable.findAll('tr')
    for tr in trs:
        if gu in str(tr):
            print "현재 : ", gu 
            return tr;

def MakeMessage(data):
    if  data is None :
       return "system is preparing... coming later "
    tds = data.findAll('td')
    message1 = u' 통합대기환경지수는 {}({}) 입니다.'.format(tds[7].getText(), tds[8].getText())
    message2 = u'미세먼지: {}㎍/㎥, 초미세먼지: {}㎍/㎥, 오존: {}ppm, 이산화질소: {}ppm, 일산화탄소: {}ppm, 아황산가스: {}ppm'.format(tds[1].getText(), tds[2].getText(), tds[3].getText(), tds[4].getText(), tds[5].getText(), tds[6].getText())
    messageTotal = message1 + u"(" + message2 + ")"

    urlt = thingurl_pm + tds[2].getText()+ PM10 + tds[1].getText()
    f =  urllib2.urlopen(urlt)
    d  = str(f.read())
    print("Got songpa ", d)
    print("put songpa ", urlt)

    return messageTotal

def loop():
    while  True:
      s = MakeMessage(GetInfo(GUNAME))
#     print s
      print "end get data..." 
      k = random.randrange(1200,2400)
      print "sleeping..... ", k
#      time.sleep(k)
      break

if __name__ == "__main__":
    loop()
