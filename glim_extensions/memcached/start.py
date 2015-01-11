from memcached import Cache
from glim import Log

def before(config):
	try:
		Cache.register(config)
	except Exception as e:
		Log.error(e)
