
import  datetime, time
import  urllib.request
import  random
import  readtemp

thinkurl ="https://api.thingspeak.com/update?api_key=JYQPWHB0ENBYQ3TP&field2="

while True:
    url = thinkurl + str(readtemp.read_temp())
    f =  urllib.request.urlopen(url)
    data = str(f.read())
    print("Got", data)
    print(url)
    time.sleep(20)
    
