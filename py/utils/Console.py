def get_input_file_path():
	'''
	从Windows的console中读取文件路径
	支持拖拽形式（拖拽时，如果路径中含有空格等，路径会由引号括起来，该函数会将引号去掉后返回真是路径）
	'''
	file_path = input()
	if len(file_path) > 2 and file_path.startswith('"') and file_path.endswith('"'):
		return file_path[1:-1]
	else:
		return file_path