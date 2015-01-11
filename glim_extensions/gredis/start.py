from gredis import Redis
from glim import Log

def before(config):
	try:
		Redis.register(config)
	except Exception as e:
		Log.error(e)
