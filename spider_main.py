#coding:utf-8
'''
Created on 2017年5月16日 上午9:00:59

@author: caowei13622
'''

from pic_spider import url_manager, html_downloader, html_parser, html_outputer

class SpiderMain(object):
    
    """docstring for SpiderMain"""
    def __init__(self):
        self.urls = url_manager.Url_Manager()
        self.downloader=html_downloader.HtmlDwnloader()
        self.parser=html_parser.HtmlParser()
        self.outputer=html_outputer.HtmlOutputer()

    def craw(self, root_rul):
        count=1
        self.urls.add_new_url(root_rul)
        while self.urls.has_new_url():
            try:
                new_url=self.urls.get_new_url()
                print(count)
                html_cont = self.downloader.download(new_url)
                (new_urls, link_urls) = self.parser.parse(new_url,html_cont)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(link_urls)
                if count==5:
                    break
                count+=1
                
            except:
                print("faild!")
        self.outputer.output_pic()
        print('over!')


if __name__ == '__main__':
    root_rul="https://www.XXXXX/XXXXX/XX.htm"
    obj_spider=SpiderMain()
    obj_spider.craw(root_rul)