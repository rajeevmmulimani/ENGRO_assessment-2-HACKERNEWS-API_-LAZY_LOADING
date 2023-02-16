# -*- coding: utf-8 -*-
"""
Created on Mon, Feb 09, 2023, 12:38 PM

@author: RajeevMulimani
"""

import requests
import json
from flask import Flask, render_template
import numpy as npp2

import threading



flask_test = Flask(__name__)



title_item=[]
url_item=[]

try:
    def create_app():
        
        with flask_test.app_context():
            response_API1 = requests.get('https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty')
            #response_API1 = requests.get('https://hacker-news.firebaseio.com/v0/askstories.json?print=pretty')
            data1 = response_API1.text
            raw_data1 = data1
            parse_json1 = json.loads(raw_data1)
            
            length_of_news_id=0
            parse_json_clone1=(npp2.random.choice(parse_json1, size=10, replace=False))
            

            for news_id_dump in parse_json_clone1:
    
                var1=len(parse_json1)
    
                
                news_id=news_id_dump

    
    
    
    

                type_search ="type"
                title_search = "title"
                url_search = "url"


                response_API2 = requests.get('https://hacker-news.firebaseio.com/v0/item/'+str(news_id)+'.json')
                data2 = response_API2.text
                raw_data2 = data2
                parse_json2 = json.loads(raw_data2)

    
    
                for raw_tuples,tuple_count in parse_json2.items():
        
                    if(raw_tuples==title_search):
                        tempxy1=tuple_count
            
                        title_item.append(tempxy1)
        
                    if(raw_tuples==url_search):
                        tempxy2=tuple_count
            
                        url_item.append(tempxy2)                 
        
            home()
        return flask_test
        
finally:
    @flask_test.route('/')
    
    def home():
        threading.Timer(5.0, create_app).start()
    
        title_1_temp=title_item[:1]
        title_dep1 = str(*title_1_temp)[0:]

        url_1_temp=url_item[:1]
        url_dep1 = str(*url_1_temp)[0:]
        
        title_2_temp=title_item[1:2]
        title_dep2 = str(*title_2_temp)[0:]

        url_2_temp=url_item[1:2]
        url_dep2 = str(*url_2_temp)[0:]
        
        title_3_temp=title_item[2:3]
        title_dep3 = str(*title_3_temp)[0:]

        url_3_temp=url_item[2:3]
        url_dep3 = str(*url_3_temp)[0:]

        title_4_temp=title_item[3:4]
        title_dep4 = str(*title_4_temp)[0:]

        url_4_temp=url_item[3:4]
        url_dep4 = str(*url_4_temp)[0:]

        title_5_temp=title_item[4:5]
        title_dep5 = str(*title_5_temp)[0:]

        url_5_temp=url_item[4:5]
        url_dep5 = str(*url_5_temp)[0:]

        title_6_temp=title_item[5:6]
        title_dep6 = str(*title_6_temp)[0:]

        url_6_temp=url_item[5:6]
        url_dep6 = str(*url_6_temp)[0:]

        title_7_temp=title_item[6:7]
        title_dep7 = str(*title_7_temp)[0:]

        url_7_temp=url_item[6:7]
        url_dep7 = str(*url_7_temp)[0:]

        title_8_temp=title_item[7:8]
        title_dep8 = str(*title_8_temp)[0:]

        url_8_temp=url_item[7:8]
        url_dep8 = str(*url_8_temp)[0:]

        title_9_temp=title_item[8:9]
        title_dep9 = str(*title_9_temp)[0:]

        url_9_temp=url_item[8:9]
        url_dep9 = str(*url_9_temp)[0:]

        title_10_temp=title_item[9:10]
        title_dep10 = str(*title_10_temp)[0:]

        url_10_temp=url_item[9:10]
        url_dep10 = str(*url_10_temp)[0:]
                        
        
        return render_template('ENGROW.html', title1=title_dep1, url1=url_dep1)

flask_test.run()
