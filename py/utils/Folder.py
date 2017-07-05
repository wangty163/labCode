import os

def list_all_files(folder):
	if os.path.isfile(folder):
		yield folder
	else:
		for child in os.listdir(folder):
			yield from list_all_files(os.path.join(folder, child))