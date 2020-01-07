import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
page = requests.get('https://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168#.Xg65OFUzbIU')
soup = BeautifulSoup(page.content ,'html.parser')
seven_day = soup.find(id='seven-day-forecast')
forcast_item = seven_day.find_all(class_='tombstone-container')
# for today in forcast_item:
#     period = today.find(class_='period-name').get_text()
#     short_desc = today.find(class_='short-desc').get_text()
#     temp = today.find(class_='temp').get_text()
#     img = today.find('img')
#     desc = img['src']
    # print(period)
    # print(short_desc)
    # print(temp)
    #print(desc)
period = [pt.get_text() for pt in seven_day.select('.tombstone-container .period-name')]
short_desc = [sd.get_text() for sd in seven_day.select('.tombstone-container .short-desc')]
temp = [tem.get_text() for tem in seven_day.select('.tombstone-container .temp')]
img = [image['title'] for image in seven_day.select('.tombstone-container img')]
# print(period)
# print(short_desc)
# print(temp)
# print(img)

weather = pd.DataFrame({
    "Period":period,
    "Short_desc":short_desc,
    "Temp":temp,
    "Img":img,
})
pd.set_option('display.max_columns',5)
print(weather.columns)
print(weather)