import re

file_path = r"C:\Users\wuyuming\OneDrive - Office\Project\ChineseProofread\NGram\lexi_bigram_result.txt"

def search(file_path, key):
	with open(file_path, errors="ignore") as fr:
		lines = map(lambda line: line.rstrip(), fr)
		re_obj = re.compile("\\b" + key + "\\b")
		lines = filter(lambda line: re_obj.search(line) is not None, lines)
		for line in lines:
			print(line)

if __name__ == "__main__":
	while True:
		key = input("input key: ")
		search(file_path, key)