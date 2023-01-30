import requests
import os
import re

if __name__ == '__main__':
    if not os.path.exists('./doubanLibs'):
        os.mkdir('./doubanLibs')
    url = 'https://movie.douban.com/chart'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
    }
    ex = '<a class.*?<img src="(.*?)" width="75".*?</a>'
    page_text=requests.get(url=url,headers=headers).text
    img_src_list = re.findall(ex,page_text,re.S)
    for src in img_src_list:
        src = src
        # 给图片定义名称
        img_name = src.split('/')[-1]
        #读取
        img_data = requests.get(url=src,headers=headers).content
        # 图片路径
        img_path='./doubanLibs/'+img_name
        with open(img_path,'wb') as fp:
            fp.write(img_data)
            print(img_name,'下载成功！！！')



