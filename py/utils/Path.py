import os

def add_suffix(file_path, suffix):
	parts = os.path.splitext(file_path)
	return ''.join((parts[0], suffix, parts[1]))