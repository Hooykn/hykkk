import requests
import os
from lxml import etree

if __name__ == '__main__':
    for i in range(2,36):
        page = str(i)
        url = 'https://pic.netbian.com/4kmeinv/index_'+page+'.html'
        headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
        }
        response = requests.get(url=url,headers=headers)
# response.encoding='gbk'
        page_text = response.text

        tree = etree.HTML(page_text)
        li_list = tree.xpath('//div[@class="slist"]/ul/li')

        if not os.path.exists('meinv'):
            os.mkdir('meinv')

        for li in li_list:
            img_src = 'http://pic.netbian.com'+li.xpath('./a/img/@src')[0]
            # print(img_src)
            img_name = li.xpath('./a/img/@alt')[0]+'.jpg'
            img_name = img_name.encode('iso-8859-1').decode('gbk')
            # print(img_alt)
            img_path = 'meinv/'+img_name
            img_data = requests.get(url=img_src,headers=headers).content
            with open(img_path,'wb') as fp:
                fp.write(img_data)
                print(img_name+'爬取成功！！！')


