import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    # html = html.decode("utf-8")
    url = 'https://www.bequge.cc/book/36992/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
    }
    page_text = requests.get(url=url,headers=headers).content.decode('utf-8')
    #实例化
    soup = BeautifulSoup(page_text,'lxml')
    #dl_list = soup.select('.panel-body panel-chapterlist > dd')
    dl_list = soup.select('.col-md-4')
    fp = open('./yishoumicheng.txt','w',encoding='utf-8')
    for dd in dl_list:
        #获取标题
        title = dd.a.text
        print(title)
        #获取url
        detail_url = 'https://www.bequge.cc'+dd.a['href']
        # print(detail_url)
        #获取内容
        detail_page_text = requests.get(url=detail_url,headers=headers).content.decode('utf-8')
        detail_soup = BeautifulSoup(detail_page_text,'lxml')
        # print(detail_soup)
        div_tag = detail_soup.find('div',class_='panel-body')
        content = div_tag.text
        # print(content)
        fp.write(title+':'+content+'\n')
        print(title,'爬取成功')





