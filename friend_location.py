import csv
from pyecharts import Map
import pandas as pd


def analyseLocation(friends):
    headers = ['NickName','Province','City','Signature']
    with open('friends.csv','w',encoding='utf-8',newline='',) as csvFile:
        writer = csv.DictWriter(csvFile, headers)
        writer.writeheader()
        for friend in friends[1:]:
           row = {}
           row['NickName'] = friend['NickName']
           row['Province'] = friend['Province']
           row['City'] = friend['City']
           row['Signature'] = friend['Signature']
           writer.writerow(row)

    df = pd.read_csv('friends.csv')           
    province_list = df['Province'].fillna('').tolist()
    count_province = pd.value_counts(province_list)
    attr = count_province.index.tolist()
    value1 = count_province.tolist()
    map = Map("Friend distribution by city", width=1200,height=600)
    map.add("",attr, value1, maptype='china',is_visualmap=True,visualmap_text_color='#000',is_label_show=True)
    #map.show_config()
    map.render('map.html')
    map
