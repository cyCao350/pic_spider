#coding:utf-8
'''
Created on 2017年5月16日 上午9:01:30

@author: caowei13622
'''

try:
    import urllib.request as urllib2
except ImportError:
    import urllib2

class HtmlDwnloader(object):
    #headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}
    def download(self, url):
        if url is None:
            return None

        response = urllib2.urlopen(url)
        if response.getcode() != 200:
            return None
        return response.read()
