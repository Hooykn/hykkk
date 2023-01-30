import json
import requests
#破解百度翻译
if __name__ == '__main__':
    post_url = 'https://fanyi.baidu.com/sug'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
    }
    word=input('请输入单词')
    data={
        'kw':word
    }
    response = requests.post(url=post_url,headers=headers,data=data)
    dic_json=response.json()
    fileNmae=word+'.json'
    fp=open('kk/'+fileNmae,'w',encoding='utf-8')
    json.dump(dic_json,fp=fp,ensure_ascii=False)

    print('over')