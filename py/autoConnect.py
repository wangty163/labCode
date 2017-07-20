import re, time
import urllib.request
from utils.BasicLogging import *

# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0


# 程序检测间隔
sleep_time = 1 * 60 * 60

# 网络状态测试：
# 经过多长时间没有返回结果，认为超时
request_timeout = 5
# 超时后，下一次测试间隔
request_sleep_time = 1
# 最多几次超时后认为网络不连通
request_cnt = 3

# 登录
# 经过多长时间没有返回结果，认为超时
# login_timeout = 10

def need_login():
	logging.info("测试网络是否连通")
	url = "https://www.baidu.com"
	timout_cnt = 0
	for _ in range(request_cnt):
		try:
			with urllib.request.urlopen(url, timeout=request_timeout) as response:
				data_byte = response.read()
				data = data_byte.decode("utf-8", errors="ignore")
				if data.find("baidu") == -1:
					logging.info("自动跳转到登陆页面")
					return True
				else:
					return False
		except urllib.error.URLError:
			logging.info("访问超时")
			timout_cnt += 1
			time.sleep(request_sleep_time)
	return timout_cnt == request_cnt

'''
def login():
	print_info("登陆账号")
	url = "http://159.226.39.22/cgi-bin/do_login"
	post_data = urllib.parse.urlencode({
		'username': 'wangtianyu',
		'password': 'dff046abdcece8bd',
		'type': 1,
		}).encode("ascii")
	try:
		with urllib.request.urlopen(url, post_data, timeout=login_timeout) as response:
			data_byte = response.read()
			data = data_byte.decode("utf-8", errors="ignore")
			print_info("网关返回信息：", str(data))
		print_info("登陆完成")
	except urllib.error.URLError as e:
		print_info(e.reason)
'''

def get_driver():
	#return webdriver.PhantomJS()
	return webdriver.Firefox()
	firefox_profile = webdriver.FirefoxProfile()
	firefox_profile.set_preference("browser.download.folderList", 2)
	firefox_profile.set_preference("permissions.default.stylesheet", 2)
	firefox_profile.set_preference("permissions.default.image", 2)
	firefox_profile.set_preference("javascript.enable", False)

	browser = webdriver.Firefox(firefox_profile=firefox_profile)
	return browser

def login():
	logging.info("登陆账号")
	driver = get_driver()
	driver.get("http://159.226.39.22/srun_portal_pc.php?ac_id=1&")
	driver.find_element_by_id("username").clear()
	driver.find_element_by_id("username").send_keys("wangtianyu")
	driver.find_element_by_id("password").clear()
	driver.find_element_by_id("password").send_keys("8882302")
	driver.find_element_by_id("button").click()
	WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input.a.a_demo_two')))
	driver.close()
	logging.info("登陆完成")

def logout():
	driver = get_driver()
	driver.get("http://159.226.39.22/srun_portal_pc.php?ac_id=1&")
	driver.find_element_by_id("username").clear()
	driver.find_element_by_id("username").send_keys("wangtianyu")
	driver.find_element_by_id("password").clear()
	driver.find_element_by_id("password").send_keys("8882302")
	driver.find_element_by_id("button").click()
	WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input.a.a_demo_two'))).click()
	driver.close()
	
if __name__ == "__main__":
	while True:
		if need_login():
			logging.info("网络不连通，准备登陆")
			login()
		else:
			logging.info("测试结束，网络连通")
		logging.info("程序开始休眠")
		time.sleep(sleep_time)
