from selenium import webdriver
import re
import time
import platform
from selenium.common.exceptions import StaleElementReferenceException
import wordcloud


#for get zhihu biliboard info
def GetBiliboardInfo(title_list=[], popular_list=[],
                       keyword_list=[],followers_list=[],
                       viewers_list=[], answers_list=[]):

    system_env = platform.uname()
    option = webdriver.ChromeOptions()
    #如果打开这一项可以实现程序的后台运行
    #option.add_argument("headless")

    #for windows env path
    if system_env[0] == 'Windows':
        driver = webdriver.Chrome(r"C:\Users\gy\Desktop\chromedriver.exe", chrome_options=option)
    #for linux env path
    if system_env[0] == 'Linux':
        driver = webdriver.Chrome(r"/home/gy/share/nfs/chromedriver", chrome_options=option)

    driver.get('https://www.zhihu.com/billboard')
    #find element of title and popular degree
    hot_title = driver.find_elements_by_xpath('//div[@class="HotList-itemTitle"]')
    title_popular = driver.find_elements_by_xpath('//div[@class="HotList-itemMetrics"]')

    title_num = len(hot_title)

    for i in range(title_num):
        popular = re.sub('\D',"",title_popular[i].text)
        popular_list.append(popular)

    for i in range(title_num):
        hot_title = driver.find_elements_by_xpath('//div[@class="HotList-itemTitle"]')
        try:
            webdriver.ActionChains(driver).move_to_element(hot_title[i]).click(hot_title[i]).perform()
            titles = driver.find_elements_by_xpath('//h1[@class="QuestionHeader-title"]')[1].text
            followers = driver.find_elements_by_xpath('//strong[@class="NumberBoard-itemValue"]')[0].text
            viewers = driver.find_elements_by_xpath('//strong[@class="NumberBoard-itemValue"]')[1].text
            answers = driver.find_elements_by_xpath('//h4[@class="List-headerText"]')[0].text
            keyword = driver.find_elements_by_xpath('//span[@class="Tag-content"]')
            keywords = ''
            for x in range(len(keyword)):
                keywords = keywords + keyword[x].text + ","

            title_list.append(titles)
            keyword_list.append(keywords)
            followers_list.append(followers)
            viewers_list.append(viewers)
            answers_list.append(answers)
            driver.back()
        #Error handle
        except StaleElementReferenceException:
            print ("something wrong in " + str(i) + " title\n")
            time.sleep(0.5)
            return title_list, popular_list, keyword_list, followers_list, viewers_list, answers_list

    #return result
    return title_list, popular_list, keyword_list, followers_list, viewers_list, answers_list


#for handle data
def data_process(viewers_list, keyword_list):
    font = r'C:\Windows\Fonts\STXINWEI.TTF'

    cloud_text = "".join(keyword_list)
    wordtext_fd = open("keyword.txt", "w")
    wordtext_fd.write(cloud_text)
    wordtext_fd.close()

    w = wordcloud.WordCloud(font_path=font,width=1400, height=1400, margin=2)
    w.generate(cloud_text)
    w.to_file("wordcloud.png")


if __name__ == '__main__':

    [title_list , popular_list, keyword_list, followers_list, viewers_list, answers_list]=GetBiliboardInfo()

    print (title_list)
    print (answers_list)
    print (keyword_list)
    print (followers_list)
    print (viewers_list)
    print (popular_list)

    data_process(viewers_list,keyword_list)