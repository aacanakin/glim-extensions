import os

def touch(path):
	fhandle = open(path, 'a')
	try:
		os.utime(path, None)
	finally:
		fhandle.close()
	return os.path.isfile(path)
