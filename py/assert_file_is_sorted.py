import utils.Console as Console
import sys

def check_file(in_file):
	with open(in_file, 'rb') as fr:
		pre_line = bytes()
		for line in fr:
			if line < pre_line:
				print('pre_line: ', pre_line)
				print('cur_line: ', line)
				sys.exit(1)
			pre_line = line

if __name__ == '__main__':
	in_file = Console.get_input_file_path('Input file path: ')
	check_file(in_file)