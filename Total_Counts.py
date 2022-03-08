import pandas as pd

def total_passengers(df):
    sum_passengers = 0
    for i in range(0,len(df)):
        sum_passengers += df.at[i,'PASSENGERS']
    return sum_passengers

def total_freight(df):
    sum_frieght = 0
    for i in range(0, len(df)):
        sum_frieght += df.at[i, 'FREIGHT']
    return sum_frieght

def total_orgin_airport(df):
    airport_freq = {}
    for i in range(0, len(df)):
        if df.at[i, 'ORIGIN'] in airport_freq:
            airport_freq[df.at[i, 'ORIGIN']] += 1
        else:
            airport_freq[df.at[i, 'ORIGIN']] = 1
    return sorted(airport_freq.items(), key=lambda x: x[1], reverse=True)

def total_dest_airport(df):
    airport_freq = {}
    for i in range(0, len(df)):
        if df.at[i, 'DEST'] in airport_freq:
            airport_freq[df.at[i, 'DEST']] += 1
        else:
            airport_freq[df.at[i, 'DEST']] = 1
    return sorted(airport_freq.items(), key=lambda x: x[1], reverse=True)

def total_carrier(df):
    carrier_freq = {}
    for i in range(0, len(df)):
        if df.at[i, 'UNIQUE_CARRIER'] in carrier_freq:
            carrier_freq[df.at[i, 'UNIQUE_CARRIER']] += 1
        else:
            carrier_freq[df.at[i, 'UNIQUE_CARRIER']] = 1
    return sorted(carrier_freq.items(), key=lambda x: x[1], reverse=True)
