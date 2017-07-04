from utils.BasicLogging import *

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
		fw.write('\r\n'.encode('gbk').join(lines))
	logging.info('end...')

sort_file(lexi_3Gram_gen)