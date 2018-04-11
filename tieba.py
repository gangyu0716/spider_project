import requests
import time
from bs4 import BeautifulSoup

def get_html(url):
    try:
        r = requests.get(url, timeout = 30)
        r.raise_for_status()
        r.encoding = "utf-8"
        return r.text
    except:
        return "error"

def get_content(url):
    comments = []
    html = get_html(url)
    soup = BeautifulSoup(html, 'lxml')
    #找到每一个主题贴
    liTags = soup.find_all('li', attrs={'class': ' j_thread_list clearfix'})

    print (liTags)
    for li in liTags:
        #初始化一个字典用存储
        comment = {}
        try:
            comment['title'] = li.find(
            'a', attrs={'class':'j_th_tit'}).text.strip()
            comment['link'] = "http://tie.baidu.com/" + \
                li.find('a', attrs = {'class':'j_th_tit'})['href']
            comment['name'] = li.find(
                'span', attrs = {'class': 'tb_icon_author'}).text.strip()
            comment['time'] = li.find(
                'span', attrs = {'class':'pull-right is_show_create_time'}).text.strip()
            comment['replyNum'] = li.find(
            'span', attrs={'class': 'threadlist_rep_num center_text'}).text.strip()
            comments.append(comment)
        except:
            print ('Some problem happened!')
    return comments

def Out2File(dict):
    with open('TB.txt','a+') as f:
        for comment in dict:
            f.write('标题： {} \t 链接：{} \t 发帖人：{} \t 发帖时间：{} \t 回复数量： {} \n'.format(
                comment['title'], comment['link'], comment['name'], comment['time'], comment['replyNum']))
    print ('当前页面爬取完成')

def main(base_url, deep):
    url_list = []
    for i in range(0,deep):
        url_list.append(base_url + '&pn=' + str(i*50))

    print ('网页信息已经确认')
    print (url_list)

    for url in url_list:
        content = get_content(url)
        Out2File(content)

    print ('所有网页爬取完毕，已输出至文件中')

base_url = 'https://tieba.baidu.com/f?kw=%E6%80%AA%E7%89%A9%E7%8C%8E%E4%BA%BA%E4%B8%96%E7%95%8C&ie=utf-8'

deep = 1

if __name__ == '__main__':
    main(base_url,deep)