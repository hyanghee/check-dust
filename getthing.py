
import  datetime, time
import  urllib2
import  random
import  json
from pprint import  pprint

thingget="https://thingspeak.com/channels/333900/feeds.json?results="

def  read_thing():
    number =  4
    url = thingget + str(number)
    f =  urllib2.urlopen(url)
    data = str(f.read())
#    print("Got", data)
#    print(jsonstring)
#    print(type(jsonstring))

    js = json.loads(data)
    
    s = js["feeds"]
    i=0
    tp,pm25,pm10,hum = 0.0, 0.0, 0.0, 0.0

    for j in s:
        print s[i]
        print "created at --->  ", s[i]["created_at"]

        f1 =s[i]['field1']
        f2 =s[i]['field2']
        f3 =s[i]['field3']
        f4 =s[i]['field4']
        if f1 != None: 
            pm25 = f1
        if f2 != None:
            tp = f2
        if f3 != None:
            pm10 = f3 
        if f4 != None:
            hum = f4
        i=i+1
  
    return pm25,tp, pm10, hum

pm25, tp, pm10, hum = read_thing()
print "data : ", pm25, tp, pm10, hum

