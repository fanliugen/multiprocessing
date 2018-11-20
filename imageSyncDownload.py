import requests
from lxml import etree

from urllib import request
import os
import re

def parse_page(url):
    headers = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36',

    }
    response = requests.get(url,headers = headers)
    text = response.text
    # print(text)
    html = etree.HTML(text)

    images = html.xpath('//div[@class="page-content text-center"]//img[@class!="gif"]')
    for img in images:
        #print(etree.tostring(img))
        img_url = img.get('data-original')
        alt = img.get('alt')
        alt = re.sub(r"[?\？\.\*!！]",'',alt)
        suffix = os.path.splitext(img_url)[1]
        filename = alt + suffix

        request.urlretrieve(img_url,'images/'+filename)



def main():
    for x in range(1,10):
        url = 'http://www.doutula.com/photo/list/?page=%d' %x
        parse_page(url)
        


if __name__ == '__main__':
    main()