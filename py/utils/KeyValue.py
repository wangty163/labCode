# -*- coding: utf-8 -*-

from configparser import ConfigParser,ExtendedInterpolation

class KeyValue(dict):
	def __init__(self, file_path):
		self.update_from_file(file_path)
		
	def update_from_file(self, file_path):
		config = ConfigParser(interpolation=ExtendedInterpolation())
		config.read(file_path, encoding="utf-8")
		self.update(config.items())
		
	def __from_file(self, file_path):
		with open(file_path, 'r', encoding="utf8") as fr:
			config_string = '[dummy_section]\n' + fr.read()
		config = ConfigParser()
		config.read_string(config_string)
		self.update(config.items("dummy_section"))
		
if __name__ == '__main__':
	global_properties = KeyValue(r'E:\c\toTuple\config.ini')
	#global_properties.from_file(CONFIG_FILE_PATH)