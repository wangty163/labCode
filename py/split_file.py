import utils.Console as Console
import os

def add_suffix(file_path, suffix):
	parts = os.path.splitext(file_path)
	return ''.join((parts[0], suffix, parts[1]))

def solve(in_file):
	'''
	将文件拆分，每x行为一个单位，放入一个子文件中
	'''
	cnt = 0
	i = 0
	fr = open(in_file, encoding='gbk')
	fw = open(add_suffix(in_file, '_out_' + str(i)), 'w', encoding='gbk')
	for line in fr:
		fw.write(line)
		cnt += 1
		if cnt == 1000000:
			cnt = 0
			i += 1
			fw.close()
			fw = open(add_suffix(in_file, '_out_' + str(i)).format(i), 'w', encoding='gbk')
	fw.close()
	fr.close()

if __name__ == '__main__':
	while True:
		solve(Console.get_input_file_path('Input file path: '))