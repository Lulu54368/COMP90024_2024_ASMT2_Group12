import pandas as pd 
rankings_colname = ['data', '1', '2', '3', '4', '5', '6', '7']
data = pd.read_csv('./BOM-Station-Origin.csv', names=rankings_colname)
data = data.dropna(axis=1, how='all')
data = data.dropna(axis=0, how='all')

head = data.loc[:2]
databody = data.loc[4:]

rankings_colname = head.data[2].split()

def abbbbb(x):
    stationinfo = x.data[:49]
    locinfo = x.data[49:]
    Site = stationinfo.split()[0]
    Name = ' '.join(stationinfo.split()[1:])
    Lat = locinfo[:10]
    Lon = locinfo[10:19]
    Start = locinfo[19:27]
    End = locinfo[28:36]
    Years = locinfo[36:].split()[0]
    perc = locinfo[36:].split()[1]
    
    try:
        AWS = locinfo[36:].split()[2]
    except:
        AWS = 'None'
        print(x.data)
    d = {'Site': Site, 'Name': Name, 'Lat': Lat, 'Lon': Lon, 'Start':Start, 'End':End, 'Years':Years, '%':perc, 'AWS':AWS}
    return pd.Series(data=d, index=rankings_colname)

data = databody.apply(lambda x: abbbbb(x), axis = 1)

data.to_json(orient='records', path_or_buf="BOM.json")