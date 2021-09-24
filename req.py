import requests
from pyquery import PyQuery as PQ

headers = {
    'sec-ch-ua': '"Microsoft Edge";v="93", " Not;A Brand";v="99", "Chromium";v="93"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36 Edg/93.0.961.52',
}

params = (
    ('page', '1'),
    ('project_classname_list', '面上项目,青年科学基金项目,管理科学,重点项目,优秀青年科学基金项目,国家自然科学基金'),
    ('sort_type', '3'),
)

response = requests.get('https://www.medsci.cn/sci/nsfc.do', headers=headers, verify=False, params=params)
obj = PQ(response.text)
print('许玮元' in response.text)

