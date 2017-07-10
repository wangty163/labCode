from utils.BasicLogging import *
import utils.Console as Console


def solve_file(in_file, out_file):
	with open(in_file) as fr:
		with open(out_file, 'w') as fw:
			lines = map(lambda line: line.split(' '), fr)
			lines = map(lambda line: '{} {}'.format(line[0], line[2]), lines)
			fw.writelines(lines)

if __name__ == '__main__':
	#in_file = Console.get_input_file_path('Input file path: ')
	#out_file = Console.get_input_file_path('Output file path: ')
	in_file = r'C:\Users\wuyuming\OneDrive - Office\Project\ChineseProofread\NGram\lexi_3Gram.txt'
	out_file = 'out.txt'
	solve_file(in_file, out_file)