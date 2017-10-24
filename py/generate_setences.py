from utils.BasicLogging import *
import utils.Console as Console
import utils.Path as Path
import re

def generate_sentences(in_file, encoding='gbk'):
	'''
	将proofread.exe的结果文件中的句子，还原出来。
	注：由于含有空格的句子，经过将proofread.exe处理后会丢失空格，故由此方法还原出来的句子也不会含有空格（和真实的原句有出入）。
	'''
	out_file = Path.add_suffix(in_file, '_sentences')
	sentence_selector = re.compile('^\S')
	error_selector = re.compile('[【】](?!/)')
	pos_selector = re.compile('/[a-z]+ ')
	with open(in_file, encoding=encoding) as fr:
		lines = map(lambda line: line.rstrip('\r\n'), fr)
		# 选择句子所在的行
		lines = filter(lambda line: sentence_selector.match(line), lines)
		# 删除错误标注的【和】
		lines = map(lambda line: error_selector.sub('', line), lines)
		# 删除词性
		lines = map(lambda line: pos_selector.sub('', line), lines)
		
		with open(out_file, 'w', encoding=encoding) as fw:
			for line in lines:
				fw.write(line)
				fw.write('\n')
			
if __name__ == '__main__':
	#generate_sentences(r'C:\Users\wuyuming\Desktop\caotest-old.txt')
	while True:
		generate_sentences(Console.get_input_file_path('Input file path: '))