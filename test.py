from selenium import webdriver
import re
import time
from selenium.common.exceptions import StaleElementReferenceException

option = webdriver.ChromeOptions()
#option.add_argument("headless")
driver = webdriver.Chrome(r"C:\Users\gy\Desktop\chromedriver.exe", chrome_options=option)
driver.get('https://www.zhihu.com/billboard')

hot_title = driver.find_elements_by_xpath('//div[@class="HotList-itemTitle"]')
title_popular = driver.find_elements_by_xpath('//div[@class="HotList-itemMetrics"]')

title_num = len(hot_title)
title_list = []
popular_list = []
keyword_list = []
followers_list = []
viewers_list = []
answers_list = []


for i in range(3):
    hot_title = driver.find_elements_by_xpath('//div[@class="HotList-itemTitle"]')
    try:
        webdriver.ActionChains(driver).move_to_element(hot_title[i]).click(hot_title[i]).perform()
        titles = driver.find_elements_by_xpath('//h1[@class="QuestionHeader-title"]')[0].text
        followers = driver.find_elements_by_xpath('//strong[@class="NumberBoard-itemValue"]')[0].text
        viewers = driver.find_elements_by_xpath('//strong[@class="NumberBoard-itemValue"]')[1].text
        answers = driver.find_elements_by_xpath('//h4[@class="List-headerText"]')[0].text
        keyword = driver.find_elements_by_xpath('//span[@class="Tag-content"]')
        keywords = ''
        for x in range(len(keyword)):
            keywords = keywords + keyword[x].text + ","

        print (titles + '1')

        title_list.append(titles)
        keyword_list.append(keywords)
        followers_list.append(followers)
        viewers_list.append(viewers)
        answers_list.append(answers)
        driver.back()
    except StaleElementReferenceException:
        print ("something wrong!\n")
        time.sleep(0.5)

print (title_list)
print (answers_list)
print (keyword_list)
print (followers_list)
print (viewers_list)
# str_test = driver.find_elements_by_xpath(
#                 '//div[contains(text(), ' + '\"' + '2' + '\")' + ' and @class="HotList-itemIndex HotList-itemIndexHot"]')
# webdriver.ActionChains(driver).move_to_element(str_test[0]).click(str_test[0]).perform()
#
# answer_number = driver.find_elements_by_class_name("List-headerText")

#print (answer_number)
#print (answer_number)
#languages = [x.text for x in answer_number]
#print (languages)
#languages = str(languages)
