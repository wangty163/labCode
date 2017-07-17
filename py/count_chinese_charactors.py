# -*- coding: utf-8 -*-
#!/usr/bin/env python3

from pyquery import PyQuery as pq
import utils.Console as Console

def get_text_from_html(html_content):
	try:
		d = pq(html_content)
	except:
		return ""
	for remove_selecter in ["head", "img", "link", "form", "script", "style", "a"]:
		d(remove_selecter).remove()
	text = d("p").text()
	return text
	
def get_from_string(html_content):
	text = get_text_from_html(html_content)
	cnt = 0
	for char in text:
		if '\u4e00' <= char <= '\u9fff':
			cnt += 1
	return cnt

def main():
	while True:
		file_path = Console.get_input_file_path("Input file path: ")
		with open(file_path) as fr:
			print(get_from_string(fr.read()))

if __name__ == "__main__":
	main()