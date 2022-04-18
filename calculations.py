import pandas as pd

xlsx = pd.ExcelFile("Files/homework.xlsx")
readings = pd.read_excel(xlsx, 'MeterReadings')
meters = pd.read_excel(xlsx, 'Meter')

EDW_meters = meters[meters['Description'] == 'EDW']
manufacturer_meters = meters[meters['Description'] == 'Üretici']


def calc_edw_in():
    EDW_in_total = 0
    for i in EDW_meters.values:
        for j in readings.values:
            if i[0] == j[0]:
                if pd.isna(j[2]) and pd.isna(j[3]):
                    continue
                elif (pd.isna(j[3]) == False) and (pd.isna(j[2])):
                    EDW_in_total += (j[3] * i[2])
                else:
                    EDW_in_total += (j[2] * i[2])
    return EDW_in_total


def calc_edw_out():
    EDW_out_total = 0
    for i in EDW_meters.values:
        for j in readings.values:
            if i[0] == j[0]:
                if pd.isna(j[4]) and pd.isna(j[5]):
                    continue
                elif (pd.isna(j[5]) == False) and (pd.isna(j[4])):
                    EDW_out_total += (j[5] * i[3])
                else:
                    EDW_out_total += (j[4] * i[3])
    return EDW_out_total


def calc_manufacturer_in():
    manufacturer_in_total = 0
    for i in manufacturer_meters.values:
        for j in readings.values:
            if i[0] == j[0]:
                if pd.isna(j[2]) and pd.isna(j[3]):
                    continue
                elif (pd.isna(j[3]) == False) and (pd.isna(j[2])):
                    manufacturer_in_total += (j[3] * i[2])
                else:
                    manufacturer_in_total += (j[2] * i[2])
    return manufacturer_in_total


def calc_manufacturer_out():
    manufacturer_out_total = 0
    for i in manufacturer_meters.values:
        for j in readings.values:
            if i[0] == j[0]:
                if pd.isna(j[4]) and pd.isna(j[5]):
                    continue
                elif (pd.isna(j[5]) == False) and (pd.isna(j[4])):
                    manufacturer_out_total += (j[5] * i[3])
                else:
                    manufacturer_out_total += (j[4] * i[3])
    return manufacturer_out_total


def calc_edw_total():
    return calc_edw_in() + calc_edw_out()


def calc_manufacturer_total():
    return calc_manufacturer_in() + calc_manufacturer_out()


def calc_total():
    return calc_manufacturer_total() + calc_edw_total()


def edw_hourly_in():
    pass

def edw_hourly_out():
    pass

def edw_hourly_total():
    pass

def manufacturer_hourly_in():
    pass

def manufacturer_hourly_out():
    pass

def manufacturer_hourly_total():
    pass

def hourly_total():
    pass

