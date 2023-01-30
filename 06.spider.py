#国家药品监督总局化妆品生产许可证相关
import requests

if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
    }
    url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/allQyxx/allQyxx.jsp'

    page_text = requests.get(url=url,headers=headers).text

    with open('kk/huazhuangpin.html','w',encoding='utf-8') as fp:
        fp.write(page_text)

    print('over')
    #http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?hKHnQfLv=5Dy6TvMCFA0wARHH7UxJz3BJ04tV0x_skzuJNfX5.P6KUJMogXB3T2eB3pt.kXs0LKbx2B0EgypKJeUkCYmfCnoKrBivanPE7yierKGqPlSUdnA4dzE5I4r2Q7g1M10fPeyOiTe5vM9UG2SLco.qMQROGhuJxDFvh1bAZ4MsXHS.hfhqjl.t0wj4MokMVrKJmnVy5prDjpbKQoLZkV3Drrw_7gMrPmEugCG8izfaMMVqtXu8KVknHEoBc0f8mh6bWu9sIRiJURbb64Y8vmGtn9ZKmUkhYeaQKTDdE3w18DE9&8X7Yi61c=4Xg2rMGi5cjNpai6sDD1l2kscoeCJZryycec8XxdNjS0h6lBqzKEj7ork3DNXziuwFj3J6qCHjdZaXEtDySfIsXd1dS3NfW5p2DIFT7fytbWXvOve5Ypm1cnwcXx_iTmV
    #http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?hKHnQfLv=5rOyPERvsG89RzLZW3R42auc2OMvuq_T7jch_5BY1MO7HKPUSbO7jzOFL1Aav8K2WgkIZCiOJbxkXYmjInArDP5wB2c9tvrxqscZRbZvqldG1U7y6eq3MUz_EWGHOB5P1.4.zAO59KKo7tsrYz_J37iytIMHps2BggkhS3fqSszsa9H4.O7EaaZayCCZUd0Ovovut7K0JP8J.AxiasAEvtPz7EPt15yH6p2HDXLOq.2tC2aFZmW9xyQVvIjJC_cEMVRQhM3CiXzmvocXLJvavUCaWlB8ilD0MGd_Pa4NGK69&8X7Yi61c=4DNGozoOA8TTiuFy3rj2c33Ctnk1.IAYoHZu0OmTbsF06ZbfUUmr8n46CGmsXppQhX2OUMn.AB9aBwssdRaV52_mgeMMgjNTnzlxy_COQazhzOAHceCFx__QeiekeHAe4

