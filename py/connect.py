# -*- coding: utf-8 -*-
from utils.BasicLogging import *

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0

def get_driver():
	#return webdriver.PhantomJS()
	#return webdriver.Firefox()
	firefox_profile = webdriver.FirefoxProfile()
	firefox_profile.set_preference("browser.download.folderList", 2)
	firefox_profile.set_preference("permissions.default.stylesheet", 2)
	firefox_profile.set_preference("permissions.default.image", 2)
	#firefox_profile.set_preference("javascript.enable", False)

	browser = webdriver.Firefox(firefox_profile=firefox_profile)
	return browser

def login():
	logging.info("登陆账号")
	driver = get_driver()
	try:
		driver.get("http://159.226.39.22/srun_portal_pc.php?ac_id=1&")
	except:
		logging.error('打开登录页面失败')
	else:
		driver.find_element_by_id("username").clear()
		driver.find_element_by_id("username").send_keys("wangtianyu")
		driver.find_element_by_id("password").clear()
		driver.find_element_by_id("password").send_keys("321321")
		driver.find_element_by_id("button").click()
		WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input.a.a_demo_two')))
		logging.info("登陆完成")
	finally:
		driver.close()

if __name__ == "__main__":
	login()