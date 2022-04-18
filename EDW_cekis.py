import pandas as pd
import numpy as np

xlsx = pd.ExcelFile("Files/homework.xlsx")
readings = pd.read_excel(xlsx, 'MeterReadings')
meters = pd.read_excel(xlsx, 'Meter')

EDW_meters = meters[meters['Description'] == 'EDW']
manufacturer_meters = meters[meters['Description'] == 'Üretici']


# ['40Z000047400374P' '729 _ ÇARSAMBA 380 TM _ TR-B' 1 -1 'EDW']
# i[0] = ETSOCode
# i[2] = cekisKatsayisi
# i[3] = verisKatsayisi
for i in EDW_meters.values:
    print(i)
    
# ['40Z000047400374P' Timestamp('2017-10-18 00:00:00') 0.0 nan 0.0 nan]
# j[0] = ETSOCode
# j[1] = Timestamp
# j[2] = inOriginal
# j[3] = inReconstructed
# j[4] = outOriginal
# j[5] = outReconstructed
for j in readings.values:
    print(j)

def calc_edw_in():
    EDW_in_total = 0
    for i in EDW_meters.values:
        for j in readings.values:
            for k in range(0, len(readings), )
    return EDW_in_total