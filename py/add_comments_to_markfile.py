from utils.BasicLogging import *
import utils.Console as Console
import utils.Path as Path
import re,shutil
from collections import OrderedDict

def add_comments_to_markfile(in_file, encoding='gbk'):
	'''
	由人工标注的文件，生成用于合并操作的格式：
	原句子：
		Benchmark: 含有标注的句子
	'''
	out_file = Path.add_suffix(in_file, '_bench')
	origin_word_selector = re.compile('【([^】]*)】【[^】]*】')
	with open(in_file, encoding=encoding) as fr:
		with open(out_file, 'w', encoding=encoding) as fw:
			for line in fr:
				line = line.rstrip('\r\n')
				if line:
					fw.write(origin_word_selector.sub(r'\1', line))
					fw.write('\n')
					benchmark = line if origin_word_selector.search(line) else ''
					fw.write('\tBenchmark: ' + benchmark)
				else:
					fw.write(line)
				fw.write('\n')

if __name__ == '__main__':
	add_comments_to_markfile(r'C:\Users\wuyuming\Desktop\mark.txt')
	while True:
		add_comments_to_markfile(Console.get_input_file_path('Input file path: '))