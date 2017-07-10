from utils.BasicLogging import *
import utils.Console as Console

lexi_uigram = r'C:\Users\wuyuming\OneDrive - Office\Project\ChineseProofread\NGram\lexi_ungram.txt'
lexi_bigram_result = r'C:\Users\wuyuming\OneDrive - Office\Project\ChineseProofread\NGram\lexi_bigram_result.txt'
lexi_3Gram = r'C:\Users\wuyuming\OneDrive - Office\Project\ChineseProofread\NGram\lexi_3Gram.txt'
lexi_3Gram_gen = r'C:\Users\wuyuming\OneDrive - Office\Project\ChineseProofread\NGram\lexi_3Gram_gen.txt'
#file_path = r'C:\Users\wuyuming\Desktop\lexi_3Gram_gen.txt'

def sort_file(in_file):
	'''
	将文件内容进行排序
	此程序按照字节对文件进行排序，符合c++的排序规则
	'''
	logging.info('start...')
	with open(in_file, 'rb') as fr:
		lines = map(lambda line: line.rstrip(), fr)
		lines = list(lines)
		lines.sort()
	with open(in_file, 'wb') as fw:
		for line in lines:
			fw.write(line)
			fw.write('\r\n'.encode('gbk'))
	logging.info('end...')

if __name__ == '__main__':
	while True:
		sort_file(Console.get_input_file_path('Input file path: '))