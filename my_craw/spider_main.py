# coding:utf-8

import url_manager
import html_downloader
import html_parser
import html_outputer

class SpiderMain(object):
    
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlPaser()
        self.outputer = html_outputer.HtmlOutputer()
    
    def craw(self, root_Url):
        count = 1
        self.urls.add_new_url(root_Url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print('craw %d: %s' % (count, new_url))
                html_content = self.downloader.downHtml(new_url)
                new_urls, new_data = self.parser.parse(new_url, html_content)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)
                if count >= 10:
                    break
                
                count = count + 1
            except:
                print('craw failed')
        self.outputer.output_html()


if __name__ == '__main__':
    root_Url = 'http://baike.baidu.com/view/21087.htm'
    my_spider = SpiderMain()
    my_spider.craw(root_Url)