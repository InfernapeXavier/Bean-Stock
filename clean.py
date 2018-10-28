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
data['VarOpen'] = '' #30
data['VarHigh'] = '' #31
data['VarLow'] = '' #32
data['VarClose'] = '' #33
data['VarAvg'] = '' #34
data['VarPA'] = '' #35
data['VarHH'] = '' #36
data['VarLL'] = '' #37
data['VarSMA'] = '' #38
data['VarEMA'] = '' #39
data['VarATR'] = '' #40
data['VarK'] = '' #41
data['VarD'] = '' #42
data['VarMomentum'] = '' #43
data['VarUB'] = '' #44
data['VarLB'] = '' #45
data['VarPPO'] = '' #46
data['Class'] = '' #47



for count in range (3333):
    if count > 0:
        data.iat[count, 14] = data.iloc[count, 2] - data.iloc[count-1, 2] #UpMove
        data.iat[count, 15] = data.iloc[count-1, 3] - data.iloc[count, 3] #DownMove

        if data.iat[count, 14] > data.iat[count, 15] and data.iat[count, 14] > 0:
            data.iat[count, 16] = data.iat[count, 14] #PlusDM
        else:
            data.iat[count, 16] = 0

        if data.iat[count, 15] > data.iat[count, 14] and data.iat[count, 15] > 0:
            data.iat[count, 17] = data.iat[count, 15] #MinusDI
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

