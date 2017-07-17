import utils.Console as Console
import os,sys

def merge_file_by_line(in_file):
	out_file = '{}_merge_by_line{}'.format(*os.path.splitext(in_file))
	with open(in_file, errors='ignore') as fr:
		with open(out_file, 'w') as fw:
			pre_line = ''
			pre_parts = ['', 0]
			for line in fr:
				if line.encode('gbk') < pre_line.encode('gbk'):
					print('pre_line: ', pre_line)
					print('cur_line: ', line)
					sys.exit(1)
				parts = line.split('\t')
				if parts[0] == pre_parts[0]:
					pre_parts[1] += int(parts[1])
				else:
					if pre_parts[0]:
						fw.write(pre_parts[0])
						fw.write('\t')
						fw.write(str(pre_parts[1]))
						fw.write('\n')
					pre_parts = [parts[0],int(parts[1])]
				pre_line = line
			if pre_parts[0]:
				fw.write(pre_parts[0])
				fw.write('\t')
				fw.write(str(pre_parts[1]))

if __name__ == '__main__':
	while True:
		in_file = Console.get_input_file_path('Input file path: ')
		merge_file_by_line(in_file)