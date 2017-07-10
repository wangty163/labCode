from pyquery import PyQuery as pq
from utils.Folder import *
from utils.BasicLogging import *
import re,sys,pdb,multiprocessing

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
			yield url,'\n'.join(page_lines)
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

def solve_file(file_path, out_folder):
    logging.debug(file_path)
    file_name = os.path.basename(file_path)
    out_file = os.path.join(out_folder, file_name + '_extracted.txt')

    if not os.path.exists(out_folder):
        os.makedirs(out_folder)

    with open(out_file, 'w', encoding='gbk', errors='ignore') as fw:
        e = Extrator(file_path, encoding='utf-8', errors='ignore')
        for url,page in e.extract():
            for line in BaikeParser.parse(page):
            #for line in filter(filter_line, BaikeParser.parse(page)):
                fw.write(line)
                fw.write('\n')
                #uprint(line)
                #print(line)
                #input('wait..')
                #sys.exit(0)
        r'''
        for line in filter(filter_line, BaikeParser.parse(page)):
            uprint(line)
            input('wait..')
            '''

def main():
    processes = []
    for file_path in list_all_files('/home/wty/copus'):
        processes.append(multiprocessing.Process(target=solve_file, args=(file_path, '/home/wty/copus_extracted')))
    for process in processes:
        process.start()
    for process in processes:
        process.join()

main()
