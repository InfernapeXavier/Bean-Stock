import pandas as pd
import numpy as np

data = pd.read_csv('google.csv')
data = data.fillna('0')
for column in data:
    if column == 'Date':
        continue
    sum = data[column].sum()
    if sum == 0:
        data = data.drop([column], axis = 1)

AveragePrice = (data.High + data.Low)/2
data['AveragePrice'] = AveragePrice #06

TrueRange = data.High - data.Low
data['TrueRange'] = TrueRange #07

PriceAction = ((data.Close - data.Open) + (data.Close - data.High) + (data.Close - data.Low))/2
data['PriceAction'] = PriceAction #08

data['HighestHigh'] = '' #09
data['LowestLow'] = '' #10
data['SMA'] = '' #11
data['EMA'] = '' #12
data['EMA26'] = '' #13
data['UpMove'] = '' #14
data['DownMove'] = '' #15
data['PlusDM'] = '' #16
data['MinusDI'] = '' #17
data['EMADM'] = '' #18
data['ATR'] = '' #19
data['PercK'] = '' #20
data['PercD'] = '' #21
data['AverageGain'] = '' #22
data['AverageLoss'] = '' #23
data['RSI'] = '' #24
data['Momentum'] = '' #25
data['MiddleBand'] = '' #26
data['UpperBand'] = '' #27
data['LowerBand'] = '' #28
data['PPO'] = '' #29

for count in range (3333):
    if count > 0:
        data.iat[count, 14] = data.iloc[count, 2] - data.iloc[count-1, 2]
        data.iat[count, 15] = data.iloc[count-1, 3] - data.iloc[count, 3]

        if data.iat[count, 14] > data.iat[count, 15] and data.iat[count, 14] > 0:
            data.iat[count, 16] = data.iat[count, 14]
        else:
            data.iat[count, 16] = 0

        if data.iat[count, 15] > data.iat[count, 14] and data.iat[count, 15] > 0:
            data.iat[count, 17] = data.iat[count, 15]
        else:
            data.iat[count, 17] = 0

    if count > 12:
        data.iat[count, 9] = max(data.iloc[count-13:count, 2]) #HighestHigh
        data.iat[count, 10] = min(data.iloc[count-13:count, 3]) #LowestLow
        data.iat[count, 11] = (data.iloc[count-13:count+1, 4]).mean() #SMA
        data.iat[count, 20] = (data.iloc[count, 4] - data.iloc[count, 9])/(data.iloc[count, 8] - data.iloc[count, 9]) * 100 #PercK
        data.iat[count, 22] = (data.iloc[count-12:count+1, 14]).mean() #AvgGain
        data.iat[count, 23] = (data.iloc[count-12:count+1, 15]).mean() #AvgLoss
        #data.iat[count, 24] = 100 - (100 / 1 + (data.iloc[count, 14] / data.iloc[count, 15])) #RSI
        data.iat[count, 25] = 100 * (data.iloc[count-13,  4]/data.iloc[count,  4])  #Momentum
        data.iat[count, 26] = data.iloc[count,  11]  #MiddleBand
        data.iat[count, 27] = data.iloc[count, 26] + (data.iloc[count-13:count+1, 6].std() * 2) #UpperBand
        data.iat[count, 28] = data.iloc[count, 26] - (data.iloc[count-13:count+1, 6].std() * 2) #LowerBand

        if count == 13:
            data.iat[count, 12] = (data.iloc[count, 4] - data.iloc[count, 11]) * (2/15) + data.iloc[count, 11] #InitEMA
            data.iat[count, 19] = (data.iloc[count-13:count+1, 7].mean()) #InitATR
        else:
            data.iat[count, 12] = (data.iloc[count, 4] - data.iloc[count-1, 12]) * (2/15) + data.iloc[count-1, 12] #EMA
            data.iat[count, 19] = ((data.iloc[count-1, 19] * 13) + data.iloc[count, 7])/14 #ATR

        if count > 14:
            data.iat[count, 21] = (data.iloc[count-2:count+1, 20].mean()) #PercD

        if count > 24:
            if count == 25:
                data.iat[count, 13] = (data.iloc[count, 4] - data.iloc[count-1, 11]) * (2/27) + data.iloc[count, 11] #Init26EMA
            else:
                data.iat[count, 13] = (data.iloc[count, 4] - data.iloc[count-1, 13]) * (2/27) + data.iloc[count-1, 13] #26EMA
            data.iat[count, 29] = ((data.iloc[count, 12] - data.iloc[count, 13]) / data.iloc[count, 13]) * 100  #PPO

data.replace('', np.nan, inplace=True)
data = data.fillna('0')
data.to_csv('google_clean.csv', index = False)
