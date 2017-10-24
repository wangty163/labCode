from utils.BasicLogging import *
import utils.Console as Console
import utils.Path as Path
import re,shutil
from collections import OrderedDict

'''
每次merge进来的comments所在的行，都会以改符号作为前缀
如果正常内容以改符号作为起始，会出错，因此应当保证该符号不会出现在正常内容所在行的开头
'''
add_line_prefix = '+++++'

def get_sentence_and_comments(in_file, delete_error_mark=True, encoding='gbk'):
	'''
	将proofread.exe的结果文件中的句子和对应的注释（人工注释、程序输出等以留白开头的行），还原出来。
	'''
	ret = OrderedDict()
	sentence_selector = re.compile('^\S')
	error_selector = re.compile('[【】](?!/)')
	with open(in_file, encoding=encoding) as fr:
		sentence,comments = None,list()
		for line in fr:
			line = line.rstrip('\r\n')
			# 去除状态标记
			if line.startswith(add_line_prefix):
				line = line[len(add_line_prefix):]
			# line非空时处理
			if not line:
				pass
			# 所在行是句子
			elif sentence_selector.match(line):
				if sentence:
					if sentence in ret:
						print('【' + in_file + '】', '文件中有两个相同的句子，结果将被忽略：\n\t', sentence, '\n')
					ret[sentence] = comments
					sentence,comments = None,list()
				if delete_error_mark:
					# 将句子中的 “【” 和 “】” 符号都删除，防止句子定位因为错词标注出现问题
					sentence = error_selector.sub('', line)
				else:
					sentence = line
			else:
				comments.append(line)
		if sentence:
			assert sentence not in ret, '文件中有两个相同的句子：' + sentence
			ret[sentence] = comments
		return ret

def merge_files_by_setence(dst_file, src_file, encoding='gbk'):
	'''
	将src_file中的句子结果合并到dst_file中。
	'''
	dst_dict = get_sentence_and_comments(dst_file, True)
	src_dict = get_sentence_and_comments(src_file, True)
	# 备份原有文件
	shutil.move(dst_file, dst_file + '.bak')
	# 合并两个文件结果
	with open(dst_file, 'w', encoding=encoding) as fw:
		for sentence in dst_dict:
			fw.write(sentence)
			fw.write('\n')
			for line in dst_dict[sentence]:
				fw.write(line)
				fw.write('\n')
			for line in src_dict.get(sentence, []):
				fw.write(add_line_prefix)
				fw.write(line)
				fw.write('\n')
			
if __name__ == '__main__':
	#merge_files_by_setence(r'C:\Users\wuyuming\Desktop\caotest-old.txt')
	while True:
		dst_file = Console.get_input_file_path('Input destination file path: ')
		src_file = Console.get_input_file_path('Input source file path: ')
		merge_files_by_setence(dst_file, src_file)