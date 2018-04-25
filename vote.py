# -*- coding : utf-8 -*-
import requests
import urllib
import random
import string
import time
import threading

def vote():
	global tnum
	headers = {
		'Host': 'smc.tthud.cn',
		'Connection': 'keep-alive',
		'Accept': '*/*',
		'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
		'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 MicroMessenger/6.5.2.501 NetType/WIFI WindowsWechat QBCore/3.43.691.400 QQBrowser/9.0.2524.400',
		'X-Requested-With': 'XMLHttpRequest',
		#'Referer': 'http://smc.tthud.cn/wechat.php/xjb_player_detail?BiUMYgFbB20GNQI%2FVTQKbgVhATpUMVc7UTFXMFYzAjgCMFozCWoMPlQxBGJRZlg8WTgKNgF2A2sCJAU%2BUCZTKAYPDGkBYAc5BmU%3D',
		'Accept-Encoding': 'deflate',
		'Accept-Language': 'zh-CN,zh;q=0.8,en-us;q=0.6,en;q=0.5;q=0.4',
		'Cookie': """PHPSESSID=mbpoj3eer4jjfhli7p5v5q0cfa; \
	LETOU_party_keys=xjb; \
	Hm_lvt_c817603a3b7ba93c3872f6c4b4c10491=1523452271; \
	Hm_lpvt_c817603a3b7ba93c3872f6c4b4c10491=1523452326; \
	LETOU_wechat_oauth_array=think%3A%7B%22openid%22%3A%22orWD41DzI2Wv_cHrh1qKTXFyf-kQ%22%2C%22nickname%22%3A%22wyjstar%22%2C%22sex%22%3A%221%22%2C%22language%22%3A%22zh_CN%22%2C%22city%22%3A%22%25E9%2595%25BF%25E6%25B2%25BB%22%2C%22province%22%3A%22%25E5%25B1%25B1%25E8%25A5%25BF%22%2C%22country%22%3A%22%25E4%25B8%25AD%25E5%259B%25BD%22%2C%22headimgurl%22%3A%22http%253A%252F%252Fthirdwx.qlogo.cn%252Fmmopen%252Fvi_32%252FDYAIOgq83eor6UHYRGR4IiaTWBBxneqbD1lkvVOI76dfe7rzleOxo6sLPW3vEfiaeHIhRfESLK8t32r89DEh9ywA%252F132%22%7D; \
	LETOU_wechat_oauth_json=%7B%22openid%22%3A%22orWD41DzI2Wv_cHrh1qKTXFyf-kQ%22%2C%22nickname%22%3A%22wyjstar%22%2C%22sex%22%3A%221%22%2C%22language%22%3A%22zh_CN%22%2C%22city%22%3A%22%5Cu957f%5Cu6cbb%22%2C%22province%22%3A%22%5Cu5c71%5Cu897f%22%2C%22country%22%3A%22%5Cu4e2d%5Cu56fd%22%2C%22headimgurl%22%3A%22http%3A%5C%2F%5C%2Fthirdwx.qlogo.cn%5C%2Fmmopen%5C%2Fvi_32%5C%2FDYAIOgq83eor6UHYRGR4IiaTWBBxneqbD1lkvVOI76dfe7rzleOxo6sLPW3vEfiaeHIhRfESLK8t32r89DEh9ywA%5C%2F132%22%7D; \
	LETOU_wechat_oauth_openid=orWD41DzI2Wv_cHrh1qKTXFyf-kQ; \
	LETOU_wechat_oauth_client=wx; \
	LETOU_signPackage=think%3A%7B%22appId%22%3A%22wxfbf6197881064650%22%2C%22nonceStr%22%3A%22srIXEW2KUbwQ9UrO%22%2C%22timestamp%22%3A%221523453140%22%2C%22url%22%3A%22http%253A%252F%252Fsmc.tthud.cn%252Fwechat.php%252Fxjb_ranking_ajax%22%2C%22signature%22%3A%223675b284472d7febbeaee09d228ab3981c239ae6%22%2C%22rawString%22%3A%22jsapi_ticket%253DHoagFKDcsGMVCIY2vOjf9ips9yD3FQ_34q1DaYa4rGQZtHL25QgbNfJOpSKWyjdMhMS02nuX0WK6TSkWg-Xc5w%2526noncestr%253DsrIXEW2KUbwQ9UrO%2526timestamp%253D1523453140%2526url%253Dhttp%253A%252F%252Fsmc.tthud.cn%252Fwechat.php%252Fxjb_ranking_ajax%22%7D"""
	}
	
	
	data = {
		'pl_id' : "28424c43f1def12fd815",
		'prop_id' : "4"
	}

	data2 = {
		'pl_id' : "28424c43f1def12fd815",
		'prop_id' : "4",
		'num':'1500',
		'realname':'realname',
		'addname':'addname',
		'addmobile':'18888888888',
		'address':'address',
		'time':'2018-4-19',
		'prop_type':'2',
		'pno':'10356',
		'client_url':'http://smc.tthud.cn/wechat.php/xjb_player_detail?BiUBb1QOBmxUZwc6WDkMaFg8DDcAZQRoCGgDZFA1ATsJO1gxUTIHNVA1BGIEMwBkVTRaZgRzB28JLwU%2BAXcDeAYPAWRUNQY4VDc%3D='
	}
	
	
	url = 'http://smc.tthud.cn/wechat.php/xjb_prise'
	url2 = 'http://smc.tthud.cn/wechat.php/xjb_goods'
	
	old0 = 'mbpoj3eer4jjfhli7p5v5q0cfa'
	old1 = 'orWD41DzI2Wv'
	old2 = 'cHrh1qKTXFyf'
	old3 = 'kQ'
	old4 = 'wyjstar'
	old5 = '1523453140'
	
	post_data = urllib.parse.urlencode(data2)
	new0 = ''.join(random.sample(string.ascii_letters + string.digits, 26))
	new1 = ''.join(random.sample(string.ascii_letters + string.digits, 12))
	new2 = ''.join(random.sample(string.ascii_letters + string.digits, 12))
	new3 = ''.join(random.sample(string.ascii_letters + string.digits, 2))
	new4 = ''.join(random.sample(string.ascii_letters + string.digits, 16))
	new5 = str(int(time.time()))
	headers['Cookie'] = headers['Cookie'].replace(old0, new0)
	headers['Cookie'] = headers['Cookie'].replace(old1, new1)
	headers['Cookie'] = headers['Cookie'].replace(old2, new2)
	headers['Cookie'] = headers['Cookie'].replace(old3, new3)
	headers['Cookie'] = headers['Cookie'].replace(old4, new4)
	headers['Cookie'] = headers['Cookie'].replace(old5, new5)
	old0 = new0
	old1 = new1
	old2 = new2
	old3 = new3
	old4 = new4
	old5 = new5
	print ('%s    %s_%s-%s    %s    %s' % (old0, old1, old2, old3, old4, old5))
	for y in range(5):
		req = requests.post(url= url2, headers = headers, data = post_data)
		html = req.text
		print (html)
	#time.sleep(random.random())
	req.close()
	tnum = tnum - 1
	return

def run():
	global tnum
	while True:
		while(tnum > maxThread):
			pass
		threading.Thread(target = vote).start()
		time.sleep(random.random())

def main():
	#run()
	vote()
	
if __name__ == '__main__':
	tnum = 0
	maxThread = 128
	main()
