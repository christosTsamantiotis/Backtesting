import json
def exp(mins,percentage,f):
     rez = []
     n = 0
     for x in f:
        line = f.readline().split(",")
        up = 0
        down = 0
        b = 0
        s = 0
        whaleBuy = 0
        whaleSell = 0
        whaleVol = 0
        totalVol = 0
        mts = int(line[1])
        transaction = float(line[2])
        price = float(line[3])
        nextMTS = mts + (mins * 60 * 1000)
        while mts <= nextMTS:
            line = f.readline().split(",")
            change = (price/float(line[3]))*100-100
            mts = int(line[1])
            transaction = transaction + float(line[2])
            
            if float(line[2]) > 9.7:
                whaleBuy = whaleBuy + float(line[2])
                b=b+1
                whaleVol = whaleVol + whaleTemp
            if float(line[2]) < -9.7:
                whaleSell = whaleSell + float(line[2])
                s = s + 1
                whaleTemp = float(line[2]) ** 2
                whaleTemp = whaleTemp ** 0.5
                whaleVol = whaleVol + whaleTemp
            if change > 0:
                if change >= percentage:
                    up = up + 1
                    mts = nextMTS
                    whaleBase = whaleBuy - whaleSell
                    whale2base = whaleBase / transaction
                    whale2buy = whaleBuy / transaction
                    whale2sell = whaleSell / transaction
                    temp = float(line[2]) ** 2
                    temp = temp ** 0.5
                    totalVol = totalVol + temp
                    volRatio = whaleVol/totalVol
                    rez.append({'up': up,'down': down,'change': change,'whaleBuy': whaleBuy,'whaleSell':whaleSell,'whaleBase':whaleBase,'transaction':transaction, 'whale / transaction RATIO':whale2base, 'Volume':totalVol, 'whale2buy':whale2buy, 'whale2sell':whale2sell, 'volRatio':volRatio, 'mts':mts})
            if change < 0:
                change = change ** 2
                change = change ** 0.5
                if change >= percentage:
                    down = down + 1
                    mts = nextMTS
                    whaleBase = whaleBuy - whaleSell
                    whale2base = whaleBase / transaction
                    whale2buy = whaleBuy / transaction
                    whale2sell = whaleSell / transaction
                    temp = float(line[2]) ** 2
                    temp = temp ** 0.5
                    totalVol = totalVol + temp
                    volRatio = whaleVol/totalVol
                    rez.append({'up': up,'down': down,'change': change,'whaleBuy': whaleBuy,'whaleSell':whaleSell,'whaleBase':whaleBase,'transaction':transaction, 'whale / transaction RATIO':whale2base, 'Volume':totalVol, 'whale2buy':whale2buy, 'whale2sell':whale2sell, 'volRatio':volRatio, 'mts':mts})
                    return rez




            





f = open('tape.csv', "r")
f2 = open('result.json', "w")
rez = exp(60, 2, f)
json.dump(rez, f2)
f.close()
f2.close()