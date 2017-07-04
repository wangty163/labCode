from utils.BasicLogging import *

file_path = 'C:\\Users\\wuyuming\\OneDrive - Office\\Project\\ChineseProofread\\NGram\\lexi_bigram.txt'

def solve(in_file, out_file):
	'''
	输入格式：上文【空格】下文【TAB】条件概率【TAB】频度
		如：纷纷 逃荒	0.00003487	2
	输出格式：SET【空格】'上文---下文'【TAB】频度
		如：SET 纷纷---逃荒 2
	'''
	logging.info('start...')
	with open(in_file, encoding='gbk') as fr:
		lines = map(lambda line: line.rstrip(), fr)
		lines = map(lambda line: line.split('\t'), lines)
		lines = filter(lambda line: len(line) == 3, lines)
		lines = map(lambda line: "SET '{}' {}".format(line[0], line[2]), lines)
		with open(out_file, 'w', encoding='gbk') as fw:
			for line in lines:
				fw.write(line)
				fw.write('\n')
	logging.info('end...')

solve(file_path, "out.txt")