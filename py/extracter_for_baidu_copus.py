from pyquery import PyQuery as pq
from utils.Folder import *
import re,sys,pdb

'''
为了从百度百科语料中抽取出纯文本
'''
class Extrator:
	RE_P = re.compile('(http://baike\.baidu\.com/view/\d+\.htm)\*\*\*\*\*')
	
	def __init__(self, file_path, **args):
		self.__fr = open(file_path, **args)
	
	def __del__(self):
		self.__fr.close()
	
	@staticmethod
	def isStart(line):
		return bool(Extrator.RE_P.match(line))
	
	@staticmethod
	def extractURL(line):
		return Extrator.RE_P.match(line).group(1)
	
	@staticmethod
	def removeStartMark(line):
		return Extrator.RE_P.sub('', line)

	def extract(self):
		url = ''
		page_lines = []
		for line in self.__fr:
			# begin of one page
			if Extrator.isStart(line):
				if page_lines:
					yield url,'\n'.join(page_lines)
					page_lines.clear()
				url = Extrator.extractURL(line)
				line = Extrator.removeStartMark(line)
			page_lines.append(line)
		# the last page
		if page_lines:
			yield '\n'.join(page_lines)
			page_lines.clear()

class BaikeParser:
	@staticmethod
	def parse(html):
		d = pq(html)
		d('sup').remove()
		d('br').replaceWith('\n')
		d('div.pic').remove()
		d('div.text_pic').remove()
		d = d('div.para')
		for para in d('div.para').items():
			for x in para.children().items():
				x.replaceWith(x.text())
		return d.map(lambda i, e: pq(this).text())

def filter_line(line):
	return line.find('。') != -1

def uprint(s):
	'''
	can print string which may contains utf-8 charactors.
	'''
	if s:
		sys.stdout.buffer.write(s.encode('gbk', errors='ignore'))
		sys.stdout.buffer.write('\n'.encode('gbk'))

def main():
	file = 'part-r-00043'
	e = Extrator(file, encoding='utf-8')
	for url,page in e.extract():
		r'''
		with open(r'C:\Users\wuyuming\Desktop\1.html', 'w', encoding='utf8') as fw:
			fw.write(page)
		input('wait..')
			'''
		for line in filter(filter_line, BaikeParser.parse(page)):
			uprint(line)
			input('wait..')
main()