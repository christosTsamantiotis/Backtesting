import requests
import time

def tapeRead(start):
    params = {'limit':'10000','start':start,'sort':'1'}
    url = requests.get("https://api-pub.bitfinex.com/v2/trades/tBTCUSD/hist", params)
    data = url.json()
    file(data)
    start = data[-1][1]
    print("Next...\n")
    time.sleep(2)
    return start


def file(data):
    f = open("tape.csv","r")
    lines = f.read().splitlines()
    last = lines[-1]
    f.close()
    sp = list(last.split(","))
    stri = "" #This is the string that will be appended to the file
    if data[-1][0] == sp[0]:        ##Check if the last entry in the file is the same as the last one in the json data
        del data[-1]                ## Delete it from the json data
        for x in range(0,7500,1):
            for y in range(0,4,1):
                stri = stri + str(data[x][y])
                if y == 3:
                    stri = stri +"\n"
                elif y == 4:
                    print(".")
                else:
                    stri = stri +","
    else:
        for x in range(0,7500,1):
            for y in range(0,4,1):
                stri = stri + str(data[x][y])
                if y == 3:
                    stri = stri +"\n"
                elif y == 4:
                    print(".")
                else:
                    stri = stri +","
    a = open("tape.csv", "a")
    a.write(stri)
    a.close()


start = 1587909853368  #UNIX epoch
y = tapeRead(start)
while True:
    x = tapeRead(y)
    y = tapeRead(x)


