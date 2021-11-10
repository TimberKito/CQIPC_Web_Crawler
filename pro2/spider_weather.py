#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
# @Time    : 2021/10/25 14:29
# @Author  : Timber
# @Id      : 201950130527
# @File    : spider_weather.py
# @说明/注释: 
"""
from bs4 import BeautifulSoup
from bs4 import UnicodeDammit
import urllib.request


class WeatherForecast:
    def __init__(self):
        self.headers = {
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.30"
        }

    def forecastCity(self, city):
        url = 'http://www.weather.com.cn/weather/101280601.shtml'
        try:
            req = urllib.request.Request(url, headers=self.headers)
            data = urllib.request.urlopen(req)
            data = data.read()
            dammit = UnicodeDammit(data, ["utf-8", "gbk"])
            data = dammit.unicode_markup
            soup = BeautifulSoup(data, "lxml")
            lis = soup.select("ul[class='t clearfix'] li")

            for li in lis:
                try:
                    date = li.select('h1')[0].text

                    weather = li.select('p[class="wea"]')[0].text
                    temp = li.select('p[class="tem"] span')[0].text + "/" + li.select('p[class="tem"] i')[0].text
                    print(city, date, weather, temp)
                except Exception as err:
                    pass
        except Exception as err:
            print(err)

    def process(self, cities):
        for city in cities:
            self.forecastCity(city)


ws = WeatherForecast()
ws.process(["乐山"])

print("completed")
