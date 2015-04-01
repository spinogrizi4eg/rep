import urllib2
import pandas as pd
from datetime import datetime

mass = [0, 22, 24, 23, 25, 3, 4, 8, 19, 20, 21, 9, 26, 10, 11, 12, 13, 14, 15, 16, 27, 17, 18, 6, 1, 2, 7, 5]
d = datetime.now()


def load():
    i = 1

    while i <= 27:
        if i < 10:
            url = "http://www.star.nesdis.noaa.gov/smcd/emb/vci/gvix/G04/ts_L1/ByProvince/Mean/L1_Mean_UKR.R0" + str(
                i) + ".txt"
        else:
            url = "http://www.star.nesdis.noaa.gov/smcd/emb/vci/gvix/G04/ts_L1/ByProvince/Mean/L1_Mean_UKR.R" + str(
                i) + ".txt"
        vhi_url = urllib2.urlopen(url)
        out = open('vhi_id_' + str(mass[i]) + '_' + str(d.date()) + '.csv', 'wb')
        out.write(vhi_url.read())
        out.close()

        i = i + 1


def VHI():
    num = input('Enter ID to the field')
    df = pd.read_csv('vhi_id_' + str(num) + '_' + str(d.date()) + '.csv', index_col=False, header=1)
    year = input('Year')
    week = input('Week')
    print('number  VHI')
    print (df[(df['year'] == year) & (df['week'] == week) & (df['VHI'] != -1.00)]['VHI'])
    print('MAXIMUM')
    print max(df[(df['year'] == year)]['VHI'])
    print('MINIMUM')
    print min(df[(df['year'] == year)]['VHI'])


def fun(percent):
    num = input('Enter ID to the field')
    df = pd.read_csv('vhi_id_' + str(num) + '_' + str(d.date()) + '.csv', index_col=False, header=1)
    print (df[(df['VHI'] < 20) & (df['%Area_VHI_LESS_15'] > int(percent)) & (df['VHI'] != -1.00)]['year'])


def Less(percent):
    num = input('Enter ID to the field')
    df = pd.read_csv('vhi_id_' + str(num) + '_' + str(d.date()) + '.csv', index_col=False, header=1)
    print (df[(df['VHI'] < 30) & (df['VHI'] > 20) & (df['%Area_VHI_LESS_35'] > int(percent))& (df['VHI'] != -1.00)]['year'])


def dopka():
    print('Dopka:')
    num = input('Enter ID to the field')
    df = pd.read_csv('vhi_id_' + str(num) + '_' + str(d.date()) + '.csv', index_col=False, header=1)
    print (df[(df['VHI'] > 60) & (df['week'] >= 23) & (df['week'] <= 36) & (df['VHI'] != -1.00)]['year'])

#load()
#VHI()
#fun('15')
#Less('70')
dopka()