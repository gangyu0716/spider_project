#修改自知乎专栏 《从零开始写爬虫》https://zhuanlan.zhihu.com/p/26786056
#该爬虫用于爬取http://dianying.2345.com/top/的最新电影信息和图片
#时间 2018-4-26

import requests
import bs4

def get_html(url):
    try:
        r = requests.get(url, timeout = 50)
        r.raise_for_status()
        r.encoding = 'gbk'
        return r.text
    except:
        return 'something wrong'

def get_content(url):
    html = get_html(url)
    soup = bs4.BeautifulSoup(html, 'lxml')

    movies_list = soup.find('ul', class_='picList clearfix')
    movies = movies_list.find_all('li')

    for top in movies:
        img_url = 'https:' + top.find('img')['src']
        name = top.find('span',class_='sTit').a.text

        try :
            time = top.find('span',class_='sIntro').text
        except:
            time = "暂无上映时间"

        actors = top.find('p',class_ = 'pActor')
        actor = ''

        for act in actors.contents:
            actor = actor + act.string + ' '

        intro = top.find('p',class_ = 'pTxt pIntroShow').text

        print ("片名：{}\t{}\n{}\n{}\n \n".format(name,time,actor,intro))
        print ("图片url:{}\n".format(img_url))

        with open ('test/' + name + '.jpg', 'wb+') as f:
            f.write(requests.get(img_url).content)

def main():
    url = 'http://dianying.2345.com/top/'
    get_content(url)

if __name__ == "__main__":
    main()

    #testurl = "https://imgwx1.2345.com/dypcimg/img/c/66/sup198060_223x310.jpg"
    #pic = requests.get(testurl, stream=True).content
    #print (pic)
    #with open('test.jpg', 'wb+') as f:
        #f.write(pic)

