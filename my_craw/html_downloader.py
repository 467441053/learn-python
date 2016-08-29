# coding:utf-8
import urllib.request

class HtmlDownloader(object):
    
    
    def downHtml(self, url):
        if url is None:
            return None
        response = urllib.request.urlopen(url)
        if response.getcode() != 200:
            return None
        else:
            return response.read()
    
    



