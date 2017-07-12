#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from BasicLogging import *
import time,threading
	
def _start(start_threshold, func, *args):
	'''
	定时启动任务
	'''
	last_run = -float("inf")
	while True:
		delta = start_threshold - time.time() + last_run
		if delta <= 0:
			func(*args)
			last_run = time.time()
		else:
			sleep_seconds = delta
			info = ['sleep for']
			info.append(str(int(delta / 3600)))
			info.append("hours,")
			delta %= 3600
			
			info.append(str(int(delta / 60)))
			info.append("minutes,")
			delta %= 60
			
			info.append(str(int(delta)))
			info.append("seconds")
			
			logging.info(' '.join(info))
			time.sleep(sleep_seconds)

def start(start_threshold, func, *args):
	"""
	启动线程，在线程中定时启动任务
	start_threshold: seconds
	"""
	#class threading.Thread(group=None, target=None, name=None, args=(), kwargs={}, *, daemon=None)
	thread = threading.Thread(target=_start, args=(start_threshold, func, *args))
	thread.start()
	return thread

if __name__ == "__main__":
	tds = []
	
	td = threading.Thread(target=logging.info, args=("aaa",))
	td.start()
	tds.append(td)
	time.sleep(1)
	
	tds.append(start(61, logging.info, "bbb"))
	time.sleep(1)
	
	tds.append(start(3700, logging.info, "ccc"))
	for td in tds:
		td.join()