for count in range (27, 3333):

    prev = data.iloc[count-1, 1]
    current = data.iloc[count, 1]
    basis = (10/100)*prev
    if current - prev > basis:
        data.iloc[count, 30] = "Uptrend" #VarOpen
    elif prev - current < basis:
        data.iloc[count, 30] = "Downtrend" #VarOpen
    else:
        data.iloc[count, 30] = "Notrend" #VarOpen

    prev = data.iloc[count-1, 2]
    current = data.iloc[count, 2]
    basis = (10/100)*prev
    if current - prev > basis:
        data.iloc[count, 31] = "Uptrend" #VarHigh
    elif prev - current < basis:
        data.iloc[count, 31] = "Downtrend" #VarHigh
    else:
        data.iloc[count, 31] = "Notrend" #VarHigh

    prev = data.iloc[count-1, 3]
    current = data.iloc[count, 3]
    basis = (10/100)*prev
    if current - prev > basis:
        data.iloc[count, 32] = "Uptrend" #VarLow
    elif prev - current < basis:
        data.iloc[count, 32] = "Downtrend" #VarLow
    else:
        data.iloc[count, 32] = "Notrend" #VarLow

    prev = data.iloc[count-1, 4]
    current = data.iloc[count, 4]
    basis = (10/100)*prev
    if current - prev > basis:
        data.iloc[count, 33] = "Uptrend" #VarClose
    elif prev - current < basis:
        data.iloc[count, 33] = "Downtrend" #VarClose
    else:
        data.iloc[count, 33] = "Notrend" #VarClose

    prev = data.iloc[count-1, 6]
    current = data.iloc[count, 6]
    basis = (10/100)*prev
    if current - prev > basis:
        data.iloc[count, 34] = "Uptrend" #VarAvg
    elif prev - current < basis:
        data.iloc[count, 34] = "Downtrend" #VarAvg
    else:
        data.iloc[count, 34] = "Notrend" #VarAvg

    prev = data.iloc[count-1, 8]
    current = data.iloc[count, 8]
    basis = (10/100)*prev
    if current - prev > basis:
        data.iloc[count, 35] = "Uptrend" #VarPA
    elif prev - current < basis:
        data.iloc[count, 35] = "Downtrend" #VarPA
    else:
        data.iloc[count, 35] = "Notrend" #VarPA

    prev = data.iloc[count-1, 9]
    current = data.iloc[count, 9]
    basis = (10/100)*prev
    if current - prev > basis:
        data.iloc[count, 36] = "Uptrend" #VarHH
    elif prev - current < basis:
        data.iloc[count, 36] = "Downtrend" #VarHH
    else:
        data.iloc[count, 36] = "Notrend" #VarHH

    prev = data.iloc[count-1, 10]
    current = data.iloc[count, 10]
    basis = (10/100)*prev
    if current - prev > basis:
        data.iloc[count, 37] = "Uptrend" #VarLL
    elif prev - current < basis:
        data.iloc[count, 37] = "Downtrend" #VarLL
    else:
        data.iloc[count, 37] = "Notrend" #VarLL

    prev = data.iloc[count-1, 11]
    current = data.iloc[count, 11]
    basis = (10/100)*prev
    if current - prev > basis:
        data.iloc[count, 38] = "Uptrend" #VarSMA
    elif prev - current < basis:
        data.iloc[count, 38] = "Downtrend" #VarSMA
    else:
        data.iloc[count, 38] = "Notrend" #VarSMA

    prev = data.iloc[count-1, 12]
    current = data.iloc[count, 12]
    basis = (10/100)*prev
    if current - prev > basis:
        data.iloc[count, 39] = "Uptrend" #VarEMA
    elif prev - current < basis:
        data.iloc[count, 39] = "Downtrend" #VarEMA
    else:
        data.iloc[count, 39] = "Notrend" #VarEMA

    prev = data.iloc[count-1, 19]
    current = data.iloc[count, 19]
    basis = (10/100)*prev
    if current - prev > basis:
        data.iloc[count, 40] = "Uptrend" #VarATR
    elif prev - current < basis:
        data.iloc[count, 40] = "Downtrend" #VarATR
    else:
        data.iloc[count, 40] = "Notrend" #VarATR

    prev = data.iloc[count-1, 20]
    current = data.iloc[count, 20]
    basis = (10/100)*prev
    if current - prev > basis:
        data.iloc[count, 41] = "Uptrend" #VarK
    elif prev - current < basis:
        data.iloc[count, 41] = "Downtrend" #VarK
    else:
        data.iloc[count, 41] = "Notrend" #VarK

    prev = data.iloc[count-1, 21]
    current = data.iloc[count, 21]
    basis = (10/100)*prev
    if current - prev > basis:
        data.iloc[count, 42] = "Uptrend" #VarD
    elif prev - current < basis:
        data.iloc[count, 42] = "Downtrend" #VarD
    else:
        data.iloc[count, 42] = "Notrend" #VarD

    prev = data.iloc[count-1, 25]
    current = data.iloc[count, 25]
    basis = (10/100)*prev
    if current - prev > basis:
        data.iloc[count, 43] = "Uptrend" #VarMomentum
    elif prev - current < basis:
        data.iloc[count, 43] = "Downtrend" #VarMomentum
    else:
        data.iloc[count, 43] = "Notrend" #VarMomentum

    prev = data.iloc[count-1, 27]
    current = data.iloc[count, 27]
    basis = (10/100)*prev
    if current - prev > basis:
        data.iloc[count, 44] = "Uptrend" #VarUB
    elif prev - current < basis:
        data.iloc[count, 44] = "Downtrend" #VarUB
    else:
        data.iloc[count, 44] = "Notrend" #VarUB

    prev = data.iloc[count-1, 28]
    current = data.iloc[count, 28]
    basis = (10/100)*prev
    if current - prev > basis:
        data.iloc[count, 45] = "Uptrend" #VarLB
    elif prev - current < basis:
        data.iloc[count, 45] = "Downtrend" #VarLB
    else:
        data.iloc[count, 45] = "Notrend" #VarLB

    prev = data.iloc[count-1, 29]
    current = data.iloc[count, 29]
    basis = (10/100)*prev
    if current - prev > basis:
        data.iloc[count, 46] = "Uptrend" #VarPPO
    elif prev - current < basis:
        data.iloc[count, 46] = "Downtrend" #VarPPO
    else:
        data.iloc[count, 46] = "Notrend" #VarPPO

    for attribute in range(30, 47):
        countUp = 0
        if data.iloc[count, attribute] == "Uptrend":
            countUp += 1
        if countUp > 12 or countUp < 4:
            data.iat[count, 47] = "Sell"
        elif countUp < 6:
            data.iat[count, 47] = "Hold"
        else:
            data.iat[count, 47] = "Buy"

data.to_csv('google_clean.csv', index = False)

print (data.shape)
