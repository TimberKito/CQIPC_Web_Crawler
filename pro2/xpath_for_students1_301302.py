#-*- coding =  utf-8 -*-
#@Time: 2021/9/23 21:39
#@author: baijialian001
#@file: chapter2_15_xpath_getinfo.py
#@software: PyCharm
import lxml.html
source = '''
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <title>测试</title>
    </head>
    <body>
     <div class="useful">
            <ul>
            <li class=“info”>我需要的信息1</li>
            <li class=“info”>我需要的信息2</li>
            <li class=“info”>我需要的信息3</li>
            </ul>
    </div>
    <div class="useless">
        <ul>
        <li class=“info”>垃圾信息1</li>
        <li class=“info”>垃圾信息2</li>
        </ul>
    </div>
    </body>
</html>
'''


