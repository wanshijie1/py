"""
[使用模块]: requests >>> pip install requests        <第三方模块>
           parsel >>> pip install parsel            <第三方模块>
           prettytable >>> pip install prettytable  <第三方模块>
https://www.bqg70.com/ 首先进入这个网址，进入笔趣阁官网
搜索你想要看的小说
选择你想看的小说后，在地址栏会出现一个数字，举例：“https://www.bqg70.com/book/3315/”
那个数字请复制好，例如：”3315”
运行代码，输入这个数字 ，即可下载对应的小说
"""
import requests  # 第三方的模块
import parsel  # 第三方的模块
import os  # 内置模块 文件或文件夹

filename = '小说\\'
if not os.path.exists(filename):
    os.mkdir(filename)

headers = {
    'user-agent': ('Mozilla/5.0 (Windows NT 10.0; Win64; x64)' +
                   'AppleWebKit/537.36 ' +
                   '(KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36')
}


rid = input('输入书名ID：')
link = f'https://www.bqg70.com/book/{rid}/'

html_data = requests.get(url=link, headers=headers).text
# print(html_data)
selector_2 = parsel.Selector(html_data)
divs = selector_2.css('.listmain dd')
for div in divs:
    title = div.css('a::text').get()
    href = div.css('a::attr(href)').get()
    url = 'https://www.bqg70.com' + href

    try:
        response = requests.get(url=url, headers=headers)
        selector = parsel.Selector(response.text)
        # getall 返回的是一个列表 []
        book = selector.css('#chaptercontent::text').getall()
        book = '\n'.join(book)
        # 数据保存
        with open(filename + title + '.txt', mode='a', encoding='utf-8') as f:
            f.write(book)
            print('正在下载章节:  ', title)
    except Exception as e:
        print(e)
