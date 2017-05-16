#coding:utf-8
'''
Created on 2017年5月16日 上午9:01:55

@author: caowei13622
'''

import requests
import re


class HtmlOutputer(object):
    def __init__(self):
        self.datas=[]

    def collect_data(self, content_url):
        if content_url is None:
            return
        self.datas.append(content_url)

    def output_pic(self):
        list_urls = []
        i = 0
        for list_urls in self.datas:
            #list_urls = self.datas.pop()
            for new_url in list_urls:
                response = requests.get(new_url, stream=True)
                buf = response.text
                listurl = re.findall(r'http.+attaches.+?\.jpg', buf)
                #print(listurl)
                for urlIndex in listurl:
                    with open(str(i)+'.jpg', 'wb') as fd:
                        req = requests.get(urlIndex)
                        for chunk in req.iter_content(128):
                            fd.write(chunk)
                        i+=1
                        fd.close()
