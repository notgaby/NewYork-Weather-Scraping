import tkinter as tk
import requests
from bs4 import BeautifulSoup




days = []
highlow = []
dates = []
precip = []
humidity = []

def get_data(daysList, datesList, tempList, precipList, humidityList):
    page = requests.get("https://weather.com/weather/tenday/l/New+York+City+NY?canonicalCityId=a701ee19c4ab71bbbe2f6ba2fe8c250913883e5ae9b8eee8b54f8efbdb3eec03")
    soup = BeautifulSoup(page.content,"html.parser")
    daysList[:] = [d.get_text() for d in soup.select(".twc-sticky-col .date-time")]
    datesList[:] = [num.get_text() for num in soup.select(".day-detail.clearfix")]
    #high = [high.get_text() for high in soup.select("")]
    tempList[:] = [t.get_text() for t in soup.select(".temp ")]
    tempList.pop(0) #removes the text that says 'high/low'
    #print(highlow)
    precipList[:] = [rain.get_text() for rain in soup.select(".precip")]
    precip.pop(0)

    humidityList[:] = [humid.get_text() for humid in soup.select(".humidity")]
    humidityList.pop(0)



    #data = []
    #for i in range(15):
     #   data.append(datesList[i] + ' // ' + daysList[i] + ' // ' + tempList[i])

    #print(data)
    #return data


def get_days():
    return days

def get_dates():
    return dates

def get_temps():
    return highlow

def get_precip():
    return precip

def get_humidity():
    return humidity

#get_temp_and_dates()
#print(get_temps())

"""
    
    page = requests.get("https://weather.com/weather/tenday/l/New+York+City+NY?canonicalCityId=a701ee19c4ab71bbbe2f6ba2fe8c250913883e5ae9b8eee8b54f8efbdb3eec03")
    soup = BeautifulSoup(page.content,"html.parser")
    print(soup)
    #all=soup.findAll(attrs={'class':'date-time'})
    #print(all.get_text())
"""

get_data(days, dates, highlow, precip, humidity)
#print(get_humidity())
#print((highlow))
#print(dates)
#print(days)

#get_temps()
