#coding:utf-8
'''
Created on 2017年5月16日 上午9:01:43

@author: caowei13622
'''

from urllib.parse import urljoin
from bs4 import BeautifulSoup
import re

class HtmlParser(object):
    
    #def _get_new_urls(self, page_url, soup):
    #    new_urls = set()
    #    links = soup.find_all('a', href = re.compile(r'^/XXXXXXX/\d'))
    #    for link in links:
    #        new_url = link['href']
    #        new_ful_url = urljoin(page_url, new_url)
    #        new_urls.add(new_ful_url)
    #    if len(new_urls) == 0:
    #        print('没有获取到页面！')
    #    print('+++++', new_urls)  
    #    
    #    link_urls = set()
    #    tps = soup.find_all('a', href = re.compile(r'^\d\.htm'))
    #    for tp in tps:
    #        content_url = tp['href']
    #        new_con_url = urljoin(page_url, content_url)
    #        link_urls.add(new_con_url)  
    #    if len(link_urls) == 0:
    #        print('没有获取到图片链接!')
    #    print('-----', link_urls)    
    #    return (new_urls, link_urls)

    def _get_new_urls(self, page_url, soup):
        new_urls = set()
        links = soup.find_all('a', href = re.compile(r'^/XXXXXXX/\d'))
        for link in links:
            new_url = link['href']
            new_ful_url = urljoin(page_url, new_url)
            new_urls.add(new_ful_url)
        if len(new_urls) == 0:
            print('没有获取到页面！') 
        return new_urls
        
    def _get_new_data(self, page_url, soup2):
        link_urls = set()
        tps = soup2.find_all('a', href = re.compile(r'^\d\.htm'))
        for tp in tps:
            content_url = tp['href']
            new_con_url = urljoin(page_url, content_url)
            link_urls.add(new_con_url)  
        if len(link_urls) == 0:
            print('没有获取到图片链接!')
        return link_urls


    def parse(self,page_url,html_cont):
        if page_url is None or html_cont is None:
            return
        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        #(new_urls, content_url) = self._get_new_urls(page_url, soup)
        new_urls = self._get_new_urls(page_url, soup)
        content_url = self._get_new_data(page_url, soup)
        return(new_urls, content_url)