# -*- coding: utf-8 -*-
from pyquery import PyQuery as pq
import urllib.request
import os

'''
从https://tools.wmflabs.org/pinyin-wiki/w/index.php?oldid=????页面，提取拼音、汉字信息。
'''

# 网络状态测试：
# 经过多长时间没有返回结果，认为超时
request_timeout = 10
# 最多几次超时后认为网络不连通
request_cnt = 3

def load(filePath=r'C:\Users\wuyuming\Desktop\111.html'):
	with open(filePath, encoding='utf-8') as fr:
		content = fr.read()
	return content

def get_content_from_url(url):
	for _ in range(request_cnt):
		try:
			with urllib.request.urlopen(url, timeout=request_timeout) as response:
				data_byte = response.read()
				data = data_byte.decode("utf-8", errors="ignore")
				return data
		except urllib.error.URLError:
			pass
	raise Exception(str(id) + ' 页面抓取失败')

def getValidParents(d, all_parents_selectors='p, li, ul, ol', direct_parent_selector='div'):
	allParents = list()
	parent = None
	for x in d('span[title]').items():
		cur_parent = x.parent()
		if cur_parent.not_(direct_parent_selector):
			cur_parent = x.parents(all_parents_selectors).eq(-1)
		if parent != cur_parent and cur_parent:
			parent = cur_parent
			allParents.append(parent)
	return allParents

def get_result(nodes):
	for x in nodes:
		tx = x.clone()
		for nd in tx.items('span[title]'):
			nd.text(nd.attr('title'))
		yield tx.text()
		for pair in x.items('span[title]'):
			yield '\t{0} {1}'.format(pair.attr('title'), pair.text())

def solve(folder, id):
	url = 'https://tools.wmflabs.org/pinyin-wiki/w/index.php?oldid=' + str(id)
	with open(os.path.join(folder, str(id)), 'w', encoding='utf-8') as fw:
		content = get_content_from_url(url)
		
		try:
			d = pq(content)
		except:
			raise Exception(str(id) + ' 页面解析失败')
		
		nodes = getValidParents(d)
		for info in get_result(nodes):
			fw.write(info)
			fw.write('\n')

if __name__ == "__main__":
	folder = r'C:\Users\wuyuming\Desktop\ff'
	if not os.path.exists(folder):
		os.makedirs(folder)
	with open('err.log', 'w') as fw:
		for id in range(1, 2 + 1):
			try:
				solve(folder, id)
			except Exception as e:
				print(e)
				fw.write(e)